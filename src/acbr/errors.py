"""Diagnósticos seguros; retornos privados exigem acesso explícito."""
from copy import deepcopy
from dataclasses import asdict, dataclass


def _copy_original_frame(frame: dict | None) -> dict | None:
    if frame is None:
        return None
    if not isinstance(frame, dict):
        raise TypeError("O retorno original deve ser um objeto JSON ou None.")
    return deepcopy(frame)


@dataclass(frozen=True)
class Diagnostico:
    codigo: str
    etapa: str
    mensagem: str
    acao: str
    status_envio: str = "nao_enviado"
    campo: str | None = None
    c_stat: int | None = None
    limpeza_confirmada: bool = True

    def to_dict(self) -> dict:
        return asdict(self)


class AcbrError(Exception):
    def __init__(self, codigo: str, mensagem: str, resultado_desconhecido: bool = False,
                 *, etapa: str = "operacao", campo: str | None = None,
                 xml_original: str | None = None, limpeza_confirmada: bool = True,
                 retorno_original: dict | None = None):
        super().__init__(mensagem)
        self.codigo = codigo
        self.resultado_desconhecido = resultado_desconhecido
        self.xml_original = xml_original
        self.limpeza_confirmada = limpeza_confirmada
        self._retorno_original = _copy_original_frame(retorno_original)
        self.diagnostico = Diagnostico(
            codigo, etapa, mensagem,
            "Confira a situação fiscal antes de repetir." if resultado_desconhecido
            else "Confira os parâmetros e as dependências da etapa.",
            "resultado_incerto" if resultado_desconhecido else "nao_enviado",
            campo, limpeza_confirmada=limpeza_confirmada,
        )

    @property
    def retorno_original(self) -> dict | None:
        """Cópia privada do último frame terminal validado, se recebido.

        É o JSON decodificado do worker; não é o SOAP original da SEFAZ.
        Pode coexistir com erro de transporte ou encerramento não confirmado.
        """
        return _copy_original_frame(self._retorno_original)

    @property
    def origem_retorno_original(self) -> str | None:
        return "acbr_worker_jsonl" if self._retorno_original is not None else None

    def __repr__(self) -> str:
        return f"AcbrError(codigo={self.codigo!r})"
