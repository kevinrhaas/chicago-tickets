---
id: T-1774
title: Wolf Point's books closed once T-1760, T-1761, T-1766, T-1208 and T-1209 land: the pre-plat West roofs reconciled, the refusals resolved, the frame budget read, T-1208 handed on
state: split
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1764
opened: 2026-09-30
closed: 2026-10-01
pr: null
claimed_by: run 10/1/2026, 4:07:06 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-01T21:10:04.755Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36924321574
claimed_at: 2026-10-01T21:07:06.447Z
decision: null
decision_answer: null
---

Wolf Point's books closed once T-1760, T-1761, T-1766, T-1208 and T-1209 land: the pre-plat West roofs reconciled, the refusals resolved, the frame budget read, T-1208 handed on.

Piece 2 of 2 of **T-1764 — The cabins and boarding houses of the forks, and Wolf Point's books closed: the pre-plat West roofs reconciled, the refusals resolved, the frame budget read, T-1208 handed on**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The parent's closing clauses, sequenced behind the West builds that move the numbers it
reconciles (T-1760, T-1761, T-1766, T-1208, T-1209 — and T-1773, the freight roof):
the 55 `phase2_west_wolf_point_approaches` roofs adopted/redealt and the recipe's stale
`status: research_recipe_not_instantiated` restated; `recon_1835_west_020` (a C2
storefront standing `roofs_offered_and_unspent`) occupied or its use stated; the frame
budget read on the published tree (`measure_detail_ceilings.mjs`); a screenshot from the
Wolf Point tavern door; T-1208 handed on with the West's exact remainder.

## Finding from T-1782 (2026-10-01): recon_1835_west_046's H2 verdict moves the lodger layer

T-1782 carried 046's outstanding T-1445 verdict out alone (`execute_roof_redeal.py --apply --only
recon_1835_west_046`, the `--only` flag that run added: F1 24×44 → H2 24×36 ft, baked). The
platted deal then seated `hh_adams_james` on it (`blk_west_randolph_des_plaines#01`,
merchant_and_professional_dwellings). The run had to back it out, because 046 enters the lodging
model's H2 `boarding_house` class and re-splits that class's beds by floor area:
`seat_lodgers_1835.py --build` then re-dealt the boarders ALREADY STANDING in nine houses
(north_h1_007, north_h2_022/028/030/045, west_006, west_035, steamboat_hotel, kelsey) — west_035's
six seated names all changed. Two defects surfaced on the way:
(a) the reconstructed-house keeper is `pick()`ed off the frozen room with no ceiling test, so a house
new to the deal can mint its keeper into a closed cell (`refuse()` then fails: "drew 2 out of
persons/male/10_19/west/lodging/trade and the book now orders only 1"); a re-pick-only-when-closed
patch (closed in the frozen ceiling OR the live book) fixed that without moving any standing keeper;
(b) after that, `build_order_book_1835.py` faulted: "the re-family ledger lands 6 head(s) in
persons/male/under_10/west/lodging/none, which orders 9 and already holds 5".
So carrying 046 out needs either the lodging model to leave a deal-seated merchant H2 out of the
boarding-house class, or the lodger re-deal argued and accepted. 047's stated use (T-1782) names the
freight shed and must be restated when 046 changes.

**Addendum, same day (a concurrent lap on #211, finished after #211 had merged narrowed):** the
accepted-re-deal route was carried all the way to green, and is kept for whoever takes this as
branch `salvage/046-h2-lodgers-open-ceiling` (48ea0dfb, merged with dev@b18a0346, pre-#211 — a
reference, not a mergeable branch). Beyond (a), it fixes (b) in `seat_lodgers_1835.py`: a house new
to the deal has its keeper's children drawn after every committed house and under the same
ceiling (frozen open-order AND the live book less the boarders), so 046's four wanted children are
refused rather than overrunning the re-family arrivals. With dev's lodging model and ledger the
patched stage reproduces dev's cards exactly. The rest of the cascade it needed: transients;
`reconstruct_businesses_1835.py --group lodging_river_and_transport` (*Donnelly's boarding house*,
an 8th L257 firm); staffing join, reconstructed seating, mint order, re-family rule and report,
employment coverage; L252 (94 in 17 → 103 in 18), L254/L257–L260/L262 (33 → 34 houses of trade),
the dossier's closing-table lodgers row, and `build_order_book_1835.py`'s self-test pin on
`seated` (249 → 250). That tree read `check.sh` CHECK PASS 712/712 and smoke part 1 80/80 on
desktop and 390×780.

## Finding from T-1783 (2026-10-01): the order book's two West rows now point here

T-1783 (#215) opened the outer platted West blocks at a West lot density and built the four roofs
on `blk_west_randolph_des_plaines`. Its merge with dev after T-1794 (#216) and T-1773 (#217) left
two rows of `build_order_book_1835.py`'s owner table on done tickets, which the gate refuses:
`structures/ordinary_dwellings/west` (19 left, was T-1794) and `structures/warehouses_freight/west`
(2 of 2, was T-1773). With T-1781..T-1784 all closed, this ticket is the one whose acceptance hands
T-1208 on "with the West's exact remainder", so both rows now name T-1774. The queue was over its
ceiling, so this is a finding here, not a new line. The remainder this ticket hands on includes
`blk_west_lake_canal`'s dealt cottages. T-1773's warehouse now stands on plat lot 1 there, so
`reconcile_665.py` reads that block at 3 standing / 3 room (6 per 10 lots): **three** cottages, not
the four T-1783's first reading named. The households the platted deal seats as slots on them are
in `1835_platted_seats.json`. Hand the cottages and the district balance on as their own build
(needs_bake) when this closes; do not build them here.
