"""Erros e diagnósticos seguros: nunca incluem resposta, XML ou segredo bruto."""
from dataclasses import asdict, dataclass


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
                 xml_original: str | None = None, limpeza_confirmada: bool = True):
        super().__init__(mensagem)
        self.codigo = codigo
        self.resultado_desconhecido = resultado_desconhecido
        self.xml_original = xml_original
        self.limpeza_confirmada = limpeza_confirmada
        self.diagnostico = Diagnostico(
            codigo, etapa, mensagem,
            "Confira a situação fiscal antes de repetir." if resultado_desconhecido
            else "Confira os parâmetros e as dependências da etapa.",
            "resultado_incerto" if resultado_desconhecido else "nao_enviado",
            campo, limpeza_confirmada=limpeza_confirmada,
        )

    def __repr__(self) -> str:
        return f"AcbrError(codigo={self.codigo!r})"
