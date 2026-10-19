---
id: T-2878
title: One run per house at a time: ticket.mjs claim refuses a 1904 house ticket while that house has a live claim, a ticket in review or an open PR, and list --workable marks the row HOUSE BUSY
state: open
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-19
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

One run per house at a time: ticket.mjs claim refuses a 1904 house ticket while that house has a live claim, a ticket in review or an open PR, and list --workable marks the row HOUSE BUSY.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked for it directly (2026-10-19, 'serialize tickets per house'); three Glessner PRs (#1090, #1091, #1094) collided on the house's bakes that day

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
