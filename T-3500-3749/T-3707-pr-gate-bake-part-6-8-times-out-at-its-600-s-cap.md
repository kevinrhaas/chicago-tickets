---
id: T-3707
title: PR gate bake part 6/8 times out at its 600 s cap on busy CI runners (rc 124 on #2257 and #2259, 2026-11-20) while it passes in 286 s locally and ~7.5 min on dev's CI: raise N or split the part before more PRs go red on it
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-20
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

PR gate bake part 6/8 times out at its 600 s cap on busy CI runners (rc 124 on #2257 and #2259, 2026-11-20) while it passes in 286 s locally and ~7.5 min on dev's CI: raise N or split the part before more PRs go red on it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (finish-only slice 1/5, 2026-11-20)

- `bake gate part 6/8` runs `timeout --kill-after=5s 600s ./tools/check.sh --part "6/8"`. It ended on exit 124 on #2259 at 391f236 (job 136334166562: started 14:14:27Z, publish done 14:21:09Z, killed 14:26:32Z) and on #2257 (run 44741728254: 13:21:15Z → 13:33:21Z, rc 124). Every other bake part on those runs that finished was green.
- Dev's own part 6/8 on run 44735878349 passed in 7 min 38 s (12:35:51Z → 12:43:29Z), which is already past the ~540 s the check.sh header says should trigger raising N.
- Locally on #2259's head 391f236 (4 cores, nothing beside it): `CHECK_TIMINGS=… ./tools/check.sh --part 6/8` → CHECK PASS, 178 steps, none red, in 286 s. Its heaviest steps: `k01_emit.py --check` 84 s, `check_entrance_kit.py --self-test` 65 s, `fit_portrait_face.py --check` 58 s, `publish.sh` 54 s, `check_conservatory_kit.py --self-test` 49 s, `test_k01_chamfer_return.py` 47 s.
- So the red is runner contention on a part with no headroom, not the diff. The job cannot be re-run while its workflow run is still going (403 "already running"), so each PR that hits it waits on a whole matrix before a re-run, and `pr-automerge` refuses it as red meanwhile.
- Likely fix: raise the CI matrix N for the bake gate (check.sh already partitions any N; the harness proves the partition), or move one of the 50-85 s steps out of part 6. Do not raise the 600 s cap or drop a step.
