---
id: T-2557
title: GPU-procedural near grass: the near ring dealt in the vertex shader from the lattice's own hash, the heightfield and the ground masks, with no CPU lattice and no re-deal on move
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

GPU-procedural near grass: the near ring dealt in the vertex shader from the lattice's own hash, the heightfield and the ground masks, with no CPU lattice and no re-deal on move.

## Why

The prairie is the town's largest moving cost and its most delicate look. `flora.js` (6,200 lines) deals a **world-anchored lattice** on the CPU (per-slot generator, salt, species deal, height/width/yaw/colour), writes instance arrays, and re-deals the near ring every 0.6 m of walking (`step.near`) and the far shrubs every 4 m. Every re-deal is CPU time, upload bandwidth and a typed array held twice. But a world-anchored, deterministic, per-slot lattice is exactly what a GPU can compute itself, per vertex, every frame, for free. This is how modern native engines draw grass fields: no instance buffer, and nothing to rebuild when the camera moves.

## What (one set first, as the proof)

- Take **the near ring's grass** (the `near` set, cap 2,400) and draw it as instancing whose instance data is computed **in the vertex shader** from `gl_InstanceID` and the camera's lattice cell: cell → slot → the **same hash/salt** `flora.js` uses → position jitter, species, scale, yaw, colour. Height comes from the heightfield as a texture (terrain already has it as a sampler, `terrain.js`). Exclusions (roads, footprints, plank floors, turf communities: T-2085 / T-2122) come from the ground masks the town already rasterises (`ground-strip-mask.js`, the turf mask) as one mask texture.
- The CPU does **nothing** per step: no lattice, no instance buffer, no rebuild. The fade ring stays the shader's own dither as today.
- WebGL2 is sufficient (instancing + `texelFetch` + integer hash). A later WebGPU renderer would compute the same in a compute pass.

Pairs with T-2556 (workers), which keeps the other sets off the main thread until they are moved too.

## Acceptance

1. **Same field:** at the critic anchors, the placement statistics (density per m², species shares, exclusion hits = 0 on roads and floors) match the CPU lattice within sampling error. Captures pass `critic_metrics.mjs` (crown/grass detail ratio, flower bloom) against today's reading. Name any liberty the hash changes, and append a **Revised** line in `docs/LIBERTIES.md` if one does.
2. `measure_walk_frames.mjs` throttled phone: the near ring's re-deal time goes to zero and moving p95 falls. Quote both.
3. Zero page errors at both viewports. Then file the remaining sets (mid, forb, heads, far shrubs) as one follow-up.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

