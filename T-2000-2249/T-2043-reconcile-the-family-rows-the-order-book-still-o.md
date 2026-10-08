---
id: T-2043
title: Reconcile the family rows the order book still orders after T-2021's ruling: 464 family and store households and 208 adult men in family houses, against the 1,293 head records awaiting a household and a town at its 3,265 ceiling
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: null
claimed_by: run 10/8/2026, 1:38:30 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37825101507
claimed_at: 2026-10-08T18:38:30.337Z
decision: null
decision_answer: null
---

Reconcile the family rows the order book still orders after T-2021's ruling: 464 family and store households and 208 adult men in family houses, against the 1,293 head records awaiting a household and a town at its 3,265 ceiling.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 205 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2021's close leaves the order book's family_dwelling, store_residence and adult-male family rows owing work under a done ticket, which every_work_order_names_a_live_ticket refuses; no open ticket owns households awaiting a household

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding, 2026-10-08 (T-2155, PR #508): the town holds more people present on 1 July than the census figure counts

T-2155 made `town_census.py` read the completion audit's two joins and reconcile with it. The census population is the residents INDEX plus the presence rulings: **2,926** (2,437 housed + 489 waiting on a roof). The audit also reads five resident folders the index does not carry, and every one of their present people is housed: reconstructed_trades 308, lodgers 155, readmitted 111, underdocumented 86, institutional 1 — **661**. So the audit reads **3,587 present on 1 July**, past the November census's 3,265 four months later. `data/town_census.json` now states the 661 under `beyond_the_index` and does not sum them into the population. Whether the staffing/lodger mints over-ordered or the index is short is this ticket's reconciliation; the census screen states the gap and leaves the question here.
