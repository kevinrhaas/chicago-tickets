---
id: T-3121
title: The full smoke's push path fires on every PR that merges dev after a chicago-4d-smoke.yml edit, cannot finish in 150 min, and so holds those PRs unmergeable (#1277, #1278)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-24
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

The full smoke's push path fires on every PR that merges dev after a chicago-4d-smoke.yml edit, cannot finish in 150 min, and so holds those PRs unmergeable (#1277, #1278).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> #1278 and #1277 are complete with a green gate but carry an incidental full-smoke run that times out (cancelled) — gh-rest refuses it as red and merge-ready reads the PR as unstable, so neither path can merge them

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
