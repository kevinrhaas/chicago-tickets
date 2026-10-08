---
id: T-2150
title: The West Division's one owed freight roof (F3): seat it on the South Branch bank or at the forks, since the only West block that dealt it (plat block 50) is a module inland
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-05
closed: 2026-10-08
pr: 510
claimed_by: run 10/7/2026, 11:08:03 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-08T06:00:52Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37725699610
claimed_at: 2026-10-08T04:08:03.340Z
decision: null
decision_answer: null
---

The West Division's one owed freight roof (F3): seat it on the South Branch bank or at the forks, since the only West block that dealt it (plat block 50) is a module inland.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 157 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2148 closes with West dwellings at 75 of 75 and the warehouses_freight/west row 1 short; the order book's owner gate needs that row (and the complete stores and workshops rows) to name a live ticket the moment T-2148 settles done, and no other live ticket raises a West roof

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Handed on by T-2148 (2026-10-06)

T-2148 carried Clinton, Jefferson and Des Plaines to Madison, which put plat blocks 48, 49
and 50 on the layer. Block 50 (`blk_washington_clinton`, Clinton to Canal) is cut on the
Original Town's west tier and took the West balance that had stood gated as
`west_division_beyond_committed_control`: thirteen roofs were built there (H2, H3, D5, D4, H1
on Canal and eight yard buildings), and its F3 was DEFERRED, because F3 needs water and block
50 stands a plat module from the South Branch (waterside, T-0316; L203). Blocks 48 and 49 were
dealt nothing. What `1835_reconstruction_order_book.json` reads at T-2148's close:

- `structures/ordinary_dwellings/west` — 75 of 75, complete.
- `structures/warehouses_freight/west` — **1 to build**.
- `stores_mixed_use/west` and `workshops/west` read complete and are routed here only so the
  rows name a live ticket.

**Where it could stand.** The West ground that touches water is West Water Street's river
face (plat blocks 29, 44 and 51, whose West Water lots T-1829, T-2132 and T-2143 left mostly
open) and the forks. T-1773 built the West's other freight roof at Lake and West Water facing
the forks; the same argument on one of those open West Water lots is the obvious first reading.

**Acceptance:** either (a) the F3 dealt onto a West Water lot (or the forks) by an argument
made on its own evidence, generated, baked and seated; or (b) the roof restated in writing as
unbuildable on committed ground, with the row moved to whichever ticket owns that decision.

## Finding, 2026-10-06 (slice 3/5 run 37523361307): this waits on T-2148 landing

Claimed and handed straight back, unbuilt. Everything above is read off T-2148's branch, and
that branch is not on dev: PR #496 was `dirty` at 20:13Z, conflicting with dev on about 200
paths after T-2145 (#503), and a sibling holds its lap lock. On dev today blocks 48-50 are not
on the layer and the West F3 still stands in the gated `west_division_beyond_committed_control`
balance, so an F3 built here now would be dealt against a schedule T-2148 is about to rewrite.
It would also add a second West PR conflicting on the same generated files (order book, kept
ground, yard layers) that #496's lap is already fighting. So `blocked_on: T-2148`, state open,
rank kept. When T-2148 settles done the ticket gate flags that field, and the next run clears
it and builds here.

**Unblocked 2026-10-06 ~22:00Z:** T-2148 merged as #496, so blocks 48-50 are on dev and this ticket is buildable from there.
