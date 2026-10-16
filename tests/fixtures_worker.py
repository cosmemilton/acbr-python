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
frame.update(sucesso=True, estado="XML_GERADO", envioIniciado=False,
             xmlBase64=base64.b64encode("<NFe>SINTÉTICO</NFe>".encode()).decode())
if request["comando"] == "validar":
    frame.update(estado="VALIDADO")
if request["comando"] == "recuperarXml":
    frame.update(estado="XML_RECUPERADO", cStat=100, chave="1" * 44, protocolo="1" * 15)
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
if mode == "marker":
    print(json.dumps({"id": request["id"], "tipo": "envioIniciado"}), flush=True)
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
if mode == "nonzero":
    raise SystemExit(7)
