---
id: T-2332
title: Mobile smoke part 10 is red on dev: the near-walk flora arrival reading sees 0 arrivals and 0 plant-frames, and z09 sand prairie's butterfly weed is drawn nowhere
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-10
closed: null
pr: 674
claimed_by: run 10/10/2026, 6:43:56 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38095866159
claimed_at: 2026-10-10T23:43:57.116Z
decision: null
decision_answer: null
---

Mobile smoke part 10 is red on dev: the near-walk flora arrival reading sees 0 arrivals and 0 plant-frames, and z09 sand prairie's butterfly weed is drawn nowhere.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's bake smoke (mobile, 10-13) is red on these three checks, so every bake PR into dev fails its smoke leg

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by T-2331's run, 2026-10-10)

- Reproduced on a FULL clone of dev (committed meshes, `publish.sh` mirror),
  `SMOKE_VIEWPORT=mobile SMOKE_STAGE=10 node tools/smoke_renderer.mjs --published`:
  33 passed, 3 failed — so these are NOT the sparse-checkout gap T-2331 repaired.
  1. `no sward species its own list owes a plant to is drawn nowhere` — DRAWN NOWHERE:
     `z09_sand_prairie.forb.asclepias_tuberosa` owed 1.38 at full detail (balanced and
     light: 0 drawn nowhere).
  2. `a plant in front of the walker never arrives already visible` — 0 arrivals over 3.00 m.
  3. `a plant is drawn at its own height, faint, never short` — 0 arrivals, 0 plant-frames.
- Same three in dev's bake runs 38085627738 and 38083892732 (mobile 10-13). mobile part 10
  last PASSED in CI on 2026-10-03 (dev-smoke-state.json), so the cause landed after that.
  A candidate, unproven: T-2059 (#513, 2026-10-08) "the mobile flora heartbeat back under
  250 ms" — the arrival walk calls `a.step()` 20 times and reads nothing drawn at all.
- Desktop part 10 is unread: dev's desktop 10-13 legs were cancelled in both runs.
