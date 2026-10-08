---
id: T-2023
title: Seat the lodging remainder as lodging roofs rise: 7 West adults the book orders with no free bed, and 44 boarding-house and inn households waiting on roofs. T-1538's frozen top-up deals new roofs to them automatically
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
claimed_by: run 10/8/2026, 12:37:12 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37817443904
claimed_at: 2026-10-08T17:37:12.195Z
decision: null
decision_answer: null
---

Seat the lodging remainder as lodging roofs rise: 7 West adults the book orders with no free bed, and 44 boarding-house and inn households waiting on roofs. T-1538's frozen top-up deals new roofs to them automatically.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 213 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> closing T-1538 strands the book's lodging rows (gate: closing this branch's tickets strands nobody); they need a live owner in the same PR

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Filed by T-1538 (PR #340, 2026-10-03)

**What is left, measured on the build that closed T-1538** (`1835_lodgers_seated.json` → `quota_basis.top_up.what_is_left`):

- **7 West adults ordered with no free bed**: male 20-29 ×2, 30-39 ×2, 40-49 ×1, 50+ ×1, and female 40-49 ×1, all `lodging/none`. They are already in the top-up's FROZEN room. A West lodging roof raised later is dealt to them automatically, last in the house order, so nobody already standing moves. This needs no new machinery, only the roof (T-1209) and a `seat_lodgers_1835.py --build`.
- **44 lodging households** (boarding_house + inn_tavern; the book orders 66 and the stage fills 22). These also wait on roofs.
- **29 ordinary-night beds with no order**: 13 North (Kelsey's 4, Chapin's H3 6, the Steamboat 3) and 16 South (the Dearborn and Market H3 houses). No adult `lodging/none` order is open in those divisions, so nobody is minted into them. Either the lodging model over-apportions beds in those divisions or the book under-orders them. Reconcile the two before minting.
- **The housing deal moves on every resident mint.** One more lodger took one place under the town-wide ceiling, so `hh_pennington_sack_f` (presence `ruled_in`, last in the line) now waits on a roof. The greedy least-crowded pass also re-shuffled about 367 boarded seats. An invented boarder outranking a named ruled-in household for a roof may be backwards (L252: documented people displace invented ones). It is worth a ruling.

## Carried here from T-1532 (2026-10-03): the staffing mint's DIVISION axis is still unpriced

T-1532 dealt the book's last `lodging/trade` order (four South youths, PR #343). It had
absorbed **T-1566** in the 2026-10-03 queue cleanup, and **T-1566's piece was NOT done
there**. `tools/staffing_mint_order_1835.py` still pays a hand from the first bucket by
key, whatever division its house stands in, so a north lodging slot can pay for a hand
in a south shop. It was not worth a run on its own: the mint pays **0** slots today, and
pricing the axis mints nobody. It rides with this ticket, because it becomes live the
moment the lodging roofs rise and the purse can pay again. T-1532's file keeps the
reading: 7 of 26 hands are derivable (5 `premises` and 2 `street_only` on
`south_water`), and 19 are not. Five of those 19 are out of town (Flag Creek and
Naper's Settlement), where "elsewhere" is the honest word rather than "unplaceable".
