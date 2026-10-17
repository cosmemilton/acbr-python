"""ACBr Python, integração independente de frameworks com worker upstream."""
from ._version import __version__
from .client import Emissor
from .config import CertificadoA1, Configuracao, Csc
from .contract import Documento, describe_field, describe_type, validate_document
from .errors import AcbrError, Diagnostico
from .operations import Cancelamento, Consulta, EventoEnvio, Inutilizacao
from .result import ResultadoFiscal

__all__ = ["Emissor", "CertificadoA1", "Configuracao", "Csc", "Documento", "describe_field", "describe_type",
           "validate_document", "AcbrError", "Diagnostico", "ResultadoFiscal",
           "Consulta", "Cancelamento", "Inutilizacao", "EventoEnvio"]
