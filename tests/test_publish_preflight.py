"""Exercita o Python real do workflow proposto com HTTP totalmente simulado."""
from contextlib import contextmanager
from copy import deepcopy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError


def python_blocks(workflow):
    lines = workflow.read_text('utf-8').splitlines()
    blocks = []
    for index, line in enumerate(lines):
        if line != '        shell: python':
            continue
        cursor = index + 1
        while lines[cursor] != '        run: |':
            cursor += 1
        code = []
        for current in lines[cursor + 1:]:
            if current and not current.startswith('          '):
                break
            code.append(current[10:])
        blocks.append('\n'.join(code))
    return blocks


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github/workflows/publish-pypi.yml'
CODE = compile(python_blocks(WORKFLOW)[0], str(WORKFLOW) + ':preflight', 'exec')
SHA_CANDIDATE = 'a' * 40  # SHA sintetico da revisao candidata
SHA_PREVIOUS = 'b' * 40  # SHA sintetico de uma revisao anterior
RELEASE_VERSIONS = ('0.1.0a3', '0.1.0a4')
REPOSITORY = 'cosmemilton/acbr-python'
JOBS = [{'name': f'Offline {os_name} / Python {version}', 'status': 'completed', 'conclusion': 'success'}
        for os_name in ('ubuntu-24.04', 'windows-latest') for version in ('3.11', '3.12', '3.13', '3.14')]
JOBS += [{'name': f'Runtime offline {os_name}', 'status': 'completed', 'conclusion': 'success'}
         for os_name in ('ubuntu-24.04', 'windows-latest')]


def run_fixture(**overrides):
    value = {'id': 100, 'run_number': 10, 'run_attempt': 1, 'head_sha': SHA_CANDIDATE,
             'status': 'completed', 'conclusion': 'success', 'event': 'push', 'head_branch': 'main',
             'head_repository': {'full_name': REPOSITORY}}
    value.update(overrides)
    return value


class PreflightTests(unittest.TestCase):
    def exercise(self, runs=None, jobs=None, *, environment=None, http_error=None, malformed=False, name='acbr-python',
                 version='0.1.0a4', source_version=None, notice_version=None, readme=None, version_source=None):
        runs = deepcopy([run_fixture()] if runs is None else runs)
        jobs = deepcopy(JOBS if jobs is None else jobs)
        env = {'GH_TOKEN': 'offline-synthetic-token', 'GITHUB_REPOSITORY': REPOSITORY,
               'GITHUB_SHA': SHA_CANDIDATE, 'GITHUB_REF': 'refs/tags/v' + str(version)}
        env.update(environment or {})
        requested = []
        self.requested = requested

        @contextmanager
        def response(request, *, timeout):
            # This mock is the only HTTP entry point. No socket is opened.
            self.assertEqual(timeout, 30)
            url = request.full_url
            self.assertTrue(url.startswith('https://api.github.com/repos/' + REPOSITORY + '/actions/'))
            requested.append(url)
            if http_error:
                raise http_error
            payload = {'workflow_runs': runs} if '/workflows/ci.yml/runs?' in url else {'jobs': jobs}
            yield io.BytesIO(b'not-json' if malformed else json.dumps(payload).encode())

        with tempfile.TemporaryDirectory(prefix='acbr-preflight-') as directory:
            target = Path(directory)
            (target / 'pyproject.toml').write_text(f'[project]\nname = {json.dumps(name)}\nversion = {json.dumps(version)}\n', encoding='utf-8')
            source_version = version if source_version is None else source_version
            notice_version = version if notice_version is None else notice_version
            package = target / 'src/acbr'
            package.mkdir(parents=True)
            if version_source is None:
                version_source = '"""Versao sintetica, nunca importada pelo preflight."""\n__version__ = ' + json.dumps(source_version) + '\n'
            (package / '_version.py').write_text(version_source, encoding='utf-8')
            (target / 'NOTICE').write_text('ACBr Python ' + str(notice_version) + '\nAviso sintetico.\n', encoding='utf-8')
            if readme is None:
                readme = '# ACBr Python\n\nVersão alpha ' + str(version) + '\n\nCandidato; publicação ainda não afirmada.\n'
            (target / 'README.md').write_text(readme, encoding='utf-8')
            previous = Path.cwd()
            try:
                os.chdir(target)
                with (
                    patch.dict(os.environ, env, clear=True),
                    patch('urllib.request.urlopen', response),
                    patch('socket.getaddrinfo', side_effect=AssertionError('REDE_PROIBIDA_NO_TESTE')),
                    patch('socket.socket', side_effect=AssertionError('REDE_PROIBIDA_NO_TESTE')),
                ):
                    exec(CODE, {})
            finally:
                os.chdir(previous)
        return requested

    def test_main_push_exact_sha_all_ten_jobs(self):
        for version in RELEASE_VERSIONS:
            with self.subTest(version=version):
                urls = self.exercise(version=version)
                self.assertEqual(len(urls), 2)
                self.assertIn('head_sha=' + SHA_CANDIDATE, urls[0])
                self.assertNotIn('status=completed', urls[0])
                self.assertIn('/runs/100/jobs?filter=latest', urls[1])

    def test_manual_tag_exact_sha(self):
        for version in RELEASE_VERSIONS:
            with self.subTest(version=version):
                self.exercise([run_fixture(event='workflow_dispatch', head_branch='v' + version)], version=version)

    def test_previous_revision_success_cannot_approve_candidate(self):
        with self.assertRaises(AssertionError): self.exercise([run_fixture(head_sha=SHA_PREVIOUS)])

    def test_pr_only_cannot_prove_checkout(self):
        with self.assertRaises(AssertionError): self.exercise([run_fixture(event='pull_request')])

    def test_fork_cannot_approve_release(self):
        with self.assertRaises(AssertionError): self.exercise([run_fixture(head_repository={'full_name': 'someone/fork'})])

    def test_feature_push_cannot_approve_release(self):
        with self.assertRaises(AssertionError): self.exercise([run_fixture(head_branch='feature')])

    def test_no_ci(self):
        with self.assertRaises(AssertionError): self.exercise([])

    def test_newer_failure_blocks_old_success(self):
        with self.assertRaises(AssertionError):
            self.exercise([run_fixture(), run_fixture(id=101, run_number=11, conclusion='failure')])

    def test_newer_pending_blocks_old_success(self):
        with self.assertRaises(AssertionError):
            self.exercise([run_fixture(id=101, run_number=11, status='in_progress', conclusion=None), run_fixture()])

    def test_latest_rerun_failure_blocks_previous_attempt(self):
        with self.assertRaises(AssertionError):
            self.exercise([run_fixture(run_attempt=2, conclusion='failure'), run_fixture()])

    def test_latest_success_is_selected_independent_of_list_order(self):
        urls = self.exercise([run_fixture(conclusion='failure'), run_fixture(id=101, run_number=11)])
        self.assertIn('/runs/101/jobs?', urls[1])

    def test_missing_native_jobs(self):
        with self.assertRaises(AssertionError): self.exercise(jobs=JOBS[:8])

    def test_skipped_native_job(self):
        jobs = deepcopy(JOBS); jobs[-1]['conclusion'] = 'skipped'
        with self.assertRaises(AssertionError): self.exercise(jobs=jobs)

    def test_incomplete_job(self):
        jobs = deepcopy(JOBS); jobs[0]['status'] = 'in_progress'
        with self.assertRaises(AssertionError): self.exercise(jobs=jobs)

    def test_duplicate_name_does_not_replace_missing_job(self):
        jobs = deepcopy(JOBS); jobs[-1]['name'] = jobs[0]['name']
        with self.assertRaises(AssertionError): self.exercise(jobs=jobs)

    def test_unexpected_extra_job_does_not_weaken_exact_ten_job_gate(self):
        jobs = deepcopy(JOBS) + [{'name': 'Unexpected job', 'status': 'completed', 'conclusion': 'success'}]
        with self.assertRaises(AssertionError): self.exercise(jobs=jobs)

    def test_http_unavailable_fails_closed(self):
        with self.assertRaises(URLError): self.exercise(http_error=URLError('offline simulated'))

    def test_invalid_json_fails_closed(self):
        with self.assertRaises(json.JSONDecodeError): self.exercise(malformed=True)

    def test_wrong_tag(self):
        with self.assertRaises(AssertionError): self.exercise(environment={'GITHUB_REF': 'refs/tags/v0.1.0a3'})
        self.assertEqual(self.requested, [])

    def test_wrong_distribution_name(self):
        with self.assertRaises(AssertionError): self.exercise(name='another-project')

    def test_wrong_target_repository(self):
        with self.assertRaises(AssertionError): self.exercise(environment={'GITHUB_REPOSITORY': 'another/project'})

    def test_zero_components_and_alpha_zero_are_canonical(self):
        self.exercise(version='0.0.0a0')

    def test_nonfinal_or_noncanonical_versions_fail_before_http(self):
        versions = ('0.1.0a4.dev0', '0.1.0rc1', '0.1.0b1', '0.1.0', '0.1.0a4.post1', '0.1.0a4+local',
                    '1!0.1.0a4', '0.1.0alpha4', '0.1.0a04', '00.1.0a4', '0.01.0a4',
                    '0.1.00a4', '0.1a4', '0.1.0.1a4', ' 0.1.0a4', '0.1.0a4\n', 4)
        for version in versions:
            with self.subTest(version=version), self.assertRaises(AssertionError):
                self.exercise(version=version)
            self.assertEqual(self.requested, [])

    def test_source_version_must_equal_pyproject_before_http(self):
        for project, source in (('0.1.0a3', '0.1.0a4'), ('0.1.0a4', '0.1.0a3'), ('0.1.0a4', '0.1.0a4.dev0')):
            with self.subTest(project=project, source=source), self.assertRaises(AssertionError):
                self.exercise(version=project, source_version=source)
            self.assertEqual(self.requested, [])

    def test_notice_version_must_equal_pyproject_before_http(self):
        for version in RELEASE_VERSIONS:
            with self.subTest(version=version), self.assertRaises(AssertionError):
                self.exercise(version=version, notice_version='0.1.0a4.dev0')
            self.assertEqual(self.requested, [])

    def test_version_module_is_a_literal_and_is_never_executed(self):
        versions = ('__version__ = "0.1.0" + "a4"\n',
                    '__version__ = "0.1.0a4"\n__version__ = "0.1.0a4"\n',
                    '__version__ = "0.1.0a4"\nraise RuntimeError("VERSION_MODULE_WAS_EXECUTED")\n',
                    '__version__ = 4\n')
        for source in versions:
            with self.subTest(source=source), self.assertRaises(AssertionError):
                self.exercise(version_source=source)
            self.assertEqual(self.requested, [])

    def test_readme_requires_exact_unique_release_marker_not_draft_or_substring(self):
        readmes = ('Este checkout: 0.1.0a4.dev0, em desenvolvimento.\n',
                   'Versão alpha 0.1.0a4.dev0\n', 'Versão alpha 0.1.0a40\n',
                   '**Versão alpha 0.1.0a4**\n', 'Versão alpha 0.1.0a4.\n',
                   'Versão alpha 0.1.0a4\nVersão alpha 0.1.0a4\n')
        for readme in readmes:
            with self.subTest(readme=readme), self.assertRaises(AssertionError):
                self.exercise(readme=readme)
            self.assertEqual(self.requested, [])

    def test_candidate_readme_can_document_previous_published_release(self):
        self.exercise(readme='Versão alpha 0.1.0a4\n\nVersão publicada no PyPI: 0.1.0a3.\n'
                            'Este candidato ainda não foi publicado.\npython -m pip install acbr-python==0.1.0a3\n')


if __name__ == '__main__':
    unittest.main()
