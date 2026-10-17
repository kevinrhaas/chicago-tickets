---
id: T-2696
title: Water, floors, verges and heights read in the worker beside the zones (the floor circles, water.isWater, streets.verge and terrain.surfaceHeight the deal still asks on the main thread), with measure_walk_frames at the throttled phone profile: spread-pass main-thread ms per pass and moving p95 down for walk and turn, boot to ready quoted before and after
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2684
opened: 2026-10-16
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

Water, floors, verges and heights read in the worker beside the zones (the floor circles, water.isWater, streets.verge and terrain.surfaceHeight the deal still asks on the main thread), with measure_walk_frames at the throttled phone profile: spread-pass main-thread ms per pass and moving p95 down for walk and turn, boot to ready quoted before and after.

Piece 2 of 2 of **T-2684 — The rest of the flora re-deal off the main thread (zones, water, floors, verges and heights read in the worker): spread-pass main-thread ms per pass and moving p95 down at the throttled phone profile, boot to ready quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2684 was split (2026-10-16T23:00:38.715Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 7m ago, run 10/16/2026, 5:53:56 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977942976) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977942976) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Carried from T-2695 (2026-10-17, PR #924)

- The zones are answered on ONE worker (pool.js `holdOnWorker`) from a held ground of about **13.6 MB** (heightfield 7.6 MB as float32, shore fields 5.9 MB, blend grid 0.1 MB). Water and heights read in the worker can read the same ground. Two ways to shrink it: send the heightfield as its int16 encoding and decode it on the worker, and derive the shore fields there from the heightfield (flora.js `waterField`'s chamfer as a shared function) instead of copying them.
- **Never make the walk's reply slower.** Folding the zones into the walk job made each walk about 3 ms slower, and the turn drained a third more passes, with frames to 64 ms. What shipped is a second job chained after the slots, which the deal never waits on. Anything T-2696 moves should follow it, either as more answers in `slotZones` or as its own chained job.
- Turn flora p95 did not fall with T-2695 (8.7-12.3 before, 11.2-12.1 after). Main-thread ms per pass fell (51-55 to 42-45), but in the turn many rows are dealt before the zone reply is home. Readings: `docs/measurements/t-2695-walk-frames-*-mobile.json`.
