"""Testes offline do instalador; executáveis e certificados não são usados."""

from __future__ import annotations

from contextlib import ExitStack
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

from acbr.errors import AcbrError
from acbr import runtime as rt


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.platform = "win32" if sys.platform == "win32" else "linux"
        self.release = copy.deepcopy(rt._release())
        self.manifest = {
            "formatVersion": 1, "sourceRevision": self.release["sourceRevision"],
            "contractHash": self.release["contractHash"], "platform": self.platform,
            "arch": "x64", "executable": "worker.exe" if self.platform == "win32" else "worker",
            "capabilities": ["recuperarXml"],
        }
        required = set(rt._REQUIRED) | {"schemas/synthetic.xsd", "sources/native/synthetic.pas", self.manifest["executable"]}
        if self.platform == "win32":
            required |= {"ossl-modules/legacy.dll", "sources/win32-x64-SOURCE.json", "licenses/GCC-Runtime.LICENSE", "licenses/GCC-GPL-3.LICENSE", "licenses/MinGW-w64.LICENSE", "licenses/libcrypto-3-x64.dll.LICENSE", "licenses/libssl-3-x64.dll.LICENSE", "licenses/libxml2.dll.LICENSE", "licenses/legacy.dll.LICENSE"}
        else:
            required.add("ossl-modules/legacy.so")
        self.data = {name: b"SYNTHETIC OFFLINE FIXTURE\n" for name in required}
        self.data["sources/build.json"] = json.dumps({"sourceRevision": self.release["sourceRevision"], "sourceTreeHash": self.release["sourceHash"]}).encode()
        self.manifest["files"] = {name: hashlib.sha256(data).hexdigest() for name, data in self.data.items()}
        self.archive = self.root / "synthetic.tgz"
        self._write_archive()
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.object(rt, "_release", return_value=self.release))
        self.stack.enter_context(patch.object(rt, "_platform_key", return_value=self.platform))

    def _manifest_bytes(self):
        data = json.dumps(self.manifest, sort_keys=True).encode()
        self.release["platforms"][self.platform]["manifestSha256"] = hashlib.sha256(data).hexdigest()
        return data

    def _write_archive(self, extra=()):
        manifest = self._manifest_bytes()
        package = {"name": self.release["platforms"][self.platform]["name"], "version": self.release["version"], "license": "LGPL-2.1-or-later"}
        entries = {"package.json": json.dumps(package).encode(), "LICENSE": b"SYNTHETIC LICENSE", "NOTICE": b"SYNTHETIC NOTICE", "README.md": b"SYNTHETIC README", "runtime/manifest.json": manifest}
        entries.update({"runtime/" + name: data for name, data in self.data.items()})
        with tarfile.open(self.archive, "w:gz", format=tarfile.USTAR_FORMAT) as handle:
            for name, data in entries.items():
                member = tarfile.TarInfo("package/" + name)
                member.size = len(data)
                handle.addfile(member, io.BytesIO(data))
            for member, data in extra:
                handle.addfile(member, io.BytesIO(data))
        pin = self.release["platforms"][self.platform]
        pin["sha256"] = hashlib.sha256(self.archive.read_bytes()).hexdigest()
        pin["bytes"] = self.archive.stat().st_size

    def _install(self, name="installed"):
        return rt.install_runtime(self.root / name, self.archive)

    def assertCode(self, code, function, *args, **kwargs):
        with self.assertRaises(AcbrError) as caught:
            function(*args, **kwargs)
        self.assertEqual(code, caught.exception.codigo)
        self.assertFalse(caught.exception.resultado_desconhecido)
        self.assertEqual("runtime", caught.exception.diagnostico.etapa)

    def test_install_preserves_package_and_verifies_inventory(self):
        with patch.object(rt, "_download", side_effect=AssertionError("offline")):
            directory = self._install()
        native = rt.verify_runtime(directory)
        self.assertEqual(self.root / "installed/runtime", native.directory)
        self.assertEqual({"recuperarXml"}, native.capabilities)
        self.assertEqual(self.data["sources/acbr-source.tar.gz"], (directory / "sources/acbr-source.tar.gz").read_bytes())
        self.assertEqual(b"SYNTHETIC LICENSE", (directory.parent / "LICENSE").read_bytes())
        self.assertTrue((directory.parent / "NOTICE").is_file())
        self.assertTrue((directory / "sources/native/synthetic.pas").is_file())
        if self.platform == "linux":
            self.assertTrue(native.executable.stat().st_mode & 0o100)

    def test_existing_destination_refused_before_download(self):
        destination = self.root / "existing"
        destination.mkdir()
        with patch.object(rt, "_download", side_effect=AssertionError("offline")):
            self.assertCode("RUNTIME_DESTINO_EXISTENTE", rt.install_runtime, destination)

    def test_racing_destination_is_never_overwritten(self):
        original = rt._publish
        def racing(staging, destination):
            destination.mkdir()
            original(staging, destination)
        with patch.object(rt, "_publish", side_effect=racing):
            self.assertCode("RUNTIME_DESTINO_EXISTENTE", self._install)
        self.assertTrue((self.root / "installed").is_dir())
        self.assertEqual([], list((self.root / "installed").iterdir()))

    def test_explicit_download_only_when_archive_is_absent(self):
        def download(pin, target):
            shutil.copyfile(self.archive, target)
        with patch.object(rt, "_download", side_effect=download) as request:
            rt.install_runtime(self.root / "downloaded")
        request.assert_called_once()

    def test_https_download_size_and_deadline_limits(self):
        pin = {"url": "https://example.invalid/runtime.tgz", "bytes": 2}
        for data, clock in ((b"large", None), (b"ok", [0, 121])):
            with self.subTest(data=data), ExitStack() as stack:
                response = io.BytesIO(data)
                opener = SimpleNamespace(open=lambda *args, **kwargs: response)
                stack.enter_context(patch.object(rt, "build_opener", return_value=opener))
                if clock:
                    stack.enter_context(patch.object(rt.time, "monotonic", side_effect=clock))
                target = self.root / "download.tgz"
                self.assertCode("RUNTIME_DOWNLOAD_FALHOU", rt._download, pin, target)
                target.unlink()

    def test_download_and_redirect_require_https(self):
        self.assertCode("RUNTIME_DOWNLOAD_FALHOU", rt._download, {"url": "http://example.invalid/runtime.tgz"}, self.root / "download.tgz")
        self.assertCode("RUNTIME_DOWNLOAD_FALHOU", rt._HTTPSRedirect().redirect_request, None, None, 302, "", {}, "http://example.invalid/runtime.tgz")

    def test_archive_corruption_and_staging_cleanup(self):
        with self.archive.open("r+b") as handle:
            handle.write(b"CORRUPT")
        self.assertCode("RUNTIME_ALTERADO", self._install)
        self.assertFalse((self.root / "installed").exists())
        self.assertEqual([], list(self.root.glob(".acbr-install-*")))

    def test_file_corruption(self):
        directory = self._install()
        (directory / self.manifest["executable"]).write_bytes(b"altered")
        self.assertCode("RUNTIME_ALTERADO", rt.verify_runtime, directory)

    def test_modified_manifest_cannot_authenticate_modified_file(self):
        directory = self._install()
        worker = directory / self.manifest["executable"]
        worker.write_bytes(b"altered")
        self.manifest["files"][self.manifest["executable"]] = hashlib.sha256(b"altered").hexdigest()
        (directory / "manifest.json").write_text(json.dumps(self.manifest), encoding="utf-8")
        self.assertCode("RUNTIME_ALTERADO", rt.verify_runtime, directory)

    def test_unlisted_file_and_missing_source_refused(self):
        directory = self._install()
        (directory / "extra.dll").write_bytes(b"extra")
        self.assertCode("RUNTIME_INCOMPLETO", rt.verify_runtime, directory)
        (directory / "extra.dll").unlink()
        (directory / "sources/acbr-source.tar.gz").unlink()
        self.assertCode("RUNTIME_INCOMPLETO", rt.verify_runtime, directory)

    def test_manifest_platform_and_contract_mismatch(self):
        for field, value, code in (("platform", "other", "RUNTIME_INVALIDO"), ("arch", "arm64", "RUNTIME_INVALIDO"), ("contractHash", "0" * 64, "CONTRATO_DIVERGENTE"), ("sourceRevision", 1, "CONTRATO_DIVERGENTE"), ("testOnly", True, "RUNTIME_INVALIDO")):
            with self.subTest(field=field):
                old = self.manifest.get(field)
                self.manifest[field] = value
                self._write_archive()
                self.assertCode(code, self._install)
                if old is None:
                    self.manifest.pop(field)
                else:
                    self.manifest[field] = old

    def test_executable_must_be_listed(self):
        self.manifest["executable"] = "not-in-inventory"
        self._write_archive()
        self.assertCode("RUNTIME_INVALIDO", self._install)

    def test_build_provenance_must_match(self):
        self.data["sources/build.json"] = b"{}"
        self.manifest["files"]["sources/build.json"] = hashlib.sha256(b"{}").hexdigest()
        self._write_archive()
        self.assertCode("CONTRATO_DIVERGENTE", self._install)

    def test_path_traversal_absolute_windows_ads_and_case_collision(self):
        for name in ("package/../escaped", "/escaped", "package/C:/escaped", "package/runtime\\escaped", "package/runtime/worker:secret", "package/runtime/CON.txt", "package/runtime/../escaped", "package/license"):
            with self.subTest(name=name):
                member = tarfile.TarInfo(name)
                member.size = 1
                self._write_archive([(member, b"x")])
                self.assertCode("RUNTIME_INVALIDO", self._install)
                self.assertFalse((self.root / "escaped").exists())

    def test_links_special_files_and_extended_headers_refused(self):
        for kind in (tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.FIFOTYPE, tarfile.XHDTYPE):
            with self.subTest(kind=kind):
                member = tarfile.TarInfo("package/link")
                member.type = kind
                member.linkname = "runtime/worker"
                self._write_archive([(member, b"")])
                self.assertCode("RUNTIME_INVALIDO", self._install)

    def test_unpack_limits(self):
        for option, value in (("_MAX_FILE", 1), ("_MAX_ENTRIES", 1), ("_MAX_UNPACKED", 512)):
            with self.subTest(option=option), patch.object(rt, option, value):
                self.assertCode("RUNTIME_INVALIDO", self._install)

    def test_environment_does_not_inherit_secrets_or_openssl_options(self):
        runtime = rt.Runtime(self.root, self.root / "worker", frozenset())
        with patch.dict(os.environ, {"PRIVATE_TOKEN": "sensitive", "OPENSSL_CONF": "unsafe", "LD_PRELOAD": "unsafe", "PYTHONPATH": "unsafe"}):
            environment = rt.runtime_environment(runtime)
        self.assertNotIn("PRIVATE_TOKEN", environment)
        self.assertNotIn("LD_PRELOAD", environment)
        self.assertNotIn("PYTHONPATH", environment)
        self.assertEqual(str(self.root / "openssl.cnf"), environment["OPENSSL_CONF"])
        self.assertEqual(str(self.root / "ossl-modules"), environment["OPENSSL_MODULES"])

    def test_unsupported_platform_and_python_bitness(self):
        self.stack.close()
        for platform_name, machine, bits in (("darwin", "x86_64", 8), ("linux", "aarch64", 8), ("win32", "AMD64", 4)):
            with self.subTest(platform=platform_name, machine=machine), patch.object(rt.sys, "platform", platform_name), patch.object(rt.platform, "machine", return_value=machine), patch.object(rt.struct, "calcsize", return_value=bits):
                self.assertCode("PLATAFORMA_NAO_SUPORTADA", rt._platform_key)

    def test_linux_musl_refused(self):
        self.stack.close()
        with patch.object(rt.sys, "platform", "linux"), patch.object(rt.platform, "machine", return_value="x86_64"), patch.object(rt.struct, "calcsize", return_value=8), patch.object(rt.platform, "libc_ver", return_value=("musl", "1.2")):
            self.assertCode("PLATAFORMA_NAO_SUPORTADA", rt._platform_key)

    def test_runtime_symlink_refused(self):
        directory = self._install()
        link = self.root / "linked"
        try:
            link.symlink_to(directory, target_is_directory=True)
        except OSError:
            self.skipTest("criação de symlink exige permissão adicional neste Windows")
        self.assertCode("RUNTIME_INVALIDO", rt.verify_runtime, link)


if __name__ == "__main__":
    unittest.main()
