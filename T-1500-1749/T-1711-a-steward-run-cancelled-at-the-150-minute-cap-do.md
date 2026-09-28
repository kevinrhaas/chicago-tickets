---
id: T-1711
title: A steward run cancelled at the 150-minute cap does not tell the scheduler its slot is free, so the lane sits empty until a cron tick that arrives 20-40 minutes apart
state: open
epic: PIPELINE
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-27
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

A steward run cancelled at the 150-minute cap does not tell the scheduler its slot is free, so the lane sits empty until a cron tick that arrives 20-40 minutes apart.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked for it filed as a band-9 ticket, 2026-09-27 10:50 PM CT

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
