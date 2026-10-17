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
from collections.abc import Callable

from .errors import AcbrError, Diagnostico
from .result import ResultadoFiscal
from .operations import EventoEnvio

STATES = frozenset("DENEGADO XML_GERADO VALIDADO ASSINADO XML_RECUPERADO AUTORIZADO REJEITADO PENDENTE INDETERMINADO CONSULTADO CANCELADO EVENTO_REGISTRADO INUTILIZADO ERRO".split())
COMMANDS = frozenset({"gerarXml", "validar", "assinar", "transmitir", "consultar", "recuperarXml", "cancelar", "inutilizar"})
MUTATING = frozenset({"transmitir", "cancelar", "inutilizar"})
PENDING_CODES = frozenset({103, 104, 105, 108, 109, 204, 539, 573})
PHASES = {"gerarXml": "geracao", "validar": "validacao", "assinar": "assinatura", "transmitir": "transmissao",
          "consultar": "consulta", "recuperarXml": "consulta", "cancelar": "cancelamento", "inutilizar": "inutilizacao"}
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


def _xml_text(value):
    if not isinstance(value, str):
        raise ValueError()
    decoded = base64.b64decode(value, validate=True)
    if not 0 < len(decoded) <= 4 * 1024 * 1024 or base64.b64encode(decoded).decode("ascii") != value:
        raise ValueError()
    return decoded.decode("utf-8")


def _fiscal_state(command, code):
    """Mesma classificação de NativeMotor.Resultado do worker 0.2.0."""
    if code in {100, 150}:
        return "AUTORIZADO"
    if code in {110, 301, 302}:
        return "DENEGADO"
    if code in {101, 151, 155}:
        return "CANCELADO"
    if code in PENDING_CODES:
        return "PENDENTE"
    if command == "cancelar" and code in {135, 136}:
        return "CANCELADO"
    if command == "inutilizar" and code == 102:
        return "INUTILIZADO"
    if command == "consultar" and code == 217:
        return "CONSULTADO"
    return "REJEITADO"


class ProcessTransport:
    def __init__(self, timeout: float = 120, max_bytes: int = MAX_BYTES, *,
                 ao_iniciar_envio: Callable[[EventoEnvio], None] | None = None):
        if type(timeout) not in (float, int) or not math.isfinite(timeout) or not 0 < timeout <= 120 or type(max_bytes) is not int or not 256 <= max_bytes <= MAX_BYTES:
            raise AcbrError("CONFIGURACAO_INVALIDA", "Prazo ou limite de bytes inválido.")
        self.timeout = timeout
        self.max_bytes = max_bytes
        if ao_iniciar_envio is not None and not callable(ao_iniciar_envio):
            raise AcbrError("CONFIGURACAO_INVALIDA", "ao_iniciar_envio deve ser uma função.", campo="ao_iniciar_envio")
        self.ao_iniciar_envio = ao_iniciar_envio
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
        except Exception:
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
        if not isinstance(request, dict) or not isinstance(request.get("comando"), str) or request["comando"] not in COMMANDS:
            raise AcbrError("OPERACAO_NAO_SUPORTADA", "Comando não suportado pelo transporte público.")
        if type(request.get("versao")) is not int or request["versao"] != 1 or type(request.get("sourceRevision")) is not int or request["sourceRevision"] <= 0 or not isinstance(request.get("contractHash"), str) or not re.fullmatch(r"[a-f0-9]{64}", request["contractHash"]) or not isinstance(request.get("id"), str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,100}", request["id"]):
            raise AcbrError("REQUISICAO_INVALIDA", "Identificação ou contrato da requisição inválido.")
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
        original_xml = None
        if request["comando"] == "transmitir":
            try:
                original_xml = _xml_text(request.get("xmlBase64"))
            except (ValueError, TypeError, UnicodeError, binascii.Error):
                pass
        error = None
        clean = True
        events: queue.Queue = queue.Queue(maxsize=32)
        stop = threading.Event()
        total = 0
        overflow = threading.Event()
        counters = threading.Lock()
        threads = []
        writer_thread = None
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
            finally:
                if stop.is_set():
                    payload[:] = b"\0" * len(payload)

        def fail(code, message):
            # Um marcador não recebido pode estar no pipe ou ter sido perdido
            # antes de o processo falhar. Nunca repetir uma mutação após spawn.
            uncertain = request["comando"] in MUTATING and process is not None
            return AcbrError(code, message, uncertain, etapa="runtime",
                             xml_original=original_xml if uncertain else None)

        def check_stopped():
            if self._closed.is_set():
                raise fail("EMISSOR_FECHADO", "Emissor encerrado.")
            if cancel is not None and cancel.is_set():
                raise fail("OPERACAO_CANCELADA", "Operação cancelada.")
            if time.monotonic() >= deadline:
                raise fail("TIMEOUT_MOTOR", "O motor excedeu o prazo.")

        def emit_send_event():
            if self.ao_iniciar_envio is None:
                return
            event = EventoEnvio(id=request["id"], comando=request["comando"])
            finished, failed = threading.Event(), threading.Event()

            def invoke():
                try:
                    self.ao_iniciar_envio(event)
                except BaseException:
                    # Nunca expõe mensagens/tracebacks do callback do consumidor.
                    failed.set()
                finally:
                    finished.set()

            thread = threading.Thread(target=invoke, daemon=True)
            thread.start()
            threads.append(thread)
            while not finished.wait(timeout=.02):
                check_stopped()
            check_stopped()
            if failed.is_set():
                raise fail("FALHA_EVENTO_ENVIO", "Não foi possível concluir o callback do evento de envio.")

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
                thread.start()
                threads.append(thread)
                if target is writer:
                    writer_thread = thread
            buffer = bytearray()
            done = set()
            result = None
            while True:
                check_stopped()
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
                                if request["comando"] not in MUTATING or sending or result is not None or set(frame) != {"id", "tipo"}:
                                    raise ValueError()
                                sending = True
                                emit_send_event()
                                continue
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
        except (KeyboardInterrupt, SystemExit):
            error = fail("OPERACAO_CANCELADA", "Operação interrompida; confira a situação fiscal antes de continuar.")
            raise error from None
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
                    except Exception:
                        clean = False
                with self._active_lock:
                    self._active = None
            # Leitores e callbacks não acessam o buffer de PFX da requisição.
            # Um callback preso não pode impedir a limpeza quando o writer acabou.
            if writer_thread is None or not writer_thread.is_alive():
                payload[:] = b"\0" * len(payload)
            if not clean:
                self._closed.set()
                if error is not None:
                    error.limpeza_confirmada = False
                    object.__setattr__(error.diagnostico, "limpeza_confirmada", False)
                else:
                    failure = fail("ENCERRAMENTO_NAO_CONFIRMADO", "Encerramento do motor não confirmado.")
                    failure.limpeza_confirmada = False
                    object.__setattr__(failure.diagnostico, "limpeza_confirmada", False)
                    raise failure

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
        cmd = request["comando"]
        if type(frame.get("envioIniciado")) is not bool or frame["envioIniciado"] != sending or sending and cmd not in MUTATING:
            raise ValueError()
        for key, width in (("chave", 44), ("protocolo", 15), ("recibo", 15)):
            if key in frame and not re.fullmatch(r"[0-9]{" + str(width) + r"}", frame[key]):
                raise ValueError()
        if "chave" in frame and cmd in {"consultar", "cancelar"} and frame["chave"] != request.get("chave"):
            raise ValueError()
        if "recibo" in frame and cmd == "consultar" and frame["recibo"] != request.get("recibo"):
            raise ValueError()
        xml = frame.get("xmlBase64")
        if xml is not None:
            _xml_text(xml)
        state, success, code = frame["estado"], frame["sucesso"], frame.get("cStat")
        if state == "ERRO":
            if success or sending or code is not None:
                raise ValueError()
        elif state == "INDETERMINADO":
            if success or not sending or cmd not in MUTATING or any(key in frame for key in ("cStat", "protocolo", "recibo")) or cmd != "transmitir" and xml is not None:
                raise ValueError()
            if cmd == "transmitir" and (xml is None or xml != request.get("xmlBase64")):
                raise ValueError()
        elif cmd in {"gerarXml", "validar", "assinar"}:
            if not success or state != {"gerarXml": "XML_GERADO", "validar": "VALIDADO", "assinar": "ASSINADO"}[cmd] or code is not None or cmd != "validar" and xml is None:
                raise ValueError()
        elif cmd == "recuperarXml":
            if success:
                if state != "XML_RECUPERADO" or code != 100 or "chave" not in frame or "protocolo" not in frame or xml is None:
                    raise ValueError()
            elif state != "CONSULTADO" or code is None or code == 100 or "chave" not in frame or any(key in frame for key in ("xmlBase64", "protocolo", "recibo")):
                raise ValueError()
        else:
            expected = _fiscal_state(cmd, code)
            if code is None or state != expected or success != (expected not in {"DENEGADO", "REJEITADO", "PENDENTE"}) or cmd in MUTATING and not sending:
                raise ValueError()
            if cmd in {"transmitir", "consultar", "cancelar"} and "chave" not in frame:
                raise ValueError()
            if code in {100, 150} or cmd == "cancelar" and code in {135, 136} or cmd == "inutilizar" and code == 102:
                if "protocolo" not in frame:
                    raise ValueError()
            if state == "AUTORIZADO" and "chave" not in frame or cmd == "transmitir" and state == "AUTORIZADO" and xml is None:
                raise ValueError()
            if cmd == "inutilizar" and state == "INUTILIZADO" and (xml is None or "chave" in frame):
                raise ValueError()
            if cmd == "transmitir" and code == 103 and "recibo" not in frame:
                raise ValueError()
            if cmd == "consultar" and request.get("recibo") is not None and frame.get("recibo") != request["recibo"]:
                raise ValueError()
        status = {"AUTORIZADO": "autorizado", "XML_RECUPERADO": "autorizado", "CANCELADO": "cancelado",
                  "INUTILIZADO": "inutilizado", "DENEGADO": "denegado", "REJEITADO": "rejeitado",
                  "PENDENTE": "pendente", "INDETERMINADO": "resultado_incerto"}.get(state, "nao_enviado")
        if cmd == "consultar" and code == 217 or cmd == "recuperarXml" and not success and code is not None:
            status = "nao_autorizado" if code == 217 else "recuperacao_nao_comprovada"
        if status == "resultado_incerto":
            action = "Confira a situação fiscal antes de repetir; não retransmita automaticamente."
        elif state == "PENDENTE":
            action = "Consulte a situação fiscal antes de qualquer nova tentativa."
        else:
            action = "Guarde o resultado fiscal." if success else "Confira os dados e o código retornado antes de continuar."
        diagnostic = Diagnostico(
            state if success and cmd not in {"gerarXml", "validar"} else "ETAPA_LOCAL_CONCLUIDA" if success else "OPERACAO_FISCAL_FALHOU",
            PHASES[cmd], "Etapa concluída." if success else "O motor não concluiu a etapa.", action,
            status, c_stat=code)
        return ResultadoFiscal(frame["sucesso"], frame["estado"], diagnostic, frame.get("codigo"), frame.get("cStat"), frame.get("chave"), frame.get("protocolo"), frame.get("recibo"), xml, frame.get("xMotivo"), sending)
