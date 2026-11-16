---
id: T-3613
title: Dev's desktop smoke part 13 is red: the Confidence view's three overlays add 19 geometries and 19 draw calls on switch-on (T-2650 check: 709 → 728, programs 150 both)
state: review
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: null
pr: 2119
claimed_by: run 11/16/2026, 12:13:48 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43923475678
claimed_at: 2026-11-16T18:13:48.825Z
decision: null
decision_answer: null
---

Dev's desktop smoke part 13 is red: the Confidence view's three overlays add 19 geometries and 19 draw calls on switch-on (T-2650 check: 709 → 728, programs 150 both).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: smoke (desktop, 13) fails identically on dev 2ae2ea7bf (job 133199210806) and on PR #2096's head fede3be6b (job 133181153314), so every open PR's leg 13 inherits it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
