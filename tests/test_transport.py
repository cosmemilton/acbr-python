import base64
import json
import os
from pathlib import Path
import sys
import threading
import time
import unittest
from unittest.mock import patch
import io
import subprocess

from acbr.contract import CONTRACT_HASH, SOURCE_REVISION
from acbr import EventoEnvio
from acbr.errors import AcbrError
from acbr.transport import ProcessTransport

FIXTURE = Path(__file__).with_name("fixtures_worker.py").resolve()


class MockPipe:
    """Pipe sintética bloqueada até kill, sem criar qualquer processo."""
    def __init__(self, process, chunks=()):
        self.process = process
        self.chunks = list(chunks)
        self.closed = False

    def read(self, size):
        if self.chunks:
            return self.chunks.pop(0)
        self.process.stopped.wait()
        return b""

    def close(self):
        self.closed = True


class MockProcess:
    def __init__(self, *, refuse_kill=False, stdout=(), bad_stdin=False):
        self.stopped = threading.Event()
        self.payload = None
        owner = self
        class CapturingInput(io.BytesIO):
            def write(self, data):
                owner.payload = data.obj
                return super().write(data)
        self.stdin = CapturingInput()
        if bad_stdin:
            class BrokenInput(io.BytesIO):
                def write(self, data):
                    raise OSError("PRIVATE-SYNTHETIC")
            self.stdin = BrokenInput()
        self.stdout = MockPipe(self, stdout)
        self.stderr = MockPipe(self)
        self.refuse_kill = refuse_kill
        self.returncode = None
        self.kill_calls = 0

    def poll(self):
        if self.stopped.is_set():
            self.returncode = -9
        return self.returncode

    def kill(self):
        self.kill_calls += 1
        if self.refuse_kill:
            raise OSError("PRIVATE-SYNTHETIC")
        self.stopped.set()

    def wait(self, timeout):
        if self.poll() is None:
            raise subprocess.TimeoutExpired("mock", timeout)
        return self.returncode


class TransportTests(unittest.TestCase):
    def request(self, cmd="gerarXml"):
        request = {"versao": 1, "sourceRevision": SOURCE_REVISION, "contractHash": CONTRACT_HASH,
                   "id": "synthetic", "comando": cmd, "config": {}}
        if cmd in {"consultar", "cancelar"}:
            request["chave"] = "1" * 44
        if cmd == "transmitir":
            request["xmlBase64"] = base64.b64encode("<NFe>ORIGINAL SINTÉTICO\n</NFe>".encode()).decode()
        return request

    def run_worker(self, mode, *, transport=None, cancel=None, request=None):
        return (transport or ProcessTransport(timeout=5)).execute(
            Path(sys.executable), FIXTURE.parent, dict(os.environ), request or self.request(),
            cancel=cancel, _args=(str(FIXTURE), mode))

    def test_valid_fragmented_utf8_and_safe_result(self):
        result = self.run_worker("slow")
        self.assertEqual(result.xml, "<NFe>SINTÉTICO</NFe>")
        self.assertTrue(result.sucesso)
        self.assertNotIn("SINTÉTICO", repr(result))
        self.assertNotIn("xml", json.dumps(result.to_dict()))

    def test_invalid_frames_and_exit(self):
        for mode in ("wrong_id", "contract", "version_bool", "state", "failure_state", "unknown_type", "xml", "utf8",
                     "duplicate_key", "nan", "empty", "partial", "duplicate", "trailing", "nonzero"):
            with self.subTest(mode=mode), self.assertRaises(AcbrError) as caught:
                self.run_worker(mode)
            self.assertIn(caught.exception.codigo, ("RESPOSTA_INVALIDA", "FALHA_MOTOR"))
            self.assertTrue(caught.exception.limpeza_confirmada)

    def test_stderr_drained_and_counted_without_leak(self):
        self.assertTrue(self.run_worker("stderr").sucesso)
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("stderr", transport=ProcessTransport(timeout=5, max_bytes=1024))
        self.assertEqual(caught.exception.codigo, "RESPOSTA_EXCESSIVA")
        self.assertNotIn("SEGREDO", str(caught.exception) + repr(caught.exception))

    def test_raw_code_does_not_leak_into_safe_repr(self):
        result = self.run_worker("secret_code")
        self.assertEqual(result.codigo, "SYNTHETIC-PASSWORD-SENTINEL")
        self.assertNotIn("SYNTHETIC-PASSWORD", repr(result) + json.dumps(result.to_dict()))

    def test_original_worker_frame_keeps_extra_fields_out_of_safe_logs(self):
        result = self.run_worker("original", request=self.request("consultar"))
        original = result.retorno_original
        self.assertEqual("acbr_worker_jsonl", result.origem_retorno_original)
        self.assertEqual("SYNTHETIC-PRIVATE-WORKER-RETURN", original["xMotivo"])
        self.assertEqual(result.c_stat, original["cStat"])
        self.assertEqual(result.protocolo, original["protocolo"])
        self.assertEqual(result.xml_base64, original["xmlBase64"])
        self.assertEqual("SYNTHETIC-PRIVATE-WORKER-RETURN", original["extraACBr"]["itens"][2]["codigoExtra"])
        original["extraACBr"]["itens"].clear()
        self.assertEqual(3, len(result.retorno_original["extraACBr"]["itens"]))
        self.assertNotIn("PRIVATE", repr(result) + json.dumps(result.to_dict()))
        self.assertNotIn("soap", result.retorno_original)

    def test_native_error_frame_is_preserved_without_fabricating_missing_fields(self):
        result = self.run_worker("original_error", request=self.request("transmitir"))
        self.assertFalse(result.sucesso)
        self.assertEqual("ERRO", result.estado)
        self.assertEqual("SYNTHETIC-PRIVATE-CODE", result.retorno_original["codigo"])
        self.assertEqual("SYNTHETIC-PRIVATE-WORKER-RETURN", result.retorno_original["xMotivo"])
        for absent in ("cStat", "protocolo", "xmlBase64", "soap"):
            self.assertNotIn(absent, result.retorno_original)
        self.assertIsNone(result.c_stat)
        self.assertIsNone(result.xml)
        self.assertNotIn("PRIVATE", repr(result) + json.dumps(result.to_dict()))

    def test_transport_error_after_valid_terminal_preserves_only_valid_frame(self):
        for mode, code in (("original_nonzero", "FALHA_MOTOR"), ("original_invalid_after", "RESPOSTA_INVALIDA"),
                           ("original_timeout", "TIMEOUT_MOTOR")):
            with self.subTest(mode=mode), self.assertRaises(AcbrError) as caught:
                # Preserve the terminal frame without requiring Python startup in 500 ms.
                self.run_worker(mode, request=self.request("transmitir"), transport=ProcessTransport(timeout=5))
            error = caught.exception
            self.assertEqual(code, error.codigo)
            self.assertTrue(error.resultado_desconhecido)
            self.assertEqual("AUTORIZADO", error.retorno_original["estado"])
            self.assertEqual("SYNTHETIC-PRIVATE-WORKER-RETURN", error.retorno_original["xMotivo"])
            self.assertEqual("acbr_worker_jsonl", error.origem_retorno_original)
            self.assertNotIn("PRIVATE", repr(error) + str(error) + json.dumps(error.diagnostico.to_dict()))
            self.assertEqual(base64.b64decode(self.request("transmitir")["xmlBase64"]).decode(), error.xml_original)

    def test_invalid_or_absent_frames_are_not_exposed_as_original(self):
        for command, mode in (("gerarXml", "wrong_id"), ("gerarXml", "empty"), ("gerarXml", "partial"),
                              ("transmitir", "no_marker"), ("transmitir", "bad_state_code")):
            with self.subTest(command=command, mode=mode), self.assertRaises(AcbrError) as caught:
                self.run_worker(mode, request=self.request(command))
            self.assertIsNone(caught.exception.retorno_original)
            self.assertIsNone(caught.exception.origem_retorno_original)

    def test_unconfirmed_cleanup_keeps_previously_validated_terminal_frame(self):
        request = self.request("transmitir")
        final = {key: request[key] for key in ("id", "versao", "sourceRevision", "contractHash")}
        final.update(sucesso=True, estado="AUTORIZADO", envioIniciado=True, cStat=100,
                     chave="1" * 44, protocolo="1" * 15, xmlBase64=request["xmlBase64"], extra={"private": "SYNTHETIC-PRIVATE"})
        marker = {"id": request["id"], "tipo": "envioIniciado"}
        process = MockProcess(refuse_kill=True, stdout=[(json.dumps(marker) + "\n").encode(), (json.dumps(final) + "\n").encode()])
        try:
            with patch("acbr.transport.subprocess.Popen", return_value=process):
                with self.assertRaises(AcbrError) as caught:
                    self.run_worker("ok", request=request, transport=ProcessTransport(timeout=.15))
            self.assertTrue(caught.exception.resultado_desconhecido)
            self.assertFalse(caught.exception.limpeza_confirmada)
            self.assertEqual(final, caught.exception.retorno_original)
            self.assertNotIn("PRIVATE", repr(caught.exception) + str(caught.exception))
        finally:
            process.stopped.set()

    def test_stdout_flood_is_bounded(self):
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("flood", transport=ProcessTransport(timeout=5, max_bytes=1024))
        self.assertEqual(caught.exception.codigo, "RESPOSTA_EXCESSIVA")

    def test_timeout_includes_blocked_stdin(self):
        for mode in ("hang", "no_read"):
            request = self.request()
            request["documento"] = {"large": "X" * 1024 * 1024}
            started = time.monotonic()
            with self.subTest(mode=mode), self.assertRaises(AcbrError) as caught:
                self.run_worker(mode, transport=ProcessTransport(timeout=.3), request=request)
            self.assertEqual(caught.exception.codigo, "TIMEOUT_MOTOR")
            self.assertTrue(caught.exception.limpeza_confirmada)
            self.assertLess(time.monotonic() - started, 2)

    def test_cancel_before_and_during(self):
        cancel = threading.Event()
        cancel.set()
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("hang", cancel=cancel)
        self.assertEqual(caught.exception.codigo, "OPERACAO_CANCELADA")
        cancel.clear()
        timer = threading.Timer(.3, cancel.set)
        timer.start()
        try:
            with self.assertRaises(AcbrError) as caught:
                self.run_worker("hang", cancel=cancel)
            self.assertEqual(caught.exception.codigo, "OPERACAO_CANCELADA")
        finally:
            timer.cancel()

    def test_close_while_running_and_reuse_rejected(self):
        transport = ProcessTransport(timeout=5)
        timer = threading.Timer(.3, transport.close)
        timer.start()
        try:
            with self.assertRaises(AcbrError) as caught:
                self.run_worker("hang", transport=transport)
            self.assertEqual(caught.exception.codigo, "EMISSOR_FECHADO")
            with self.assertRaises(AcbrError):
                self.run_worker("ok", transport=transport)
        finally:
            timer.cancel()

    def test_recovery_contract_and_send_marker(self):
        request = self.request("recuperarXml")
        self.assertEqual(self.run_worker("ok", request=request).estado, "XML_RECUPERADO")
        with self.assertRaises(AcbrError):
            self.run_worker("recover150", request=request)
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("marker")
        self.assertFalse(caught.exception.resultado_desconhecido)

    def test_new_commands_success_and_native_diagnostics(self):
        expected = {"assinar": ("ASSINADO", "nao_enviado", False),
                    "transmitir": ("AUTORIZADO", "autorizado", True),
                    "consultar": ("AUTORIZADO", "autorizado", False),
                    "cancelar": ("CANCELADO", "cancelado", True),
                    "inutilizar": ("INUTILIZADO", "inutilizado", True)}
        for command, (state, status, sending) in expected.items():
            with self.subTest(command=command):
                result = self.run_worker("ok", request=self.request(command))
                self.assertTrue(result.sucesso)
                self.assertEqual(state, result.estado)
                self.assertEqual(status, result.diagnostico.status_envio)
                self.assertEqual(sending, result.envio_iniciado)
                if command == "inutilizar":
                    self.assertIsNone(result.chave)

    def test_query_statuses_are_not_misreported_as_authorization(self):
        expected = {100: ("AUTORIZADO", True), 150: ("AUTORIZADO", True),
                    101: ("CANCELADO", True), 151: ("CANCELADO", True), 155: ("CANCELADO", True),
                    217: ("CONSULTADO", True), 110: ("DENEGADO", False), 301: ("DENEGADO", False),
                    302: ("DENEGADO", False), 103: ("PENDENTE", False), 104: ("PENDENTE", False),
                    105: ("PENDENTE", False), 108: ("PENDENTE", False), 109: ("PENDENTE", False),
                    204: ("PENDENTE", False), 539: ("PENDENTE", False), 573: ("PENDENTE", False),
                    999: ("REJEITADO", False)}
        for status, (state, success) in expected.items():
            with self.subTest(status=status):
                result = self.run_worker("status_" + str(status), request=self.request("consultar"))
                self.assertEqual((state, success), (result.estado, result.sucesso))
                self.assertFalse(result.envio_iniciado)
                if status == 217:
                    self.assertEqual("nao_autorizado", result.diagnostico.status_envio)
        result = self.run_worker("recovery_unproven", request=self.request("recuperarXml"))
        self.assertFalse(result.sucesso)
        self.assertIsNone(result.xml)
        self.assertEqual("nao_autorizado", result.diagnostico.status_envio)

    def test_mutation_uncertainty_after_spawn_without_marker_and_original_xml(self):
        for command in ("transmitir", "cancelar", "inutilizar"):
            request = self.request(command)
            with self.subTest(command=command), self.assertRaises(AcbrError) as caught:
                self.run_worker("hang", request=request, transport=ProcessTransport(timeout=.15))
            error = caught.exception
            self.assertEqual("TIMEOUT_MOTOR", error.codigo)
            self.assertTrue(error.resultado_desconhecido)
            if command == "transmitir":
                self.assertEqual(base64.b64decode(request["xmlBase64"]).decode(), error.xml_original)
                self.assertNotIn("ORIGINAL", repr(error) + str(error) + json.dumps(error.diagnostico.to_dict()))
            else:
                self.assertIsNone(error.xml_original)

    def test_read_and_local_timeout_never_invent_send_outcome(self):
        for command in ("assinar", "consultar", "recuperarXml"):
            with self.subTest(command=command), self.assertRaises(AcbrError) as caught:
                self.run_worker("hang", request=self.request(command), transport=ProcessTransport(timeout=.15))
            self.assertFalse(caught.exception.resultado_desconhecido)
            self.assertIsNone(caught.exception.xml_original)

    def test_mutating_marker_order_flags_and_state_code_are_strict(self):
        modes = ("no_marker", "duplicate_marker", "late_marker", "wrong_marker_id", "extra_marker",
                 "false_send", "missing_send", "bool_send", "bad_state_code", "bad_receipt", "bad_protocol", "no_protocol")
        for command in ("transmitir", "cancelar", "inutilizar"):
            for mode in modes:
                with self.subTest(command=command, mode=mode), self.assertRaises(AcbrError) as caught:
                    self.run_worker(mode, request=self.request(command))
                self.assertTrue(caught.exception.resultado_desconhecido)
                self.assertEqual("RESPOSTA_INVALIDA", caught.exception.codigo)
        for command in ("assinar", "consultar", "recuperarXml"):
            with self.subTest(command=command), self.assertRaises(AcbrError) as caught:
                self.run_worker("marker", request=self.request(command))
            self.assertFalse(caught.exception.resultado_desconhecido)

    def test_remote_result_keys_are_correlated_and_xml_rules_are_operation_specific(self):
        for command in ("consultar", "cancelar"):
            with self.subTest(command=command), self.assertRaises(AcbrError):
                self.run_worker("wrong_key", request=self.request(command))
        for command in ("assinar", "transmitir", "inutilizar"):
            with self.subTest(command=command), self.assertRaises(AcbrError):
                self.run_worker("no_xml", request=self.request(command))
        # Consulta informa o protocolo/situação: não promete nfeProc nem XML recuperado.
        self.assertTrue(self.run_worker("no_xml", request=self.request("consultar")).sucesso)
        request = {**self.request("consultar"), "recibo": "1" * 15}
        self.assertEqual(request["recibo"], self.run_worker("ok", request=request).recibo)
        for mode in ("wrong_receipt", "no_receipt"):
            with self.subTest(mode=mode), self.assertRaises(AcbrError) as caught:
                self.run_worker(mode, request=request)
            self.assertFalse(caught.exception.resultado_desconhecido)

    def test_pending_and_native_indeterminate_results(self):
        for command in ("transmitir", "cancelar", "inutilizar"):
            with self.subTest(command=command):
                result = self.run_worker("indeterminate", request=self.request(command))
                self.assertFalse(result.sucesso)
                self.assertTrue(result.envio_iniciado)
                self.assertEqual("resultado_incerto", result.diagnostico.status_envio)
                self.assertNotIn("SINTÉTICO", repr(result) + json.dumps(result.to_dict()))
                if command == "transmitir":
                    self.assertEqual(base64.b64decode(self.request(command)["xmlBase64"]).decode(), result.xml)
        result = self.run_worker("status_204", request=self.request("transmitir"))
        self.assertEqual(("PENDENTE", False), (result.estado, result.sucesso))
        self.assertEqual("pendente", result.diagnostico.status_envio)

    def test_preflight_failure_without_marker_is_not_a_fiscal_success(self):
        for command in ("assinar", "consultar", "transmitir", "cancelar", "inutilizar"):
            with self.subTest(command=command):
                result = self.run_worker("native_error", request=self.request(command))
                self.assertEqual((False, "ERRO", False), (result.sucesso, result.estado, result.envio_iniciado))
                self.assertEqual("nao_enviado", result.diagnostico.status_envio)
                self.assertNotIn("PRIVATE", repr(result) + json.dumps(result.to_dict()))

    def test_indeterminate_xml_cannot_replace_signed_original(self):
        request = self.request("transmitir")
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("indeterminate_altered_xml", request=request)
        self.assertEqual("RESPOSTA_INVALIDA", caught.exception.codigo)
        self.assertTrue(caught.exception.resultado_desconhecido)
        self.assertEqual(base64.b64decode(request["xmlBase64"]).decode(), caught.exception.xml_original)
        self.assertNotIn("ALTERED", repr(caught.exception))

    def test_structured_send_hook_fires_once_without_fiscal_payload(self):
        for command in ("transmitir", "cancelar", "inutilizar"):
            observed = []
            with self.subTest(command=command):
                result = self.run_worker("ok", request=self.request(command),
                    transport=ProcessTransport(ao_iniciar_envio=observed.append))
                self.assertTrue(result.sucesso)
                self.assertEqual([EventoEnvio(id="synthetic", comando=command)], observed)
                self.assertEqual({"id", "comando"}, set(observed[0].__slots__))
        observed = []
        with self.assertRaises(AcbrError):
            self.run_worker("duplicate_marker", request=self.request("transmitir"),
                transport=ProcessTransport(ao_iniciar_envio=observed.append))
        self.assertEqual(1, len(observed))
        observed.clear()
        with self.assertRaises(AcbrError):
            self.run_worker("wrong_marker_id", request=self.request("transmitir"),
                transport=ProcessTransport(ao_iniciar_envio=observed.append))
        self.assertEqual([], observed)
        for command in ("gerarXml", "validar", "assinar", "consultar", "recuperarXml"):
            self.run_worker("ok", request=self.request(command),
                transport=ProcessTransport(ao_iniciar_envio=observed.append))
        self.assertEqual([], observed)

    def test_send_hook_failure_is_safe_uncertain_and_keeps_input_xml(self):
        def fail(event):
            raise RuntimeError("PRIVATE-SYNTHETIC")
        request = self.request("transmitir")
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("ok", request=request, transport=ProcessTransport(ao_iniciar_envio=fail))
        self.assertEqual("FALHA_EVENTO_ENVIO", caught.exception.codigo)
        self.assertTrue(caught.exception.resultado_desconhecido)
        self.assertEqual(base64.b64decode(request["xmlBase64"]).decode(), caught.exception.xml_original)
        self.assertNotIn("PRIVATE", str(caught.exception) + repr(caught.exception))

    def test_blocked_send_hook_is_bounded_and_disables_reuse(self):
        gate = threading.Event()
        marker = (json.dumps({"id": "synthetic", "tipo": "envioIniciado"}) + "\n").encode()
        process = MockProcess(stdout=[marker])
        transport = ProcessTransport(timeout=.5, ao_iniciar_envio=lambda event: gate.wait())
        started = time.monotonic()
        try:
            with patch("acbr.transport.subprocess.Popen", return_value=process):
                with self.assertRaises(AcbrError) as caught:
                    self.run_worker("ok", request=self.request("transmitir"), transport=transport)
            self.assertEqual("TIMEOUT_MOTOR", caught.exception.codigo)
            self.assertTrue(caught.exception.resultado_desconhecido)
            self.assertFalse(caught.exception.limpeza_confirmada)
            self.assertTrue(transport._closed.is_set())
            self.assertLess(time.monotonic() - started, 2)
        finally:
            gate.set()
            process.stopped.set()

    def test_blocked_send_hook_does_not_retain_request_byte_buffer(self):
        gate = threading.Event()
        marker = (json.dumps({"id": "synthetic", "tipo": "envioIniciado"}) + "\n").encode()
        process = MockProcess(stdout=[marker])
        transport = ProcessTransport(timeout=.5, ao_iniciar_envio=lambda event: gate.wait())
        try:
            with patch("acbr.transport.subprocess.Popen", return_value=process):
                with self.assertRaises(AcbrError) as caught:
                    self.run_worker("ok", request=self.request("transmitir"), transport=transport)
            self.assertTrue(caught.exception.resultado_desconhecido)
            self.assertIsNotNone(process.payload)
            self.assertEqual(b"\0" * len(process.payload), process.payload)
        finally:
            gate.set()
            process.stopped.set()

    def test_send_hook_cancellation_and_close_are_uncertain(self):
        for close in (False, True):
            cancel = threading.Event()
            transport = ProcessTransport()
            transport.ao_iniciar_envio = (lambda event: transport.close()) if close else (lambda event: cancel.set())
            with self.subTest(close=close), self.assertRaises(AcbrError) as caught:
                self.run_worker("ok", request=self.request("cancelar"), transport=transport, cancel=cancel)
            self.assertEqual("EMISSOR_FECHADO" if close else "OPERACAO_CANCELADA", caught.exception.codigo)
            self.assertTrue(caught.exception.resultado_desconhecido)

    def test_thread_start_failure_still_cleans_owned_process_and_hides_payload(self):
        process = MockProcess()
        transport = ProcessTransport()
        with patch("acbr.transport.subprocess.Popen", return_value=process), patch("acbr.transport.threading.Thread.start", side_effect=RuntimeError("PRIVATE-SYNTHETIC")):
            with self.assertRaises(AcbrError) as caught:
                self.run_worker("ok", request=self.request("transmitir"), transport=transport)
        self.assertEqual("FALHA_MOTOR", caught.exception.codigo)
        self.assertTrue(caught.exception.resultado_desconhecido)
        self.assertTrue(caught.exception.limpeza_confirmada)
        self.assertTrue(process.stopped.is_set())
        self.assertTrue(all(pipe.closed for pipe in (process.stdin, process.stdout, process.stderr)))
        self.assertIsNone(transport._active)

    def test_pipe_failure_and_unconfirmed_teardown_are_uncertain_without_marker(self):
        for bad_stdin in (False, True):
            process = MockProcess(refuse_kill=not bad_stdin, bad_stdin=bad_stdin)
            # Only the stalled-process case tests the short deadline; a broken
            # writer must have time to report its distinct pipe error.
            transport = ProcessTransport(timeout=5 if bad_stdin else .06)
            try:
                with self.subTest(bad_stdin=bad_stdin), patch("acbr.transport.subprocess.Popen", return_value=process) as spawn:
                    with self.assertRaises(AcbrError) as caught:
                        self.run_worker("ok", request=self.request("transmitir"), transport=transport)
                spawn.assert_called_once()
                self.assertEqual("FALHA_PIPE" if bad_stdin else "TIMEOUT_MOTOR", caught.exception.codigo)
                self.assertTrue(caught.exception.resultado_desconhecido)
                self.assertEqual(bad_stdin, caught.exception.limpeza_confirmada)
                self.assertNotIn("PRIVATE", str(caught.exception))
            finally:
                process.stopped.set()

    def test_busy_has_no_hidden_queue_or_extra_spawn(self):
        process = MockProcess()
        transport = ProcessTransport(timeout=.5)
        entered = threading.Event()
        errors = []
        def launch(*args, **kwargs):
            entered.set()
            return process
        def first():
            try:
                self.run_worker("ok", request=self.request("transmitir"), transport=transport)
            except AcbrError as error:
                errors.append(error)
        with patch("acbr.transport.subprocess.Popen", side_effect=launch) as spawn:
            owner = threading.Thread(target=first)
            owner.start()
            self.assertTrue(entered.wait(timeout=1))
            try:
                with self.assertRaises(AcbrError) as caught:
                    self.run_worker("ok", request=self.request("transmitir"), transport=transport)
                self.assertEqual("EMISSOR_OCUPADO", caught.exception.codigo)
                self.assertFalse(caught.exception.resultado_desconhecido)
                spawn.assert_called_once()
            finally:
                transport.close()
                owner.join(timeout=2)
            self.assertFalse(owner.is_alive())
            self.assertTrue(errors[0].resultado_desconhecido)

    def test_spawn_failure_is_known_and_never_retried(self):
        for command in ("transmitir", "cancelar", "inutilizar"):
            with self.subTest(command=command), patch("acbr.transport.subprocess.Popen", side_effect=OSError("PRIVATE")) as spawn:
                with self.assertRaises(AcbrError) as caught:
                    self.run_worker("ok", request=self.request(command))
                spawn.assert_called_once()
                self.assertEqual("FALHA_INICIAR_MOTOR", caught.exception.codigo)
                self.assertFalse(caught.exception.resultado_desconhecido)
                self.assertIsNone(caught.exception.xml_original)

    def test_unsupported_command_rejected_without_spawn(self):
        with patch("acbr.transport.subprocess.Popen") as spawn, self.assertRaises(AcbrError) as caught:
            self.run_worker("ok", request=self.request("cartaCorrecao"))
        spawn.assert_not_called()
        self.assertEqual("OPERACAO_NAO_SUPORTADA", caught.exception.codigo)

    def test_cancellation_proc_evento_preserves_worker_xml_and_original_frame(self):
        """Fixture anônima estrutural; AA== não constitui assinatura/certificado válido."""
        import xml.etree.ElementTree as ET

        raw = (FIXTURE.parent / "fixtures" / "cancelamento-procEvento-anon.xml").read_bytes()
        ns = "{http://www.portalfiscal.inf.br/nfe}"
        root = ET.fromstring(raw)
        self.assertEqual(ns + "procEventoNFe", root.tag)
        self.assertIsNotNone(root.find(ns + "evento/" + ns + "infEvento"))
        returned = root.find(ns + "retEvento/" + ns + "infEvento")
        self.assertIsNotNone(returned)
        request = {**self.request("cancelar"), "chave": returned.findtext(ns + "chNFe")}
        frame = {key: request[key] for key in ("id", "versao", "sourceRevision", "contractHash")}
        frame.update(sucesso=True, estado="CANCELADO", envioIniciado=True,
                     cStat=int(returned.findtext(ns + "cStat")), xMotivo=returned.findtext(ns + "xMotivo"),
                     chave=request["chave"], protocolo=returned.findtext(ns + "nProt"),
                     xmlBase64=base64.b64encode(raw).decode("ascii"))

        with patch("acbr.transport.subprocess.Popen") as spawn:
            result = ProcessTransport._result(frame, request, sending=True)
        spawn.assert_not_called()
        self.assertEqual((True, "CANCELADO", 135, True),
                         (result.sucesso, result.estado, result.c_stat, result.envio_iniciado))
        self.assertEqual("Evento sintetico registrado e vinculado a NF-e", result.x_motivo)
        self.assertEqual("0" * 15, result.protocolo)
        self.assertEqual(raw, base64.b64decode(result.xml_base64, validate=True))
        self.assertEqual(raw, result.xml.encode("utf-8"))
        self.assertEqual(frame, result.retorno_original)
        self.assertEqual("acbr_worker_jsonl", result.origem_retorno_original)
        self.assertNotIn("<procEventoNFe", repr(result) + json.dumps(result.to_dict()))

    def test_request_and_limits_validation(self):
        for timeout in (True, 0, 121, float("nan"), float("inf")):
            with self.assertRaises(AcbrError):
                ProcessTransport(timeout=timeout)
        with self.assertRaises(AcbrError) as caught:
            self.run_worker("ok", transport=ProcessTransport(max_bytes=256),
                            request={**self.request(), "documento": "X" * 1000})
        self.assertEqual(caught.exception.codigo, "REQUISICAO_EXCESSIVA")


if __name__ == "__main__":
    unittest.main()
