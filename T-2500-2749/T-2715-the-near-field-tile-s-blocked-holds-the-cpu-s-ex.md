---
id: T-2715
title: The near field tile's BLOCKED holds the CPU's exclusion slot for slot: the worked bank's bare patches dealt per field texel instead of per point, any edge the tile still misses closed, and measure_flora_gpu_deal.mjs's exclusion hits 0 at all 22 critic stations on phone and desktop, with density and every species share still within 1 sigma of the CPU
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2708
opened: 2026-10-17
closed: null
pr: 972
claimed_by: run 10/17/2026, 3:18:38 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39016210646
claimed_at: 2026-10-17T08:18:38.509Z
decision: null
decision_answer: null
---

The near field tile's BLOCKED holds the CPU's exclusion slot for slot: the worked bank's bare patches dealt per field texel instead of per point, any edge the tile still misses closed, and measure_flora_gpu_deal.mjs's exclusion hits 0 at all 22 critic stations on phone and desktop, with density and every species share still within 1 sigma of the CPU.

Piece 1 of 3 of **T-2708 — The near ring's grass drawn from the shader in the page: the near set's instances computed from the GLSL lattice, deal and field tile with their heads, placement statistics at the critic anchors within sampling error of the CPU lattice, critic captures passing, the near re-deal at zero and moving p95 quoted at the throttled phone profile, zero page errors; the remaining sets (mid, forb, heads, far shrubs) filed as one follow-up**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2708 was split (2026-10-17T08:18:26.662Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 10/17/2026, 3:15:10 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39016210646) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39016210646) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

Stated 2026-10-17 by the run that claimed it, before the reading:

1. `working-bank.js` `blocksGrowth` answers per FIELD TEXEL (0.125 m, world-aligned with `near-field.js`'s grid): the wet test, the wear, the apron and the bare-patch draw are all taken at the texel's centre, and the draw is an integer hash of the texel's index rather than the per-point sin-hash no raster can hold. The bank keeps its bare share; its patches stop being finer than the tile.
2. Any exclusion the tile still misses at a slot (a travelway's, a yard's, a floor's edge running through a texel) is closed on the side of exclusion, and its cost is counted rather than hidden.
3. `node tools/measure_flora_gpu_deal.mjs --write`, phone and desktop, all 22 critic stations: GPU exclusion hits **0** (were 31 / 46), 0 rule disagreements, plants per m² and every species share within 1 sigma of the CPU, zero page errors; written to `docs/measurements/t-2706-flora-gpu-deal.json` with T-2715 named.
