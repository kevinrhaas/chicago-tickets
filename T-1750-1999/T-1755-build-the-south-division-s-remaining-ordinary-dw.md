---
id: T-1755
title: Build the South Division's remaining ordinary dwellings: the roofs the district still owes after the plat's last tier and the outer books closed, on the blocks the street carry emitted
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-29
closed: null
pr: null
claimed_by: run 10/5/2026, 1:53:01 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37358954436
claimed_at: 2026-10-05T18:53:01.914Z
decision: answered
decision_answer: b
---

Build the South Division's remaining ordinary dwellings: the roofs the district still owes after the plat's last tier and the outer books closed, on the blocks the street carry emitted.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Read by a run, 2026-10-05: there is no committed ground left for these 40

Slice 2 of 5 claimed this ticket to build it. It found nothing to build on, released the claim, and asked the question below. Every figure is from `data/reconstruction/1835_665_roof_programme.json` and `data/reconstruction/1835_platted_seats.json` on dev at 76e5674b.

- **The street carry's blocks are full.** T-1707 emitted the plat's last tier and T-2130 (#466) built its Dearborn and Clark blocks to their lot ceilings. All six `blk_washington_*` blocks now read `at_capacity`, with 1 free lot each (the lot every block keeps open) and 0 headroom.
- **The two South blocks with headroom refuse it.** `blk_south_water_wells` and `blk_south_water_dearborn` each have 4 roofs of headroom (8 in all). Each has only one free lot left (`#01` and `#07`), and that is the lot `block_rooms` keeps open. `plan_left_unclaimed` therefore refuses every dwelling family there (T-1623) and the households stay owed.
- **The remaining 46 roofs are on no ground at all.** `blk_south_water_market` (22 roofs) is the wedge the owner's 2026-08-29 closure ruling could not cut, and it is back with him. `south_plat_beyond_committed_control` (24) is a balance, not a block. Its `waiting_on` still says the south columns "end at local N -519 … the OLD south edge of the field". That is now Madison itself (-525), so street control carries the plat to its south line. There is no plat south of that line.
- **No ground outside the plat may raise a slot.** `1835_off_plat_ledger.json` holds the School Section's Madison–Monroe tier (T-1477): 80 lots, sold lot by lot in October 1833, cut and dry on the modelled field. The 665-roof schedule carries no row for that ground, so `may_raise_a_slot` is false on every one of its parcels. T-1713's close-out (`data/render/south_outer_close_out.json`) reached the same nil balance for the reservation, the Addition and the country seats.

So the ticket's own premise ("on the blocks the street carry emitted") is spent. The 40 dwellings can only stand if somebody decides where the South's houses may go beyond the Original Town's lot grid. That is a choice about the town's shape, so it is asked below rather than taken.

## Decision needed

**Question:** The South still owes 40 ordinary dwellings, but every Original Town block the street carry emitted is at its lot ceiling, and the plat has no ground south of Madison. Where may they stand?

- (a) Densify inside the plat: rear dwellings behind houses already standing on occupied South lots, extending your 2026-09-23 rear-cottage ruling past the 154:508 yard-building ratio
- (b) Cross Madison: build them on the School Section's Madison–Monroe tier (80 lots sold in October 1833, cut by T-1477), so the town spills over its south line
- (c) Return them: the plat cannot hold the South's dwelling target, so cut the target by 40 and re-close the order book (folds into T-1983)

**Recommendation:** (a) Densify inside the plat: rear dwellings behind houses already standing on occupied South lots, extending your 2026-09-23 rear-cottage ruling past the 154:508 yard-building ratio — 1835 houses clustered inside the Original Town and few stood south of Madison, so (b) would move about a quarter of the South's houses onto ground that was mostly empty. (a) keeps the town's shape and matches your 2026-08-18 ruling ('more and denser buildings'). It builds at the reconstructed tier and is recorded in LIBERTIES.

**Asked:** 2026-10-05 by https://github.com/kevinrhaas/polecat-platform/actions/runs/37343630267. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

**Owner answer (2026-10-05, via Manager):** (b) Cross Madison: build them on the School Section's Madison–Monroe tier (80 lots sold in October 1833, cut by T-1477), so the town spills over its south line
