---
id: T-2148
title: The West Division's remainder after T-2143: 2 ordinary dwellings and one freight roof. Carry Clinton, Jefferson and Des Plaines to Madison as T-2143 carried Canal and West Water, so plat blocks 48-50 (180 ft printed) join the layer
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-05
closed: null
pr: 496
claimed_by: run 10/5/2026, 7:28:57 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37393911440
claimed_at: 2026-10-06T00:28:57.998Z
decision: null
decision_answer: null
---

The West Division's remainder after T-2143: 2 ordinary dwellings and one freight roof. Carry Clinton, Jefferson and Des Plaines to Madison as T-2143 carried Canal and West Water, so plat blocks 48-50 (180 ft printed) join the layer.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 159 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2143 closes with plat block 51's six houses built and the West order-book rows (ordinary_dwellings 2 left, warehouses_freight 1 left, stores and workshops complete) must name a live ticket, or the order book's owner gate goes red the moment T-2143 settles done; no other live ticket raises West roofs

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Handed on by T-2143 (2026-10-05)

T-2143 carried Canal and West Water from local N -400 (the old south edge of the modelled
field) to Madison, the plat's south town line, and `tools/generate_plat_lots.py` now maps
"south town line" to `madison`. That put plat block 51 (`blk_west_washington_canal`) on the
layer, cut on its own two printed depths (180 / 88), and the programme dealt it six roofs.
What is left, read from `1835_reconstruction_order_book.json` at its close:

- `structures/ordinary_dwellings/west` — **2 to build**.
- `structures/warehouses_freight/west` — **1 to build** (a `commercial_front` line).
- `stores_mixed_use/west` and `workshops/west` read complete and are routed here only so the
  rows name a live ticket.

**Where the next ground is.** The same tier's blocks 48, 49 and 50 each print 180 ft under
both columns (`thompson_west_division_lots.json`, documented), and the grid now reaches their
cells — they are omitted only because Des Plaines, Jefferson and Clinton still stop at N -400
("committed centreline stops 107 m short"). Carrying those three to Madison by the rules they
are already drawn on would land 30 lots. Two things to respect: Jefferson and Des Plaines carry
Clinton's bearing AND (Des Plaines) Clinton's reach, which `tools/measure_west_division_streets.py`
asserts, so Clinton moves first and the assertion follows; and a carried line must declare its
carry in `generate_plat_lots.CARRIED_REACHES`, or every block it already bounds is re-cut on a
moved chord (T-2143 measured 8.2 m on block 44 before it added that rule).

**Acceptance:** either (a) the three lines carried and blocks 48-50 on the layer, and the
remaining roofs dealt, generated, baked and seated on them; or (b) the remainder restated in
writing as unbuildable on committed ground, with the rows moved to whichever ticket owns that.
