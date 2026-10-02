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
blocked_on: null
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
