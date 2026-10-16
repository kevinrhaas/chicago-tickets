---
id: T-2554
title: 1904 texture residency: textured houses resident by distance under a per-tier texture budget, uploads paced per frame, and the boot fetch bounded
state: split
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: 2026-10-16
pr: null
claimed_by: run 10/16/2026, 9:03:51 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T14:04:02.844Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330
claimed_at: 2026-10-16T14:03:51.119Z
decision: null
decision_answer: null
---

1904 texture residency: textured houses resident by distance under a per-tier texture budget, uploads paced per frame, and the boot fetch bounded.

## Why

`loadScene` (`scene-loader.js`) fetches and parses **every** structure of the year at boot, all at once, with no concurrency bound. Every texture of every house is resident from the first frame to the last, wherever the visitor stands. For 1835's untextured roofs that was affordable. For 1904's photographic houses it is not: each refined house adds tens of MB decoded, and the owner's programme refines ~60 more (the reading in T-2546). Native engines solve this with **residency**: the full asset is resident only where the camera can resolve it, and a cheap stand-in carries it elsewhere.

## What

- **A residency manager for textured structures.** Each textured house has two states: *resident* (its web derivative's materials and textures) and *distant* (the same batched geometry drawn with its untextured vertex-colour / material-colour fallback, the look a reader at 150 m cannot tell from the textured one). Swap by camera distance with hysteresis (enter < R_in, leave > R_out, per tier) under a **per-tier texture-memory budget** from `memory_ceilings.json`, nearest first.
- **Upload pacing:** call `renderer.initTexture()` on newly resident textures under a per-frame byte/ms budget (e.g. ≤ 4 MB or ≤ 3 ms a frame), so walking up the street never hitches on a `texImage2D`. Free textures on leaving (`dispose` + `releaseSharedImage`).
- **Bound the boot fetch:** a concurrency pool (6 to 8) in `loadScene` instead of an unbounded `Promise.all`, so peak memory during load is not every GLB's ArrayBuffer at once.
- Placement, picking, the card and the confidence view never depend on residency. Doctrine 5 holds: a tier may not degrade the reconstruction, and this changes only what is *uploaded* at a distance where it cannot be resolved. Prove it with captures.

Builds on T-2546 (the budget) and T-2553 (KTX2 derivatives, so a resident house is affordable).

## Acceptance

1. A scripted walk down Prairie Avenue (1800 → 1600 block) at phone profile holds GPU texture bytes under the tier budget at every step (`measure_memory.mjs` sampling along the walk), and the moving p95 frame time does not regress (`measure_walk_frames.mjs`).
2. Captures at the five Glessner stands and the street-eye stands are identical to today (residency is invisible at those stands).
3. The boot-time peak (max ArrayBuffers during load) falls and is quoted.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

