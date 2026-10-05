---
id: T-2131
title: Dev's gate is red on the 1835 order book: the south ordinary-dwellings row still names T-1758, split at 06:09Z into T-2129/T-2130; repoint it at live work so dev, #460 and #461 go green again
state: review
epic: META
requested_by: loop
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-05
closed: null
pr: 462
claimed_by: run 10/5/2026, 1:41:11 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37273148325
claimed_at: 2026-10-05T06:41:11.446Z
decision: null
decision_answer: null
---

Dev's gate is red on the 1835 order book: the south ordinary-dwellings row still names T-1758, split at 06:09Z into T-2129/T-2130; repoint it at live work so dev, #460 and #461 go green again.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 180 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> dev's own gate is red on this one row, which blocks every open PR (#460, #461 wait on it); the repair cannot ride on T-2129, which a live sibling run holds mid-build, and a gate repair must be its own revertible PR

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
