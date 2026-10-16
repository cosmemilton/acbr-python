import json
import os
from pathlib import Path
import sys
import threading
import time
import unittest

from acbr.contract import CONTRACT_HASH, SOURCE_REVISION
from acbr.errors import AcbrError
from acbr.transport import ProcessTransport

FIXTURE = Path(__file__).with_name("fixtures_worker.py").resolve()


class TransportTests(unittest.TestCase):
    def request(self, cmd="gerarXml"):
        return {"versao": 1, "sourceRevision": SOURCE_REVISION, "contractHash": CONTRACT_HASH,
                "id": "synthetic", "comando": cmd, "config": {}}

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
        self.assertTrue(caught.exception.resultado_desconhecido)

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
