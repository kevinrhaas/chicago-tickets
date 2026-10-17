---
id: T-2699
title: The near ring's grass drawn from the shader: species and placeGraminoid's attributes dealt from the GLSL lattice and the field tile, placement statistics at the critic anchors within sampling error of the CPU lattice, critic captures passing, the near re-deal at zero and moving p95 quoted at the throttled phone profile, zero page errors; the remaining sets filed as one follow-up
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2557
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

The near ring's grass drawn from the shader: species and placeGraminoid's attributes dealt from the GLSL lattice and the field tile, placement statistics at the critic anchors within sampling error of the CPU lattice, critic captures passing, the near re-deal at zero and moving p95 quoted at the throttled phone profile, zero page errors; the remaining sets filed as one follow-up.

Piece 3 of 3 of **T-2557 — GPU-procedural near grass: the near ring dealt in the vertex shader from the lattice's own hash, the heightfield and the ground masks, with no CPU lattice and no re-deal on move**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2557 was split (2026-10-17T00:25:27.235Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 7:25:15 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38985727841) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38985727841) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding (T-2698's run, 2026-10-17) — the field tile's build is the cost to plan for

T-2698 built the field (`renderers/web/js/near-field.js`: community, WET, TURF, BLOCKED, TRODDEN and height in a 32 m tile at 0.125 m, re-centred every 8 m) and read it back through the GPU at every near slot of the 22 critic stations (`docs/measurements/t-2698-near-field.json`, PR #928). The shader agrees with the CPU mirror everywhere but one float32 texel-edge slot a viewport; the tile disagrees with the CPU at 1.17 % of phone slots and 0.90 % of desktop slots, height p95 under 0.6 mm.

**But built on the main thread it costs ~386-421 ms a tile — 48 ms per metre walked on the phone against the near re-deal's 2.3, and 53 against 9.3 on the desktop.** This piece cannot just call `flora.nearField.build` in the frame. Build it in the job pool (T-2695/T-2696 move the finder, water, floors and heights there) and re-rasterise only the quarter an 8 m re-centre exposes (a toroidal texture), and quote main-thread ms per metre walked against the re-deal's with `tools/measure_near_field.mjs`. Filed here rather than as a new line: the queue was at 176 against its ceiling of 140.

Also: the wharf's misses (12-13 % at every texel) are `working-bank.js` `blocksGrowth`'s per-point sin-hash, which no raster holds slot for slot; the raster keeps its SHARE, which is what this ticket's placement statistics measure. If per-slot parity there is ever wanted, carry the wear share as a channel and hash in the shader.
