---
id: T-1672
title: The three south-division freight roofs left after the Dearborn bank filled: the ground for them, or the cell cut so the street-line warehouses and the sheds behind them are owed apart
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
claimed_by: run 9/27/2026, 10:29:57 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36329575867
claimed_at: 2026-09-27T15:29:58.036Z
decision: null
decision_answer: null
---

The three south-division freight roofs left after the Dearborn bank filled: the ground for them, or the cell cut so the street-line warehouses and the sheds behind them are owed apart.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

MEASURED 2026-09-27, in the pull request that closed T-1640. That ticket built
`south_bank_shed_dearborn_e2`, the second shed of the south-bank row below the Dearborn
draw, and it took **the last position the south-bank ground rule admits**:
`tools/measure_south_bank_ground.py` now reads `takes_more` 0, 0, 3, 4 where it read
1, 1, 3, 5, so at the generators' own 0.30 m relief clause the reach is FULL. The three
positions left are at a metre of relief, up on the higher ground north of the riverside
plank walk, and `fits_beside_the_street` is still 0 at every clause — T-0134's refusal of
the frontage the plate draws is untouched and is not the thing to re-open.

The order book's `structures/warehouses_freight/south` row moved onto this ticket in the
same commit: target 11, standing 8, **3 to build**.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

One of the two, chosen deliberately and written down where the next reader will find it:

1. **GROUND.** Name where the three stand, on evidence or at the reconstructed tier with
   its bounds — the south side of South Water Street's own blocks, the west approach, or
   the higher bank north of the walk with a conscious re-budget of the 0.30 m relief
   clause (AGENTS.md § the frame budget names that as one of the two honest routes, and
   it is a number this project chose, not a claim about 1835). Then build them.
2. **CUT THE CELL.** The inventory holds the street-line warehouses and the sheds behind
   them in ONE `warehouses_freight` cell it does not divide, which is why two runs
   disagreed about who owned the row (PR #95's `owning_tickets` tuple against dev's single
   ticket). If the honest answer is that the street line owes some of the three and the
   bank owes none, cut it in `data/reconstruction/1835_building_inventory.json` so the two
   halves are owed apart, and let the order book follow the inventory rather than a tuple.

Either way the row stops reading 3-owed-against-full-ground, which is what it reads today.

Links: T-1640 (the shed that filled the bank), T-1200 (the parent ask), T-1641 (the
district's books), `docs/RESEARCH/south_bank_dearborn_ground.md`, L281, L274.
