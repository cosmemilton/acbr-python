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
SHA_A3 = 'a' * 40  # SHA sintetico da revisao candidata
SHA_A2 = 'b' * 40  # SHA sintetico de uma revisao anterior
REPOSITORY = 'cosmemilton/acbr-python'
JOBS = [{'name': f'Offline {os_name} / Python {version}', 'status': 'completed', 'conclusion': 'success'}
        for os_name in ('ubuntu-24.04', 'windows-latest') for version in ('3.11', '3.12', '3.13', '3.14')]
JOBS += [{'name': f'Runtime offline {os_name}', 'status': 'completed', 'conclusion': 'success'}
         for os_name in ('ubuntu-24.04', 'windows-latest')]


def run_fixture(**overrides):
    value = {'id': 100, 'run_number': 10, 'run_attempt': 1, 'head_sha': SHA_A3,
             'status': 'completed', 'conclusion': 'success', 'event': 'push', 'head_branch': 'main',
             'head_repository': {'full_name': REPOSITORY}}
    value.update(overrides)
    return value


class PreflightTests(unittest.TestCase):
    def exercise(self, runs=None, jobs=None, *, environment=None, http_error=None, malformed=False, name='acbr-python'):
        runs = deepcopy([run_fixture()] if runs is None else runs)
        jobs = deepcopy(JOBS if jobs is None else jobs)
        env = {'GH_TOKEN': 'offline-synthetic-token', 'GITHUB_REPOSITORY': REPOSITORY,
               'GITHUB_SHA': SHA_A3, 'GITHUB_REF': 'refs/tags/v0.1.0a3'}
        env.update(environment or {})
        requested = []

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
            (target / 'pyproject.toml').write_text(f'[project]\nname = "{name}"\nversion = "0.1.0a3"\n', encoding='utf-8')
            (target / 'README.md').write_text('Versao alpha 0.1.0a3', encoding='utf-8')
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
        urls = self.exercise()
        self.assertEqual(len(urls), 2)
        self.assertIn('head_sha=' + SHA_A3, urls[0])
        self.assertNotIn('status=completed', urls[0])
        self.assertIn('/runs/100/jobs?filter=latest', urls[1])

    def test_manual_tag_exact_sha(self):
        self.exercise([run_fixture(event='workflow_dispatch', head_branch='v0.1.0a3')])

    def test_a2_success_cannot_approve_a3(self):
        with self.assertRaises(AssertionError): self.exercise([run_fixture(head_sha=SHA_A2)])

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

    def test_http_unavailable_fails_closed(self):
        with self.assertRaises(URLError): self.exercise(http_error=URLError('offline simulated'))

    def test_invalid_json_fails_closed(self):
        with self.assertRaises(json.JSONDecodeError): self.exercise(malformed=True)

    def test_wrong_tag(self):
        with self.assertRaises(AssertionError): self.exercise(environment={'GITHUB_REF': 'refs/tags/v0.1.0a2'})

    def test_wrong_distribution_name(self):
        with self.assertRaises(AssertionError): self.exercise(name='another-project')

    def test_wrong_target_repository(self):
        with self.assertRaises(AssertionError): self.exercise(environment={'GITHUB_REPOSITORY': 'another/project'})


if __name__ == '__main__':
    unittest.main()
