---
id: T-3535
title: Use conservative shadow culling at Balanced detail
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-10
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

Use conservative shadow culling at Balanced detail.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> T-3533 cannot pass the published desktop stage 5 gate: Balanced exceeds its unchanged triangle ceiling. The existing culler saves 66537 triangles at the failing view with zero changed pixels.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
