---
id: T-3259
title: The moving-frames PR leg is cancelled by its own 30-minute timeout on a busy fleet: on 2026-10-30 PR #1463 ran it out on three successive heads (walk 10-20 min + phone 7-12 min) with zero FAILs, and #1470 the same — a cancel reads as red to the merge gate, so a green PR cannot merge without a blind merge; raise timeout-minutes or split the phone step into its own job
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-30
closed: null
pr: 1478
claimed_by: run 10/30/2026, 1:48:29 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41014945660
claimed_at: 2026-10-30T06:48:30.668Z
decision: null
decision_answer: null
---

The moving-frames PR leg is cancelled by its own 30-minute timeout on a busy fleet: on 2026-10-30 PR #1463 ran it out on three successive heads (walk 10-20 min + phone 7-12 min) with zero FAILs, and #1470 the same — a cancel reads as red to the merge gate, so a green PR cannot merge without a blind merge; raise timeout-minutes or split the phone step into its own job.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
