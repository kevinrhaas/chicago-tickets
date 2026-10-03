---
id: T-2017
title: Rebake the 1835 terrain and water meshes on PR #329's branch, for South Water's carried 22 m
state: open
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Rebake the 1835 terrain and water meshes on PR #329's branch, for South Water's carried 22 m.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 214 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> PR #329 (T-2012, owner-approved) cannot pass its gate without it, and only a pinned-Blender runner can rebuild the meshes

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #329's gate is red on terrain__e1834_harbor_cut and water__e1834_harbor_cut, stale against the regenerated heightfield

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
