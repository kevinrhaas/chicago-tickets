---
id: T-2151
title: The boot payload is 13.488 MB against the 13 MB budget after T-2058 took liberties.json off it: the town grew ~0.97 MB and 140 requests since cb56e2e4 — find what grew (SITE-BUDGET §4b asks first whether the household seats belong in the boot sidecars) rather than raise the budget
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-06
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

The boot payload is 13.488 MB against the 13 MB budget after T-2058 took liberties.json off it: the town grew ~0.97 MB and 140 requests since cb56e2e4 — find what grew (SITE-BUDGET §4b asks first whether the household seats belong in the boot sidecars) rather than raise the budget.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 155 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2058 takes its named cut and the measure_boot_payload --check gate is still red at 13.488 MB; the overrun needs a live owner or the next refusal starts from nothing

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
