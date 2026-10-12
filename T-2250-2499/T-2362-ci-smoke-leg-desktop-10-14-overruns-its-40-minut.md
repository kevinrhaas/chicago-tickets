---
id: T-2362
title: CI smoke leg desktop 10-14 overruns its 40-minute timeout on every run since T-2337 split part 10 into 10+11: five parts at ~8 min each, cancelled at 40m on dev (run 38138197680) and on #696 (run 38140175452); re-tile the bake workflow's desktop legs so each fits its cap, and let merge-ready see a PR go clean again
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-11
closed: 2026-10-11
pr: 710
claimed_by: run 10/11/2026, 6:08:21 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-12T01:01:14Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38182891652
claimed_at: 2026-10-11T23:08:21.282Z
decision: null
decision_answer: null
---

CI smoke leg desktop 10-14 overruns its 40-minute timeout on every run since T-2337 split part 10 into 10+11: five parts at ~8 min each, cancelled at 40m on dev (run 38138197680) and on #696 (run 38140175452); re-tile the bake workflow's desktop legs so each fits its cap, and let merge-ready see a PR go clean again.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> no PR can reach 'clean' while this leg is always cancelled, so merge-ready never merges and every run must merge by hand past a cancelled check

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (loop, 2026-10-11, lapping #693): desktop 3-6 hits the same cap

Desktop 10-14 is not the only leg. `smoke (desktop, 3-6)` also ended at **"The job has exceeded the maximum execution time of 40m0s"** (conclusion `cancelled`), on four branches in one afternoon:
- #693 at `bf7e6b14e` (run 38151202325, 16:01→16:42Z), and again at `a10aba342` (17:03→17:43Z). At `a10aba342`, desktop 10-14 was cancelled as well.
- #701 (run 38151542795), #696 (run 38145860632), and T-2351's branch (run 38144928088).
- The same leg passed in 24–38 min on #698 and #699, so it sits right at the cap and tips over whenever runners are contended.

The parts themselves are fast on a quiet machine: locally (4 cpu, `--published`), desktop parts 3/4/5/6 took 3m04/3m05/3m06/5m37 on `a10aba342`, all green with zero page errors. That points at runner contention on the leg rather than slow parts. Re-tiling has to cover 3-6 as well as 10-14 (or the cap has to rise), or merge-ready still never sees `clean`.
