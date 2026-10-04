---
id: T-2065
title: The derived manifest's in-sequence lags T-1602 left: location_spend reads the reconciliation a later step rebuilds, the seating passes sit outside the manifest, and nothing gates the 84-132 answer
state: open
epic: META
requested_by: loop
seen: false
effort: M
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

The derived manifest's in-sequence lags T-1602 left: location_spend reads the reconciliation a later step rebuilds, the seating passes sit outside the manifest, and nothing gates the 84-132 answer.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 199 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1602 had T-1671 and T-1720 folded into it; PR #382 closed T-1602's own acceptance (the stale model) and not theirs, so without this line the folded work left the queue when T-1602 settled done. Net zero: T-1602's line left as this one joins.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
