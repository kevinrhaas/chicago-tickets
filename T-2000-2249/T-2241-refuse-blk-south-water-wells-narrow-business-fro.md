---
id: T-2241
title: Refuse blk_south_water_wells' narrow business-front lot in reconcile_665's sizing: lot 0 is free only under the clause, and H. Jones's store leaves 7.46 m of face against an 8.128 m party-line unit, so the schedule stops dealing the block a D2, D4 and F4 it cannot build (they join the gated South balance)
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2239
opened: 2026-10-09
closed: null
pr: 566
claimed_by: run 10/9/2026, 4:51:33 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37913002798
claimed_at: 2026-10-09T09:51:33.153Z
decision: null
decision_answer: null
---

Refuse blk_south_water_wells' narrow business-front lot in reconcile_665's sizing: lot 0 is free only under the clause, and H. Jones's store leaves 7.46 m of face against an 8.128 m party-line unit, so the schedule stops dealing the block a D2, D4 and F4 it cannot build (they join the gated South balance).

Piece 1 of 2 of **T-2239 — The South's five ordinary dwellings still owed once the wedge's D5 stands: the D2 and D4 the schedule deals blk_south_water_wells, which T-1623 measured has no frontage left (refuse the room in reconcile_665's sizing), and the D2, D4 and D5 on the gated balance beyond committed street control — re-budget the structures/ordinary_dwellings/south row by name**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2239 was split (2026-10-09T09:51:21.466Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 5m ago, run 10/9/2026, 4:45:49 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37913002798) — held by the run that split it
- branch `steward/t2239-south-dwellings-rebudget` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37913002798) may be working one of the pieces now.

**Acceptance:** `reconcile_665.py` refuses, in its free-lot sizing, any lot freed only by the business-front clause whose widest stretch of face not under a standing footprint is under one party-line unit (24.384 m / 3); `blk_south_water_wells` reads `at_capacity` with lot 0 listed under `narrow_front_lots`, its D2, D4 and F4 move to the gated South balance, `check.sh` is green, and no household seat moves.
