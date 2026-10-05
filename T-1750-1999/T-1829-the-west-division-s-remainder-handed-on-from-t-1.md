---
id: T-1829
title: The West Division's remainder handed on from T-1208: the 16 ordinary dwellings the programme still orders, blk_west_lake_canal's three dealt frame cottages first, built and baked with their households seated
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: T-1208
opened: 2026-10-01
closed: 2026-10-05
pr: 463
claimed_by: run 10/5/2026, 12:58:10 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-05T07:50:05Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37269845291
claimed_at: 2026-10-05T05:58:10.433Z
decision: null
decision_answer: null
---

The West Division's remainder handed on from T-1208: the 16 ordinary dwellings the programme still orders, blk_west_lake_canal's three dealt frame cottages first, built and baked with their households seated.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 147 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1826 closes Wolf Point's books and its acceptance hands T-1208 on with the West's exact remainder: 16 ordinary dwellings still to build. Every ticket in T-1208's chain is split or done (T-1209, T-1784, T-1785 split; T-1781..T-1783, T-1794 done), so no live ticket builds West roofs, and T-1215 is the town's closing report, not a place for a 16-roof bake to hide.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The West's exact remainder as T-1826 read it on 2026-10-01, from
`data/reconstruction/1835_reconstruction_order_book.json`: `structures/ordinary_dwellings/west`
75 target, 59 standing, **16 to build**; `stores_mixed_use/west` 6 of 6, `workshops/west` 8 of 8
(0 left, owned here so the rows name a live ticket). Build first `blk_west_lake_canal`'s three
dealt frame cottages (T-1773's warehouse holds lot 1, so `reconcile_665.py` reads the block at
3 standing / 3 room; the households the platted deal seats as slots on them are in
`1835_platted_seats.json`), then as many of the other 13 as the West's committed ground and
`measure_detail_ceilings.mjs` allow, baked, households seated, and the rest stated with the ground
each waits on. `warehouses_freight/west` moved to T-1827 (046's H2 verdict moves that row).

## Finding from T-1827 (2026-10-01): the West freight row is yours too

T-1827 (PR #247) carried out `recon_1835_west_046`'s H2 verdict: the F1 freight shed on Des
Plaines is now an H2 merchant's house, so `structures/warehouses_freight/west` reads **1 of 2**
and orders one freight roof. #244 had pointed that row at T-1827; it closes with #247, so the row
moves to T-1829 beside the stores and workshops rows you already hold. A freight roof belongs on
a street line (`commercial_front`): the forks or the Canal approach, not the outer prairie.
