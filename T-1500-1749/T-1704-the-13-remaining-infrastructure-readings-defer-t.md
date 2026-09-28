---
id: T-1704
title: The 13 remaining INFRASTRUCTURE readings defer to T-1586, whose whole chain has closed: dev's gate is red on all of them until they are repointed at a live ticket
state: open
epic: META
requested_by: loop
seen: false
effort: M
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

The 13 remaining INFRASTRUCTURE readings defer to T-1586, whose whole chain has closed: dev's gate is red on all of them until they are repointed at a live ticket.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> clean origin/dev fails tools/measure_research_spend.py --check on 13 units whose unresolved pointer is T-1586, a split parent whose children T-1591 and T-1592 both settled done; check.sh is therefore red on three steps for every open PR, which is the T-1584 shape exactly

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
