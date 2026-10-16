---
id: T-2683
title: A snap turn or arrival deals its flora lattice off the main thread, every walk of the pass sent to the pool at once and the old lattice drawing until the new one lands: no flora task over 50 ms in walk and turn at the throttled phone profile (the 120 ms one-frame pass at the walk's right turn), with what the visitor sees in the frames between stated
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2605
opened: 2026-10-16
closed: 2026-10-16
pr: 903
claimed_by: run 10/16/2026, 3:22:44 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T22:47:47Z
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

`measure_walk_frames --only mobile --tiers full --moves walk,turn --throttle 4 --source --verify`, before and after on the same runner: the walk's right-turn one-frame pass (frame 1655) is gone and the snap is dealt as jump passes, the turn has no flora frame over 50 ms, and `--verify` still finds every spread pass identical to the one-frame pass.

## Finding (T-2683's run, 2026-10-16, PR #903)

- dev at 115f9d096: frame 1655 of the walk is a one-frame pass, 140.5 ms flora; 10 passes dealt in one frame. After: the snap is 2 jump passes landing in 20-22 frames in every one of six readings; walk flora max 13.7-15.8 ms in three of four walk runs.
- Not everything: one slow after-run (median 3.3 ms) had a 58 ms frame at 2169, a SPREAD pass drained late by SPREAD_MAX_MS, not a jump. Before-runs drain 0-5 such passes too. That is T-2684's (the deal itself off the main thread).
- Between: about 10 frames a pass after a 90 degree snap, the newly faced side beyond CONE_KEEP_M (3.5 m) shows bare ground texture, then the plants land at once (the same plants, --verify).

## Carried from T-2682 (2026-10-16)

- `measure_walk_frames` now names every frame over 50 ms (`longs`). Before T-2682 the walk had two: frame 1655 (this ticket's 90° right turn, ~130 ms at 4x) and frame 2029 (an eye-height "cone change" on a grade, fixed by T-2682). After it, the snap at 1655 read 120 ms in one of three readings and did not appear in the other two, so it depends on timing (whether a pass is pending or due when the snap lands). Read it more than once before calling it fixed or not. Readings: `docs/measurements/t-2682-walk-frames-*-mobile.json`.
