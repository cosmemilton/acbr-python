"""Acesso explícito a retornos privados, com dados inteiramente sintéticos."""
import base64
from dataclasses import asdict
import json
import unittest

from acbr import AcbrError, Diagnostico, ResultadoFiscal


SECRET = "SYNTHETIC-PRIVATE-RETURN"


class OriginalReturnTests(unittest.TestCase):
    def diagnostic(self):
        return Diagnostico("VALIDADO", "validacao", "Etapa concluída.", "Guarde o resultado fiscal.")

    def result(self, frame=None):
        return ResultadoFiscal(True, "VALIDADO", self.diagnostic(), _retorno_original=frame)

    def test_absent_return_and_provenance_stay_absent(self):
        for value in (self.result(), AcbrError("FALHA_MOTOR", "Falha do motor.")):
            self.assertIsNone(value.retorno_original)
            self.assertIsNone(value.origem_retorno_original)

    def test_full_frame_is_copied_on_input_and_on_every_access(self):
        frame = {"versao": 1, "id": "synthetic", "cStat": 102, "xMotivo": SECRET,
                 "adicional": {"lista": [None, True, {"xml": "<SYNTHETIC/>"}], "numero": 12345678901234567890}}
        result = self.result(frame)
        error = AcbrError("FALHA_MOTOR", "Falha após resposta.", retorno_original=frame)
        frame["adicional"]["lista"][2]["xml"] = "changed source"
        frame["xMotivo"] = "changed source"
        for value in (result, error):
            with self.subTest(type=type(value).__name__):
                self.assertEqual("acbr_worker_jsonl", value.origem_retorno_original)
                original = value.retorno_original
                self.assertEqual(SECRET, original["xMotivo"])
                self.assertEqual("<SYNTHETIC/>", original["adicional"]["lista"][2]["xml"])
                original["adicional"]["lista"].append("changed getter")
                self.assertEqual(3, len(value.retorno_original["adicional"]["lista"]))
                self.assertNotIn("soap", value.retorno_original)
                self.assertNotIn("xmlBase64", value.retorno_original)

    def test_safe_summary_and_repr_exclude_original_extra_fields_and_xml(self):
        encoded = base64.b64encode(SECRET.encode()).decode()
        result = self.result({"xmlBase64": encoded, "diagnostico": {"mensagem": SECRET}, "unknown": SECRET})
        expected = {"sucesso": True, "estado": "VALIDADO", "diagnostico": self.diagnostic().to_dict()}
        self.assertEqual(expected, result.to_dict())
        self.assertNotIn(SECRET, repr(result) + json.dumps(result.to_dict()))
        self.assertNotIn(encoded, repr(result) + json.dumps(result.to_dict()))
        self.assertIn(SECRET, json.dumps(result.retorno_original))
        # asdict é uma serialização privada explícita, diferente do resumo seguro.
        self.assertIn(SECRET, json.dumps(asdict(result)))
        restored = ResultadoFiscal(**asdict(result))
        self.assertEqual(result.retorno_original, restored.retorno_original)
        self.assertNotIn(SECRET, repr(restored))
        error = AcbrError("FALHA_MOTOR", "Falha após resposta.", retorno_original=result.retorno_original)
        self.assertNotIn(SECRET, str(error) + repr(error) + json.dumps(error.diagnostico.to_dict()))
        self.assertEqual(("Falha após resposta.",), error.args)

    def test_positional_constructor_and_comparison_remain_compatible(self):
        old = ResultadoFiscal(True, "VALIDADO", self.diagnostic(), None, None, None, None, None, None, None, False)
        self.assertEqual(old, self.result({"extra": SECRET}))
        self.assertEqual(hash(old), hash(self.result({"extra": SECRET})))
        self.assertIsNone(old.retorno_original)


if __name__ == "__main__":
    unittest.main()
