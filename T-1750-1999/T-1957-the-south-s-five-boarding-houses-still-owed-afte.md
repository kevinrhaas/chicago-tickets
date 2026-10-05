---
id: T-1957
title: The South's five boarding houses still owed after T-1951: the schedule's re-apportioned H3 on blk_washington_market, the gated one on blk_south_water_market, and the three the plan holds no roof for
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: null
pr: null
claimed_by: null
blocked_on: T-2144
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The South's five boarding houses still owed after T-1951: the schedule's re-apportioned H3 on blk_washington_market, the gated one on blk_south_water_market, and the three the plan holds no roof for.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 247 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1951 closes on its three houses and the order book's South larger_boarding_houses cell (28 ordered, 23 standing) must name a live ticket or dev's order-book step goes red when T-1951 settles

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What T-1951 measured (2026-10-02, PR #266)

- After T-1951's three houses (`recon_1835_blk_washington_market_h3_01`/`_h3_04`, `recon_1835_blk_washington_dearborn_h3_01`), the order book's South `larger_boarding_houses` cell reads **28 ordered, 23 standing, 5 owed**. The 665-roof schedule re-apportions them: **1 H3 on `blk_washington_market`** (open, free lots 0/2/3/6/7, lot 1 kept open), **1 on `blk_south_water_market`** (gated), and **3 the plan holds no roof for**.
- **Two placement traps, both measured.** (1) A yard building behind a house on the Washington-and-Market corner is refused by `ancillary_behind_its_own_roof` (Market Street is `principal`). (2) A new H3 on ANY Washington-tier corner ties the Clark block's corner houses in `seat_platted_ground_1835.deal`'s `score` (corner is the only `prefers` term these lots answer) and wins on `max(lot_id)`, pulling `hh_beaubien_mark` / `hh_sweet_alanson` off the houses raised for them. Mid-block lots avoid both.
- **The South's adult `lodging/none` orders are spent**: T-1951's houses sleep 4/10, 6/12 and 8/12 under "no order left, no mint". A further house will stand mostly empty unless the book's lodging orders move; say so, or take that question first.

## Finding, 2026-10-05 (slice 3/5 run 37360845139): nothing owed here stands on buildable ground today

Read on dev @ c0d973c3. The South `larger_boarding_houses` cell now reads **28 ordered, 25 standing, 3 owed** (two of the five were built after T-1951). The 668-roof schedule (`1835_665_roof_programme.json`) holds those three as H-family roofs, and **all three are on gated ground**:

- **H1 + H2 on `blk_south_water_market`**, state `gated`. That is the wedge the owner's 2026-08-29 closure ruling could not cut (`refused_control.market_south_water`, 2.8 m of depth at Market). T-1755's body says it is "back with him". No open ticket carries that question, so a run cannot build these two.
- **H3 on `south_plat_beyond_committed_control`**, a `district_balance` entry with no block. T-2144, which is in flight, turns the School Section's dry tier south of Madison into platted blocks in the roof schedule (owner ruling T-1755 (b)). Once it lands, the schedule should re-apportion this H3 onto one of those blocks, and the house becomes buildable.

The re-apportioned H3 on `blk_washington_market` that this title names **no longer exists**: the schedule gives that block nothing now.

So this ticket waits on **T-2144**, and it keeps its queue rank. When T-2144 merges, re-read the schedule: build whatever H-family roof it places on School Section ground, and take the wedge's two either to the owner or to T-1983's re-budget.
