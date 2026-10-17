import base64
from dataclasses import FrozenInstanceError
import json
import threading
import unittest
from unittest.mock import patch
from pathlib import Path
from types import SimpleNamespace

from acbr import (AcbrError, Cancelamento, CertificadoA1, Configuracao, Consulta, Csc,
                  Documento, Emissor, EventoEnvio, Inutilizacao)
from acbr.contract import CONTRACT_HASH, SOURCE_REVISION


KEY = "0" * 44
PROTOCOL = "0" * 15
REASON = "JUSTIFICATIVA SINTETICA DE TESTE"


class ClientTests(unittest.TestCase):
    @staticmethod
    def config(certificate=True):
        return Configuracao("0" * 14, "SP", certificado=CertificadoA1(b"SYNTHETIC-NOT-A-PFX", "synthetic-password") if certificate else None)

    @staticmethod
    def runtime():
        return SimpleNamespace(directory=Path("."), executable=Path("worker"), capabilities=frozenset({"recuperarXml"}))

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

    def test_operation_data_are_immutable_safe_and_match_worker_wire(self):
        values = [
            (Consulta(KEY), {"chave": KEY}),
            (Consulta(KEY, PROTOCOL), {"chave": KEY, "recibo": PROTOCOL}),
            (Cancelamento(KEY, PROTOCOL, REASON), {"chave": KEY, "protocolo": PROTOCOL, "justificativa": REASON}),
            (Inutilizacao(26, 0, 1, 2, REASON), {"inutilizacao": {"ano": 26, "serie": 0, "numeroInicial": 1, "numeroFinal": 2}, "justificativa": REASON}),
        ]
        for value, expected in values:
            with self.subTest(operation=type(value).__name__):
                self.assertEqual(value.to_wire(), expected)
                self.assertNotIn(KEY, repr(value))
                self.assertNotIn(PROTOCOL, repr(value))
                self.assertNotIn(REASON, repr(value))
                field = "ano" if isinstance(value, Inutilizacao) else "chave"
                with self.assertRaises(FrozenInstanceError):
                    setattr(value, field, 99)
                wire = value.to_wire()
                wire.clear()
                self.assertEqual(value.to_wire(), expected)

    def test_operation_digits_and_reasons_are_strict_without_fiscal_logic(self):
        cases = [
            (lambda: Consulta(0), "CHAVE_INVALIDA", "chave"),
            (lambda: Consulta("０" * 44), "CHAVE_INVALIDA", "chave"),
            (lambda: Consulta("0" * 43), "CHAVE_INVALIDA", "chave"),
            (lambda: Consulta(KEY, True), "RECIBO_INVALIDO", "recibo"),
            (lambda: Consulta(KEY, ""), "RECIBO_INVALIDO", "recibo"),
            (lambda: Cancelamento(KEY, "0" * 14, REASON), "PROTOCOLO_INVALIDO", "protocolo"),
            (lambda: Cancelamento(KEY, PROTOCOL, None), "JUSTIFICATIVA_INVALIDA", "justificativa"),
            (lambda: Cancelamento(KEY, PROTOCOL, "x" * 14), "JUSTIFICATIVA_INVALIDA", "justificativa"),
            (lambda: Cancelamento(KEY, PROTOCOL, "x" * 256), "JUSTIFICATIVA_INVALIDA", "justificativa"),
            (lambda: Cancelamento(KEY, PROTOCOL, "ç" * 200), "JUSTIFICATIVA_INVALIDA", "justificativa"),
            (lambda: Cancelamento(KEY, PROTOCOL, "😀" * 64), "JUSTIFICATIVA_INVALIDA", "justificativa"),
            (lambda: Cancelamento(KEY, PROTOCOL, "\ud800" * 15), "JUSTIFICATIVA_INVALIDA", "justificativa"),
            (lambda: Inutilizacao(26, 0, 1, 2, "x" * 14), "JUSTIFICATIVA_INVALIDA", "justificativa"),
        ]
        for operation, code, field in cases:
            with self.subTest(code=code, field=field):
                with self.assertRaises(AcbrError) as caught:
                    operation()
                self.assertEqual(caught.exception.codigo, code)
                self.assertEqual(caught.exception.diagnostico.campo, field)
        # Match NativeMotor's UTF-8 byte count, including accented/astral text.
        self.assertEqual(Cancelamento(KEY, PROTOCOL, "😀" * 4).justificativa, "😀" * 4)
        self.assertEqual(Cancelamento(KEY, PROTOCOL, "ç" * 127).justificativa, "ç" * 127)
        self.assertEqual(Cancelamento(KEY, PROTOCOL, "😀" * 63).justificativa, "😀" * 63)
        with self.assertRaises(AcbrError):
            Cancelamento(KEY, PROTOCOL, "ç" * 128)
        self.assertEqual(Cancelamento(KEY, PROTOCOL, "x" * 255).to_wire()["chave"], KEY)

    def test_inutilizacao_ranges_reject_bool_float_and_coercion(self):
        invalid = [(-1, 0, 1, 1), (100, 0, 1, 1), (2026, 0, 1, 1), (26, -1, 1, 1),
                   (26, 1000, 1, 1), (26, 1, 0, 1), (26, 1, 2, 1), (26, 1, 1, 1000000000),
                   (True, 1, 1, 1), (26, False, 1, 1), (26, 1, 1.0, 1), (26, 1, 1, "2")]
        for numbers in invalid:
            with self.subTest(numbers=numbers):
                with self.assertRaises(AcbrError) as caught:
                    Inutilizacao(*numbers, REASON)
                self.assertEqual(caught.exception.codigo, "INUTILIZACAO_INVALIDA")
                self.assertEqual(caught.exception.diagnostico.campo, "inutilizacao")
        self.assertEqual(Inutilizacao(0, 0, 1, 1, REASON).to_wire()["inutilizacao"]["ano"], 0)
        self.assertEqual(Inutilizacao(99, 999, 999999999, 999999999, REASON).to_wire()["inutilizacao"]["numeroFinal"], 999999999)

    def test_each_network_method_rejects_truthy_opt_in_before_runtime_and_certificate_serialization(self):
        with Emissor(self.config(), runtime_directory="absent") as emitter:
            methods = [lambda flag: emitter.transmitir(None, allow_network=flag),
                       lambda flag: emitter.consultar(None, allow_network=flag),
                       lambda flag: emitter.cancelar(None, allow_network=flag),
                       lambda flag: emitter.inutilizar(None, allow_network=flag),
                       lambda flag: emitter.recuperar_xml(None, allow_network=flag)]
            with patch("acbr.client.verify_runtime") as verify, patch.object(Configuracao, "to_wire") as config_wire, patch.object(emitter._transport, "execute") as execute:
                for operation in methods:
                    for flag in (False, None, 1, "true", object()):
                        with self.assertRaises(AcbrError) as caught:
                            operation(flag)
                        self.assertEqual(caught.exception.codigo, "REDE_NAO_AUTORIZADA")
                verify.assert_not_called()
                config_wire.assert_not_called()
                execute.assert_not_called()

    def test_certificate_is_required_before_runtime_for_signature_and_network_methods(self):
        with Emissor(self.config(False), runtime_directory="absent") as emitter:
            operations = [lambda: emitter.assinar("<NFe/>"),
                          lambda: emitter.transmitir("<NFe/>", allow_network=True),
                          lambda: emitter.consultar(Consulta(KEY), allow_network=True),
                          lambda: emitter.cancelar(Cancelamento(KEY, PROTOCOL, REASON), allow_network=True),
                          lambda: emitter.inutilizar(Inutilizacao(26, 1, 1, 2, REASON), allow_network=True),
                          lambda: emitter.recuperar_xml("<NFe/>", allow_network=True)]
            with patch("acbr.client.verify_runtime") as verify, patch.object(Configuracao, "to_wire") as config_wire, patch.object(emitter._transport, "execute") as execute:
                for operation in operations:
                    with self.assertRaises(AcbrError) as caught:
                        operation()
                    self.assertEqual(caught.exception.codigo, "CERTIFICADO_AUSENTE")
                verify.assert_not_called()
                config_wire.assert_not_called()
                execute.assert_not_called()

    def test_generation_and_validation_do_not_require_a_certificate(self):
        with patch("acbr.client.verify_runtime", return_value=self.runtime()), patch("acbr.client.runtime_environment", return_value={}):
            with Emissor(self.config(False), runtime_directory=".") as emitter, patch.object(emitter._transport, "execute", return_value="offline-mock") as execute:
                self.assertEqual(emitter.gerar_xml({}), "offline-mock")
                self.assertNotIn("certificado", execute.call_args.args[3]["config"])
                self.assertEqual(emitter.validar("<NFe/>"), "offline-mock")
                self.assertNotIn("certificado", execute.call_args.args[3]["config"])

    def test_new_public_methods_send_exact_protocol_data_and_forward_cancellation(self):
        xml = "<NFe>SINTÉTICO</NFe>"
        xml_wire = {"xmlBase64": base64.b64encode(xml.encode()).decode("ascii")}
        with patch("acbr.client.verify_runtime", return_value=self.runtime()) as verify, patch("acbr.client.runtime_environment", return_value={}):
            with Emissor(self.config(), runtime_directory=".") as emitter, patch.object(emitter._transport, "execute", return_value="offline-mock") as execute:
                cancel = threading.Event()
                operations = [
                    (lambda: emitter.assinar(xml, cancel=cancel), "assinar", xml_wire),
                    (lambda: emitter.transmitir(xml, allow_network=True, cancel=cancel), "transmitir", xml_wire),
                    (lambda: emitter.consultar(Consulta(KEY, PROTOCOL), allow_network=True, cancel=cancel), "consultar", {"chave": KEY, "recibo": PROTOCOL}),
                    (lambda: emitter.cancelar(Cancelamento(KEY, PROTOCOL, REASON), allow_network=True, cancel=cancel), "cancelar", {"chave": KEY, "protocolo": PROTOCOL, "justificativa": REASON}),
                    (lambda: emitter.inutilizar(Inutilizacao(26, 1, 1, 2, REASON), allow_network=True, cancel=cancel), "inutilizar", {"inutilizacao": {"ano": 26, "serie": 1, "numeroInicial": 1, "numeroFinal": 2}, "justificativa": REASON}),
                ]
                ids = set()
                for call, command, payload in operations:
                    with self.subTest(command=command):
                        self.assertEqual(call(), "offline-mock")
                        request = execute.call_args.args[3]
                        self.assertEqual(request["versao"], 1)
                        self.assertEqual(request["sourceRevision"], SOURCE_REVISION)
                        self.assertEqual(request["contractHash"], CONTRACT_HASH)
                        self.assertEqual(request["comando"], command)
                        self.assertEqual({key: value for key, value in request.items() if key not in {"id", "versao", "sourceRevision", "contractHash", "comando", "config"}}, payload)
                        self.assertEqual(base64.b64decode(request["config"]["certificado"]["pfxBase64"]), b"SYNTHETIC-NOT-A-PFX")
                        self.assertIs(execute.call_args.kwargs["cancel"], cancel)
                        self.assertNotIn("allow_network", request)
                        ids.add(request["id"])
                self.assertEqual(len(ids), len(operations))
                self.assertEqual(verify.call_count, len(operations))

    def test_wrong_operation_parameters_do_not_reach_runtime(self):
        with Emissor(self.config(), runtime_directory="absent") as emitter, patch("acbr.client.verify_runtime") as verify:
            for operation, invalid in [(emitter.consultar, {"chave": KEY}), (emitter.cancelar, Consulta(KEY)), (emitter.inutilizar, None)]:
                with self.assertRaises(AcbrError) as caught:
                    operation(invalid, allow_network=True)
                self.assertEqual(caught.exception.codigo, "OPERACAO_INVALIDA")
            verify.assert_not_called()

    def test_closed_and_cancelled_requests_fail_before_runtime(self):
        emitter = Emissor(self.config(), runtime_directory="absent")
        with patch("acbr.client.verify_runtime") as verify:
            with self.assertRaises(AcbrError) as caught:
                emitter.assinar("<NFe/>", cancel=True)
            self.assertEqual(caught.exception.codigo, "OPERACAO_INVALIDA")
            cancel = threading.Event()
            cancel.set()
            with self.assertRaises(AcbrError) as caught:
                emitter.assinar("<NFe/>", cancel=cancel)
            self.assertEqual(caught.exception.codigo, "OPERACAO_CANCELADA")
            emitter.fechar()
            emitter.fechar()
            with self.assertRaises(AcbrError) as caught:
                emitter.assinar("<NFe/>")
            self.assertEqual(caught.exception.codigo, "EMISSOR_FECHADO")
            verify.assert_not_called()

    def test_public_send_event_has_only_safe_id_and_command_and_is_frozen(self):
        event = EventoEnvio("a" * 32, "transmitir")
        self.assertEqual(event.id, "a" * 32)
        self.assertEqual(event.comando, "transmitir")
        self.assertEqual(event.__slots__, ("id", "comando"))
        with self.assertRaises(FrozenInstanceError):
            event.comando = "cancelar"
        for event_id, command in [(None, "transmitir"), ("x\ny", "cancelar"), ("x", "consultar")]:
            with self.assertRaises(AcbrError) as caught:
                EventoEnvio(event_id, command)
            self.assertEqual(caught.exception.codigo, "EVENTO_ENVIO_INVALIDO")

    def test_send_callback_is_validated_and_propagated_to_transport(self):
        events = []
        callback = events.append
        with patch("acbr.client.ProcessTransport") as transport:
            with Emissor(self.config(), runtime_directory=".", ao_iniciar_envio=callback):
                transport.assert_called_once_with(120, 8 * 1024 * 1024, ao_iniciar_envio=callback)
                self.assertEqual(events, [])
            transport.return_value.close.assert_called_once_with()
        for callback in (True, "callback", 1, []):
            with patch("acbr.client.ProcessTransport") as transport:
                with self.assertRaises(AcbrError) as caught:
                    Emissor(self.config(), runtime_directory=".", ao_iniciar_envio=callback)
                self.assertEqual(caught.exception.codigo, "CONFIGURACAO_INVALIDA")
                self.assertEqual(caught.exception.diagnostico.campo, "ao_iniciar_envio")
                transport.assert_not_called()


if __name__ == "__main__":
    unittest.main()
