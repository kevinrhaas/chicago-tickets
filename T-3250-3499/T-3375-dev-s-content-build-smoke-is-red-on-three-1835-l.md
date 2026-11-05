---
id: T-3375
title: dev's content-build smoke is red on three 1835 legs: light tier not materially cheaper than full at West prairie (desktop 4981 vs 5445, mobile 4100 vs 4498), a THREE.Object3D.add page error at stage 5, and the boot payload at 39.696 MB over its 39.6 MB budget
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
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

dev's content-build smoke is red on three 1835 legs: light tier not materially cheaper than full at West prairie (desktop 4981 vs 5445, mobile 4100 vs 4498), a THREE.Object3D.add page error at stage 5, and the boot payload at 39.696 MB over its 39.6 MB budget.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed while lapping PR #1710, 2026-11-05)

- dev's own content build, run 41814891441 on dev 16dab2f5a (2026-11-04): smoke legs desktop 5 and mobile 5 fail
  "the light tier stays materially cheaper than full at the worst stand" (4981/5445 and 4100/4498 calls, worst stand
  West prairie, east across the sward toward town) and "zero page errors" (`console.error: THREE.Object3D.add: object
  not an instance of THREE.Object3D. undefined`). Desktop 1-2 fails `BOOT PAYLOAD OVER BUDGET: 39.696 MB > 39.600 MB`
  (T-3300 re-argued the budget to 39.6 MB on 2026-11-01, and dev has since grown past it). The same run also failed
  mobile 1-2, mobile 8, mobile 9-12, mobile 14, desktop 8 and desktop 9-12, which were not read here.
- PR #1710's content build (run 41973585471 on 0c96252) reproduced the first two and the boot payload (39.697 MB), with
  identical draw-call numbers. Its diff was a single 1904 house, so these reds are dev's. #1710 merged past them, and its
  PR comment gives the reasoning.
- Every steward PR that bakes now meets the same red on `pr-automerge` and needs either a blind merge with the reasoning
  written down or a `resume`. Until this is green, each bake costs a run that reasoning.
