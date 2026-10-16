"""Generate lossless Python input/output types from the pinned upstream IR."""

from __future__ import annotations

import argparse
import hashlib
import json
import keyword
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src/acbr/resources/contract.json"
TARGET = ROOT / "src/acbr/models.py"
FILE_SHA256 = "94eae66c4194998a1b72f7363380d66cde8a3a1f435e4984706f65211d5e49bc"
CONTRACT_HASH = "e5a497cefe8e0e350a30da5cc04e88b35c38a98535893d52f878890260d1346d"
UPSTREAM_COMMIT = "5ff66828eb70f942608517f1e11719272b2786b8"


def load_contract() -> dict:
    raw = SOURCE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != FILE_SHA256:
        raise ValueError("Bundled contract differs from pinned upstream bytes")
    metadata = json.loads(raw)
    canonical = {key: metadata[key] for key in ("sourceRevision", "sourceHash", "ir")}
    digest = hashlib.sha256(json.dumps(canonical, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    if digest != CONTRACT_HASH or metadata["contractHash"] != CONTRACT_HASH:
        raise ValueError("Contract IR hash is incompatible")
    return metadata


def render(metadata: dict) -> str:
    types = metadata["ir"]["types"]
    kinds = {node["name"]: node["kind"] for node in types}
    lines = [
        '"""Generated ACBr wire types; edit tools/generate_models.py instead.',
        "",
        "All input properties are optional; omitted values use native defaults.",
        "Readonly properties occur only in Output types. Decimal and civil ISO",
        "date/time values are strings. Runtime validation is in acbr.contract.",
        f"Source: cosmemilton/acbr-node@{UPSTREAM_COMMIT} (LGPL-2.1-or-later).",
        f"Contract SHA256: {CONTRACT_HASH}.",
        '"""', "", "from __future__ import annotations", "",
        "from typing import Literal, TypeAlias, TypedDict", "",
    ]

    def reference(name: str, output: bool) -> str:
        return name + ("Output" if output and kinds[name] in ("object", "list") else "")

    # Enums precede TypedDicts for readable annotations and editor completion.
    for node in types:
        if node["kind"] == "enum":
            values = ", ".join(repr(value) for value in node["values"])
            lines.extend([f'{node["name"]}: TypeAlias = Literal[{values}]', ""])

    for output in (False, True):
        for node in types:
            if node["kind"] != "object":
                continue
            name = reference(node["name"], output)
            props = [prop for prop in node["properties"] if output or not prop["readonly"]]
            if any(not prop["name"].isidentifier() or keyword.iskeyword(prop["name"]) for prop in props):
                raise ValueError(f"Python keyword requires explicit generator handling in {name}")
            lines.append(f"class {name}(TypedDict, total=False):")
            if not props:
                lines.append("    pass")
            for prop in props:
                annotation = reference(prop["ref"], output) if "ref" in prop else {"integer": "int", "boolean": "bool", "string": "str", "decimal": "str", "datetime": "str"}[prop["kind"]]
                lines.append(f'    {prop["name"]}: {annotation}')
            lines.append("")
        for node in types:
            if node["kind"] == "list":
                lines.extend([f'{reference(node["name"], output)}: TypeAlias = list["{reference(node["item"], output)}"]', ""])
    names = [node["name"] for node in types]
    names.extend(reference(node["name"], True) for node in types if node["kind"] in ("object", "list"))
    lines.extend(["__all__ = [", *[f"    {name!r}," for name in names], "]", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if models.py is not the deterministic generated output")
    args = parser.parse_args()
    expected = render(load_contract()).encode("utf-8")
    if args.check:
        if not TARGET.exists() or TARGET.read_bytes() != expected:
            parser.exit(1, "models.py differs; run python tools/generate_models.py\n")
        print("204 contract types verified; generated models are current.")
    else:
        TARGET.write_bytes(expected)
        print("Generated 204 contract types with complete Output variants.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
