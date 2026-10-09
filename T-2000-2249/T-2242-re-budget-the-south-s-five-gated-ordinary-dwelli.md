---
id: T-2242
title: Re-budget the South's five gated ordinary dwellings (D2, D2, D4, D4, D5 on south_plat_beyond_committed_control) by name: the South's district target feeds the order book's household division shares (build_order_book_1835.division_shares), so shedding them moves family households between divisions and the household layer has to be walked to its fixpoint in the same PR
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2239
opened: 2026-10-09
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

Re-budget the South's five gated ordinary dwellings (D2, D2, D4, D4, D5 on south_plat_beyond_committed_control) by name: the South's district target feeds the order book's household division shares (build_order_book_1835.division_shares), so shedding them moves family households between divisions and the household layer has to be walked to its fixpoint in the same PR.

Piece 2 of 2 of **T-2239 — The South's five ordinary dwellings still owed once the wedge's D5 stands: the D2 and D4 the schedule deals blk_south_water_wells, which T-1623 measured has no frontage left (refuse the room in reconcile_665's sizing), and the D2, D4 and D5 on the gated balance beyond committed street control — re-budget the structures/ordinary_dwellings/south row by name**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2239 was split (2026-10-09T09:51:21.466Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 5m ago, run 10/9/2026, 4:45:49 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37913002798) — held by the run that split it
- branch `steward/t2239-south-dwellings-rebudget` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37913002798) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Measured when it was split (2026-10-09, T-2241's run)

- After T-2241 all five owed South dwellings stand on `south_plat_beyond_committed_control`
  (gated, 10 roofs: D2 2, D4 2, D5 1, F3 2, F4 1, H3 2). The F3s and F4 are T-2175's, the H3s T-2196's.
- Shedding them is not a matrix-only edit. The column must sum to `districts.south.target`
  (`generate_inferred_infill.validate_programme`), and `build_order_book_1835.division_shares` reads
  those targets to split the HOUSEHOLD targets: South 365 → 360 moves the South share from 0.5598 to
  0.5564 (West 0.2071 → 0.2087, North 0.2331 → 0.2349). households/family_dwelling/south reads 258 today,
  so about two South family households move to West and North, and `seat_known_1835`'s policy-only deal
  takes its division shape from those buckets. `model_town_1835` also prints the matrix's
  ordinary-dwelling division table. Budget a fixpoint walk of the household layer, or argue in the PR for
  decoupling division_shares from the roof target.
- `roof_total` 668 → 663, `principal_functional` 510 → 505, `family_targets` D2/D4/D5 and the
  `roof_total_note` would all move with it; 663 is inside the 565-765 range.

## Finding, 2026-10-09 (T-2196's run, slice 3/5): the owner declined this kind of cut a day ago

On 2026-10-08 the owner answered T-1957's question about the Market wedge's 8 roofs (including
D2, D4 and D5 dwellings). He chose **(b) build on the wedge's eastern lots and re-deal the rest**
over **(c) "Return them: cut the South's targets by these 8 and re-close the order book"**. Shedding
the South's gated dwellings from `districts.south.target` is that cut in substance, even though
the schedule's district-wide re-apportionment means no gated roof can be traced to the wedge one by
one. T-2196 now asks him the same question for its two gated H3s (`decision: pending`). Option (b)
there is the cut, and the ask names this ticket. **Read his answer on T-2196 before shedding any
roof here.** If he chooses the cut, both tickets can share one household fixpoint walk.
