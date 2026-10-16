"""Resultado fiscal tipado; campos sensíveis exigem acesso explícito."""
import base64
from dataclasses import dataclass, field
from typing import Literal

from .errors import Diagnostico

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

    @property
    def xml(self) -> str | None:
        return base64.b64decode(self.xml_base64, validate=True).decode("utf-8") if self.xml_base64 is not None else None

    def to_dict(self) -> dict:
        """Resumo seguro, sem identidade fiscal, XML ou xMotivo bruto."""
        return {"sucesso": self.sucesso, "estado": self.estado, "diagnostico": self.diagnostico.to_dict()}
