---
id: T-3641
title: PR gate part 7/8 is intermittently red on the Catalogue Brougham check (T-3084): brougham_v20/check.py 'far: every triangle re-derives' fails on some CI runners, passes on rerun and locally
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-17
closed: null
pr: null
claimed_by: run 11/18/2026, 3:04:46 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/44265091868
claimed_at: 2026-11-18T09:04:47.607Z
decision: null
decision_answer: null
---

PR gate part 7/8 is intermittently red on the Catalogue Brougham check (T-3084): brougham_v20/check.py 'far: every triangle re-derives' fails on some CI runners, passes on rerun and locally.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR gates on #2151, #2111 and #2149 go red on this step independently of their diffs; #2151's part 7/8 failed twice and passed on a plain rerun (job 134198487869)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (finish-only slice 4/8, 2026-11-17)

- `tools/transport/brougham_v20/check.py:198` asserts `expanded_signature(far regenerated) == committed far`. The far source comes from `produce.far_source()`, which re-runs V19's `generate.py` (numpy) and then simplifies; the near and mid levels compare bytes and pass on the same runs.
- Red on #2151 at f2cbb1f (job 134099573403) and at 513f083 (job 134160844279); a plain rerun of the second (job 134198487869) passed, with nothing pushed in between. Dev's own gate part 7/8 on 285b225 passed the same step.
- Not reproduced locally on 513f083: `check.py` passes under Python 3.14.4 (numpy 2.5.5) and under 3.11.18 in a fresh venv (numpy 2.4.6, scipy 1.17.1, the CI install line), and `check.sh --part 7/8` is green.
- The same `bake gate part 7/8` red shows on #2111 (its lap notes it too) and #2149.
- Likely suspects: per-runner float differences in the numpy path that re-derives far (CPU SIMD dispatch varies between runner hosts), or the CI's unpinned `pip install numpy scipy`. The fix is to make the far comparison robust or the derivation deterministic. Do not loosen the check.
