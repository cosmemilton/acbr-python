"""Offline contract tests: no runtime, certificate or fiscal endpoint is used."""

from __future__ import annotations

import dataclasses
import hashlib
import inspect
import json
from pathlib import Path
import subprocess
import sys
import typing
import unittest
from unittest.mock import patch

import acbr
from acbr import contract, models
from acbr.contract import Documento, describe_field, describe_type, validate_document
from acbr.errors import AcbrError


class ContractTests(unittest.TestCase):
    def assert_code(self, code: str, data: object, field: str | None = None) -> AcbrError:
        with self.assertRaises(AcbrError) as raised:
            validate_document(data)
        error = raised.exception
        self.assertEqual(error.codigo, code)
        self.assertEqual(error.diagnostico.campo, field)
        self.assertFalse(error.resultado_desconhecido)
        self.assertEqual(error.diagnostico.etapa, "documento")
        return error

    def test_exact_upstream_bytes_and_ir_are_authenticated(self):
        source = Path(contract.__file__).parent / "resources/contract.json"
        raw = source.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), contract.CONTRACT_FILE_SHA256)
        metadata = contract._decode_contract(raw)
        self.assertEqual(metadata["contractHash"], contract.CONTRACT_HASH)
        self.assertEqual(len(metadata["ir"]["types"]), 204)
        with self.assertRaises(AcbrError) as raised:
            contract._decode_contract(raw + b"\n")
        self.assertEqual(raised.exception.codigo, "CONTRATO_INVALIDO")
        changed = json.loads(raw)
        changed["ir"]["types"][0]["values"].append("unexpected")
        altered = json.dumps(changed, ensure_ascii=False, separators=(",", ":")).encode()
        # Even if an attacker bypassed the file hash, the independently pinned
        # contractHash must still reject altered field definitions.
        with patch.object(contract, "CONTRACT_FILE_SHA256", hashlib.sha256(altered).hexdigest()):
            with self.assertRaises(AcbrError):
                contract._decode_contract(altered)

    def test_validation_returns_detached_data_and_preserves_omission(self):
        data = {"Ide": {"cUF": 35, "tpAmb": "taHomologacao", "dEmi": "2024-02-29T12:34:56.123"},
                "Det": [{"Prod": {"xProd": "PRODUTO SINTÉTICO", "vProd": "10.1234", "vUnCom": "1.123456789"}}]}
        result = validate_document(data)
        self.assertEqual(result, data)
        self.assertIsNot(result, data)
        self.assertIsNot(result["Ide"], data["Ide"])
        self.assertIsNot(result["Det"], data["Det"])
        self.assertIsNot(result["Det"][0], data["Det"][0])
        self.assertEqual(validate_document({}), {})
        self.assertNotIn("tpEmis", result["Ide"])

    def test_objects_lists_and_scalar_types_are_not_coerced(self):
        cases = [
            ([], "OBJETO_ESPERADO", "TNFe"),
            ({"Ide": None}, "OBJETO_ESPERADO", "TNFe.Ide"),
            ({"Det": {}}, "ARRAY_ESPERADO", "TNFe.Det"),
            ({"Det": ()}, "ARRAY_ESPERADO", "TNFe.Det"),
            ({"Det": [None]}, "OBJETO_ESPERADO", "TNFe.Det[0]"),
            ({"Ide": {"cUF": True}}, "INTEIRO_INVALIDO", "TNFe.Ide.cUF"),
            ({"Ide": {"cUF": 35.0}}, "INTEIRO_INVALIDO", "TNFe.Ide.cUF"),
            ({"Ide": {"cUF": "35"}}, "INTEIRO_INVALIDO", "TNFe.Ide.cUF"),
            ({"Ide": {"cUF": 2**31}}, "INTEIRO_INVALIDO", "TNFe.Ide.cUF"),
            ({"Ide": {"cUF": -(2**31) - 1}}, "INTEIRO_INVALIDO", "TNFe.Ide.cUF"),
            ({"Ide": {"natOp": 1}}, "TEXTO_ESPERADO", "TNFe.Ide.natOp"),
            ({"Ide": {"tpAmb": 2}}, "ENUM_INVALIDO", "TNFe.Ide.tpAmb"),
            ({"Ide": {"tpAmb": "homologacao"}}, "ENUM_INVALIDO", "TNFe.Ide.tpAmb"),
        ]
        for value, code, field in cases:
            with self.subTest(code=code, field=field):
                self.assert_code(code, value, field)
        self.assertEqual(validate_document({"Ide": {"cUF": -(2**31), "nNF": 2**31 - 1}})["Ide"]["nNF"], 2**31 - 1)

    def test_decimals_follow_text_format_length_and_currency_scale(self):
        for value in [1, 1.1, None, "1,1", "+1", "1e2", "NaN", "Inf", "1.", ".1", "1.12345", "１", "1\n", "1" * 65]:
            with self.subTest(value_type=type(value).__name__):
                self.assert_code("DECIMAL_INVALIDO", {"Det": [{"Prod": {"vProd": value}}]}, "TNFe.Det[0].Prod.vProd")
        for value in ["0", "-1.2345", "0001.20"]:
            self.assertEqual(validate_document({"Det": [{"Prod": {"vProd": value}}]})["Det"][0]["Prod"]["vProd"], value)

    def test_dates_are_valid_civil_iso_without_timezone(self):
        for value in ["2024-02-29", "2024-02-29T00:00:00", "2024-02-29T23:59:59.1", "2024-02-29T23:59:59.123"]:
            self.assertEqual(validate_document({"Ide": {"dEmi": value}})["Ide"]["dEmi"], value)
        for value in ["2024-01-01T00:00:00Z", "2024-01-01T00:00:00-03:00", "2024-01-01 00:00:00", "2024-01-01T00:00:00.1234", "2024-01-01T00:00", 20240101]:
            with self.subTest(value_type=type(value).__name__):
                self.assert_code("DATA_HORA_INVALIDA", {"Ide": {"dEmi": value}}, "TNFe.Ide.dEmi")
        for value in ["2023-02-29", "2024-02-30", "2024-13-01", "0000-01-01", "2024-01-01T24:00:00", "2024-01-01T00:60:00", "2024-01-01T00:00:60"]:
            with self.subTest(invalid_civil_date=value):
                self.assert_code("DATA_INVALIDA", {"Ide": {"dEmi": value}}, "TNFe.Ide.dEmi")

    def test_unknown_fields_and_readonly_are_rejected_without_data_leaks(self):
        secret = "SYNTHETIC_SECRET_DO_NOT_LOG"
        for data, field in [({secret: secret}, "TNFe"), ({"Ide": {secret: secret}}, "TNFe.Ide"), ({"ide": {}}, "TNFe"), ({1: secret}, "TNFe")]:
            error = self.assert_code("CAMPO_DESCONHECIDO", data, field)
            self.assertNotIn(secret, str(error))
            self.assertNotIn(secret, repr(error))
            self.assertNotIn(secret, json.dumps(error.diagnostico.to_dict()))
        for name in ("procNFe", "signature", "infNFeSupl"):
            self.assert_code("CAMPO_SOMENTE_LEITURA", {name: {}}, "TNFe." + name)
        self.assert_code("CAMPO_SOMENTE_LEITURA", {"Det": [{"Prod": {"veicProd": {"CombDescricao": secret}}}]}, "TNFe.Det[0].Prod.veicProd.CombDescricao")

    def test_document_is_immutable_and_snapshots_all_nested_values(self):
        data = {"Det": [{"Prod": {"xProd": "SYNTHETIC_PRIVATE_TEXT"}}]}
        document = Documento(data)
        data["Det"][0]["Prod"]["xProd"] = "changed"
        self.assertEqual(document.to_wire()["Det"][0]["Prod"]["xProd"], "SYNTHETIC_PRIVATE_TEXT")
        wire = document.to_wire()
        wire["Det"][0]["Prod"]["xProd"] = "changed again"
        self.assertNotEqual(document.to_wire(), wire)
        self.assertNotIn("SYNTHETIC_PRIVATE_TEXT", repr(document))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            document._snapshot = b"{}"

    def test_field_help_resolves_types_paths_constraints_and_readonly(self):
        help_ = describe_field("Ide.cUF")
        self.assertEqual(help_["path"], "TNFe.Ide.cUF")
        self.assertEqual(help_["kind"], "integer")
        self.assertEqual(help_["constraints"], {"min": -(2**31), "max": 2**31 - 1})
        self.assertEqual(help_["contractHash"], contract.CONTRACT_HASH)
        self.assertEqual(help_["sourceRevision"], 48590)
        self.assertEqual(describe_field("TNFe.Det[12].Prod.vProd")["path"], "TNFe.Det[].Prod.vProd")
        self.assertEqual(describe_field("Det[].Prod.vProd")["constraints"], {"scale": 4})
        self.assertEqual(describe_field("Det")["itemType"], "TDetCollectionItem")
        self.assertEqual(describe_field("Det[]")["pascalType"], "TDetCollectionItem")
        self.assertEqual(describe_field("Ide.tpAmb")["values"], ["taProducao", "taHomologacao"])
        self.assertEqual(describe_field("Ide.tpAmb")["declaredDefault"], "taHomologacao")
        self.assertTrue(describe_field("procNFe.cStat")["readonly"])
        self.assertTrue(all(member["readonly"] for member in describe_field("procNFe")["members"]))
        self.assertEqual(describe_field("TProd")["path"], "TProd")
        self.assertEqual(describe_field("cIndOp")["path"], "TNFe.Ide.cIndOp")

    def test_field_help_rejects_ambiguous_or_invalid_queries(self):
        for query, code in [("vBC", "CAMPO_AMBIGUO"), ("Det.Prod", "COLECAO_REQUER_INDICE"),
                            ("Ide[]", "CAMPO_NAO_COLECAO"), ("ide.cUF", "CAMPO_INEXISTENTE"),
                            ("Ide.cUF.child", "CAMINHO_INVALIDO"), ("Det[-1]", "CAMINHO_INVALIDO"),
                            ("", "CAMINHO_INVALIDO"), (None, "CAMINHO_INVALIDO")]:
            with self.subTest(code=code):
                with self.assertRaises(AcbrError) as raised:
                    describe_field(query)
                self.assertEqual(raised.exception.codigo, code)
                self.assertIsNone(raised.exception.diagnostico.campo)

    def test_type_help_matches_legacy_help_for_every_exact_contract_type(self):
        metadata, _ = contract._contract()
        for node in metadata["ir"]["types"]:
            with self.subTest(type=node["name"]):
                help_ = describe_type(node["name"])
                self.assertEqual(help_, describe_field(node["name"]))
                self.assertEqual(help_["path"], node["name"])
                self.assertEqual(help_["kind"], node["kind"])
                if node["kind"] == "enum":
                    self.assertEqual(help_["values"], node["values"])
                elif node["kind"] == "list":
                    self.assertEqual(help_["itemType"], node["item"])
                else:
                    self.assertEqual([member["name"] for member in help_["members"]],
                                     [prop["name"] for prop in node["properties"]])

    def test_type_help_requires_exact_ir_names_and_does_not_leak_queries(self):
        class TextSubclass(str):
            pass

        secret = "SYNTHETIC_SECRET_TYPE_DO_NOT_LOG"
        invalid = [None, True, 1, b"TNFe", [], {}, TextSubclass("TNFe"), "", " TNFe", "TNFe ",
                   "tnfe", "TProdOutput", "Ide", "cIndOp", "Ide.cUF", "TNFe.Det[].Prod",
                   "TProd[]", "Tcompra", "Integer", "Currency", secret, "T" * 513]
        for query in invalid:
            with self.subTest(query_type=type(query).__name__):
                with self.assertRaises(AcbrError) as raised:
                    describe_type(query)
                error = raised.exception
                self.assertEqual(error.codigo, "TIPO_INVALIDO")
                self.assertEqual(error.diagnostico.etapa, "documento")
                self.assertIsNone(error.diagnostico.campo)
                self.assertFalse(error.resultado_desconhecido)
                self.assertNotIn(secret, str(error))
                self.assertNotIn(secret, repr(error))
                self.assertNotIn(secret, json.dumps(error.diagnostico.to_dict()))
        self.assertEqual(describe_type("TCompra")["pascalType"], "TCompra")
        self.assertEqual(describe_field("compra")["pascalType"], "Tcompra")
        self.assertEqual(describe_field("compra")["typeReference"], "TCompra")

    def test_type_help_preserves_literal_values_and_field_context(self):
        help_ = describe_type("TTipoNFe")
        self.assertEqual(help_["values"], ["tnEntrada", "tnSaida"])
        self.assertEqual(typing.get_args(models.TTipoNFe), ("tnEntrada", "tnSaida"))
        self.assertNotIn("declaredDefault", help_)
        self.assertEqual(describe_field("Ide.tpNF")["declaredDefault"], "tnSaida")
        self.assertTrue(next(member for member in describe_type("TNFe")["members"]
                             if member["name"] == "procNFe")["readonly"])

    def test_type_and_field_help_return_detached_metadata(self):
        enum = describe_type("TTipoNFe")
        enum["values"].append("SYNTHETIC_INVALID_ENUM")
        obj = describe_type("TNFe")
        obj["members"][0]["name"] = "changed"
        obj["members"].clear()
        field_help = describe_field("Ide.cUF")
        field_help["constraints"]["min"] = 0
        self.assertEqual(describe_type("TTipoNFe")["values"], ["tnEntrada", "tnSaida"])
        self.assertEqual(describe_field("TTipoNFe")["values"], ["tnEntrada", "tnSaida"])
        self.assertNotEqual(describe_type("TNFe")["members"], [])
        self.assertNotEqual(describe_type("TNFe")["members"][0]["name"], "changed")
        self.assertEqual(describe_field("Ide.cUF")["constraints"]["min"], -(2**31))

    def test_help_is_public_and_reports_code_version_without_package_metadata(self):
        self.assertIs(acbr.describe_type, describe_type)
        self.assertIn("describe_type", acbr.__all__)
        self.assertEqual(describe_type("TNFe")["sdkVersion"], acbr.__version__)
        self.assertEqual(describe_field("Ide.cUF")["sdkVersion"], acbr.__version__)
        repository = Path(__file__).resolve().parents[1]
        # Import after hiding metadata to exercise a source checkout rather than
        # trusting any older installed distribution in the same environment.
        probe = """
import importlib.metadata
import json
import sys
sys.path.insert(0, sys.argv[1])
def unavailable(name):
    raise importlib.metadata.PackageNotFoundError(name)
importlib.metadata.version = unavailable
import acbr
print(json.dumps([acbr.__version__, acbr.describe_type('TNFe')['sdkVersion'],
                  acbr.describe_field('Ide.cUF')['sdkVersion']]))
"""
        result = subprocess.run([sys.executable, "-B", "-c", probe, str(repository / "src")],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout), [acbr.__version__] * 3)

    def test_generated_typeddict_docstrings_describe_structural_input_and_output(self):
        metadata, _ = contract._contract()
        for node in metadata["ir"]["types"]:
            if node["kind"] != "object":
                continue
            for suffix, mode in [("", "Entrada"), ("Output", "Saída")]:
                with self.subTest(type=node["name"] + suffix):
                    generated = getattr(models, node["name"] + suffix)
                    doc = inspect.getdoc(generated)
                    self.assertIsInstance(generated.__doc__, str)
                    self.assertTrue(doc.startswith(mode))
                    self.assertIn(node["name"], doc)
                    self.assertIn(node["unit"], doc)
                    self.assertIn("total=False", doc)
                    self.assertIn("opcionais estruturalmente", doc)
                    self.assertIn("TypedDict não valida valores em execução", doc)
                    self.assertIn("estrutura de uma entrada TNFe", doc)
                    self.assertIn("Schema e regras fiscais dependem do runtime ACBr", doc)
                    self.assertIn(f"acbr.describe_type({node['name']!r})", doc)
                    self.assertFalse(generated.__total__)

    def test_generated_types_cover_all_contract_fields_and_enum_values(self):
        metadata, _ = contract._contract()
        for node in metadata["ir"]["types"]:
            with self.subTest(type=node["name"]):
                generated = getattr(models, node["name"])
                help_ = describe_field(node["name"])
                self.assertEqual(help_["kind"], node["kind"])
                if node["kind"] == "enum":
                    self.assertEqual(typing.get_args(generated), tuple(node["values"]))
                elif node["kind"] == "object":
                    inputs = typing.get_type_hints(generated, vars(models))
                    outputs = typing.get_type_hints(getattr(models, node["name"] + "Output"), vars(models))
                    self.assertEqual(set(inputs), {prop["name"] for prop in node["properties"] if not prop["readonly"]})
                    self.assertEqual(set(outputs), {prop["name"] for prop in node["properties"]})
                    self.assertFalse(generated.__total__)
                    self.assertEqual({member["name"] for member in help_["members"]}, set(outputs))
                else:
                    self.assertEqual(typing.get_origin(generated), list)
                    self.assertTrue(hasattr(models, node["name"] + "Output"))

    def test_model_generation_is_reproducible(self):
        repository = Path(__file__).resolve().parents[1]
        result = subprocess.run([sys.executable, str(repository / "tools/generate_models.py"), "--check"],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
