"""Subprocesso de teste sintético. Nenhuma dependência ou chamada de rede."""
import base64
import json
import os
import sys
import time

mode = sys.argv[1]
if mode == "no_read":
    time.sleep(30)
    raise SystemExit()
request = json.loads(sys.stdin.buffer.readline())
if mode == "hang":
    time.sleep(30)
    raise SystemExit()
frame = {key: request[key] for key in ("id", "versao", "sourceRevision", "contractHash")}
command = request["comando"]
mutating = command in {"transmitir", "cancelar", "inutilizar"}
frame.update(sucesso=True, estado="XML_GERADO", envioIniciado=False,
             xmlBase64=base64.b64encode("<NFe>SINTÉTICO</NFe>".encode()).decode())
if command == "validar":
    frame.update(estado="VALIDADO")
if command == "assinar":
    frame.update(estado="ASSINADO", chave="1" * 44)
if command == "recuperarXml":
    frame.update(estado="XML_RECUPERADO", cStat=100, chave="1" * 44, protocolo="1" * 15)
if command in {"transmitir", "consultar", "cancelar", "inutilizar"}:
    frame.update(estado={"transmitir": "AUTORIZADO", "consultar": "AUTORIZADO", "cancelar": "CANCELADO", "inutilizar": "INUTILIZADO"}[command],
                 cStat={"transmitir": 100, "consultar": 100, "cancelar": 135, "inutilizar": 102}[command],
                 protocolo="1" * 15, envioIniciado=mutating)
    if command != "inutilizar":
        frame["chave"] = request.get("chave", "1" * 44)
    if command == "consultar" and "recibo" in request:
        frame["recibo"] = request["recibo"]
if mode.startswith("status_"):
    status = int(mode.split("_", 1)[1])
    state = {100: "AUTORIZADO", 150: "AUTORIZADO", 101: "CANCELADO", 151: "CANCELADO", 155: "CANCELADO",
             110: "DENEGADO", 301: "DENEGADO", 302: "DENEGADO", 103: "PENDENTE", 104: "PENDENTE", 105: "PENDENTE",
             108: "PENDENTE", 109: "PENDENTE", 204: "PENDENTE", 539: "PENDENTE", 573: "PENDENTE", 217: "CONSULTADO"}.get(status, "REJEITADO")
    frame.update(cStat=status, estado=state, sucesso=state not in {"DENEGADO", "PENDENTE", "REJEITADO"})
    if status == 103 and command == "transmitir":
        frame["recibo"] = "1" * 15
    if status not in {100, 150}:
        frame.pop("protocolo", None)
if mode == "native_error":
    frame.update(sucesso=False, estado="ERRO", envioIniciado=False, codigo="SYNTHETIC-PRIVATE-CODE")
    for name in ("cStat", "xmlBase64", "protocolo", "recibo"):
        frame.pop(name, None)
if mode == "recovery_unproven":
    frame.update(sucesso=False, estado="CONSULTADO", cStat=217)
    for name in ("xmlBase64", "protocolo", "recibo"):
        frame.pop(name, None)
if mode == "indeterminate":
    frame.update(sucesso=False, estado="INDETERMINADO", envioIniciado=True, codigo="RESULTADO_INDETERMINADO")
    for name in ("cStat", "protocolo", "recibo"):
        frame.pop(name, None)
    if command == "transmitir":
        frame["xmlBase64"] = request.get("xmlBase64", frame["xmlBase64"])
    else:
        frame.pop("xmlBase64", None)
if mode == "indeterminate_altered_xml":
    frame.update(sucesso=False, estado="INDETERMINADO", envioIniciado=True,
                 xmlBase64=base64.b64encode(b"<NFe>ALTERED</NFe>").decode())
    for name in ("cStat", "protocolo", "recibo"):
        frame.pop(name, None)
if mode == "false_send":
    frame["envioIniciado"] = False
if mode == "missing_send":
    frame.pop("envioIniciado", None)
if mode == "bool_send":
    frame["envioIniciado"] = 1
if mode == "bad_state_code":
    frame.update(sucesso=False, estado="REJEITADO", cStat=204)
if mode == "bad_receipt":
    frame["recibo"] = "123"
if mode == "wrong_receipt":
    frame["recibo"] = "9" * 15
if mode == "bad_protocol":
    frame["protocolo"] = "123"
if mode == "wrong_key":
    frame["chave"] = "9" * 44
if mode in {"no_protocol", "no_xml", "no_key", "no_receipt"}:
    frame.pop({"no_protocol": "protocolo", "no_xml": "xmlBase64", "no_key": "chave", "no_receipt": "recibo"}[mode], None)
if mode == "stderr":
    sys.stderr.write("SEGREDO-QUE-NAO-PODE-VAZAR" * 10000)
    sys.stderr.flush()
if mode == "flood":
    sys.stdout.write("X" * 10000)
    sys.stdout.flush()
    time.sleep(30)
if mode == "wrong_id":
    frame["id"] = "other"
if mode == "contract":
    frame["contractHash"] = "a" * 64
if mode == "version_bool":
    frame["versao"] = True
if mode == "state":
    frame["estado"] = "AUTORIZADO"
if mode == "failure_state":
    frame.update(sucesso=False, estado="AUTORIZADO")
if mode == "unknown_type":
    frame["tipo"] = "unknown"
if mode == "secret_code":
    frame["codigo"] = "SYNTHETIC-PASSWORD-SENTINEL"
if mode == "recover150":
    frame["cStat"] = 150
if mode == "xml":
    frame["xmlBase64"] = "eA==="
if mode == "utf8":
    sys.stdout.buffer.write(b"\xff\n")
    raise SystemExit()
marker = {"id": request["id"], "tipo": "envioIniciado"}
if mode == "wrong_marker_id":
    marker["id"] = "other"
if mode == "extra_marker":
    marker["extra"] = 1
if mode == "marker" or mutating and mode not in {"no_marker", "late_marker", "native_error"}:
    print(json.dumps(marker), flush=True)
if mode == "duplicate_marker":
    print(json.dumps(marker), flush=True)
if mode == "hang_after_marker":
    time.sleep(30)
    raise SystemExit()
if mode == "empty":
    raise SystemExit()
encoded = json.dumps(frame, ensure_ascii=False).encode("utf-8")
if mode == "duplicate_key":
    encoded = encoded[:-1] + b',"sucesso":true}'
if mode == "nan":
    encoded = encoded[:-1] + b',"cStat":NaN}'
if mode == "slow":
    for byte in encoded + b"\n":
        sys.stdout.buffer.write(bytes([byte]))
        sys.stdout.buffer.flush()
else:
    sys.stdout.buffer.write(encoded + (b"" if mode == "partial" else b"\n"))
    sys.stdout.buffer.flush()
if mode == "duplicate":
    sys.stdout.buffer.write(encoded + b"\n")
if mode == "trailing":
    sys.stdout.write("TRAILING")
if mode == "late_marker":
    print(json.dumps(marker), flush=True)
if mode == "nonzero":
    raise SystemExit(7)
