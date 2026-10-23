"""ROOT-owned full gate; only actual green releases commit, push, publish and draft PR."""
import datetime
import hashlib
import json
import os
import pathlib
import re
import shutil
import signal
import subprocess
import sys

R = pathlib.Path('/workspace/chicago-waistcoat')
A = R / 'chicago/4d'
G = pathlib.Path('/workspace/shared/T2800-STANDING-STALE-DIAGNOSTICS-FULL-PREFLIGHT-G10-ACTUAL-20261023')
O = pathlib.Path('/workspace/shared/T2800-ACTUAL-GREEN-COMMIT-PUSH-PUBLISH-20261023')
W = pathlib.Path('/workspace/shared/T2800-POSTGREEN-COMMIT-PUSH-PUBLISH-STALE-DIAGNOSTICS-G10-20261023.py')
B = pathlib.Path('/workspace/shared/T2800-STANDING-G10-DRAFT-PR-BODY-TEMPLATE-20261023.md')
HELPER = pathlib.Path('/workspace/shared/owned_child_reaper_20261023.py')
BASE = 'e4745b3c5714185079215d06d8072a4791c6de4a'
TREE = '3ce3cf74571fd82bdd6dc098dc1e0cc03a4b1c1d'
BRANCH = 'steward/t2800-planted-standing-v16-dev-20261023'
PINS = {
    HELPER: '60ea8bdddc4491cdc788c2574194e2e33410c0c01c3d9a9a0c73a9751b37df2f',
    W: 'cdbd9bf717a08413f55679bf94c3c8fcb7602525841e2db165052dafc39000a0',
    B: 'b622c91ddb1f174ba1c14582b3b9b883973a45b4b270fb0c2ab405bba1c05b1b',
}


def main():
    assert sys.argv[1:] == ['--root-authorized']
    for path, digest in PINS.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, path
    sys.path.insert(0, '/workspace/shared')
    import owned_child_reaper_20261023 as owned
    owned.enable()
    env = os.environ.copy()
    env['PATH'] = '/workspace/shared/w01-python-sum-recovery-20261022/venv311/bin:/workspace/shared/chicago-tools/usr/bin:' + env['PATH']
    env.update(CHECK_JOBS='1', NODE_OPTIONS='--v8-pool-size=1 --disable-sigusr1', UV_THREADPOOL_SIZE='1',
               GOMAXPROCS='1', C4D_GATE_REQUIRE_READERS='1', BASE=BASE,
               GIT_CONFIG_COUNT='3', GIT_CONFIG_KEY_0='index.threads', GIT_CONFIG_VALUE_0='1',
               GIT_CONFIG_KEY_1='pack.threads', GIT_CONFIG_VALUE_1='1',
               GIT_CONFIG_KEY_2='core.preloadIndex', GIT_CONFIG_VALUE_2='false')
    env.update({key: '1' for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
                                   'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS']})
    now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()

    def git(*args):
        value = subprocess.check_output(['git', '-C', str(R), *args], env=env, text=True).strip()
        owned.reap_orphans()
        return value

    def save(path, value):
        path.write_text(json.dumps(value, indent=2) + '\n')

    def progress(signum, frame):
        # Same existing parent, no child/thread/command; monitoring cannot consume
        # the headroom needed by deeply nested real ticket-CLI fixtures.
        try:
            timings = G / 'TIMINGS.tsv'
            lines = timings.read_text().splitlines() if timings.exists() else []
            print('PREFLIGHT PROGRESS ' + json.dumps({'at': now(),
                  'completed_timing_entries_not_check_count': len(lines),
                  'last_completed_timing': lines[-1:] }), flush=True)
        except Exception:
            pass  # Best-effort telemetry must never change the gate's result.

    def run(command, log, timeout):
        watching = command == ['bash', 'tools/preflight.sh']
        if watching:
            signal.signal(signal.SIGALRM, progress)
            signal.setitimer(signal.ITIMER_REAL, 30, 30)
        try:
            value = owned.run(command, A, env, log, timeout)
        finally:
            if watching:
                signal.setitimer(signal.ITIMER_REAL, 0)
        value['new_owned_orphans_reaped_count'] = len(value.pop('new_owned_orphans_reaped', []))
        return value

    def checked(name, command, timeout=90):
        value = run(command, O / (name + '.log'), timeout)
        save(O / (name + '.json'), value)
        assert value['returncode'] == 0, name
        return (O / (name + '.log')).read_text()

    try:
        assert not G.exists() and not O.exists()
        assert git('rev-parse', 'HEAD') == BASE and git('write-tree') == TREE
        assert git('branch', '--show-current') == BRANCH
        assert not git('diff', '--name-only') and not git('ls-files', '-u')
        assert not git('ls-files', '--others', '--exclude-standard')
        assert len(git('diff', '--cached', '--name-only', BASE).splitlines()) == 43
        G.mkdir()
        env['CHECK_TIMINGS'] = str(G / 'TIMINGS.tsv')
        start = {'started': now(), 'head': BASE, 'staged_tree': TREE, 'owner_pid': os.getpid(),
                 'command': ['bash', 'tools/preflight.sh'], 'CHECK_JOBS': 1,
                 'standard_Node_launcher': True, 'disable_SIGUSR1_inspector_watcher': True,
                 'actual_simple_Node_threads': 3, 'progress_uses_parent_SIGALRM_no_extra_process': True,
                 'all_other_local_launches_paused': True, 'Node_V8_workers': 1, 'UV_workers': 1,
                 'math_threads': 1, 'Git_index_threads': 1, 'Git_pack_threads': 1,
                 'Git_preloadIndex': False, 'whole_serial_deadline_seconds': 5400,
                 'own_child_subreaper': True, 'nine_prior_nonpasses_preserved': True,
                 'never_touches_PID1_or_existing_orphans': True, 'ticket_commands_frozen': True,
                 'commit_push_executed': False, 'postgreen_writer_sha256': PINS[W],
                 'postgreen_PR_action': 'create one draft only after exact committed/pushed/published PASS'}
        save(G / 'START.json', start)
        print(json.dumps(start), flush=True)
        result = run(['bash', 'tools/preflight.sh'], G / 'PRE-FLIGHT.log', 5400)
        for name in ['preflight-check.log', 'preflight-cl.log', 'preflight-ids.log']:
            path = pathlib.Path('/tmp') / name
            if path.exists():
                shutil.copyfile(path, G / name)
        result = {**start, **result, 'finished': now(), 'final_staged_tree': git('write-tree'),
                  'unstaged': git('diff', '--name-only').splitlines()}
        save(G / 'RESULT.json', result)
        cleanup = owned.finish()
        save(G / 'OWNED-PREFLIGHT-CLEANUP.json', cleanup)
        assert not cleanup['remaining_owned_children']
        print('FULL PREFLIGHT ' + json.dumps(result), flush=True)
        print((G / 'PRE-FLIGHT.log').read_text()[-7000:], flush=True)
        assert result['final_staged_tree'] == TREE and result['unstaged'] == []
        if result['returncode'] != 0:
            raise SystemExit(result['returncode'])
        post = run([sys.executable, str(W), '--root-authorized'], G / 'POSTGREEN-CONTINUATION.log', 1200)
        save(G / 'POSTGREEN-RESULT.json', post)
        print('POSTGREEN ' + json.dumps(post), flush=True)
        print((G / 'POSTGREEN-CONTINUATION.log').read_text()[-12000:], flush=True)
        assert post['returncode'] == 0
        terminal = json.loads((O / 'TERMINAL.json').read_text())
        head = git('rev-parse', 'HEAD')
        assert terminal['status'] == 'PASS' and terminal['head'] == head and terminal['tree'] == TREE
        assert git('rev-parse', 'HEAD^{tree}') == TREE and not git('status', '--porcelain')
        assert json.loads((O / 'PUSHED.json').read_text())['head'] == head
        full = json.loads((O / 'ACTUAL-FULLGATE-PASS.json').read_text())
        body = B.read_text().replace('[[HEAD]]', head).replace('[[STEP_COUNT]]', str(full['actual_steps']))
        assert len(full['selftests']) == 1
        body = body.replace('[[SELFTEST_COUNT]]', full['selftests'][0])
        assert '[[' not in body
        body_path = O / 'DRAFT-PR-BODY.md'
        body_path.write_text(body)
        existing = json.loads(checked('13-EXISTING-BRANCH-PRS',
            ['gh', 'pr', 'list', '--repo', 'kevinrhaas/chicago', '--head', BRANCH,
             '--state', 'all', '--json', 'number,headRefOid,baseRefName,state,isDraft,url']))
        assert existing == [], 'Existing branch PR requires explicit review; never duplicate or edit blindly'
        url = checked('14-CREATE-DRAFT-PR', ['gh', 'pr', 'create', '--repo', 'kevinrhaas/chicago',
            '--base', 'dev', '--head', BRANCH, '--draft', '--title',
            'T-2800: add a planted standing horse to the Western Hotel yard',
            '--body-file', str(body_path)]).strip()
        match = re.fullmatch(r'https://github\.com/kevinrhaas/chicago/pull/(\d+)', url)
        assert match, url
        number = int(match.group(1))
        pr = json.loads(checked('15-VERIFY-DRAFT-PR',
            ['gh', 'api', '--method', 'GET', f'repos/kevinrhaas/chicago/pulls/{number}']))
        assert pr['head']['sha'] == head and pr['head']['ref'] == BRANCH
        assert pr['head']['repo']['full_name'] == 'kevinrhaas/chicago'
        assert pr['base']['ref'] == 'dev' and pr['state'] == 'open' and pr['draft'] is True
        assert pr['auto_merge'] is None
        save(O / 'PR-CREATED.json', {'number': number, 'url': url, 'head': head, 'tree': TREE,
             'draft': True, 'created_or_verified_at': now(), 'ready': False, 'merged': False,
             'normal_CI_and_actual_yard_qualification': 'PENDING'})
        print('DRAFT PR CREATED ' + url, flush=True)
    finally:
        cleanup = owned.finish()
        if G.exists():
            save(G / 'FINAL-OWNED-CLEANUP.json', cleanup)
        print('FINAL OWNED CLEANUP ' + json.dumps(cleanup), flush=True)


if __name__ == '__main__':
    main()
