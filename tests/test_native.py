"""Opt-in smoke real, estritamente offline: sem A1 privado ou consulta SEFAZ."""
import json
import os
from pathlib import Path
import unittest

from acbr import Configuracao, Documento, Emissor
from acbr.contract import describe_field
from acbr.runtime import verify_runtime

FIXTURES = Path(__file__).with_name("fixtures")


@unittest.skipUnless(os.environ.get("ACBR_TEST_RUNTIME"), "Defina ACBR_TEST_RUNTIME para smoke nativo offline")
class NativeTests(unittest.TestCase):
    def test_native_generation_and_schema(self):
        document = Documento(json.loads((FIXTURES / "documento.json").read_text(encoding="utf-8")))
        runtime = Path(os.environ["ACBR_TEST_RUNTIME"])
        self.assertIn("recuperarXml", verify_runtime(runtime).capabilities)
        config = Configuracao("11222333000181", "CE", modelo=55, ambiente=2)
        with Emissor(config, runtime_directory=runtime, timeout=20) as emitter:
            generated = emitter.gerar_xml(document)
            self.assertTrue(generated.sucesso, generated.to_dict())
            self.assertEqual(generated.estado, "XML_GERADO")
            self.assertIn("Café São José", generated.xml)
            # O worker exige assinatura para schema da NFe. Fixture tem apenas certificado público.
            signed = (FIXTURES / "signed.xml").read_text(encoding="utf-8")
            validated = emitter.validar(signed)
            self.assertTrue(validated.sucesso, validated.to_dict())
            self.assertEqual(validated.estado, "VALIDADO")
            malformed = emitter.validar("<NFe>INVALIDO-SINTETICO</NFe>")
            self.assertFalse(malformed.sucesso)
            self.assertEqual(malformed.estado, "ERRO")
            self.assertIsNotNone(malformed.codigo)


if __name__ == "__main__":
    unittest.main()
