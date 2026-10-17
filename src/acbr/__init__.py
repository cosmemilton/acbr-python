"""ACBr Python, integração independente de frameworks com worker upstream."""
from .client import Emissor
from .config import CertificadoA1, Configuracao, Csc
from .contract import Documento, describe_field, validate_document
from .errors import AcbrError, Diagnostico
from .operations import Cancelamento, Consulta, EventoEnvio, Inutilizacao
from .result import ResultadoFiscal

__version__ = "0.1.0a3"
__all__ = ["Emissor", "CertificadoA1", "Configuracao", "Csc", "Documento", "describe_field",
           "validate_document", "AcbrError", "Diagnostico", "ResultadoFiscal",
           "Consulta", "Cancelamento", "Inutilizacao", "EventoEnvio"]
