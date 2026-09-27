---
id: T-1665
title: C3's crosswalk asks for 2-3 shop bays and the archetype's 5 ft bay module cannot give 3 on any footprint in C3's own band: 1 bay is built on 7 of 7, 2 fit on 4 of 7, and SHOPFRONT_MAX_FRACTION refuses even the first
state: done
epic: TOWN
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: 2026-09-27
pr: 111
claimed_by: run 9/27/2026, 1:54:23 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-27T08:04:15Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36301294944
claimed_at: 2026-09-27T06:54:23.695Z
decision: null
decision_answer: null
---

C3's crosswalk asks for 2-3 shop bays and the archetype's 5 ft bay module cannot give 3 on any footprint in C3's own band: 1 bay is built on 7 of 7, 2 fit on 4 of 7, and SHOPFRONT_MAX_FRACTION refuses even the first.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured 2026-09-27, under T-1659**, on the seven committed C3 records and the archetype's
own set-out (`tools/test_store_variants.py` covers the other three variants of that ticket;
this one it could not close):

    bay 1.524 m (5 ft), door 1.016 m, piers 0.6 m each end
      1 bay : opening 3.251 m, needs 4.451 m of frontage
      2 bays: opening 4.877 m, needs 6.077 m
      3 bays: opening 6.502 m, needs 7.702 m

    record                                      front   built  fits   within 45%
    recon_1835_blk_south_water_dearborn_c3_01    6.24 m    1    1,2      none
    recon_1835_blk_south_water_dearborn_c3_02    5.74 m    1    1        none
    recon_1835_blk_south_water_lasalle_c3_12     6.08 m    1    1,2      none
    recon_1835_blk_south_water_lasalle_c3_13     5.78 m    1    1        none
    recon_1835_blk_south_water_wells_c3_02       6.45 m    1    1,2      none
    recon_1835_south_c3_015                      6.41 m    1    1,2      none
    recon_1835_south_c3_040                      5.86 m    1    1        none

C3's own footprint band is 18x36-22x50 ft, so its FRONT is 5.49-6.71 m — and its roof line is
"front or side gable", which this town builds as a front gable, so the front is the NARROW end.
Three consequences, none of them a missing number:

1. **Three bays are impossible on every plan in C3's band.** 7.702 m of frontage is needed and
   the band's widest front is 6.71 m. No C3 can ever carry the top of its own range.
2. **`SHOPFRONT_MAX_FRACTION` (0.45) refuses even the FIRST bay** on all seven, so
   `default_shopfront_bays` reaches its `return 1` floor every time. That fraction was argued
   for a store filling a 55 ft lot frontage with its EAVES to the street — "a front that is
   nearly all opening is a plate-glass idea from fifty years later" — and a gable-front store's
   front is its narrow end, where the same rule caps the opening at about 2.8 m.
3. So the archetype and the specification disagree, and the disagreement is about **what a
   "bay" is**: the archetype's is a 5 ft show window BESIDE a door, and on an 18-22 ft front
   "2-3 bays" only closes if a bay is a structural bay INCLUDING the door, or if the show window
   is narrower than 5 ft.

**What this ticket has to settle first**, before any geometry moves: which reading of the
crosswalk's `variants` bay count is meant. Nothing should be built on a guess about it — raising
the fraction would put 73-81% of a narrow front into glass, and narrowing the bay module moves
every shopfront in the town, C1 and W4 included.
