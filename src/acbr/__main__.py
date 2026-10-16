"""CLI sem operações fiscais: ajuda, instalação explícita e diagnóstico."""
import argparse
import json
from pathlib import Path

from .contract import CONTRACT_HASH, SOURCE_REVISION, describe_field
from .errors import AcbrError
from .runtime import install_runtime, verify_runtime


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="acbr-python", description="ACBr Python: ajuda e runtime Windows/Linux x64.")
    commands = parser.add_subparsers(dest="command", required=True)
    help_parser = commands.add_parser("ajuda", help="Campos e tipos do contrato compartilhado")
    help_parser.add_argument("path", nargs="?", default="TNFe")
    runtime = commands.add_parser("runtime", help="Instalação explícita e versionada do runtime")
    operations = runtime.add_subparsers(dest="operation", required=True)
    install = operations.add_parser("install")
    install.add_argument("--directory", required=True, type=Path)
    install.add_argument("--archive", type=Path)
    doctor = commands.add_parser("doctor", help="Confere plataforma, contrato e hashes; não executa o motor")
    doctor.add_argument("--directory", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "ajuda":
            value = describe_field(args.path)
        elif args.command == "runtime":
            directory = install_runtime(args.directory, archive=args.archive)
            value = {"instalado": True, "runtime_directory": str(directory)}
        else:
            runtime_value = verify_runtime(args.directory)
            value = {"integro": True, "sourceRevision": SOURCE_REVISION, "contractHash": CONTRACT_HASH,
                     "capabilities": sorted(runtime_value.capabilities)}
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0
    except AcbrError as error:
        print(json.dumps(error.diagnostico.to_dict(), ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
