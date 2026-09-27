---
id: T-1673
title: The four warehouses the South Water and Lake street line still owes: the platted-ground half of the south freight cell, raised on the party lines at the crosswalk's required F-family variants
state: blocked-tech
epic: TOWN
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 9/27/2026, 10:57:36 AM CT
blocked_on: T-1672 — the south freight cell is still ONE undivided cell (dev c164f8ae: target 11, standing 8, 3 to build); the platted-ground half this ticket builds on only exists if T-1672 cuts it, and T-1672 is in flight
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36331173426
claimed_at: 2026-09-27T15:57:36.745Z
decision: null
decision_answer: null
---

The four warehouses the South Water and Lake street line still owes: the platted-ground half of the south freight cell, raised on the party lines at the crosswalk's required F-family variants.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

READ 2026-09-27 by the run that took this as slice 2 of 3, which then set it down
again: **this ticket's premise does not exist yet, and the run that is making it is
still in flight.**

`structures/warehouses_freight/south` is ONE cell on dev at `c164f8ae` — target 11,
standing 8, **3** to build, `owning_ticket` T-1672 — and the inventory's
`district_group_matrix` holds it undivided (`{south: 11, west: 2, north: 7, fort: 0}`).
There is no platted-ground half to build the four on. T-1672 is the ticket that decides
whether there is one: its acceptance offers GROUND (find where the last three stand) **or**
CUT THE CELL (divide the street-line warehouses from the bank sheds in
`data/reconstruction/1835_building_inventory.json` so the two halves are owed apart).
This ticket was minted at 15:43:30Z, thirteen minutes after T-1672 was claimed at
15:29:58Z, by that run — so it is T-1672's successor under the second option, and its
**four** is a number only the cut produces. Against the uncut cell the row owes three,
not four, and a run that built four here would either make T-1672's cut for it — a live
sibling's unit — or break the row.

So it waits on T-1672, and the reader who picks it up next should check what T-1672
decided:

* **T-1672 cut the cell** → this ticket is the build half. Take the four from the
  street-line side of the cut, on the platted ground of the South Water and Lake blocks,
  seated on the party lines, at the F-family variants
  `docs/RESEARCH/1835_family_archetype_crosswalk.md` requires (F1 `freight_shed_low`,
  F2 `warehouse_narrow_two_story`, F3 `warehouse_river_large` — F3 still has
  `phase1_instantiated: 0` and nothing baked, so choosing it is a generator commitment,
  not just a pick). `needs_bake` is false on this ticket today and that is wrong the
  moment it raises a roof — set it.
* **T-1672 found ground for the three instead** → there is no half, the row is full at
  11, and this ticket is moot: `withdraw` it rather than inventing a fifth warehouse to
  justify it.

**Acceptance (when T-1672 has answered):** the four stand on the platted-ground half of
the cut cell, each on a party line of its block, each at a crosswalk-required F variant
with its provenance and a source record or an `inferred` note; the order book's
street-line row reads 0 to build; the bake is taken for every roof raised; and the gate
and the `--for-diff` legs are green. It is NOT done by moving a target to meet the
roofs that stand.

Links: T-1672 (the cut, and this ticket's precondition), T-1200 (the parent ask),
T-1640 (the shed that filled the bank), `docs/RESEARCH/1835_family_archetype_crosswalk.md`.

