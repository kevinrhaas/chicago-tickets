---
id: T-2079
title: The Sources topic reads sidecars/1835/sources/ in every scene: compile a per-scene source index so 1904's Sources lists the sources its own records cite, not the 1835 catalog
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: 470
claimed_by: run 10/5/2026, 5:25:45 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37296146152
claimed_at: 2026-10-05T10:25:45.336Z
decision: null
decision_answer: null
---

The Sources topic reads sidecars/1835/sources/ in every scene: compile a per-scene source index so 1904's Sources lists the sources its own records cite, not the 1835 catalog.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 192 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1740 gated every other 1835 drawer panel by the scene's layers list; Sources cannot be gated the same way because the 1904 Glessner card and jaunt cards link into it, so it needs its own index compiled. Folded into T-1740 it would vanish when #397 merges

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
