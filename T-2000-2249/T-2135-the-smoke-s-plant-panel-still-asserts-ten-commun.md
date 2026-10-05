---
id: T-2135
title: The smoke's plant panel still asserts ten communities and 155 species, and dev has served eleven and 166 since #460 (T-2101's vacant-lot prairie): part 13 is red on dev at mobile, three checks
state: open
epic: META
requested_by: loop
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-05
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

The smoke's plant panel still asserts ten communities and 155 species, and dev has served eleven and 166 since #460 (T-2101's vacant-lot prairie): part 13 is red on dev at mobile, three checks.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 176 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a red on dev's own smoke, not a finding about an open ticket: T-2101 closed with #460, which added the eleventh community without moving tools/smoke_renderer.mjs's hard-coded 10/155 (and the clamp/worst-case note checks beside them); measured on PR #469's mobile part 13, 122 passed / 3 failed, all three on the plant panel

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's smoke part 13 is red at mobile on three plant-panel checks that every PR's --for-diff legs inherit

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
