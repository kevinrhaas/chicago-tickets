---
id: T-2683
title: A snap turn or arrival deals its flora lattice off the main thread, every walk of the pass sent to the pool at once and the old lattice drawing until the new one lands: no flora task over 50 ms in walk and turn at the throttled phone profile (the 120 ms one-frame pass at the walk's right turn), with what the visitor sees in the frames between stated
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2605
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 3:22:44 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38961045470
claimed_at: 2026-10-16T20:22:44.483Z
decision: null
decision_answer: null
---

A snap turn or arrival deals its flora lattice off the main thread, every walk of the pass sent to the pool at once and the old lattice drawing until the new one lands: no flora task over 50 ms in walk and turn at the throttled phone profile (the 120 ms one-frame pass at the walk's right turn), with what the visitor sees in the frames between stated.

Piece 2 of 3 of **T-2605 — The rest of the flora re-deal off the main thread (zones, water, floors, verges and heights read in the worker), double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2605 was split (2026-10-16T20:07:26.893Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 9m ago, run 10/16/2026, 2:58:52 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38958134513) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38958134513) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Carried from T-2682 (2026-10-16)

- `measure_walk_frames` now names every frame over 50 ms (`longs`). Before T-2682 the walk had two: frame 1655 (this ticket's 90° right turn, ~130 ms at 4x) and frame 2029 (an eye-height "cone change" on a grade, fixed by T-2682). After it, the snap at 1655 read 120 ms in one of three readings and did not appear in the other two, so it depends on timing (whether a pass is pending or due when the snap lands). Read it more than once before calling it fixed or not. Readings: `docs/measurements/t-2682-walk-frames-*-mobile.json`.
