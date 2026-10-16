---
id: T-2556
title: A worker job system for procedural geometry: a module-worker pool with transferables, first moving the flora lattice re-deal and spatial-batch chunking off the main thread
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
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

A worker job system for procedural geometry: a module-worker pool with transferables, first moving the flora lattice re-deal and spatial-batch chunking off the main thread.

## Why

All procedural geometry is built on the main thread: the flora lattice re-deal (`flora.js`, every 0.6 m on the near ring, sliced into 4 ms per frame since T-2106), `spatial-batch.js` chunking, frontage/yard/enclosure construction at boot, and terrain tiles. A phone has 6 to 8 cores and the town uses one. Every millisecond of generation is a millisecond the frame waits, and that is the "jitter while moving" the owner reports. Native engines run this as a job system on worker threads, and the browser can do the same with no build step.

## What

- `renderers/web/js/jobs/`: a small **module-worker pool** (`new Worker(url, {type:'module'})`, sized `min(hardwareConcurrency − 1, 4)`) with a promise API and **transferable** typed arrays in both directions, so nothing is copied.
- **Constraint to design around:** import maps do not apply inside workers on every browser, so worker modules import **no bare specifiers** (not `'three'`). They are pure typed-array builders (math in, `Float32Array`/`Uint16Array` out), and the main thread wraps the result in `BufferGeometry` and uploads.
- **First two users**, each converted behind the same output contract:
  1. the flora lattice re-deal (the near/mid/forb ring's per-slot generator, salts and deal, which is deterministic and so is the same in a worker), double-buffered so the old lattice draws until the new one arrives;
  2. `spatialBatch` chunking.
- A synchronous fallback where `Worker` is unavailable, giving the same output.

## Acceptance

1. **Byte parity:** the worker and synchronous paths produce identical arrays for the same inputs (a test in `check.sh`, no browser).
2. `measure_walk_frames.mjs` at the throttled phone profile: no main-thread long task > 50 ms attributable to flora or spatial-batch during the scripted walk and turn, and moving p95 falls. Quote it.
3. Captures identical at the anchors. Zero page errors. Boot time to ready is quoted before and after.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

