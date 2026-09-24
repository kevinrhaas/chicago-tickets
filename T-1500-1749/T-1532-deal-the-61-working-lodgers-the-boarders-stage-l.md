---
id: T-1532
title: Deal the 61 working lodgers the boarders stage left open: the book's 30 persons/*/lodging/trade cells, whose machinery lost its owner when T-1173's tree ended at T-1347
state: blocked-tech
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: null
pr: null
claimed_by: run 9/24/2026, 3:43:45 AM CT
blocked_on: THE BEDS ARE NOT THERE, and the wall is one refusal rather than a shortage. data/reconstruction/1835_lodgers_seated.json measures ordinary_night_beds 144, occupied_after_this_stage 133, ordinary_night_beds_still_empty 11 — and all 11 are in the only two houses the boarders stage refuses by name: new_york_house (7 empty) and sauganash_hotel (4 empty), both held under refusal 1, 'NO DIVISION, NO MINT'. Every one of the other 14 built lodging places reads at_its_ordinary_night_figure true. So the bed bound acceptance 4 asks me to state is ZERO in any house this stage may mint into, and a working lodger cannot be minted at all until either those two houses are given a division or T-1209/T-1187 raise the 37 unbuilt boarding houses (315 ordinary beds). Re-labelling one of the 50 lodgers the boarders stage already minted at none_recorded would lower a lodging/none bucket's filled count, which T-1459 refuses by name. THE SAME WALL HOLDS T-1533 AND T-1534: T-1534's own body counts those 11 beds as its own, and they are not available to it either. Unblock when the division refusal is lifted or the boarding houses stand.
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35976447879
claimed_at: 2026-09-24T08:43:45.506Z
decision: null
decision_answer: null
---

Deal the 61 working lodgers the boarders stage left open: the book's 30 persons/*/lodging/trade cells, whose machinery lost its owner when T-1173's tree ended at T-1347.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Cut by T-1500 on 2026-09-24**, which took the modelling decision T-1420's sweep
deliberately did not take. T-1500 gave the bed buckets a placeholder owner; this is one of
the three pieces the remainder actually divides into, and the division is the boarders
stage's own, quoted.

`tools/seat_lodgers_1835.py` refusal 2, written into the stage and into
`data/reconstruction/1835_lodgers_seated.json`:

> NO TRADE IS DEALT. The book's `lodging/trade` buckets want working lodgers and this
> stage does not fill them, because dealing a trade is T-1173's machinery and the 1839
> directory's shares are its table. The lodgers minted here carry `none_recorded` … and
> the `lodging/trade` order stays open for the stage that can price it.

T-1173 split into T-1346 (read the 1839 trade table) and T-1347 (draw the heads), and both
are `done`. So the machinery the refusal defers to exists and the ORDER against it has no
owner — which is the hole T-1500 was filed for, for this third of it.

**The 30 cells, as the book stands on 2026-09-24:** 67 ordered, 6 filled by the boarders
stage, **61 left**. By age band: 10-19 35, 20-29 6, 30-39 9, 40-49 5, 50+ 6. The 10-19
band is the largest of them and is not a surprise — an apprentice boarding at the shop
they work in is a working lodger with no household of their own. There is no `under_10`
trade cell; children carry no trade.

## Acceptance

1. The `lodging/trade` order is priced off the same table T-1346 read and T-1347 drew
   against — not a fresh share and not a flat deal.
2. Nothing already drawn moves (T-1459). The 6 filled stay filled.
3. Every minted person carries `tier`, `basis`, `seed` and `replaceable_by` (T-1158).
4. A lodger has to be seated in a house that stands, on the boarders stage's own bed
   accounting — so state what the bed bound allows before minting, exactly as T-1534 does
   for the adult `none` cells, and mint no more than the beds hold.
5. `build_order_book_1835.py --check`, `converge_resident_layer.py --run` and
   `./tools/check.sh` green.
