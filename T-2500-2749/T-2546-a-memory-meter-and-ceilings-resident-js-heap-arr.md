---
id: T-2546
title: A memory meter and ceilings: resident JS heap, ArrayBuffers and GPU geometry and texture bytes per year, viewport and layer, gated like frame time (phone memory crashes, owner 2026-10-16)
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: 864
claimed_by: run 10/16/2026, 12:46:35 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38856979662
claimed_at: 2026-10-16T05:46:36.126Z
decision: null
decision_answer: null
---

A memory meter and ceilings: resident JS heap, ArrayBuffers and GPU geometry and texture bytes per year, viewport and layer, gated like frame time (phone memory crashes, owner 2026-10-16).

## Why

Nothing in the gate measures memory. Frame time has ceilings (`still_frame_ceilings.json`, T-2111), triangles and draws have ceilings (`DETAIL`, `BUDGET`), and the published bytes have a budget (`SITE-BUDGET.md`). But the thing that kills a phone tab, resident memory, is read only ad hoc in per-ticket QA scripts (`qa_k01_*`, `qa_draft_*`) and never compared with anything. So every parcel can add memory and nothing goes red until a phone dies. This is the measurement half of the group (AGENTS exemption 2), filed on an owner-reported bug (exemption 1).

## The reading this group stands on (2026-10-16)

Owner, 2026-10-16: *"I see often that in a browser on mobile we get memory crashes and it's getting jittery … keep it simple and lightweight the way we have it now and rely on the local cpu gpu etc to handle the complex rendering so it is like a native application."*

Taken on the published mirror at `b1980f5d` (`tools/publish.sh`), headless Chromium, 390×780, `hasTouch` + `isMobile`, pixel ratio 1 (Sharpness Low, the phone default), welcome entered at spawn, two forced GCs. JS heap from `Runtime.getHeapUsage`; ArrayBuffer memory from its `backingStorageSize` and a heap snapshot's retainers; GPU bytes estimated from every live attribute and texture in `scene3d` (RGBA8 + mips for an image texture).

| phone | JS heap | ArrayBuffers (CPU) | GPU geometry | GPU textures |
|---|---|---|---|---|
| `/1835/` | 109 MB | **373 MB** | ~350 MB | 86 MB (19 distinct) |
| `/1904/` | 30 MB | **245 MB** | ~110 MB | **~367 MB** (77 distinct) |

- **1835, per layer, CPU kept / GPU:** frontage 80 / 118 MB, structures 37 / 71, enclosures 41 / 46, yard 30 / 38, terrain 21 / 32, trees 5 / 42, yard-ground 0 / 27. `upload-release.js` already lets go of 287 MB (T-2158); what remains is `RELEASE_KEEP`'s `position` + `index` for picking and `structures`' `color` for weathering.
- **1904, ArrayBuffers by retainer (snapshot):** 26.5 MB is the whole Glessner light GLB held in `scene-loader.js` `assetBytes`; ~120 MB is float32 batch attributes (position, color, normal, uv, `_confidence`, `_roughness`); ~22 MB is the SOURCE glTF's quantized Int16/Int8 geometry still alive beside its float32 copy.
- **Textures:** the phone's `glessner_house__as_built_1887.light.glb` is 27.8 MB, 24.4 MB of it 33 PNG/JPEG images (7 × 2048² JPEG, 16 × 1024² PNG, …), about 282 MB once decoded to RGBA8 with mips. The 17 textured Prairie houses carry 26 distinct images (128 MB decoded). Every texture ships JPEG/PNG/WebP, so every one is decoded to uncompressed RGBA8 on the GPU.
- **Vertex format:** `buildings.js` `normalizeGeometry` expands every quantized (`KHR_mesh_quantization`) attribute to float32 and adds float32 `color`, `_roughness` and `_confidence` plus a Uint32 index, at about 52 B/vertex where a compact layout is about 20.

SwiftShader is a software rasteriser, so these are byte counts, not timings. The bytes are the same on a phone, and on iOS the GPU's share counts against the same tab's memory limit.

## What

- `tools/measure_memory.mjs`: boot each year (`1812`, `1835`, `1904`) at 390×780 phone (`hasTouch`, `isMobile`, its boot tier) and at 1280×800 desktop `full`. Read, after two forced GCs: JS heap, ArrayBuffer backing store, estimated GPU geometry and texture bytes **per top-level layer**, distinct textures, shadow-map bytes, and the ten largest ArrayBuffer retainer paths from a heap snapshot. `--json` writes a reading; `--from` re-prints one with no browser.
- `tools/memory_ceilings.json`: a ceiling per year × viewport for **total resident estimate** (heap + ArrayBuffers + GPU), set from this reading with its margin stated. The first ceiling is today's figure: it holds the line while the tickets below bring the figure down, and each of them lowers the ceiling in its own PR.
- Wire it where frame time already runs (`smoke_budget.mjs` legs / nightly). Never the 600 s check.sh.
- A section in `docs/performance/` with the table above, re-measured.

## Acceptance

1. Each year × viewport has a committed reading and ceiling. A self-test breaks the ceiling (`?keep-geometry=1`, which keeps every page array) and goes red.
2. The reading names the top retainers. On `/1904/` phone it shows `assetBytes` and the float32 batch attributes; on `/1835/` phone it shows frontage / enclosures / structures / yard.
3. The cost on the gate is measured and stated.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

