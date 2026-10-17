"""API NF-e/NFC-e com consentimento explícito para cada operação de rede."""
from pathlib import Path
from collections.abc import Callable
import base64
import threading
import uuid

from .config import Configuracao
from .contract import CONTRACT_HASH, SOURCE_REVISION, Documento
from .errors import AcbrError
from .operations import Cancelamento, Consulta, EventoEnvio, Inutilizacao
from .result import ResultadoFiscal
from .runtime import runtime_environment, verify_runtime
from .transport import ProcessTransport

_STAGES = {"gerarXml": "geracao", "validar": "validacao", "assinar": "assinatura",
           "transmitir": "transmissao", "consultar": "consulta", "recuperarXml": "consulta",
           "cancelar": "cancelamento", "inutilizar": "inutilizacao"}
_CERTIFICATE_COMMANDS = frozenset(_STAGES) - {"gerarXml", "validar"}


class Emissor:
    def __init__(self, config: Configuracao, *, runtime_directory: Path | str,
                 timeout: float = 120, max_bytes: int = 8 * 1024 * 1024,
                 ao_iniciar_envio: Callable[[EventoEnvio], None] | None = None):
        if not isinstance(config, Configuracao):
            raise AcbrError("CONFIGURACAO_INVALIDA", "Informe uma Configuracao válida.", etapa="configuracao")
        if ao_iniciar_envio is not None and not callable(ao_iniciar_envio):
            raise AcbrError("CONFIGURACAO_INVALIDA", "Informe uma função para receber o início do envio.",
                            etapa="configuracao", campo="ao_iniciar_envio")
        self.config = config
        self.runtime_directory = Path(runtime_directory)
        self._transport = ProcessTransport(timeout, max_bytes, ao_iniciar_envio=ao_iniciar_envio)
        self._closed = threading.Event()

    def _request(self, command: str, data: dict, cancel: threading.Event | None) -> ResultadoFiscal:
        if command not in _STAGES:
            raise AcbrError("OPERACAO_INVALIDA", "Operação não suportada pelo cliente.")
        stage = _STAGES[command]
        if cancel is not None and not isinstance(cancel, threading.Event):
            raise AcbrError("OPERACAO_INVALIDA", "Cancelamento exige threading.Event.", etapa=stage, campo="cancel")
        if self._closed.is_set():
            raise AcbrError("EMISSOR_FECHADO", "Emissor encerrado.", etapa=stage)
        if cancel is not None and cancel.is_set():
            raise AcbrError("OPERACAO_CANCELADA", "Operação cancelada antes da execução.", etapa=stage)
        if command in _CERTIFICATE_COMMANDS and self.config.certificado is None:
            raise AcbrError("CERTIFICADO_AUSENTE", "A operação exige certificado A1.", etapa=stage)
        # Hash every operation: alterations between requests must fail before execution.
        runtime = verify_runtime(self.runtime_directory)
        if command == "recuperarXml" and "recuperarXml" not in runtime.capabilities:
            raise AcbrError("RUNTIME_SEM_CAPACIDADE", "Runtime sem recuperação de XML.", etapa="runtime")
        request = {"versao": 1, "id": uuid.uuid4().hex, "sourceRevision": SOURCE_REVISION,
                   "contractHash": CONTRACT_HASH, "comando": command, "config": self.config.to_wire(), **data}
        return self._transport.execute(runtime.executable, runtime.directory,
                                       runtime_environment(runtime), request, cancel=cancel)

    def gerar_xml(self, documento: Documento | dict, *, cancel: threading.Event | None = None) -> ResultadoFiscal:
        document = documento if isinstance(documento, Documento) else Documento(documento)
        return self._request("gerarXml", {"documento": document.to_wire()}, cancel)

    @staticmethod
    def _xml_data(xml: str) -> dict:
        if type(xml) is not str or not xml.strip():
            raise AcbrError("XML_INVALIDO", "Informe XML UTF-8 não vazio.", campo="xml")
        try:
            data = xml.encode("utf-8")
        except UnicodeError:
            raise AcbrError("XML_INVALIDO", "Informe XML UTF-8 válido.", campo="xml") from None
        if len(data) > 4 * 1024 * 1024:
            raise AcbrError("XML_INVALIDO", "XML excede o limite de bytes.", campo="xml")
        return {"xmlBase64": base64.b64encode(data).decode("ascii")}

    def validar(self, xml: str, *, cancel: threading.Event | None = None) -> ResultadoFiscal:
        return self._request("validar", self._xml_data(xml), cancel)

    def assinar(self, xml: str, *, cancel: threading.Event | None = None) -> ResultadoFiscal:
        """Assina localmente com o A1 configurado; não envia à SEFAZ."""
        return self._request("assinar", self._xml_data(xml), cancel)

    @staticmethod
    def _require_network(allow_network: bool, stage: str) -> None:
        if allow_network is not True:
            raise AcbrError("REDE_NAO_AUTORIZADA", "A operação exige allow_network=True.", etapa=stage)

    def transmitir(self, xml_assinado: str, *, allow_network: bool = False,
                   cancel: threading.Event | None = None) -> ResultadoFiscal:
        """Transmite um XML assinado, somente com autorização explícita de rede."""
        self._require_network(allow_network, "transmissao")
        return self._request("transmitir", self._xml_data(xml_assinado), cancel)

    def consultar(self, consulta: Consulta, *, allow_network: bool = False,
                  cancel: threading.Event | None = None) -> ResultadoFiscal:
        self._require_network(allow_network, "consulta")
        if type(consulta) is not Consulta:
            raise AcbrError("OPERACAO_INVALIDA", "Informe uma Consulta válida.", etapa="consulta", campo="consulta")
        return self._request("consultar", consulta.to_wire(), cancel)

    def cancelar(self, cancelamento: Cancelamento, *, allow_network: bool = False,
                 cancel: threading.Event | None = None) -> ResultadoFiscal:
        self._require_network(allow_network, "cancelamento")
        if type(cancelamento) is not Cancelamento:
            raise AcbrError("OPERACAO_INVALIDA", "Informe um Cancelamento válido.", etapa="cancelamento", campo="cancelamento")
        return self._request("cancelar", cancelamento.to_wire(), cancel)

    def inutilizar(self, inutilizacao: Inutilizacao, *, allow_network: bool = False,
                   cancel: threading.Event | None = None) -> ResultadoFiscal:
        self._require_network(allow_network, "inutilizacao")
        if type(inutilizacao) is not Inutilizacao:
            raise AcbrError("OPERACAO_INVALIDA", "Informe uma Inutilizacao válida.", etapa="inutilizacao", campo="inutilizacao")
        return self._request("inutilizar", inutilizacao.to_wire(), cancel)

    def recuperar_xml(self, xml_assinado: str, *, allow_network: bool = False,
                      cancel: threading.Event | None = None) -> ResultadoFiscal:
        """Experimental. Consulta a situação com A1; nunca transmite ou tenta novamente."""
        self._require_network(allow_network, "consulta")
        return self._request("recuperarXml", self._xml_data(xml_assinado), cancel)

    def fechar(self) -> None:
        self._closed.set()
        self._transport.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.fechar()
