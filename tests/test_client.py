import json
import threading
import unittest
from unittest.mock import patch
from pathlib import Path
from types import SimpleNamespace

from acbr import AcbrError, CertificadoA1, Configuracao, Csc, Documento, Emissor


class ClientTests(unittest.TestCase):
    def test_configuration_and_secret_repr(self):
        cert = CertificadoA1(b"SYNTHETIC-NOT-A-PFX", "password-example")
        config = Configuracao("00000000000000", "SP", certificado=cert, csc=Csc("1", "csc-example"))
        text = repr(config) + repr(cert) + repr(config.csc)
        for value in ("password-example", "SYNTHETIC", "00000000000000", "csc-example"):
            self.assertNotIn(value, text)
        for kwargs in ({"cnpj": "bad", "uf": "SP"}, {"cnpj": "0" * 14, "uf": "XX"},
                       {"cnpj": "0" * 14, "uf": "SP", "ambiente": True}):
            with self.assertRaises(AcbrError):
                Configuracao(**kwargs)

    def test_network_is_explicit_and_certificate_required(self):
        with Emissor(Configuracao("0" * 14, "SP"), runtime_directory="absent") as emitter:
            with self.assertRaises(AcbrError) as caught:
                emitter.recuperar_xml("<NFe/>")
            self.assertEqual(caught.exception.codigo, "REDE_NAO_AUTORIZADA")
            with self.assertRaises(AcbrError) as caught:
                emitter.recuperar_xml("<NFe/>", allow_network=True)
            self.assertEqual(caught.exception.codigo, "CERTIFICADO_AUSENTE")

    def test_capability_checked_and_wire_request(self):
        runtime = SimpleNamespace(directory=Path("."), executable=Path("worker"), capabilities=frozenset())
        config = Configuracao("0" * 14, "SP", certificado=CertificadoA1(b"SYNTHETIC", "example"))
        with patch("acbr.client.verify_runtime", return_value=runtime), patch("acbr.client.runtime_environment", return_value={}):
            with Emissor(config, runtime_directory=".") as emitter:
                with self.assertRaises(AcbrError) as caught:
                    emitter.recuperar_xml("<NFe/>", allow_network=True)
                self.assertEqual(caught.exception.codigo, "RUNTIME_SEM_CAPACIDADE")
                with patch.object(emitter._transport, "execute", return_value="mock-result") as execute:
                    self.assertEqual(emitter.gerar_xml(Documento({"Ide": {"modelo": 55}})), "mock-result")
                    request = execute.call_args.args[3]
                    self.assertEqual(request["comando"], "gerarXml")
                    self.assertEqual(request["documento"], {"Ide": {"modelo": 55}})
                    self.assertNotIn("senha", repr(config))
                    self.assertEqual(request["config"]["certificado"]["senha"], "example")

    def test_xml_validation(self):
        for xml in (None, "", " ", "\ud800", "x" * (4 * 1024 * 1024 + 1)):
            with self.assertRaises(AcbrError):
                Emissor._xml_data(xml)


if __name__ == "__main__":
    unittest.main()
