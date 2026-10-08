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
decision: answered
decision_answer: b
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

## Finding, 2026-10-08 (T-2165's run): T-2144 has landed and the three owed houses are all in flight

The schedule now places the South's three owed boarding houses on School Section ground: H3 on `blk_school_section_tier_81` (T-2147, PR #493) and H1 on `blk_school_section_tier_94` + H3 on `blk_school_section_tier_95` (T-2146, PR #498). Both PRs are open on `resume`. When they merge, the order book's South `larger_boarding_houses` cell should read 28/28 and this ticket closes on their work — there is nothing left for a run to build here meanwhile.

## Finding, 2026-10-08 (slice 4/5 refill, read on dev @ 3f326a60d): the two still owed are back on gated ground

PR #498 (T-2146) closed unmerged and was continued as #511, which merged; T-2147 (#493) merged. Neither raised its block's H3: both deals left the lot open for this ticket and said why (`1835_platted_block_parcels.json`, blk_school_section_tier_95 and _81) — raising a boarding house moves the lodging model, and `seat_lodgers_1835.py` then draws eight lodgers out of `persons/male/10_19/south/lodging/trade` where the order book holds seven, which that stage refuses until the lodger basis is deliberately re-frozen.

Since then the seating walked to its fixpoint and the schedule re-dealt both open lots to dwellings (block 81 lot 1 a D4, block 95 lot 1 a D5 — T-2176's work, in flight). The order book's South `larger_boarding_houses` cell reads **28 ordered, 26 standing, 2 owed to T-1957**, and the 668-roof schedule now holds those two H3s on **`blk_south_water_market`, state `gated`** — the Market wedge (`refused_control.market_south_water`) the 2026-08-29 closure ruling could not cut. No open ticket carries that question (T-2175 and T-2182 also have roofs waiting on the same block). So nothing here is buildable today. Whoever takes this next: either take the wedge to the owner (`ticket.mjs ask`), or re-budget the two through the order book, and take the lodger re-freeze question before raising any H3 anywhere.

## Decision needed

**Question:** The 668-roof schedule still deals 8 roofs (D2, D4, D5, D6, F3, F4 and these two H3 boarding houses) onto blk_south_water_market, the Market-and-South-Water wedge your 2026-08-29 closure ruling could not cut: the ground leaves 2.8 m of block depth at Market against a 24.4 m lot, so the block stays 'gated' and T-1957, T-2175 and T-2182 all wait on it. What should happen to those 8 roofs?

- (a) Re-deal them onto the School Section's Madison–Monroe tier, extending your 2026-10-05 ruling on T-1755 (b) from the 40 dwellings to the wedge's 8 roofs
- (b) Build on the wedge's eastern two-thirds only: cut reconstructed lots where the block has depth (about 5 of its 8 lots) and re-deal the rest, recorded in LIBERTIES
- (c) Return them: cut the South's targets by these 8 and re-close the order book (folds into T-1983)

**Recommendation:** (b) Build on the wedge's eastern two-thirds only: cut reconstructed lots where the block has depth (about 5 of its 8 lots) and re-deal the rest, recorded in LIBERTIES — (b) keeps the roofs inside the Original Town where 1835's houses clustered, on ground the plat really drew; only the wedge's west third is pinched out by the South Branch. (a) is the precedent you already set and is the safe fallback for whatever the wedge's east end cannot hold. Whichever you pick, the two boarding houses here also need the lodger basis re-frozen before they are raised (seat_lodgers_1835 refuses a new house's lodgers today), which the run that builds them will take first.

**Asked:** 2026-10-08 by https://github.com/kevinrhaas/polecat-platform/actions/runs/37827267592. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

**Owner answer (2026-10-08, via Manager):** (b) Build on the wedge's eastern two-thirds only: cut reconstructed lots where the block has depth (about 5 of its 8 lots) and re-deal the rest, recorded in LIBERTIES
