---
id: T-1566
title: The staffing mint's payment never prices the DIVISION axis: a north lodging slot pays for a hand in a south shop, and for 19 of the 26 the register places no premises at all
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

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

