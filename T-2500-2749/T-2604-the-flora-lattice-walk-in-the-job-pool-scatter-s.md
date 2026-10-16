---
id: T-2604
title: The flora lattice walk in the job pool: scatter's cells, cone cull, deal ranks and jitter as a three-free kernel a spread pass awaits on a worker, slot for slot the in-frame walk (a check.sh gate), with the spread pass's main-thread milliseconds quoted before and after at the throttled phone profile
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2601
opened: 2026-10-16
closed: null
pr: 895
claimed_by: run 10/16/2026, 12:54:33 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38941607051
claimed_at: 2026-10-16T17:54:33.502Z
decision: null
decision_answer: null
---

The flora lattice walk in the job pool: scatter's cells, cone cull, deal ranks and jitter as a three-free kernel a spread pass awaits on a worker, slot for slot the in-frame walk (a check.sh gate), with the spread pass's main-thread milliseconds quoted before and after at the throttled phone profile.

Piece 1 of 2 of **T-2601 — The flora lattice re-deal in the job pool, double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2601 was split (2026-10-16T17:54:23.678Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 8m ago, run 10/16/2026, 12:46:13 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38941607051) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38941607051) may be working one of the pieces now.


**Acceptance:** (stated before working, 2026-10-16)

1. `renderers/web/js/jobs/lattice-kernel.js`: `scatter`'s walk (cells, ring and cone cull, strata/lattice/wild ranks, jitter, the stream after it) as a three-free kernel in the pool's table.
2. A spread pass sends its walks to the pool and deals what comes back; a one-frame pass, `settle` and a late slice walk in the frame. Nothing waits on a reply it cannot receive.
3. `tools/check_lattice_kernel.mjs` in `check.sh`: the kernel and flora.js's own `scatter` hand `emit` the same slots, bit for bit, on every layer's lattice and random ones, with a self-test that refuses a kernel one ulp, one slot or one row off.
4. `measure_walk_frames.mjs --verify` at 390x780, 4x throttle: every spread pass is the one-frame pass, and the spread pass's main-thread milliseconds quoted before and after.

## Profile that sized it (T-2601's run, 2026-10-16)

`measure_walk_frames --source --only mobile --tiers full --moves walk,turn --sync --profile 45`, 4x: of about 7.5 s of flora self time, `yards.js suppressesSward` 2.3 s (filed as T-2606), `scatter` (the walk, with its inlined hash and deal) 2.2 s, the zone finder (`matches`, `find`, `answer`, `pointInPolygon`, `ringsNear`) about 1.9 s, `streets.blocksGrowth` 0.4 s, `fringeOf` 0.3 s, placement under 0.2 s.
