"""CLI sem operações fiscais: contrato, instalação explícita e diagnóstico."""
import argparse
import json
from pathlib import Path
import sys

from ._version import __version__
from .contract import CONTRACT_HASH, SOURCE_REVISION, describe_field
from .errors import AcbrError
from .runtime import install_runtime, verify_runtime


def _text_description(value: dict) -> str:
    """Render only the authenticated contract's existing metadata."""
    lines = [value["path"],
             f'Tipo: {value["pascalType"]} ({value["kind"]}; entrada {value["inputType"]})',
             "Somente leitura: " + ("sim" if value["readonly"] else "não")]
    if "values" in value:
        lines.append("Valores: " + ", ".join(value["values"]))
    if "declaredDefault" in value:
        default = value["declaredDefault"]
        text = default if isinstance(default, str) else json.dumps(default, ensure_ascii=False)
        lines.append("Padrão declarado: " + text)
    constraints = value.get("constraints", {})
    for key, label in (("min", "Mínimo"), ("max", "Máximo"), ("scale", "Casas decimais")):
        if key in constraints:
            lines.append(f"{label}: {constraints[key]}")
    if "itemType" in value:
        lines.append("Tipo dos itens: " + value["itemType"])
    if "members" in value:
        lines.append("Campos:")
        for member in value["members"]:
            readonly = " [somente leitura]" if member["readonly"] else ""
            lines.append(f'  {member["name"]}: {member["pascalType"]} ({member["kind"]}){readonly}')
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m acbr", description="ACBr Python: consulte campos e tipos ou gerencie o runtime local.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplos:\n  python -m acbr describe Ide.tpNF\n  python -m acbr describe TTipoNFe --json\n"
               "  python -m acbr doctor --directory .runtime/runtime")
    parser.add_argument("--version", action="version", version=f"acbr-python {__version__}",
                        help="Mostra a versão do SDK Python e encerra.")
    commands = parser.add_subparsers(dest="command", required=True, metavar="COMANDO")
    describe = commands.add_parser(
        "describe", help="Descreve um campo ou tipo do contrato, sem runtime ou rede",
        description="Consulta o contrato local. A saída padrão é texto; --json preserva os metadados da API describe_field.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplos:\n  python -m acbr describe Ide.tpNF\n  python -m acbr describe TTipoNFe --json\n"
               "  python -m acbr describe 'Det[].Prod.vProd'")
    describe.add_argument("target", nargs="?", default="TNFe", metavar="TARGET",
                          help="Campo ou tipo, respeitando maiúsculas/minúsculas (padrão: TNFe).")
    describe.add_argument("--json", dest="json_output", action="store_true",
                          help="Exibe o objeto JSON retornado por describe_field.")
    help_parser = commands.add_parser(
        "ajuda", help="Consulta o contrato em JSON, mantendo a interface existente",
        description="Interface compatível: campo ou tipo em JSON, sem runtime ou rede.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplos:\n  python -m acbr ajuda Ide.tpNF\n  python -m acbr ajuda TTipoNFe")
    help_parser.add_argument("path", nargs="?", default="TNFe", metavar="TARGET",
                            help="Campo ou tipo do contrato (padrão: TNFe).")
    runtime = commands.add_parser(
        "runtime", help="Instalação explícita e versionada do runtime",
        description="Gerencia a instalação do runtime fixado para Windows/Linux x64.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplo:\n  python -m acbr runtime install --directory .runtime")
    operations = runtime.add_subparsers(dest="operation", required=True, metavar="OPERACAO")
    install = operations.add_parser(
        "install", help="Instala o pacote fixado em um diretório novo",
        description="Verifica o pacote e preserva seus fontes e licenças. O destino deve ser novo.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplos:\n  python -m acbr runtime install --directory .runtime\n"
               "  python -m acbr runtime install --directory .runtime --archive pacote.tgz")
    install.add_argument("--directory", required=True, type=Path, metavar="DIRETORIO", help="Novo diretório de instalação.")
    install.add_argument("--archive", type=Path, metavar="ARQUIVO_TGZ", help="Usa o pacote local fixado, sem download.")
    doctor = commands.add_parser(
        "doctor", help="Confere plataforma, contrato e hashes; não executa o motor",
        description="Verifica a integridade local, sem executar o worker ou acessar a rede.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplo:\n  python -m acbr doctor --directory .runtime/runtime")
    doctor.add_argument("--directory", required=True, type=Path, metavar="DIRETORIO",
                        help="Diretório runtime retornado pelo instalador.")
    args = parser.parse_args(argv)
    try:
        if args.command == "describe":
            value = describe_field(args.target)
            if not args.json_output:
                print(_text_description(value))
                return 0
        elif args.command == "ajuda":
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
        if args.command == "describe" and not args.json_output:
            diagnostic = error.diagnostico
            print(f"Erro ({diagnostic.codigo}): {diagnostic.mensagem}", file=sys.stderr)
            print("Ação: " + diagnostic.acao, file=sys.stderr)
        else:
            print(json.dumps(error.diagnostico.to_dict(), ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
