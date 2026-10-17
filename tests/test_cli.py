"""CLI de contrato offline: sem runtime, processos nativos ou conexão de rede."""
from contextlib import ExitStack, redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from acbr import __main__ as cli
from acbr._version import __version__
from acbr.contract import describe_field


class CliTests(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.forbidden = []
        for target in ("acbr.__main__.install_runtime", "acbr.__main__.verify_runtime",
                       "acbr.client.verify_runtime", "acbr.transport.ProcessTransport.execute",
                       "subprocess.Popen", "urllib.request.urlopen", "socket.create_connection", "socket.socket"):
            mock = self.stack.enter_context(patch(target, side_effect=AssertionError("OFFLINE_CLI_FORBIDS_RUNTIME_NETWORK")))
            self.forbidden.append(mock)

    def tearDown(self):
        for mock in self.forbidden:
            mock.assert_not_called()

    def run_cli(self, *args):
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            try:
                code = cli.main(list(args))
            except SystemExit as error:
                code = error.code
        return code, stdout.getvalue(), stderr.getvalue()

    def test_describe_enum_field_has_stable_human_output(self):
        code, stdout, stderr = self.run_cli("describe", "Ide.tpNF")
        expected = ("TNFe.Ide.tpNF\nTipo: TTipoNFe (enum; entrada string)\nSomente leitura: não\n"
                    "Valores: tnEntrada, tnSaida\n")
        # A default is shown only when the authenticated contract supplies it.
        value = describe_field("Ide.tpNF")
        if "declaredDefault" in value:
            expected += "Padrão declarado: " + value["declaredDefault"] + "\n"
        self.assertEqual((code, stdout, stderr), (0, expected, ""))
        self.assertEqual(self.run_cli("describe", "Ide.tpNF"), (code, stdout, stderr))

    def test_describe_enum_type_does_not_invent_field_default(self):
        code, stdout, stderr = self.run_cli("describe", "TTipoNFe")
        self.assertEqual((code, stdout, stderr), (0,
            "TTipoNFe\nTipo: TTipoNFe (enum; entrada string)\nSomente leitura: não\nValores: tnEntrada, tnSaida\n", ""))
        self.assertNotIn("Padrão declarado", stdout)

    def test_describe_json_is_exactly_the_existing_api_object(self):
        for target in ("Ide.tpNF", "TTipoNFe", "TProd", "Det", "Det[].Prod.vProd", "procNFe"):
            with self.subTest(target=target):
                code, stdout, stderr = self.run_cli("describe", target, "--json")
                self.assertEqual(code, 0)
                self.assertEqual(stderr, "")
                self.assertEqual(json.loads(stdout), describe_field(target))
                self.assertEqual(stdout, json.dumps(describe_field(target), ensure_ascii=False, indent=2) + "\n")

    def test_json_option_works_before_or_after_target(self):
        self.assertEqual(self.run_cli("describe", "--json", "TTipoNFe"), self.run_cli("describe", "TTipoNFe", "--json"))

    def test_default_target_is_tnfe_in_both_formats(self):
        self.assertEqual(self.run_cli("describe"), self.run_cli("describe", "TNFe"))
        code, stdout, stderr = self.run_cli("describe", "--json")
        self.assertEqual((code, stderr), (0, ""))
        self.assertEqual(json.loads(stdout), describe_field("TNFe"))

    def test_human_object_lists_fields_and_declared_types(self):
        code, stdout, stderr = self.run_cli("describe", "TProd")
        self.assertEqual((code, stderr), (0, ""))
        self.assertTrue(stdout.startswith("TProd\nTipo: TProd (object; entrada object)\n"))
        self.assertIn("\nCampos:\n", stdout)
        self.assertIn("  vProd: Currency (decimal)\n", stdout)
        self.assertIn("  xProd: string (string)\n", stdout)
        self.assertNotIn("Padrão declarado", stdout)

    def test_human_collection_and_numeric_index_normalization(self):
        code, stdout, stderr = self.run_cli("describe", "Det")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Tipo: TDetCollection (list; entrada array)", stdout)
        self.assertIn("Tipo dos itens: TDetCollectionItem\n", stdout)
        self.assertNotIn("Campos:", stdout)
        code, stdout, stderr = self.run_cli("describe", "Det[12].Prod.vProd")
        self.assertEqual((code, stderr), (0, ""))
        self.assertTrue(stdout.startswith("TNFe.Det[].Prod.vProd\n"))
        self.assertIn("Casas decimais: 4\n", stdout)

    def test_human_constraints_are_shown_only_when_declared(self):
        code, stdout, stderr = self.run_cli("describe", "Ide.cUF")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Mínimo: -2147483648\nMáximo: 2147483647\n", stdout)
        self.assertNotIn("Casas decimais", stdout)
        code, stdout, stderr = self.run_cli("describe", "Ide.dEmi")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("entrada string", stdout)
        for label in ("Mínimo", "Máximo", "Casas decimais", "Padrão declarado"):
            self.assertNotIn(label, stdout)

    def test_readonly_is_visible_for_field_and_object_members(self):
        code, stdout, stderr = self.run_cli("describe", "procNFe.cStat")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Somente leitura: sim\n", stdout)
        code, stdout, stderr = self.run_cli("describe", "procNFe")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Somente leitura: sim\n", stdout)
        self.assertIn("  cStat: Integer (integer) [somente leitura]\n", stdout)

    def test_human_declared_default_is_not_an_applied_value(self):
        code, stdout, stderr = self.run_cli("describe", "Ide.tpAmb")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIn("Padrão declarado: taHomologacao\n", stdout)
        self.assertNotIn("aplicado", stdout)

    def test_legacy_ajuda_json_format_and_default_are_unchanged(self):
        for args, target in (((), "TNFe"), (("Ide.tpNF",), "Ide.tpNF"), (("TTipoNFe",), "TTipoNFe")):
            with self.subTest(target=target):
                code, stdout, stderr = self.run_cli("ajuda", *args)
                self.assertEqual((code, stderr), (0, ""))
                self.assertEqual(stdout, json.dumps(describe_field(target), ensure_ascii=False, indent=2) + "\n")
                self.assertEqual((code, stdout, stderr), self.run_cli("describe", target, "--json"))

    def test_json_errors_keep_code_one_and_existing_safe_diagnostics(self):
        for target, expected in (("vBC", "CAMPO_AMBIGUO"), ("ide.cUF", "CAMPO_INEXISTENTE"),
                                 ("Det.Prod", "COLECAO_REQUER_INDICE"), ("Ide[]", "CAMPO_NAO_COLECAO"),
                                 ("Det[-1]", "CAMINHO_INVALIDO")):
            with self.subTest(target=target):
                legacy = self.run_cli("ajuda", target)
                current = self.run_cli("describe", target, "--json")
                self.assertEqual(current, legacy)
                code, stdout, stderr = current
                self.assertEqual((code, stderr), (1, ""))
                self.assertEqual(json.loads(stdout)["codigo"], expected)
                self.assertEqual(json.loads(stdout)["status_envio"], "nao_enviado")

    def test_human_error_goes_to_stderr_without_echoing_unknown_input(self):
        sentinel = "SYNTHETIC_PRIVATE_UNKNOWN_FIELD"
        code, stdout, stderr = self.run_cli("describe", sentinel)
        self.assertEqual((code, stdout), (1, ""))
        self.assertIn("Erro (CAMPO_INEXISTENTE):", stderr)
        self.assertIn("Ação:", stderr)
        self.assertNotIn(sentinel, stderr)

    def test_help_at_every_level_never_queries_contract_or_runtime(self):
        cases = (("--help",), ("describe", "--help"), ("ajuda", "--help"),
                 ("runtime", "--help"), ("runtime", "install", "--help"), ("doctor", "--help"))
        with patch.object(cli, "describe_field", side_effect=AssertionError("HELP_MUST_NOT_QUERY_CONTRACT")):
            for args in cases:
                with self.subTest(args=args):
                    code, stdout, stderr = self.run_cli(*args)
                    self.assertEqual((code, stderr), (0, ""))
                    self.assertIn("python -m acbr", stdout)
                    self.assertIn("Exemplo", stdout)
                    self.assertIn("--help", stdout)
        code, stdout, stderr = self.run_cli("describe", "--help")
        self.assertIn("TARGET", stdout)
        self.assertIn("--json", stdout)
        self.assertIn("TTipoNFe", stdout)

    def test_version_uses_the_shared_python_sdk_version_without_contract(self):
        with patch.object(cli, "describe_field", side_effect=AssertionError("VERSION_MUST_NOT_QUERY_CONTRACT")):
            self.assertEqual(self.run_cli("--version"), (0, f"acbr-python {__version__}\n", ""))

    def test_syntax_errors_keep_argparse_code_two_without_side_effects(self):
        for args in ((), ("describe", "Ide.tpNF", "TTipoNFe"), ("describe", "--invalid-option"),
                     ("ajuda", "--json"), ("runtime",), ("runtime", "install"), ("doctor",)):
            with self.subTest(args=args), patch.object(cli, "describe_field", side_effect=AssertionError("INVALID_SYNTAX_MUST_NOT_QUERY")):
                code, stdout, stderr = self.run_cli(*args)
                self.assertEqual((code, stdout), (2, ""))
                self.assertIn("python -m acbr", stderr)

    def test_existing_runtime_and_doctor_dispatch_remain_available_via_mocks(self):
        # These two explicit commands use synthetic return values only. The
        # help/describe tests above forbid even calling these functions.
        with patch.object(cli, "install_runtime", return_value=Path("new-runtime/runtime")) as install:
            code, stdout, stderr = self.run_cli("runtime", "install", "--directory", "new-runtime", "--archive", "native.tgz")
        self.assertEqual((code, stderr), (0, ""))
        self.assertEqual(json.loads(stdout), {"instalado": True, "runtime_directory": str(Path("new-runtime/runtime"))})
        install.assert_called_once_with(Path("new-runtime"), archive=Path("native.tgz"))
        native = SimpleNamespace(capabilities=frozenset({"recuperarXml"}))
        with patch.object(cli, "verify_runtime", return_value=native) as verify:
            code, stdout, stderr = self.run_cli("doctor", "--directory", "native/runtime")
        self.assertEqual((code, stderr), (0, ""))
        self.assertIs(json.loads(stdout)["integro"], True)
        self.assertEqual(json.loads(stdout)["capabilities"], ["recuperarXml"])
        verify.assert_called_once_with(Path("native/runtime"))


if __name__ == "__main__":
    unittest.main()
