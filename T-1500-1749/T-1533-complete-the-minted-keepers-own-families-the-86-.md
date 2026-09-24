---
id: T-1533
title: Complete the minted keepers' own families: the 86 under-tens the book orders into lodging households, whom the boarders stage refused to draw because a child takes no bed on their own account
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
claimed_by: run 9/24/2026, 4:25:20 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35980824270
claimed_at: 2026-09-24T09:25:20.807Z
decision: null
decision_answer: null
---

Complete the minted keepers' own families: the 86 under-tens the book orders into lodging households, whom the boarders stage refused to draw because a child takes no bed on their own account.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Cut by T-1500 on 2026-09-24**, one of the three pieces its remainder divides into. The
division is the boarders stage's own, quoted.

`tools/seat_lodgers_1835.py` refusal 3:

> NO CHILDREN. The book orders 156 people under ten into lodging households. They are the
> keepers' own families, not boarders — a child does not take a bed at a tavern on their
> own account — so this stage draws only the adult and adolescent bands and leaves the
> `under_10` lodging order to the stage that completes a keeper's family.

And refusal 4 names who that was: "the kin of a household are `family/none` in the order
book and that quota belongs to T-1171 and T-1174". T-1174 is `done` and T-1171 is
`blocked-tech` on the attested and inferred heads — neither reaches a keeper the lodging
band MINTED, and neither is ordered against these cells. That is the hole, for this third
of T-1500.

**The 12 cells, as the book stands on 2026-09-24:** 102 ordered, 16 filled, **86 left**.
Every one of the 86 is `under_10`: the six `10_19/none` cells are discharged (16 of 16,
filled by the boarders stage). So the work is exactly the children, which is exactly what
refusal 3 said it would be.

The keepers these children belong to are named: `1835_lodgers_seated.json` `keepers` gives
every lodging place its keeper and how many persons stand on that keeper's card, and
`minted_keepers` is 6 of the 16.

## Acceptance

1. A child is written as kin of a NAMED keeper on a named house, never as a free-standing
   person in a lodging bucket — the `keepers` table is the join.
2. The count each keeper's card gains is derived from the household model's own family
   figures, not dealt flat across the 86.
3. Nothing already drawn moves (T-1459); the 16 filled stay filled.
4. `tier`, `basis`, `seed`, `replaceable_by` on every minted person (T-1158). No figures.
5. `build_order_book_1835.py --check`, `converge_resident_layer.py --run` and
   `./tools/check.sh` green.
