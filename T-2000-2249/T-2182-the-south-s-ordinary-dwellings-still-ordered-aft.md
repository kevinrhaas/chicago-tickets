---
id: T-2182
title: The South's ordinary dwellings still ordered after T-2176, with no household asking for them: the D4 and D5 the schedule deals blk_south_water_wells, the D6 on blk_south_water_dearborn, and the D4, D5 and D6 on gated blk_south_water_market — build where the ground allows, or re-budget
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The South's ordinary dwellings still ordered after T-2176, with no household asking for them: the D4 and D5 the schedule deals blk_south_water_wells, the D6 on blk_south_water_dearborn, and the D4, D5 and D6 on gated blk_south_water_market — build where the ground allows, or re-budget.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 147 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2176's close strands the order book's structures/ordinary_dwellings/south row (176 ordered, 169 standing, 7 owed) and check.sh's 'closing this branch's tickets strands nobody' gate needs a live owner; T-2176 built every roof a household asked for (no slot request is left on the plat) and the South's last barn, and no open ticket owns the remaining dwellings (T-1957 owns only the boarding houses, T-2175 the warehouses)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Where the ground stands, read 2026-10-09 (slice 4/5, claim released unworked)

A run claimed this, measured it and gave it back without building anything, because the
ground it would build on is being re-dealt under it. Read this before you claim it.

- **The schedule's deal has moved since the title was written.** On dev at 35dae52ea,
  `1835_665_roof_programme.json` deals the South's six owed dwellings as a **D2 and a D4 on
  `blk_south_water_wells`** (with an F3 that T-2175 owns) and a **D2, a D4 and two D5s on
  gated `blk_south_water_market`**. `blk_south_water_dearborn` is now `at_capacity`.
- **Wells cannot take its two.** Its free lots are lot 1 (the Lake-and-Wells corner, the
  block's reserved open lot) and lot 0 (the Wells corner of the South Water face). Lot 0
  reads free only under the business-front clause, because H. Jones's store stands at the
  street on it. T-1623 measured **4.46 m of face left east of that store** (2026-09-26). That
  isn't room for a frontage roof, and the owner answered T-1623 with **(a)**: leave them
  owed, keep the vacant corner lot. So the schedule's `lot_ceiling_principal: 1` /
  `row_lots_required: 1` for Wells promises room that `generate_block_infill.py` will not
  build. Fixing that is a schedule-sizing rule (a business-front lot with less than one
  unit of face left is not free), and it belongs in `reconcile_665.py`.
- **Market is being re-cut by T-2195 (#551, open and being lapped when this was written).**
  Its PR body says the wedge opens with four roofs of room: a **D5, a D6, an F4 and one
  ancillary**. hh_dickson_david's D5 and hh_dird_john_david's D6 slots move onto the
  wedge's lot 7, and "the rest go back to the South balance". After it lands, households
  DO ask for two Market dwellings. The South balance then has to be dealt again
  somewhere, or shed.
- **#551 rewrites `tools/reconcile_665.py` and `tools/build_order_book_1835.py`.** Any build
  or sizing change made here before it merges would be dealt against a schedule that is
  about to change, and would conflict with it on both files.

**So this ticket waits on T-2195.** Once #551 is on dev:

1. Re-read the schedule's South remainder.
2. Build the wedge's D5 and D6 against the two slots that ask for them (`generate_block_infill.py`,
   a `dealt_against_a_request` entry, `bake.sh --only`, seating to its fixpoint).
3. For whatever South dwellings are still dealt to ground that cannot hold them (Wells
   above), make the sizing rule refuse the room, and let the book's
   `structures/ordinary_dwellings/south` target shed the remainder by name, stating it as a
   re-budget.

If that is more than one run's demonstration, `split` it along those lines.

