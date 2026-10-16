---
id: T-2605
title: The rest of the flora re-deal off the main thread (zones, water, floors, verges and heights read in the worker), double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2601
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

The rest of the flora re-deal off the main thread (zones, water, floors, verges and heights read in the worker), double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after.

Piece 2 of 2 of **T-2601 — The flora lattice re-deal in the job pool, double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2601 was split (2026-10-16T17:54:23.678Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 8m ago, run 10/16/2026, 12:46:13 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38941607051) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38941607051) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Carried from T-2604 (2026-10-16)

- T-2604 put the WALK on the pool and measured the cost of doing it one walk at a time: each `scatter` call of a pass waits about a frame for its reply, about 7 frames a near pass (6 walks), so passes start earlier and more of them run (walk at 4x/390x780: 133 -> 181 passes, 23.6 -> 16.0 ms each on the main thread; `docs/measurements/t-2604-walk-frames-*-mobile.json`). Sending a pass's whole deal as ONE job, which is this ticket, removes that per-walk latency too. The pass protocol T-2604 added (`WALK_WAIT` / `MAY_WAIT` in flora.js, `waits` in `stats.spread`) is the one to extend.
- What the deal reads on the main thread, by profile: the yards' sward test (T-2606), the zone finder, `streets.blocksGrowth`/`verge`, the floor circles (`blocks.at`), `water.isWater`, `terrain.surfaceHeight`, and the census counters it increments.
