"""Transporte JSONL limitado e portátil, um processo próprio por operação."""
from __future__ import annotations

import base64
import binascii
import json
import math
import os
import queue
import re
import subprocess
import threading
import time
from pathlib import Path

from .errors import AcbrError, Diagnostico
from .result import ResultadoFiscal

STATES = frozenset("DENEGADO XML_GERADO VALIDADO ASSINADO XML_RECUPERADO AUTORIZADO REJEITADO PENDENTE INDETERMINADO CONSULTADO CANCELADO EVENTO_REGISTRADO INUTILIZADO ERRO".split())
MAX_BYTES = 8 * 1024 * 1024


def _strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError("nonfinite")


class ProcessTransport:
    def __init__(self, timeout: float = 120, max_bytes: int = MAX_BYTES):
        if type(timeout) not in (float, int) or not math.isfinite(timeout) or not 0 < timeout <= 120 or type(max_bytes) is not int or not 256 <= max_bytes <= MAX_BYTES:
            raise AcbrError("CONFIGURACAO_INVALIDA", "Prazo ou limite de bytes inválido.")
        self.timeout = timeout
        self.max_bytes = max_bytes
        self._closed = threading.Event()
        self._lock = threading.Lock()
        self._active_lock = threading.Lock()
        self._active: subprocess.Popen | None = None

    def close(self) -> None:
        self._closed.set()
        with self._active_lock:
            process = self._active
        if process is not None:
            self._terminate(process)

    @staticmethod
    def _terminate(process) -> bool:
        try:
            if process.poll() is None:
                process.kill()
            process.wait(timeout=1)
            return True
        except (OSError, subprocess.TimeoutExpired):
            return False

    def execute(self, executable: Path, directory: Path, environment: dict[str, str], request: dict,
                *, cancel: threading.Event | None = None, _args: tuple[str, ...] = ()) -> ResultadoFiscal:
        # Nonblocking acquisition: no hidden unbounded queue. Caller can schedule explicitly.
        if not self._lock.acquire(blocking=False):
            raise AcbrError("EMISSOR_OCUPADO", "Aguarde a operação em andamento.")
        try:
            return self._execute(executable, directory, environment, request, cancel, _args)
        finally:
            self._lock.release()

    def _execute(self, executable, directory, environment, request, cancel, args):
        if cancel is not None and not isinstance(cancel, threading.Event):
            raise AcbrError("OPERACAO_INVALIDA", "Cancelamento exige threading.Event.")
        if self._closed.is_set():
            raise AcbrError("EMISSOR_FECHADO", "Emissor encerrado.")
        if cancel is not None and cancel.is_set():
            raise AcbrError("OPERACAO_CANCELADA", "Operação cancelada antes da execução.")
        try:
            payload = bytearray((json.dumps(request, ensure_ascii=False, allow_nan=False, separators=(",", ":")) + "\n").encode("utf-8"))
        except (TypeError, ValueError, UnicodeError, RecursionError):
            raise AcbrError("REQUISICAO_INVALIDA", "Dados não serializáveis.") from None
        if len(payload) > self.max_bytes:
            payload[:] = b"\0" * len(payload)
            raise AcbrError("REQUISICAO_EXCESSIVA", "Requisição excede o limite de bytes.")
        process = None
        sending = False
        error = None
        clean = True
        events: queue.Queue = queue.Queue(maxsize=32)
        stop = threading.Event()
        total = 0
        overflow = threading.Event()
        counters = threading.Lock()
        threads = []
        deadline = time.monotonic() + self.timeout

        def put(item):
            while not stop.is_set():
                try:
                    events.put(item, timeout=.02)
                    return
                except queue.Full:
                    continue

        def reader(pipe, channel):
            nonlocal total
            try:
                while not stop.is_set():
                    chunk = pipe.read(65536)
                    if not chunk:
                        break
                    with counters:
                        total += len(chunk)
                        if total > self.max_bytes:
                            overflow.set()
                            break
                    if channel == "stdout":
                        put((channel, chunk))
                put((channel, None))
            except (OSError, ValueError):
                put(("pipe_error", None))

        def writer():
            try:
                view = memoryview(payload)
                offset = 0
                while offset < len(view) and not stop.is_set():
                    written = process.stdin.write(view[offset:offset + 65536])
                    if not written:
                        raise OSError()
                    offset += written
                process.stdin.close()
                put(("written", None))
            except (OSError, ValueError):
                put(("pipe_error", None))

        def fail(code, message):
            return AcbrError(code, message, sending, etapa="runtime")

        try:
            flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
            try:
                process = subprocess.Popen([str(executable), *args, "--parent-pid", str(os.getpid())],
                    cwd=directory, env=environment, shell=False, stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, creationflags=flags)
            except (OSError, ValueError):
                raise AcbrError("FALHA_INICIAR_MOTOR", "Não foi possível iniciar o motor.", etapa="runtime") from None
            with self._active_lock:
                self._active = process
            for target, arguments in ((reader, (process.stdout, "stdout")), (reader, (process.stderr, "stderr")), (writer, ())):
                thread = threading.Thread(target=target, args=arguments, daemon=True)
                threads.append(thread)
                thread.start()
            buffer = bytearray()
            done = set()
            result = None
            while True:
                if self._closed.is_set():
                    raise fail("EMISSOR_FECHADO", "Emissor encerrado.")
                if cancel is not None and cancel.is_set():
                    raise fail("OPERACAO_CANCELADA", "Operação cancelada.")
                if time.monotonic() >= deadline:
                    raise fail("TIMEOUT_MOTOR", "O motor excedeu o prazo.")
                if overflow.is_set():
                    raise fail("RESPOSTA_EXCESSIVA", "Saída do motor excede o limite de bytes.")
                try:
                    channel, chunk = events.get(timeout=.02)
                except queue.Empty:
                    channel, chunk = None, None
                if channel == "pipe_error":
                    raise fail("FALHA_PIPE", "Falha na comunicação com o motor.")
                if channel in ("written", "stderr") or channel == "stdout" and chunk is None:
                    done.add(channel)
                if channel == "stdout" and chunk is not None:
                    buffer.extend(chunk)
                    while b"\n" in buffer:
                        line, _, rest = buffer.partition(b"\n")
                        buffer = bytearray(rest)
                        if not line:
                            continue
                        try:
                            frame = json.loads(line.decode("utf-8"), object_pairs_hook=_strict_object, parse_constant=_reject_constant)
                            if not isinstance(frame, dict) or frame.get("id") != request["id"]:
                                raise ValueError()
                            if frame.get("tipo") == "envioIniciado":
                                if sending or result is not None:
                                    raise ValueError()
                                sending = True
                                # The MVP has no mutating fiscal commands. A send marker is invalid.
                                raise ValueError()
                            if result is not None:
                                raise ValueError()
                            result = self._result(frame, request, sending)
                        except (ValueError, TypeError, UnicodeError, KeyError, RecursionError, binascii.Error):
                            raise fail("RESPOSTA_INVALIDA", "Resposta inválida do motor.") from None
                if process.poll() is not None and done == {"stdout", "stderr", "written"} and events.empty():
                    break
            if process.returncode != 0 or buffer or result is None:
                raise fail("FALHA_MOTOR", "Motor encerrou sem resposta completa e válida.")
            return result
        except AcbrError as exc:
            error = exc
            raise
        except Exception:
            error = fail("FALHA_MOTOR", "Falha durante a operação do motor.")
            raise error from None
        finally:
            stop.set()
            if process is not None:
                clean = self._terminate(process)
                for thread in threads:
                    thread.join(timeout=.2)
                clean = clean and not any(thread.is_alive() for thread in threads)
                # Raw unbuffered handles do not acquire BufferedReader locks.
                for stream in (process.stdin, process.stdout, process.stderr):
                    try:
                        stream.close()
                    except (OSError, ValueError):
                        clean = False
                with self._active_lock:
                    self._active = None
            if not any(thread.is_alive() for thread in threads):
                payload[:] = b"\0" * len(payload)
            if not clean:
                self._closed.set()
                if error is not None:
                    error.limpeza_confirmada = False
                    object.__setattr__(error.diagnostico, "limpeza_confirmada", False)
                else:
                    raise AcbrError("ENCERRAMENTO_NAO_CONFIRMADO", "Encerramento do motor não confirmado.", sending, limpeza_confirmada=False)

    @staticmethod
    def _result(frame, request, sending):
        if "tipo" in frame:
            raise ValueError()
        for name in ("versao", "sourceRevision"):
            if type(frame.get(name)) is not int or frame[name] != request[name]:
                raise ValueError()
        if frame.get("contractHash") != request["contractHash"] or type(frame.get("sucesso")) is not bool or frame.get("estado") not in STATES:
            raise ValueError()
        for key in ("codigo", "xMotivo", "chave", "protocolo", "recibo", "xmlBase64"):
            if key in frame and not isinstance(frame[key], str):
                raise ValueError()
        if "cStat" in frame and (type(frame["cStat"]) is not int or not 1 <= frame["cStat"] <= 9999):
            raise ValueError()
        if "envioIniciado" in frame and (type(frame["envioIniciado"]) is not bool or frame["envioIniciado"]):
            raise ValueError()
        xml = frame.get("xmlBase64")
        if xml is not None:
            decoded = base64.b64decode(xml, validate=True)
            if not 0 < len(decoded) <= 4 * 1024 * 1024 or base64.b64encode(decoded).decode("ascii") != xml:
                raise ValueError()
            decoded.decode("utf-8")
        cmd = request["comando"]
        if not frame["sucesso"]:
            allowed_failure = {"ERRO", "CONSULTADO"} if cmd == "recuperarXml" else {"ERRO"}
            if frame["estado"] not in allowed_failure:
                raise ValueError()
        if frame["sucesso"]:
            state = {"gerarXml": "XML_GERADO", "validar": "VALIDADO", "recuperarXml": "XML_RECUPERADO"}[cmd]
            if frame["estado"] != state or cmd != "validar" and xml is None:
                raise ValueError()
        if frame["estado"] == "XML_RECUPERADO" or cmd == "recuperarXml" and frame["sucesso"]:
            if cmd != "recuperarXml" or not frame["sucesso"] or frame.get("cStat") != 100 or not re.fullmatch(r"[0-9]{44}", frame.get("chave", "")) or not re.fullmatch(r"[0-9]{15}", frame.get("protocolo", "")) or xml is None or sending:
                raise ValueError()
        diagnostic = Diagnostico(
            "XML_RECUPERADO" if frame["sucesso"] and cmd == "recuperarXml" else "ETAPA_LOCAL_CONCLUIDA" if frame["sucesso"] else "OPERACAO_FISCAL_FALHOU",
            {"gerarXml": "geracao", "validar": "validacao", "recuperarXml": "consulta"}[cmd],
            "Etapa concluída." if frame["sucesso"] else "O motor não concluiu a etapa.",
            "Guarde o resultado fiscal." if frame["sucesso"] else "Confira os dados e o código retornado antes de continuar.",
            "autorizado" if frame["sucesso"] and cmd == "recuperarXml" else "nao_enviado", c_stat=frame.get("cStat"))
        return ResultadoFiscal(frame["sucesso"], frame["estado"], diagnostic, frame.get("codigo"), frame.get("cStat"), frame.get("chave"), frame.get("protocolo"), frame.get("recibo"), xml, frame.get("xMotivo"), sending)
