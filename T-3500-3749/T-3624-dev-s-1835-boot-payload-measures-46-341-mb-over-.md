---
id: T-3624
title: dev's 1835 boot payload measures 46.341 MB over its 45.7 MB budget, so every PR's content build is red on smoke (desktop, 1-2) — measure what grew since T-3609's 45.437 reading and re-budget or cut
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
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

dev's 1835 boot payload measures 46.341 MB over its 45.7 MB budget, so every PR's content build is red on smoke (desktop, 1-2) — measure what grew since T-3609's 45.437 reading and re-budget or cut.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red: smoke (desktop, 1-2) refuses every PR's content build on the boot payload budget (PR #2125 refused on it, run 43974971949)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
