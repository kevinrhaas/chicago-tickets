---
id: T-2113
title: The arrival and welcome screens redraw an unchanged town on every frame: draw it once under the menu and again only when something under it changes
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-04
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

The arrival and welcome screens redraw an unchanged town on every frame: draw it once under the menu and again only when something under it changes.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 190 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Found by T-2111 reading the arrival screen: the owner-reported lag (T-2099) includes every second a visitor spends on the welcome, where a phone redraws an identical picture at full cost

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
