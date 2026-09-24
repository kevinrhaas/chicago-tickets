---
id: T-1534
title: Fill the 131 adult beds the book still orders into lodging households: 11 ordinary night beds stand empty across the 16 built houses and the other 37 the lodging model schedules are unbuilt, so this piece advances as T-1209 raises them
state: split
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: 2026-09-24
pr: null
claimed_by: run 9/24/2026, 5:21:48 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-24T10:32:14.504Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35986294348
claimed_at: 2026-09-24T10:21:48.138Z
decision: null
decision_answer: null
---

Fill the 131 adult beds the book still orders into lodging households: 11 ordinary night beds stand empty across the 16 built houses and the other 37 the lodging model schedules are unbuilt, so this piece advances as T-1209 raises them.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Cut by T-1500 on 2026-09-24**, one of the three pieces its remainder divides into, and
the only one of the three that is a BED rather than a machinery: the boarders proper.

**The 24 cells, as the book stands on 2026-09-24** (adults 20 and over, `trade: none`, both
sexes, three divisions): 165 ordered, 34 filled by the boarders stage, **131 left**. By age
band: 20-29 70, 30-39 38, 40-49 15, 50+ 8.

**What bounds it.** `1835_lodgers_seated.json` `measurement`, re-derived by `check.sh`:
16 built lodging places, 144 ordinary night beds, 133 occupied after the boarders stage,
**11 ordinary night beds still empty**, 14 of the 16 houses already at their ordinary-night
figure, none over its crowded ceiling. The lodging model (T-1370) schedules 42 boarding
houses and 5 of them stand; the stage's own words: the other 37 "are 333 ordinary beds with
no roof over them, and a bed cannot be slept in before it is built".

So 131 people are ordered into beds that do not yet exist, and this ticket advances with the
roofs rather than against them. **T-1209** builds the boarding houses to their beds and is
open. Two further reasons the count cannot simply be minted:

- **No division, no mint.** The New York House (7 beds) and the Sauganash Hotel (4 beds)
  stand empty because nothing this project holds says which division they were in, and a
  person has to be ordered out of a bucket for a division. That refusal is T-1371's and is
  not lifted here.
- **The crews and the works gang** sleep aboard and on site rather than in a house, and
  they are **T-1407**'s (`blocked-tech`, waiting on a committed schedule). They come out of
  this order when that ticket unblocks; this ticket may not mint them.

## Acceptance

1. The bed accounting is re-read live before any mint — not the figures quoted above — and
   the number minted is bounded by the ordinary-night beds then standing.
2. Every person is seated in a house that stands, in a division the house has.
3. The crews and works gang are left to T-1407 and said to be left; the two no-division
   houses stay empty and said to stay empty.
4. Nothing already drawn moves (T-1459); the 34 filled stay filled.
5. `tier`, `basis`, `seed`, `replaceable_by` on every minted person (T-1158).
6. `build_order_book_1835.py --check`, `converge_resident_layer.py --run` and
   `./tools/check.sh` green.

## …and 64 lodging HOUSEHOLDS, reopened the same day by T-1476

`households/boarding_house/*` and `households/inn_tavern/*` were DISCHARGED when T-1420
swept them — every boarding house and inn the model wanted was standing. T-1476 landed on
dev on 2026-09-24, separated a household RECORD from a household in the town model, and took
the count from 124 to 563. Those six cells carry work again:

| cell | target | known | to reconstruct |
|---|---|---|---|
| `households/boarding_house/north` | 11 | 1 | 10 |
| `households/boarding_house/south` | 40 | 7 | 33 |
| `households/boarding_house/west` | 9 | 1 | 8 |
| `households/inn_tavern/north` | 3 | 0 | 3 |
| `households/inn_tavern/south` | 7 | 1 | 6 |
| `households/inn_tavern/west` | 4 | 0 | 4 |

**64 lodging houses**, and they are this ticket's for the same reason the 131 beds are: a
house has to stand before it holds anybody. They are also the other half of the same fact —
the lodging model schedules 42 boarding houses and 5 stand, and the book now orders 51
boarding-house households and 13 inn-tavern households against that. Reconcile the two
counts before minting either; a household and a roof are not the same unit, which is exactly
what T-1476 was filed to establish.

So this ticket's order, as of the merge: **131 beds and 64 houses**, both waiting on roofs.
If reconciling the house count against the lodging model's 42-roof programme turns out to be
a demonstration of its own, `ticket.mjs split` it rather than shipping a self-invented half.
