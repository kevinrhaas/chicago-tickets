---
id: T-1657
title: PUBLIC_TRADES carries store_residence but none of the other commercial archetype terms, so a documented store in a C1, C3, C4 or F2 roof gets no signboard and no hitching post
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
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

PUBLIC_TRADES carries store_residence but none of the other commercial archetype terms, so a documented store in a C1, C3, C4 or F2 roof gets no signboard and no hitching post.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured

`tools/generate_frontage_works.py`'s hitching rule imports its trade set from
`generate_business_signboards.PUBLIC_TRADES` on purpose, "so the two layers cannot
drift". Read on 2026-09-27 while closing T-1648, that set contains `store_residence`,
`store` and `shop` but NOT the archetype terms `generate_block_infill.FUNCTIONS` deals:

| family | `function.value` | in `PUBLIC_TRADES` |
|---|---|---|
| C1 | `small_shop_or_office` | no |
| C2 | `store_residence` | **yes** |
| C3 | `narrow_two_story_store` | no |
| C4 | `wide_two_story_store_or_mixed_block` | no |
| F2 | `narrow_two_story_warehouse` | no — correct, a warehouse is clause 2's own refusal |

So of the ten roofs T-1648 re-familied onto South Water Street, only the four C2s were
even LOOKED AT by the hitching rule, and only they earned a written refusal. Today that
costs nothing visible, because every one of those roofs is an anonymous slot whose trade
is reconstructed and clause 3 would refuse it anyway. It stops costing nothing the first
time a DOCUMENTED trade stands in a C1, C3 or C4 roof: that building would get no
signboard and no hitching post, and — worse than the absence — no refusal saying why,
which is the one thing this project holds a rule to.

## The question to answer

Is `PUBLIC_TRADES` a list of trades, or a list of trades *as the archetype families spell
them*? If the former, the three C-family terms belong in it beside `store` and `shop`
(they are all "a customer who was a stranger off the street"), and F2 stays out as
clause 2's own example. If the latter, the set needs a second table keyed by family and
both rules need to read it. Either way the gate should refuse a commercial family whose
term no trade set knows — a silent omission is what this ticket is about.

Found while closing T-1648 (PR #102); nothing there depended on the answer.
