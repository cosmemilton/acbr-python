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
    def test_public_signing_with_ephemeral_synthetic_a1(self):
        from synthetic_certificate import synthetic_a1
        runtime = Path(os.environ["ACBR_TEST_RUNTIME"])
        config = Configuracao("11222333000181", "CE", certificado=synthetic_a1())
        data = json.loads((FIXTURES / "documento.json").read_text(encoding="utf-8"))
        with Emissor(config, runtime_directory=runtime, timeout=30) as emitter:
            generated = emitter.gerar_xml(Documento(data))
            self.assertTrue(generated.sucesso, generated.to_dict())
            signed = emitter.assinar(generated.xml)
            self.assertTrue(signed.sucesso, signed.to_dict())
            self.assertEqual(signed.estado, "ASSINADO")
            self.assertIn("<Signature", signed.xml)
            self.assertFalse(signed.envio_iniciado)
            self.assertEqual(signed.diagnostico.status_envio, "nao_enviado")
            valid = emitter.validar(signed.xml)
            self.assertTrue(valid.sucesso, valid.to_dict())
            # All calls here are local. A changed signature must fail validation.
            invalid = emitter.validar(signed.xml.replace("Café São José", "CONTEUDO SINTETICO ALTERADO"))
            self.assertFalse(invalid.sucesso)
            self.assertEqual(invalid.codigo, "ASSINATURA_INVALIDA")

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
