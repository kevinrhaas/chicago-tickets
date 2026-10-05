---
id: T-2132
title: The West Division's remainder after T-1829: 12 ordinary dwellings and one freight roof the programme still orders, with every lot-ruled West block at capacity and 19 unruled blocks gated on a lot line
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
claimed_by: run 10/5/2026, 1:09:37 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37353341843
claimed_at: 2026-10-05T18:09:37.651Z
decision: null
decision_answer: null
---

The West Division's remainder after T-1829: 12 ordinary dwellings and one freight roof the programme still orders, with every lot-ruled West block at capacity and 19 unruled blocks gated on a lot line.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 181 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1829 closes with blk_west_lake_canal's three cottages built and the West order-book rows (ordinary_dwellings 12 left, warehouses_freight 1 left, stores and workshops complete) must name a live ticket, or the order book's owner gate goes red the moment T-1829 settles done; no other live ticket raises West roofs

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Handed on by T-1829 (2026-10-05)

T-1829 built `blk_west_lake_canal`'s three dealt roofs (a D5 and a D4 on Canal Street at plat
lots 6 and 7, a D2 shanty on West Water at plat lot 8), baked, with the seating walked to its
fixpoint: 178 platted seats held, the block's three slot requests seated. What it leaves, read
from `data/reconstruction/1835_reconstruction_order_book.json` and
`1835_665_roof_programme.json` at its close:

- `structures/ordinary_dwellings/west` — 75 target, 63 standing, **12 to build**.
- `structures/warehouses_freight/west` — **1 to build** (T-1827's H2 verdict on west_046); a
  freight roof belongs on a `commercial_front` street line, the forks or the Canal approach.
- `stores_mixed_use/west` and `workshops/west` read complete and are routed here only so the
  rows name a live ticket.

**Why T-1829 could not build them:** every lot-ruled West Division block in the programme is
`at_capacity` at the West density (6 roofs per 10 lots, T-1783), and the other 19 West blocks
are `platted_block_unscheduled` / `gated`, waiting on a lot line the sheet does not print
(T-1414; "a re-read of the scan is owed and no live ticket owns it").

**Acceptance:** either (a) a West block gains dealable ground — a lot line read for one of the
19 gated blocks, argued on its own evidence — and the next roofs are dealt, generated, baked and
seated on it; or (b) the remainder is restated in writing as unbuildable on committed ground,
with the district balance re-apportioned or carried, and the order-book rows moved to whichever
ticket owns that decision.
