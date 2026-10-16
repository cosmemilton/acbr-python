"""Configuração independente de framework; segredos só são enviados pela pipe."""
import base64
import re
from dataclasses import dataclass, field
from typing import Literal

from .errors import AcbrError

UFS = frozenset("AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split())


@dataclass(frozen=True)
class CertificadoA1:
    pfx: bytes = field(repr=False)
    senha: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.pfx, bytes) or not 0 < len(self.pfx) <= 2 * 1024 * 1024 or not isinstance(self.senha, str):
            raise AcbrError("CERTIFICADO_INVALIDO", "Informe bytes PFX e senha válidos.", etapa="configuracao")


@dataclass(frozen=True)
class Csc:
    id: str
    valor: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.id, str) or not re.fullmatch(r"[0-9]{1,6}", self.id) or not isinstance(self.valor, str) or not 0 < len(self.valor) <= 256:
            raise AcbrError("CSC_INVALIDO", "Informe id e valor CSC válidos.", etapa="configuracao")


@dataclass(frozen=True)
class Configuracao:
    cnpj: str = field(repr=False)
    uf: str
    modelo: Literal[55, 65] = 55
    ambiente: Literal[1, 2] = 2
    certificado: CertificadoA1 | None = field(default=None, repr=False)
    csc: Csc | None = field(default=None, repr=False)

    def __post_init__(self):
        checks = {
            "cnpj": isinstance(self.cnpj, str) and re.fullmatch(r"[0-9]{14}", self.cnpj),
            "uf": isinstance(self.uf, str) and self.uf in UFS,
            "modelo": type(self.modelo) is int and self.modelo in (55, 65),
            "ambiente": type(self.ambiente) is int and self.ambiente in (1, 2),
            "certificado": self.certificado is None or isinstance(self.certificado, CertificadoA1),
            "csc": self.csc is None or isinstance(self.csc, Csc),
        }
        for name, valid in checks.items():
            if not valid:
                raise AcbrError("CONFIGURACAO_INVALIDA", "Campo de configuração inválido.", etapa="configuracao", campo=name)

    def to_wire(self) -> dict:
        value = {"cnpj": self.cnpj, "uf": self.uf, "modelo": self.modelo, "ambiente": self.ambiente}
        if self.certificado is not None:
            value["certificado"] = {"pfxBase64": base64.b64encode(self.certificado.pfx).decode("ascii"), "senha": self.certificado.senha}
        if self.csc is not None:
            value["csc"] = {"id": self.csc.id, "valor": self.csc.valor}
        return value
