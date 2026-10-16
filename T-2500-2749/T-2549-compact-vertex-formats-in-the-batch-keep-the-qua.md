---
id: T-2549
title: Compact vertex formats in the batch: keep the quantization the bake paid for, about 52 to at most 24 bytes a vertex for structures, frontage, enclosures and yard, with pixel parity
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

Compact vertex formats in the batch: keep the quantization the bake paid for, about 52 to at most 24 bytes a vertex for structures, frontage, enclosures and yard, with pixel parity.

## Why

`buildings.js` `normalizeGeometry` (≈ line 138) is the one funnel every structure passes through, and it throws away the compression the bake paid for. The GLBs ship `KHR_mesh_quantization` (Int16 positions, Int8 normals), and the batch re-expands them to float32 and adds float32 `color`, `_roughness` and `_confidence` plus a Uint32 index, about **52 B/vertex** on BOTH the CPU and the GPU. On `/1904/` phone that is ~120 MB of float32 attributes, and on `/1835/` the structures, frontage, enclosures and yard layers are ~270 MB of GPU geometry (the reading in T-2546).

## What

A compact layout, decoded by WebGL's own normalized-attribute path wherever possible (no shader change):

| attribute | today | compact |
|---|---|---|
| position | f32×3 (12 B) | **Int16×3 normalized, relative to the 40 m `spatial-batch` cell or the batch's box** (6 B, about 0.6 mm at 40 m), with the offset and scale in the mesh/instance matrix |
| normal | f32×3 (12 B) | Int8×3 normalized (3 B, padded to 4) |
| uv / uv1 | f32×2 (8 B) | Float16 or Uint16 normalized when in [0,1] (4 B) |
| color | f32×3 (12 B) | Uint8×3 normalized (3 B), or per-instance colour where the tone is per building |
| `_roughness` | f32 (4 B) | Uint8 normalized (1 B), or a material uniform where it is constant per batch |
| `_confidence` | f32 (4 B) | Uint8 (1 B) |
| index | Uint32 | Uint16 wherever a batch/chunk has < 65,536 vertices |

Apply the same to the other layers that build their own float32 buffers where it is cheap (`frontage`, `enclosures`, `yard`). Each layer's own shader patches (`onBeforeCompile`) must keep reading what they read. Check every one that touches `color`, `_roughness` or `_confidence`, and `confidence.js` first.

## Acceptance

1. Bytes per vertex in `structures` ≤ 24 (from ≈ 52), measured and quoted. GPU geometry for structures + frontage + enclosures + yard on `/1835/` phone falls ≥ 40 % in `measure_memory.mjs`, and the ceiling comes down.
2. **Pixel parity:** captures at the scene anchors at both viewports are identical within the existing capture tolerance. The confidence view (all levels, HIDE) and weathering look unchanged.
3. Picking still lands on the same structure ids at the smoke's pick points. Zero page errors.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

