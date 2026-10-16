"""MVP NF-e/NFC-e: geração, validação e recuperação explícita por consulta."""
from pathlib import Path
import base64
import threading
import uuid

from .config import Configuracao
from .contract import CONTRACT_HASH, SOURCE_REVISION, Documento
from .errors import AcbrError
from .result import ResultadoFiscal
from .runtime import runtime_environment, verify_runtime
from .transport import ProcessTransport


class Emissor:
    def __init__(self, config: Configuracao, *, runtime_directory: Path | str,
                 timeout: float = 120, max_bytes: int = 8 * 1024 * 1024):
        if not isinstance(config, Configuracao):
            raise AcbrError("CONFIGURACAO_INVALIDA", "Informe uma Configuracao válida.", etapa="configuracao")
        self.config = config
        self.runtime_directory = Path(runtime_directory)
        self._transport = ProcessTransport(timeout, max_bytes)

    def _request(self, command: str, data: dict, cancel: threading.Event | None) -> ResultadoFiscal:
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
        if not isinstance(xml, str) or not xml.strip():
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

    def recuperar_xml(self, xml_assinado: str, *, allow_network: bool = False,
                      cancel: threading.Event | None = None) -> ResultadoFiscal:
        """Experimental. Consulta a situação com A1; nunca transmite ou tenta novamente."""
        if allow_network is not True:
            raise AcbrError("REDE_NAO_AUTORIZADA", "Recuperação exige allow_network=True.", etapa="consulta")
        if self.config.certificado is None:
            raise AcbrError("CERTIFICADO_AUSENTE", "Recuperação exige certificado A1.", etapa="consulta")
        return self._request("recuperarXml", self._xml_data(xml_assinado), cancel)

    def fechar(self) -> None:
        self._transport.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.fechar()
