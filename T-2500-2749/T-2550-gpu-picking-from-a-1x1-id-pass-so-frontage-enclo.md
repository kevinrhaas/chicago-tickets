---
id: T-2550
title: GPU picking from a 1x1 id pass, so frontage, enclosures, yard and structures release their CPU triangles (about 188 MB on the 1835 phone) and weathering becomes a uniform
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

GPU picking from a 1x1 id pass, so frontage, enclosures, yard and structures release their CPU triangles (about 188 MB on the 1835 phone) and weathering becomes a uniform.

## Why

`upload-release.js` `RELEASE_KEEP` keeps `position` + `index` on the CPU for `frontage`, `enclosures`, `yard` and `structures`, only so `pickAt` can raycast their triangles. It also keeps `structures`' `color`, because the weathering slider rewrites it in place. On `/1835/` phone that is **~188 MB of CPU memory** (frontage 80, enclosures 41, structures 37, yard 30) duplicated on the GPU (the reading in T-2546). A CPU raycast through hundreds of thousands of triangles is also a hitch on a phone at the moment of the tap.

## What

**GPU picking**, the way native engines and every serious web editor do it:

- On a tap or click, render the pickable layers once into a 1×1 (scissored) `R32UI` / RGBA8 target with an **id material** that writes a per-object id. For a `BatchedMesh` the id is the batch id (`gl_DrawID` / the batching id three already provides); for a merged chunk it is a per-vertex Uint16/Uint32 id attribute (`frontage`, `yard` and `enclosures` merge many owners into one draw). Read back one pixel and map id → `structure_id` / lot / feature with the table each layer already keeps for its card.
- Depth at that pixel (a second 1×1 target, or the same pass packing depth) gives the world hit point for everything that uses `asked.point`.
- Then `RELEASE_KEEP` drops `position` + `index` for all four layers.
- **Weathering becomes a uniform** (`mix(base, weathered, uWeather)` in the existing structures shader patch), so `structures`' `color` goes too.

## Acceptance

1. Every pick point the smoke already taps resolves to the same id as today's raycast, at both viewports and in every year. Add a smoke assertion comparing the two paths on a fixed list while the raycast still exists, then remove the raycast.
2. `/1835/` phone ArrayBuffers fall by ≥ 150 MB in `measure_memory.mjs`, and the ceiling comes down.
3. Weathering looks identical at 0, 0.5 and 1 (captures). The confidence view is unaffected. Zero page errors.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

