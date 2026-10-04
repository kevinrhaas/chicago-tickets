---
id: T-2105
title: Moving frames measured (walk, turn, flight at both viewports and every tier, phone at 4x CPU throttle) and flora's rebuild halved by an exact floor index and cell cull, with a per-tier moving-frame ceiling
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2096
opened: 2026-10-04
closed: null
pr: 424
claimed_by: run 10/4/2026, 2:12:45 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37221734625
claimed_at: 2026-10-04T19:12:45.179Z
decision: null
decision_answer: null
---

Moving frames measured (walk, turn, flight at both viewports and every tier, phone at 4x CPU throttle) and flora's rebuild halved by an exact floor index and cell cull, with a per-tier moving-frame ceiling.

Piece 1 of 2 of **T-2096 — Lag while moving, in every mode and year: measure scripted walks, turns, flights and travel at both viewports and every tier on a throttled phone profile, fix the largest per-frame cost it names (the flora lattice rebuilt synchronously every 0.6 m and every small turn is one suspect), and hold the moving p95 frame time**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2096 was split (2026-10-04T19:12:33.914Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1.4h ago, run 10/4/2026, 12:48:29 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37221734625) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37221734625) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
