"""Resultado fiscal tipado; campos sensíveis exigem acesso explícito."""
import base64
from dataclasses import dataclass, field
from typing import Literal

from .errors import Diagnostico, _copy_original_frame

Estado = Literal["DENEGADO", "XML_GERADO", "VALIDADO", "ASSINADO", "XML_RECUPERADO", "AUTORIZADO", "REJEITADO", "PENDENTE", "INDETERMINADO", "CONSULTADO", "CANCELADO", "EVENTO_REGISTRADO", "INUTILIZADO", "ERRO"]


@dataclass(frozen=True)
class ResultadoFiscal:
    sucesso: bool
    estado: Estado
    diagnostico: Diagnostico
    codigo: str | None = field(default=None, repr=False)
    c_stat: int | None = None
    chave: str | None = field(default=None, repr=False)
    protocolo: str | None = field(default=None, repr=False)
    recibo: str | None = field(default=None, repr=False)
    xml_base64: str | None = field(default=None, repr=False)
    x_motivo: str | None = field(default=None, repr=False)
    envio_iniciado: bool = False
    _retorno_original: dict | None = field(default=None, repr=False, compare=False, kw_only=True)

    def __post_init__(self):
        # frozen não congela o conteúdo de um dict. Copiar também na entrada
        # impede que o fornecedor do frame altere posteriormente esta evidência.
        object.__setattr__(self, "_retorno_original", _copy_original_frame(self._retorno_original))

    @property
    def retorno_original(self) -> dict | None:
        """Cópia privada do frame JSON completo validado, inclusive campos extras.

        A origem é o worker JSONL, não o SOAP bruto nem uma nova consulta.
        Campos não entregues pelo worker permanecem ausentes.
        """
        return _copy_original_frame(self._retorno_original)

    @property
    def origem_retorno_original(self) -> str | None:
        return "acbr_worker_jsonl" if self._retorno_original is not None else None

    @property
    def xml(self) -> str | None:
        return base64.b64decode(self.xml_base64, validate=True).decode("utf-8") if self.xml_base64 is not None else None

    def to_dict(self) -> dict:
        """Resumo seguro, sem identidade, XML, xMotivo ou retorno original.

        dataclasses.asdict() inclui os campos privados e não serve para logs.
        """
        return {"sucesso": self.sucesso, "estado": self.estado, "diagnostico": self.diagnostico.to_dict()}
