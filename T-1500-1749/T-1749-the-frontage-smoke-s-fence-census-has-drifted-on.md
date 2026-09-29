---
id: T-1749
title: The frontage smoke's fence census has drifted on dev: 28 fence runs where the clause holds 31, and the two checks that read it are red on dev and on every branch
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
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

The frontage smoke's fence census has drifted on dev: 28 fence runs where the clause holds 31, and the two checks that read it are red on dev and on every branch.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 140 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> It is a red on dev's own tree, measured on both sides this run with byte-identical census figures, so it is nobody's branch to fix in passing: every slice that runs desktop part 2 pays to re-derive it and then steps over it. It belongs to the frontage census clause, not to any build ticket in the queue.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
