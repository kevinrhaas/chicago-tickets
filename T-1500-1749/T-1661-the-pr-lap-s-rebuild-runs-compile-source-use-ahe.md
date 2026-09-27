---
id: T-1661
title: The PR lap's rebuild runs compile_source_use ahead of compile_scene, so a lapped branch loses 38 source-use claims and gates red while looking merged
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 9/27/2026, 8:55:56 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36322660055
claimed_at: 2026-09-27T13:55:56.933Z
decision: null
decision_answer: null
---

The PR lap's rebuild runs compile_source_use ahead of compile_scene, so a lapped branch loses 38 source-use claims and gates red while looking merged.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

MEASURED 2026-09-27 on PR #105 (`steward/t-1275-loading-content`). The 2-hourly sweep
lapped the branch onto dev and pushed `4455713` — "Lap onto dev: generated files
regenerated, not merged". Gating that exact commit with `./tools/check.sh` gives

    CHECK FAIL — 3 of 657 steps failed:
      * Source-use backlinks match authored claims (T-1248)
      * source browser counts and filters
      * the three levels mean what they say

**The cause is ordering, not the merge.** `tools/derived_manifest.json` step 122 says in
as many words why `compile_source_use.py` follows `compile_scene.py`: "source-use is a
pure export of the authored families and current-scene membership, so it follows
compile_scene.py". The lap regenerated source-use against the PRE-merge scene. Re-running
the compiler in the right order on the same tree fixes all three steps and changes exactly
two files.

**What it cost, measured.** `data/sidecars/1835/sources/index.json`, source
`owner_chicago_1835_reconstruction_spec_2026`:

| | claims | entities |
|---|---|---|
| the lap's rebuild | 3582 | 324 |
| a correct derivation | 3620 | 324 |

38 claims silently absent. Nothing else in the file differs, and the source id set is
identical — so nothing about the tree announces the loss except the gate.

**Why this is not T-1521.** T-1521 (done, 2026-09-25) was the lap *refusing* to finish:
`rederive.mjs` without a publish, so `rebuild_closing_set.py --build` declined and the PR
was "left alone" on every lap. That is loud, and a PR nobody merges is recoverable. This
is the opposite failure: the rebuild SUCCEEDS, the branch looks merged and up to date, and
the tree is wrong. Worse, the sweep is the thing that merges green steward PRs, so a lap
that produces a red tree can hand the next pass a red gate it did not cause — and a run
reading `mergeable_state` alone would see nothing at all.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. The lap's regeneration honours `derived_manifest.json` step order — at minimum,
   `compile_source_use.py` never runs before `compile_scene.py` for the same tree.
2. A test that reproduces this: a branch merged onto a dev whose scene moved, regenerated
   by the lap's own code path, gates `CHECK PASS`. Breaking the order makes it fail — so
   the test proves the gate the way the rest of check.sh does.
3. `owner_chicago_1835_reconstruction_spec_2026` reads 3620 claims after a lap, not 3582.
4. If honouring the whole manifest order inside the lap is too large, the fallback is that
   the lap REFUSES to push a tree it has regenerated but not gated, and says so on the PR —
   a loud stop, which is T-1521's behaviour and is strictly better than a quiet wrong tree.

Found by the run that merged T-1275 (#105): it had to gate the lap's commit, find the red,
and re-derive before it could merge.
