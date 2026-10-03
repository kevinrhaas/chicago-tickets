---
id: T-1532
title: Deal the 61 working lodgers the boarders stage left open: the book's 30 persons/*/lodging/trade cells, whose machinery lost its owner when T-1173's tree ended at T-1347
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: null
pr: null
claimed_by: run 10/3/2026, 4:46:48 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37114015896
claimed_at: 2026-10-03T09:46:48.266Z
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


## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into this ticket:** T-1566. T-1566 said itself it must ride along with the lodging parcel rather than open a PR of its own; dealing the working lodgers is that parcel.

### Folded in from T-1566 — The staffing mint's payment never prices the DIVISION axis: a north lodging slot pays for a hand in a south shop, and for 19 of the 26 the register places no premises at all

The staffing mint's payment never prices the DIVISION axis: a north lodging slot pays for a hand in a south shop, and for 19 of the 26 the register places no premises at all.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## STEPPED OVER, 2026-09-25 — claimed, read, and released unworked

A run claimed this, read `tools/staffing_mint_order_1835.py` and the order it writes,
and RELEASED it without working it. The reason is AGENTS.md § THE VISIBLE-PROGRESS
RULE, and it is worth writing here so the next run does not spend the same calls
finding it out:

* **This ticket is invisible and carries none of the three exemptions.** Pricing the
  division axis rewrites one derived report, `data/reconstruction/1835_staffing_mint_order.json`,
  which nothing renders — `grep` for it finds `check.sh`, the writer inventory and the
  tool itself, and no renderer. It is not owner-reported (`requested_by: loop`), it is
  not the fix half of a measurement split, and it does not unblock a visible parcel:
  `the_owner_s_ruling.mintable_today` is **0**, held there by the BED bound and the
  `family/trade` household bound, neither of which the division axis touches. Pricing
  the axis correctly still mints nobody.
* **The cap was already breached when it was read.** v1107 and v1106 are both
  "Nothing you can see changed"; the cap is one invisible run in four.

**So it is not blocked and nothing here is wrong with it — it is simply not a unit a
run may spend on its own.** Take it when it rides along with a visible parcel, or when
the mint it prices can actually mint: T-1209 raises the lodging roofs the beds are in,
and until those stand this axis prices a payment nobody can spend.

**What the reading did establish, so it is not lost:**

* The three buckets are `premises` 5, `street_only` 2, `unplaceable` 19 — and
  `street_only` is *also* "no premises", so the title's 19 is the unplaceable count and
  21 houses carry no building.
* The axis IS derivable for 7 of the 26: `premises` rows name a `structure_id` whose
  record carries a position, and both `street_only` rows name `south_water`, whose
  division the street layer states. Only the 19 are genuinely unsettleable.
* **And some of those 19 are not in Chicago at all.** `biz_e_wentworth`,
  `biz_e_wentworth_s_public_house_on_flag_creek`, `biz_e_wentworth_s_tavern_flag_creek`,
  `biz_e_wentworth_s_tavern_on_flag_creek` (Flag Creek, ~15 miles south-west) and
  `biz_geo_w_laird_naper_s_settlement` (Naper's Settlement) are five of the 26 hands.
  A house outside the town has no division because it has no side of the river, and it
  is not obvious it should be short of a hand the TOWN's order book pays for at all.
  That is a finding for whoever takes this: the axis cannot be priced for them, and
  "unplaceable" may be the wrong word for "elsewhere".

## STEPPED OVER AGAIN, 2026-09-28 — the 2026-09-25 reading re-confirmed, one call spent

A second run claimed this, re-read the note above, and released it in the same minute.
The note is still exactly right and nothing about the repo has changed to make it wrong:
`the_owner_s_ruling.mintable_today` is still 0, and the axis still prices a payment
nobody can spend. **Do not claim this to check whether it is still true — the answer is
in this file.** It becomes workable the run T-1209 raises the lodging roofs, and it
should ride along with that parcel rather than open a PR of its own.

## Queue cleanup 2026-10-03 (owner: "see if there are any tickets that were blocked in the queue from before but now can be worked")

**Unblocked.** Beds now exist: dev reads 225 ordinary night beds, 30 empty (was 144, all slept in).
