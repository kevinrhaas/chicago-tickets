---
id: T-2093
title: dev's smoke part 2 is red at both viewports since #396: the frontage layer lays 33 fence runs and the check still asserts 32 — T-1679 changed town_street_edge.json and not the count; read the 33rd run and restate the count or refuse the run
state: open
epic: META
requested_by: loop
seen: false
effort: M
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

dev's smoke part 2 is red at both viewports since #396: the frontage layer lays 33 fence runs and the check still asserts 32 — T-1679 changed town_street_edge.json and not the count; read the 33rd run and restate the count or refuse the run.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 191 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a red check on dev's own gate makes every PR's part 2 red for a reason none of them owns; no open ticket holds it (found on T-2089's gate, 2026-10-04)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
