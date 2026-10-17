"""Parâmetros imutáveis das operações públicas do worker ACBr 0.2.0.

As verificações são estruturais. Identidade fiscal, schemas e regras de negócio
continuam a cargo do motor nativo; nenhum dígito verificador é calculado aqui.
"""

from dataclasses import dataclass, field
import re
from typing import Literal

from .errors import AcbrError


def _digits(value: str, size: int, code: str, name: str, stage: str) -> None:
    if type(value) is not str or re.fullmatch(r"[0-9]{" + str(size) + "}", value) is None:
        raise AcbrError(code, "Informe os dígitos exigidos para o campo.", etapa=stage, campo=name)


def _reason(value: str, stage: str) -> None:
    # NativeMotor checks Length of the UTF-8 string, so enforce its byte limit.
    size = 0
    if type(value) is str and len(value) <= 255:
        try:
            size = len(value.encode("utf-8"))
        except UnicodeError:
            pass
    if not 15 <= size <= 255:
        raise AcbrError("JUSTIFICATIVA_INVALIDA", "Justificativa deve ter de 15 a 255 bytes UTF-8 válidos.",
                        etapa=stage, campo="justificativa")


@dataclass(frozen=True, slots=True)
class EventoEnvio:
    """Aviso do motor com ID aleatório da requisição e comando, sem dados fiscais."""

    id: str
    comando: Literal["transmitir", "cancelar", "inutilizar"]

    def __post_init__(self) -> None:
        if (type(self.id) is not str or re.fullmatch(r"[A-Za-z0-9_-]{1,100}", self.id) is None
                or type(self.comando) is not str or self.comando not in ("transmitir", "cancelar", "inutilizar")):
            raise AcbrError("EVENTO_ENVIO_INVALIDO", "Evento de início de envio inválido.")


@dataclass(frozen=True, slots=True)
class Consulta:
    """Consulta por chave obrigatória, com recibo opcional de 15 dígitos."""

    chave: str = field(repr=False)
    recibo: str | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        _digits(self.chave, 44, "CHAVE_INVALIDA", "chave", "consulta")
        if self.recibo is not None:
            _digits(self.recibo, 15, "RECIBO_INVALIDO", "recibo", "consulta")

    def to_wire(self) -> dict:
        value = {"chave": self.chave}
        if self.recibo is not None:
            value["recibo"] = self.recibo
        return value


@dataclass(frozen=True, slots=True)
class Cancelamento:
    """Evento de cancelamento com protocolo e justificativa explícitos."""

    chave: str = field(repr=False)
    protocolo: str = field(repr=False)
    justificativa: str = field(repr=False)

    def __post_init__(self) -> None:
        _digits(self.chave, 44, "CHAVE_INVALIDA", "chave", "cancelamento")
        _reason(self.justificativa, "cancelamento")
        _digits(self.protocolo, 15, "PROTOCOLO_INVALIDO", "protocolo", "cancelamento")

    def to_wire(self) -> dict:
        return {"chave": self.chave, "protocolo": self.protocolo, "justificativa": self.justificativa}


@dataclass(frozen=True, slots=True)
class Inutilizacao:
    """Faixa de numeração; ano é o valor de dois dígitos entre 0 e 99."""

    ano: int = field(repr=False)
    serie: int = field(repr=False)
    numero_inicial: int = field(repr=False)
    numero_final: int = field(repr=False)
    justificativa: str = field(repr=False)

    def __post_init__(self) -> None:
        _reason(self.justificativa, "inutilizacao")
        if (any(type(value) is not int for value in (self.ano, self.serie, self.numero_inicial, self.numero_final))
                or not 0 <= self.ano <= 99 or not 0 <= self.serie <= 999
                or not 1 <= self.numero_inicial <= self.numero_final <= 999999999):
            raise AcbrError("INUTILIZACAO_INVALIDA", "Informe uma faixa de inutilização válida.",
                            etapa="inutilizacao", campo="inutilizacao")

    def to_wire(self) -> dict:
        return {"inutilizacao": {"ano": self.ano, "serie": self.serie,
                                 "numeroInicial": self.numero_inicial, "numeroFinal": self.numero_final},
                "justificativa": self.justificativa}


__all__ = ["Consulta", "Cancelamento", "Inutilizacao", "EventoEnvio"]
