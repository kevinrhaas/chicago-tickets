---
id: T-2143
title: The West Division's remainder after T-2132: 8 ordinary dwellings and one freight roof, with every lot-ruled West block at capacity and 18 unruled blocks gated on a lot line
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-05
closed: null
pr: null
claimed_by: run 10/5/2026, 2:49:06 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37365476085
claimed_at: 2026-10-05T19:49:06.925Z
decision: null
decision_answer: null
---

The West Division's remainder after T-2132: 8 ordinary dwellings and one freight roof, with every lot-ruled West block at capacity and 18 unruled blocks gated on a lot line.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 158 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2132 closes with plat block 44's four houses built and the West order-book rows (ordinary_dwellings 8 left, warehouses_freight 1 left, stores and workshops complete) must name a live ticket, or the order book's owner gate goes red the moment T-2132 settles done; no other live ticket raises West roofs

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Handed on by T-2132 (2026-10-05)

T-2132 opened plat block 44 (`blk_west_randolph_canal`, Randolph → Washington between Canal and
West Water). It had been gated with the blocks that print no dimension, but it prints two —
180 ft under its west column and 150 ft under its east — and `tools/generate_plat_lots.py` now
cuts such a block on its own two depths (`lot_depth_ft_per_column`), never averaged. The
programme then dealt it four roofs (D5, D4, D5 on Canal; D6 on West Water) beside the Western
Hotel and its stable, which were generated, baked and seated at the keeper/seating fixpoint
(182 seated). What is left, read from `1835_reconstruction_order_book.json` at its close:

- `structures/ordinary_dwellings/west` — 75 target, 67 standing, **8 to build**.
- `structures/warehouses_freight/west` — **1 to build** (a `commercial_front` line: the forks or
  the Canal approach).
- `stores_mixed_use/west` and `workshops/west` read complete and are routed here only so the rows
  name a live ticket.

**Where the next ground could come from.** Plat block 51 (Washington → south town line, Canal to
West Water) prints the same two-depth reading (180 and 88) and the cut would take it the same
way, but the committed grid does not build that block at all today, so it is not on the layer.
The other gated West cells print no dimension of their own; a tier-mate's figure is still
refused (`what_this_refutes`).

**Acceptance:** either (a) a West block gains dealable ground — a lot line read for one of the
gated blocks, or block 51 brought onto the layer, argued on its own evidence — and the next roofs
are dealt, generated, baked and seated on it; or (b) the remainder is restated in writing as
unbuildable on committed ground, with the district balance re-apportioned or carried, and the
order-book rows moved to whichever ticket owns that decision.
