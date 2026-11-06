---
id: T-3375
title: dev's content-build smoke is red on three 1835 legs: light tier not materially cheaper than full at West prairie (desktop 4981 vs 5445, mobile 4100 vs 4498), a THREE.Object3D.add page error at stage 5, and the boot payload at 39.696 MB over its 39.6 MB budget
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: null
claimed_by: run 11/6/2026, 7:10:33 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/42222136357
claimed_at: 2026-11-06T13:10:34.506Z
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

## Re-read on dev 2ab4f2c3d, 2026-11-06 (slice 1, the run that split this)

Dev's committed tree, published without a bake (`check.sh`'s publish), on the steward runner:

- **Light against full at West prairie, mobile stage 5: still red, and unchanged to the call** — 4100 light
  against 4498 full (`SMOKE_STAGE=5 SMOKE_VIEWPORT=mobile node tools/smoke_renderer.mjs`, 29 passed, 1 failed,
  7 m 34 s). 4100 / 4498 = 0.912 against the 0.9 bar: light needs about 50 fewer driver draws than it has, or
  full about 60 more. The numbers are identical to 2026-11-04's, so nothing that merged since moved either tier
  at this stand. `tools/measure_stand_budget.mjs` now accepts `--stand prairie_west` (the smoke's own pose),
  but a two-tier, one-viewport pass did not finish inside 590 s on this runner — budget that read as its own
  command, `--tiers light` alone.
- **The `THREE.Object3D.add: object not an instance of THREE.Object3D. undefined` page error did NOT reproduce**
  on mobile stage 5 here (zero page errors in the same pass). It was read on the content build's BAKED mirror;
  the unbaked publish does not show it, so the next read is a baked mirror (the content build's own smoke leg,
  or `tools/bake.sh` then stage 5), not this one.
- **Boot payload: 39.978 MB, 1,165 requests** (`measure_boot_payload.mjs --against
  docs/measurements/T-3300-boot-payload-entries.json`), +0.610 MB on T-3300's 39.368: 0.198 MB of two new shared
  kit sheets that the 1816 Fort Dearborn buildings and the Lake House shell carry
  (`data/gltf/sheets/6d1c7abde336b776.ktx2` 0.152 MB, `b12a3da2bbcc3dc2.ktx2` 0.046 MB), 0.189 MB of prebuilt
  layers (frontage +0.133, yards +0.054), 0.175 MB of walk code (37 new modules, most of them the people's and
  the driven transport's), 0.048 MB everything else.
