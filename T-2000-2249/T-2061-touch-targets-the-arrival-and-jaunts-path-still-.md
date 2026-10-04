---
id: T-2061
title: Touch targets the arrival-and-jaunts path still reaches under 44px: HUD chips 38px, the drawer's Back and Close 30px and its tabs 37px wide at 320, the place card's 'why' toggles 19x17
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
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

Touch targets the arrival-and-jaunts path still reaches under 44px: HUD chips 38px, the drawer's Back and Close 30px and its tabs 37px wide at 320, the place card's 'why' toggles 19x17.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 204 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2046's layout reading measures these on the path but they belong to the HUD, drawer and card contracts; T-2047, the report that names this section's successors, merged while T-2046 was in flight, so no live ticket owns the finding

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
