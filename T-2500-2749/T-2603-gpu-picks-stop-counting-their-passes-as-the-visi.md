---
id: T-2603
title: GPU picks stop counting their passes as the visitor's frame
state: open
epic: META
requested_by: steward
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-16
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

GPU picks stop counting their passes as the visitor's frame.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's desktop smoke part 14 fails the 1904 spawn draw budget (7,500,192 triangles against 4.6M) because T-2573's GPU pick passes stay in renderer.info; PR #851 (T-2228) cannot merge until it is fixed

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
