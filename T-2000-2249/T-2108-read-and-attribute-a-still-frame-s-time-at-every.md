---
id: T-2108
title: Read and attribute a still frame's time at every stand, tier, viewport and year (tools/measure_still_frame.mjs and the committed table)
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2099
opened: 2026-10-04
closed: null
pr: 426
claimed_by: run 10/4/2026, 2:55:12 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236
claimed_at: 2026-10-04T19:55:12.576Z
decision: null
decision_answer: null
---

Read and attribute a still frame's time at every stand, tier, viewport and year (tools/measure_still_frame.mjs and the committed table).

Piece 1 of 4 of **T-2099 — Lag in every view, not only when walking: read still-frame GPU and CPU time at every stand, the aerial and overview, arrival and jaunt views and the 1812 and 1904 scenes, attribute it by layer and pass, fix the largest causes, and hold a frame-time ceiling per tier**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2099 was split (2026-10-04T19:55:00.196Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1.9h ago, run 10/4/2026, 1:01:29 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236) — held by the run that split it
- PR #426 on steward/t2099-still-frame-time — T-2099: a still frame's time read everywhere, and whose milliseconds they are — held by the run that split it
- branch `steward/t2099-still-frame-time` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
