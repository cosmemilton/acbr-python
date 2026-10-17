"""Instalação explícita e verificação offline do runtime ACBr Node 0.2.1.

O wheel contém somente o SDK e os hashes; importar este módulo nunca baixa ou
executa programas. A instalação preserva todo o pacote nativo, fontes e licenças.
"""

from __future__ import annotations

import ctypes
import errno
import gzip
import hashlib
from importlib.resources import files
import json
import os
from pathlib import Path
import platform
import re
import stat
import struct
import sys
import tarfile
import tempfile
import time
import zlib
from dataclasses import dataclass
from typing import BinaryIO
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from .errors import AcbrError

_MAX_ARCHIVE = 64 * 1024 * 1024
_MAX_UNPACKED = 128 * 1024 * 1024
_MAX_FILE = 64 * 1024 * 1024
_MAX_MANIFEST = 256 * 1024
_MAX_ENTRIES = 2048
_CHUNK = 64 * 1024
_HASH = re.compile(r"[a-f0-9]{64}\Z")
_CAPABILITY = re.compile(r"[A-Za-z][A-Za-z0-9_]{0,63}\Z")
_RESERVED = re.compile(r"(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?\Z", re.I)
_REQUIRED = frozenset({
    "licenses/ACBr-LICENSE.TXT", "licenses/FPC-COPYING.GPL.txt",
    "licenses/FPC-COPYING.LGPL.txt", "licenses/FPC-COPYING.FPC",
    "licenses/Lazarus-COPYING.txt", "licenses/Lazarus-COPYING.LGPL.txt",
    "licenses/Lazarus-COPYING.modifiedLGPL.txt", "licenses/toolchain-notices.json",
    "sources/acbr-source.tar.gz", "sources/build.json",
    "sources/native-dependencies.json", "ACBrNFeServicos.ini", "openssl.cnf",
    "licenses/common/Apache-2.0.txt", "licenses/common/INVENTORY.json",
})


@dataclass(frozen=True, slots=True)
class Runtime:
    directory: Path
    executable: Path
    capabilities: frozenset[str]


def _fail(code: str, message: str) -> AcbrError:
    return AcbrError(code, message, etapa="runtime")


def _release() -> dict:
    return json.loads(files("acbr").joinpath("resources/runtime-release.json").read_text(encoding="utf-8"))


def _platform_key() -> str:
    # Também rejeita Python 32 bits instalado em um sistema x64.
    if sys.platform not in {"linux", "win32"} or platform.machine().lower() not in {"amd64", "x86_64"} or struct.calcsize("P") != 8:
        raise _fail("PLATAFORMA_NAO_SUPORTADA", "O runtime exige Python x64 em Windows ou Linux x64 (glibc).")
    if sys.platform == "linux" and platform.libc_ver()[0] != "glibc":
        raise _fail("PLATAFORMA_NAO_SUPORTADA", "O runtime Linux distribuído exige glibc; musl/Alpine não é suportado.")
    return sys.platform


def _path_parts(name: str) -> tuple[str, ...]:
    if not isinstance(name, str) or not name or len(name) > 512 or name.startswith("/") or "\\" in name:
        raise _fail("RUNTIME_INVALIDO", "Caminho inválido no pacote nativo.")
    parts = tuple(name.split("/"))
    if len(parts) > 32 or any(not p or p in {".", ".."} or p.endswith((".", " ")) or _RESERVED.fullmatch(p) or any(ord(c) < 32 or c in '<>:"|?*' for c in p) for p in parts):
        raise _fail("RUNTIME_INVALIDO", "Caminho inválido no pacote nativo.")
    return parts


def _is_link(info: os.stat_result) -> bool:
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & 0x400)


def _plain_path(path: Path) -> Path:
    path = Path(os.path.abspath(path))
    for parent in (path, *path.parents):
        try:
            if _is_link(parent.lstat()):
                raise _fail("RUNTIME_INVALIDO", "Links e junções não são permitidos no runtime.")
        except FileNotFoundError:
            pass
    return path


def _digest(stream: BinaryIO) -> str:
    digest = hashlib.sha256()
    size = 0
    for block in iter(lambda: stream.read(_CHUNK), b""):
        size += len(block)
        if size > _MAX_FILE:
            raise _fail("RUNTIME_INVALIDO", "Arquivo nativo excede o limite.")
        digest.update(block)
    return digest.hexdigest()


def _inventory(root: Path) -> set[str]:
    result: set[str] = set()
    stack = [root]
    count = 0
    while stack:
        directory = stack.pop()
        for child in directory.iterdir():
            count += 1
            if count > _MAX_ENTRIES:
                raise _fail("RUNTIME_INVALIDO", "Inventário nativo excede o limite.")
            info = child.lstat()
            if _is_link(info):
                raise _fail("RUNTIME_INVALIDO", "Links e junções não são permitidos no runtime.")
            relative = child.relative_to(root).as_posix()
            _path_parts(relative)
            if stat.S_ISDIR(info.st_mode):
                stack.append(child)
            elif stat.S_ISREG(info.st_mode):
                if info.st_size > _MAX_FILE:
                    raise _fail("RUNTIME_INVALIDO", "Arquivo nativo excede o limite.")
                result.add(relative)
            else:
                raise _fail("RUNTIME_INVALIDO", "Arquivo nativo não regular.")
    return result


def verify_runtime(directory: Path) -> Runtime:
    """Valida manifesto autenticado, plataforma e todos os arquivos, sem executar."""
    key = _platform_key()
    release = _release()
    pin = release["platforms"][key]
    try:
        root = _plain_path(Path(directory))
        manifest_path = root / "manifest.json"
        info = manifest_path.lstat()
        if _is_link(info) or not stat.S_ISREG(info.st_mode) or info.st_size > _MAX_MANIFEST:
            raise _fail("RUNTIME_INVALIDO", "Manifesto nativo inválido.")
        data = manifest_path.read_bytes()
        if hashlib.sha256(data).hexdigest() != pin["manifestSha256"]:
            raise _fail("RUNTIME_ALTERADO", "O manifesto não corresponde ao runtime oficial fixado pelo SDK.")
        manifest = json.loads(data)
        if not isinstance(manifest, dict) or manifest.get("formatVersion") != 1 or manifest.get("testOnly", False) is not False or manifest.get("platform") != key or manifest.get("arch") != "x64":
            raise _fail("RUNTIME_INVALIDO", "Manifesto ou plataforma do runtime inválidos.")
        if manifest.get("sourceRevision") != release["sourceRevision"] or manifest.get("contractHash") != release["contractHash"]:
            raise _fail("CONTRATO_DIVERGENTE", "O contrato do runtime diverge do contrato fixado pelo SDK.")
        inventory = manifest.get("files")
        executable = manifest.get("executable")
        capabilities = manifest.get("capabilities")
        if not isinstance(inventory, dict) or not inventory or len(inventory) > _MAX_ENTRIES or not isinstance(executable, str) or executable not in inventory:
            raise _fail("RUNTIME_INVALIDO", "Inventário nativo não contém um executável válido.")
        if not isinstance(capabilities, list) or not all(isinstance(v, str) and _CAPABILITY.fullmatch(v) for v in capabilities) or "recuperarXml" not in capabilities:
            raise _fail("RUNTIME_INVALIDO", "Capacidades nativas inválidas ou incompletas.")
        for name, digest in inventory.items():
            _path_parts(name)
            if not isinstance(digest, str) or not _HASH.fullmatch(digest):
                raise _fail("RUNTIME_INVALIDO", "Hash inválido no inventário nativo.")
        actual = _inventory(root)
        if actual != set(inventory) | {"manifest.json"}:
            raise _fail("RUNTIME_INCOMPLETO", "Há arquivos nativos ausentes ou fora do manifesto.")
        required = _REQUIRED | ({"ossl-modules/legacy.dll", "sources/win32-x64-SOURCE.json", "licenses/GCC-Runtime.LICENSE", "licenses/GCC-GPL-3.LICENSE", "licenses/MinGW-w64.LICENSE", "licenses/libcrypto-3-x64.dll.LICENSE", "licenses/libssl-3-x64.dll.LICENSE", "licenses/libxml2.dll.LICENSE", "licenses/legacy.dll.LICENSE"} if key == "win32" else {"ossl-modules/legacy.so"})
        if not required <= actual or not any(p.startswith("schemas/") for p in actual) or not any(p.startswith("sources/native/") for p in actual):
            raise _fail("RUNTIME_INCOMPLETO", "Fontes, licenças, schemas ou dependências do runtime estão ausentes.")
        for name, expected in inventory.items():
            with root.joinpath(*_path_parts(name)).open("rb") as handle:
                if _digest(handle) != expected:
                    raise _fail("RUNTIME_ALTERADO", "Um arquivo nativo diverge do manifesto autenticado.")
        build = json.loads((root / "sources/build.json").read_bytes())
        if build.get("testOnly", False) is not False or build.get("sourceRevision") != release["sourceRevision"] or build.get("sourceTreeHash") != release["sourceHash"]:
            raise _fail("CONTRATO_DIVERGENTE", "A proveniência dos fontes do runtime diverge da versão fixada.")
        return Runtime(root, root.joinpath(*_path_parts(executable)), frozenset(capabilities))
    except AcbrError:
        raise
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        raise _fail("RUNTIME_INCOMPLETO", "Não foi possível verificar os arquivos do runtime.") from exc


class _HTTPSRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlsplit(newurl).scheme != "https":
            raise _fail("RUNTIME_DOWNLOAD_FALHOU", "Redirecionamento do runtime exige HTTPS.")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _download(pin: dict, target: Path) -> None:
    if urlsplit(pin["url"]).scheme != "https":
        raise _fail("RUNTIME_DOWNLOAD_FALHOU", "O download do runtime exige HTTPS.")
    deadline = time.monotonic() + 120
    request = Request(pin["url"], headers={"User-Agent": "acbr-python/0.1", "Accept-Encoding": "identity"})
    try:
        with build_opener(_HTTPSRedirect()).open(request, timeout=15) as response, target.open("xb") as output:
            size = 0
            # read1 faz somente uma leitura de socket; read(n) pode esperar por n
            # bytes indefinidamente se um servidor enviar bytes aos poucos.
            while block := response.read1(_CHUNK):
                size += len(block)
                if size > pin["bytes"] or size > _MAX_ARCHIVE or time.monotonic() > deadline:
                    raise _fail("RUNTIME_DOWNLOAD_FALHOU", "O download do runtime excedeu o tamanho ou prazo permitido.")
                output.write(block)
    except AcbrError:
        raise
    except (OSError, URLError) as exc:
        raise _fail("RUNTIME_DOWNLOAD_FALHOU", "Não foi possível baixar o runtime oficial por HTTPS.") from exc


def _unpack(archive: BinaryIO, staging: Path) -> None:
    """Lê apenas o subconjunto USTAR usado pelos dois artefatos oficiais fixados.

    Não usa extract/extractall, extensões PAX/GNU, links, donos ou permissões do tar.
    As fontes .tar.gz internas são preservadas como arquivos, nunca expandidas.
    """
    total = 0
    entries: set[str] = set()
    with gzip.GzipFile(fileobj=archive, mode="rb") as stream:
        def read(size: int) -> bytes:
            nonlocal total
            data = stream.read(size)
            total += len(data)
            if total > _MAX_UNPACKED:
                raise _fail("RUNTIME_INVALIDO", "O pacote nativo excede o limite descomprimido.")
            return data

        while True:
            header = read(512)
            if header == b"\0" * 512:
                if read(512) != b"\0" * 512:
                    raise _fail("RUNTIME_INVALIDO", "Fim de arquivo tar inválido.")
                while tail := read(_CHUNK):
                    if any(tail):
                        raise _fail("RUNTIME_INVALIDO", "Dados adicionais após o pacote tar.")
                break
            if len(header) != 512:
                raise _fail("RUNTIME_INVALIDO", "Arquivo tar truncado.")
            member = tarfile.TarInfo.frombuf(header, "utf-8", "strict")
            if member.type not in {tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE} or member.size < 0 or member.size > _MAX_FILE or member.isdir() and member.size:
                raise _fail("RUNTIME_INVALIDO", "Tipo ou tamanho de entrada tar não permitido.")
            parts = _path_parts(member.name.rstrip("/") if member.isdir() else member.name)
            if parts[0] != "package" or len(parts) < 2:
                raise _fail("RUNTIME_INVALIDO", "Entrada tar fora da raiz package.")
            relative = "/".join(parts[1:])
            if relative.casefold() in entries or len(entries) >= _MAX_ENTRIES:
                raise _fail("RUNTIME_INVALIDO", "Entrada tar duplicada ou inventário excessivo.")
            entries.add(relative.casefold())
            target = staging.joinpath(*parts[1:])
            target.parent.mkdir(parents=True, exist_ok=True)
            if member.isdir():
                target.mkdir(exist_ok=True)
            else:
                remaining = member.size
                with target.open("xb") as output:
                    while remaining:
                        data = read(min(_CHUNK, remaining))
                        if not data:
                            raise _fail("RUNTIME_INVALIDO", "Arquivo tar truncado.")
                        output.write(data)
                        remaining -= len(data)
                padding = (-member.size) % 512
                if len(read(padding)) != padding:
                    raise _fail("RUNTIME_INVALIDO", "Arquivo tar truncado.")


def _publish(staging: Path, destination: Path) -> None:
    # os.rename recusa sobrescrita no Windows; Linux precisa RENAME_NOREPLACE.
    # A ausência desse recurso é um erro, nunca uma substituição não atômica.
    if sys.platform == "win32":
        os.rename(staging, destination)
        return
    libc = ctypes.CDLL(None, use_errno=True)
    rename = getattr(libc, "renameat2", None)
    if rename is None:
        raise OSError(errno.ENOSYS, "renameat2 indisponível")
    rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    rename.restype = ctypes.c_int
    if rename(-100, os.fsencode(staging), -100, os.fsencode(destination), 1) != 0:
        value = ctypes.get_errno()
        raise OSError(value, os.strerror(value))


def install_runtime(destination: Path, archive: Path | None = None) -> Path:
    """Instala pacote completo em destino novo; retorna ``destino/runtime``.

    ``archive`` usa um tarball oficial local e não acessa rede. Sem esse argumento,
    somente esta chamada explícita baixa o artefato HTTPS fixado para a plataforma.
    """
    key = _platform_key()
    release = _release()
    pin = release["platforms"][key]
    try:
        destination = _plain_path(Path(destination))
        if destination.exists():
            raise _fail("RUNTIME_DESTINO_EXISTENTE", "A instalação exige um destino novo; nada será sobrescrito.")
        if not destination.parent.is_dir():
            raise _fail("RUNTIME_DESTINO_INVALIDO", "A pasta pai do destino deve existir.")
        with tempfile.TemporaryDirectory(prefix=".acbr-install-", dir=destination.parent) as temporary:
            work = Path(temporary)
            payload = work / "payload"
            payload.mkdir()
            local = Path(archive) if archive is not None else work / "runtime.tgz"
            if archive is None:
                _download(pin, local)
            with local.open("rb") as handle:
                info = os.fstat(handle.fileno())
                if not stat.S_ISREG(info.st_mode) or info.st_size != pin["bytes"] or info.st_size > _MAX_ARCHIVE or _digest(handle) != pin["sha256"]:
                    raise _fail("RUNTIME_ALTERADO", "O tarball não corresponde ao tamanho e SHA256 oficiais fixados.")
                handle.seek(0)
                _unpack(handle, payload)
            package = json.loads((payload / "package.json").read_bytes())
            if package.get("name") != pin["name"] or package.get("version") != release["version"] or package.get("license") != "LGPL-2.1-or-later" or not all((payload / name).is_file() for name in ("LICENSE", "NOTICE", "README.md")):
                raise _fail("RUNTIME_INVALIDO", "Identificação ou avisos do pacote nativo estão incompletos.")
            runtime = verify_runtime(payload / "runtime")
            if key == "linux":
                runtime.executable.chmod(0o755)
            _publish(payload, destination)
        return destination / "runtime"
    except AcbrError:
        raise
    except FileExistsError as exc:
        raise _fail("RUNTIME_DESTINO_EXISTENTE", "O destino já existe; nada será sobrescrito.") from exc
    except (OSError, ValueError, TypeError, AttributeError, tarfile.TarError, EOFError, zlib.error) as exc:
        raise _fail("RUNTIME_INSTALACAO_FALHOU", "Não foi possível instalar o pacote nativo validado.") from exc


def runtime_environment(runtime: Runtime) -> dict[str, str]:
    """Ambiente mínimo do subprocesso, sem herdar tokens nem opções de OpenSSL."""
    key = _platform_key()
    env = {name: os.environ[name] for name in ("PATH", "Path", "SystemRoot", "WINDIR", "TEMP", "TMP", "HOME", "LANG", "LC_ALL") if name in os.environ}
    if key == "win32":
        inherited = env.pop("Path", env.get("PATH", ""))
        env["PATH"] = str(runtime.directory / "lib") + ";" + str(runtime.directory) + ";" + inherited
    else:
        env["LD_LIBRARY_PATH"] = str(runtime.directory / "lib")
    env["OPENSSL_MODULES"] = str(runtime.directory / "ossl-modules")
    env["OPENSSL_CONF"] = str(runtime.directory / "openssl.cnf")
    return env
