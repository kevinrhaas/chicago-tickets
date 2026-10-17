---
id: T-2707
title: The near field tile built off the main thread: built in the job pool and re-rasterised only in the strip an 8 m re-centre exposes (a toroidal tile), with main-thread ms per metre walked quoted against the near re-deal's by measure_near_field.mjs (after T-2696's worker reads)
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2699
opened: 2026-10-16
closed: null
pr: 947
claimed_by: run 10/17/2026, 12:59:26 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39008011647
claimed_at: 2026-10-17T05:59:26.817Z
decision: null
decision_answer: null
---

The near field tile built off the main thread: built in the job pool and re-rasterised only in the strip an 8 m re-centre exposes (a toroidal tile), with main-thread ms per metre walked quoted against the near re-deal's by measure_near_field.mjs (after T-2696's worker reads).

Piece 2 of 3 of **T-2699 — The near ring's grass drawn from the shader: species and placeGraminoid's attributes dealt from the GLSL lattice and the field tile, placement statistics at the critic anchors within sampling error of the CPU lattice, critic captures passing, the near re-deal at zero and moving p95 quoted at the throttled phone profile, zero page errors; the remaining sets filed as one follow-up**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2699 was split (2026-10-17T04:52:51.686Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/16/2026, 11:48:41 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39003684619) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39003684619) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

Stated 2026-10-17 by the run that claimed it, before the reading:

1. `flora.nearField.keeper()` keeps the 32 m tile around the walker as a toroidal tile: a re-centre re-rasterises only the strip it exposed (a quarter of the tile for a straight 8 m step, 7/16 on a diagonal), the strips asked of the job pool's ground worker (`jobs/zone-kernel.js` `fieldRect`: community, WET, TURF, floor, TRODDEN, height), the page adding only `growthBlocked` and any texel the worker could not answer. `tools/check_near_field_keeper.mjs` (in `check.sh`, with a self-test) holds the kept tile to `buildField` after every kind of re-centre.
2. `measure_near_field.mjs --walk`, at every critic station, phone and desktop: after a 96 m walk (12 re-centres) the pool-kept tile equals `nearField.build` at the station texel for texel — 0 differing texels — and the GPU read-back through `FIELD_GLSL` with the tile's wrap agrees with `sampleField` at every slot (float32 edges counted apart, as T-2698's).
3. The same reading quotes main-thread ms per metre walked for the pool-kept tile against the near re-deal's per metre and against the whole tile built on the page every 8 m (T-2698's 48 / 53 ms per metre), and its worst single step; written to `docs/measurements/t-2707-near-field-keeper.json`. Zero page errors.
