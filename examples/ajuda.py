"""Consulte o contrato local sem runtime, certificado ou conexão fiscal."""

from __future__ import annotations

import subprocess
import sys


def main() -> int:
    caminho = sys.argv[1] if len(sys.argv) > 1 else "Det[].Prod.vProd"
    return subprocess.run(
        [sys.executable, "-m", "acbr", "ajuda", caminho], check=False
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
