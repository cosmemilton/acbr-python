"""Pinned ACBr 0.2.0 contract, structural validation and field help.

This module checks wire types only. Omitted fields preserve native defaults;
neither this validator nor the generated TypedDicts implement fiscal rules.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from functools import lru_cache
from importlib.metadata import PackageNotFoundError, version
from importlib.resources import files
from typing import Any, NoReturn

from .errors import AcbrError
from .models import TNFe

WORKER_VERSION = "0.2.0"
SOURCE_REVISION = 48590
SOURCE_HASH = "6b768e4f45b4092d040f7576d6fb799d8b66b45ae29a0902c37334fb7c5c6816"
CONTRACT_HASH = "e5a497cefe8e0e350a30da5cc04e88b35c38a98535893d52f878890260d1346d"
CONTRACT_FILE_SHA256 = "94eae66c4194998a1b72f7363380d66cde8a3a1f435e4984706f65211d5e49bc"
_DECIMAL = re.compile(r"-?[0-9]+(?:\.[0-9]+)?", re.ASCII)
_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}(?:T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,3})?)?", re.ASCII)
_PATH = re.compile(r"[A-Za-z_]\w*(?:\[[0-9]*\])?(?:\.[A-Za-z_]\w*(?:\[[0-9]*\])?)*", re.ASCII)
_SEGMENT = re.compile(r"([A-Za-z_]\w*)(\[[0-9]*\])?", re.ASCII)
_MESSAGES = {
    "OBJETO_ESPERADO": "Informe um objeto JSON entre chaves.",
    "ARRAY_ESPERADO": "Informe uma lista JSON entre colchetes.",
    "ENUM_INVALIDO": "Use um dos valores textuais permitidos pelo contrato.",
    "CAMPO_DESCONHECIDO": "O objeto contém um campo desconhecido pelo contrato.",
    "CAMPO_SOMENTE_LEITURA": "O campo somente leitura não pode ser informado na entrada.",
    "INTEIRO_INVALIDO": "Informe um inteiro dentro dos limites do campo.",
    "BOOLEANO_ESPERADO": "Informe um booleano JSON.",
    "DECIMAL_INVALIDO": "Informe um decimal em texto, com ponto e a escala permitida.",
    "DATA_HORA_INVALIDA": "Informe uma data civil ISO sem Z ou offset: AAAA-MM-DD ou AAAA-MM-DDTHH:mm:ss[.sss].",
    "DATA_INVALIDA": "Informe uma data e um horário civis válidos.",
    "TEXTO_ESPERADO": "Informe texto JSON entre aspas.",
    "PROFUNDIDADE_EXCEDIDA": "O documento excede a profundidade máxima de 128 níveis.",
    "CAMINHO_INVALIDO": "Use nomes de campos separados por ponto e [] para coleções.",
    "CAMPO_INEXISTENTE": "O campo não existe nesse objeto do contrato.",
    "CAMPO_NAO_COLECAO": "[] ou índice só pode ser usado em uma coleção.",
    "COLECAO_REQUER_INDICE": "Use [] ou um índice para consultar um elemento da coleção.",
    "CAMPO_AMBIGUO": "O nome aparece em vários caminhos; informe o caminho completo.",
    "CAMINHO_COMPLETO_NECESSARIO": "Informe o caminho completo do campo.",
    "CONTRATO_INVALIDO": "O contrato empacotado está ausente, inválido ou incompatível.",
}


def _fail(code: str, at: str | None = None) -> NoReturn:
    # Never include submitted values or unknown keys in diagnostics.
    raise AcbrError(code, _MESSAGES[code], etapa="documento", campo=at)


def _decode_contract(raw: bytes) -> dict[str, Any]:
    """Authenticate both the exact upstream bytes and its canonical IR hash."""
    if hashlib.sha256(raw).hexdigest() != CONTRACT_FILE_SHA256:
        _fail("CONTRATO_INVALIDO")
    try:
        metadata = json.loads(raw)
        canonical = {key: metadata[key] for key in ("sourceRevision", "sourceHash", "ir")}
        digest = hashlib.sha256(json.dumps(canonical, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
        if (metadata["formatVersion"] != 1 or metadata["sourceRevision"] != SOURCE_REVISION
                or metadata["sourceHash"] != SOURCE_HASH or metadata["contractHash"] != CONTRACT_HASH
                or digest != CONTRACT_HASH or metadata["ir"]["schemaVersion"] != 1):
            _fail("CONTRATO_INVALIDO")
    except (KeyError, TypeError, ValueError, UnicodeError):
        _fail("CONTRATO_INVALIDO")
    return metadata


@lru_cache(maxsize=1)
def _contract() -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    try:
        raw = files("acbr").joinpath("resources", "contract.json").read_bytes()
    except (OSError, ModuleNotFoundError):
        _fail("CONTRATO_INVALIDO")
    metadata = _decode_contract(raw)
    return metadata, {node["name"]: node for node in metadata["ir"]["types"]}


def _validate(value: Any, node: dict[str, Any], types: dict[str, dict[str, Any]], at: str, depth: int) -> Any:
    if depth > 128:
        _fail("PROFUNDIDADE_EXCEDIDA", at)
    if node["kind"] == "enum":
        if type(value) is not str or value not in node["values"]:
            _fail("ENUM_INVALIDO", at)
        return value
    if node["kind"] == "list":
        if type(value) is not list:
            _fail("ARRAY_ESPERADO", at)
        return [_validate(item, types[node["item"]], types, f"{at}[{index}]", depth + 1)
                for index, item in enumerate(value)]
    if type(value) is not dict:
        _fail("OBJETO_ESPERADO", at)
    fields = {prop["name"]: prop for prop in node["properties"]}
    result: dict[str, Any] = {}
    for name, item in value.items():
        if type(name) is not str or name not in fields:
            _fail("CAMPO_DESCONHECIDO", at)
        prop = fields[name]
        current = f"{at}.{name}"
        if prop["readonly"]:
            _fail("CAMPO_SOMENTE_LEITURA", current)
        if "ref" in prop:
            result[name] = _validate(item, types[prop["ref"]], types, current, depth + 1)
            continue
        kind = prop["kind"]
        if kind == "integer":
            if type(item) is not int or not prop["min"] <= item <= prop["max"]:
                _fail("INTEIRO_INVALIDO", current)
        elif kind == "boolean":
            if type(item) is not bool:
                _fail("BOOLEANO_ESPERADO", current)
        elif kind == "decimal":
            if (type(item) is not str or len(item) > 64 or not _DECIMAL.fullmatch(item)
                    or ("scale" in prop and len(item.partition(".")[2]) > prop["scale"])):
                _fail("DECIMAL_INVALIDO", current)
        elif kind == "datetime":
            if type(item) is not str or not _DATE.fullmatch(item):
                _fail("DATA_HORA_INVALIDA", current)
            try:
                # Explicit components preserve the wire's civil range on every
                # Python version, even if an ISO parser normalizes 24:00:00.
                clock = item[11:].split(".", 1) if len(item) > 10 else ["00:00:00"]
                datetime(int(item[:4]), int(item[5:7]), int(item[8:10]),
                         int(clock[0][:2]), int(clock[0][3:5]), int(clock[0][6:8]),
                         int(clock[1].ljust(6, "0")) if len(clock) == 2 else 0)
            except ValueError:
                _fail("DATA_INVALIDA", current)
        elif type(item) is not str:
            _fail("TEXTO_ESPERADO", current)
        result[name] = item
    return result


def validate_document(data: TNFe | dict[str, Any]) -> dict[str, Any]:
    """Validate TNFe input and return a detached JSON-compatible snapshot.

    All fields are optional structurally. Native schema and fiscal validation
    remain the responsibility of the ACBr runtime. No defaults are inserted.
    """
    metadata, types = _contract()
    root = metadata["ir"]["root"]
    return _validate(data, types[root], types, root, 0)


@dataclass(frozen=True, slots=True, init=False)
class Documento:
    """Immutable TNFe input snapshot; repr never contains submitted content."""

    _snapshot: bytes = field(repr=False)

    def __init__(self, data: TNFe | dict[str, Any]) -> None:
        validated = validate_document(data)
        object.__setattr__(self, "_snapshot", json.dumps(validated, ensure_ascii=True, separators=(",", ":")).encode("ascii"))

    def to_wire(self) -> dict[str, Any]:
        """Return a fresh mutable copy; changing it does not change this document."""
        return json.loads(self._snapshot)


def _matching_paths(types: dict[str, dict[str, Any]], root: str, field_name: str) -> list[str]:
    matches: list[str] = []

    def visit(name: str, prefix: str, trail: frozenset[str]) -> None:
        if name in trail or len(trail) > 128 or len(matches) > 1000:
            _fail("CAMINHO_COMPLETO_NECESSARIO")
        node = types[name]
        trail = trail | {name}
        if node["kind"] == "list":
            visit(node["item"], prefix + "[]", trail)
        elif node["kind"] == "object":
            for prop in node["properties"]:
                path = (prefix + "." if prefix else "") + prop["name"]
                if prop["name"] == field_name:
                    matches.append(path)
                if "ref" in prop and prop["kind"] != "enum":
                    visit(prop["ref"], path, trail)

    visit(root, "", frozenset())
    return sorted(matches)


def _description(node: dict[str, Any], path: str, readonly: bool) -> dict[str, Any]:
    kind = node["kind"]
    result: dict[str, Any] = {
        "path": path, "kind": kind, "pascalType": node["name"],
        "inputType": {"integer": "integer", "boolean": "boolean", "object": "object", "list": "array"}.get(kind, "string"),
        "readonly": readonly,
    }
    if kind == "enum":
        result["values"] = list(node["values"])
    elif kind == "list":
        result["itemType"] = node["item"]
    elif kind == "object":
        result["members"] = [{"name": prop["name"], "kind": prop["kind"], "pascalType": prop["type"],
                              "readonly": readonly or prop["readonly"]} for prop in node["properties"]]
    return result


def describe_field(path: str) -> dict[str, Any]:
    """Describe an exact type or case-sensitive TNFe path, including enums.

    Examples: ``TProd``, ``Ide.cUF``, ``TNFe.Det[].Prod.vProd``. Numeric
    collection indices are accepted and normalized to ``[]`` in the result.
    """
    if type(path) is not str or len(path) > 512 or not _PATH.fullmatch(path):
        _fail("CAMINHO_INVALIDO")
    metadata, types = _contract()
    root = metadata["ir"]["root"]
    base = {key: metadata[key] for key in ("formatVersion", "sourceRevision", "sourceHash", "contractHash")}
    base["root"] = root
    try:
        base["sdkVersion"] = version("acbr-python")
    except PackageNotFoundError:
        base["sdkVersion"] = "0.1.0a1"
    if path in types:
        return base | _description(types[path], path, False)
    relative = path[len(root) + 1:] if path.startswith(root + ".") else path
    node = types[root]
    if _SEGMENT.fullmatch(relative) and "." not in relative and "[" not in relative and not any(prop["name"] == relative for prop in node["properties"]):
        matches = _matching_paths(types, root, relative)
        if len(matches) > 1:
            _fail("CAMPO_AMBIGUO")
        if matches:
            relative = matches[0]
    canonical = [root]
    readonly = False
    prop: dict[str, Any] = {}
    selected = False
    parts = relative.split(".")
    for index, part in enumerate(parts):
        if node["kind"] != "object":
            _fail("CAMINHO_INVALIDO")
        parsed = _SEGMENT.fullmatch(part)
        assert parsed is not None  # Full path grammar was validated above.
        prop = next((candidate for candidate in node["properties"] if candidate["name"] == parsed[1]), {})
        if not prop:
            _fail("CAMPO_INEXISTENTE")
        selected = parsed[2] is not None
        if selected and prop["kind"] != "list":
            _fail("CAMPO_NAO_COLECAO")
        readonly = readonly or prop["readonly"]
        canonical.append(prop["name"] + ("[]" if selected else ""))
        node = types[prop["ref"]] if "ref" in prop else {"name": prop["type"], "kind": prop["kind"]}
        if prop["kind"] == "list":
            if selected:
                node = types[node["item"]]
            elif index < len(parts) - 1:
                _fail("COLECAO_REQUER_INDICE")
        elif "ref" not in prop and index < len(parts) - 1:
            _fail("CAMINHO_INVALIDO")
    result = base | _description(node, ".".join(canonical), readonly)
    result["pascalType"] = node["name"] if selected else prop["type"]
    if "ref" in prop:
        result["typeReference"] = node["name"] if selected else prop["ref"]
    if "declaredDefault" in prop:
        result["declaredDefault"] = prop["declaredDefault"]
    constraints = {key: prop[key] for key in ("min", "max", "scale") if key in prop}
    if constraints:
        result["constraints"] = constraints
    return result
