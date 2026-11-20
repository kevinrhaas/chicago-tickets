---
id: T-3706
title: Dev's desktop smoke 8 is red on unrelated PRs: 'the suite body ran to completion' times out in page.screenshot (90 s) while a frame costs 8-11 s on the software-GL runner — #2254, #2255 and #2251 all fail it, #2252 passes
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-20
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

Dev's desktop smoke 8 is red on unrelated PRs: 'the suite body ran to completion' times out in page.screenshot (90 s) while a frame costs 8-11 s on the software-GL runner — #2254, #2255 and #2251 all fail it, #2252 passes.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content-build smoke is red on desktop 8 for three open PRs (#2251, #2254, #2255) that do not touch what it reads; reproduced locally on #2254 at 17153e5ad

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
