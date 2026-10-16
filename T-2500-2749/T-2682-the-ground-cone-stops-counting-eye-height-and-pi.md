---
id: T-2682
title: The ground cone stops counting eye height and pitch as a new cone: walking up a grade no longer drops the spread pass and deals both flora lattices in one frame (the walk's long flora task at frame 2029), read with measure_walk_frames at the throttled phone profile, spread and one-frame passes still identical
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2605
opened: 2026-10-16
closed: null
pr: 901
claimed_by: run 10/16/2026, 3:07:40 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38958134513
claimed_at: 2026-10-16T20:07:40.294Z
decision: null
decision_answer: null
---

The ground cone stops counting eye height and pitch as a new cone: walking up a grade no longer drops the spread pass and deals both flora lattices in one frame (the walk's long flora task at frame 2029), read with measure_walk_frames at the throttled phone profile, spread and one-frame passes still identical.

Piece 1 of 3 of **T-2605 — The rest of the flora re-deal off the main thread (zones, water, floors, verges and heights read in the worker), double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2605 was split (2026-10-16T20:07:26.893Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 9m ago, run 10/16/2026, 2:58:52 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38958134513) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38958134513) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

measure_walk_frames --only mobile --tiers full --moves walk,turn --throttle 4 --source --verify, before and after on the same runner: the walk's flora tasks over 50 ms go from 2 to 1 (the one left is the right turn's snap, T-2683's), the turn's reading no worse, and --verify still reads every spread pass equal to the one-frame pass. Boot to ready quoted before and after.
