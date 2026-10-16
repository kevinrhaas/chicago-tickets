---
id: T-2548
title: 1904 phone: stop holding what it never reads again: the 26.5 MB Glessner GLB in assetBytes, the source glTF beside its batch copy, and decoded images after upload
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: 861
claimed_by: run 10/15/2026, 10:28:18 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38845327511
claimed_at: 2026-10-16T03:28:18.544Z
decision: null
decision_answer: null
---

1904 phone: stop holding what it never reads again: the 26.5 MB Glessner GLB in assetBytes, the source glTF beside its batch copy, and decoded images after upload.

## Why

On `/1904/` phone, about 50 MB of ArrayBuffers are held for nothing a phone reads (the reading in T-2546):

- **26.5 MB:** `scene-loader.js` `loadDetailAsset` keeps the WHOLE Glessner light GLB in `assetBytes`, so a detail switch can re-parse without a fetch. A phone boots `light` and almost never switches.
- **~22 MB:** the source glTF's quantized Int16/Int8 geometry stays alive beside the float32 copy `normalizeGeometry` made of it. The source should be disposed (`disposeLoadedAsset`) once the batch holds its copy. Find what retains it (the snapshot path ends in `InterleavedBufferAttribute.data`) and drop that reference.
- **Decoded images:** three keeps every `texture.image` (an ImageBitmap) after upload. On a phone, close it after upload (`Source` / `onUpdate`, the same hook pattern as `upload-release.js`). Keep the bitmap only where something re-uploads it (context loss already reloads; T-2158).

## What

Release all three on a coarse pointer (desktop keeps `assetBytes` for instant switching). A phone that switches detail re-fetches the GLB, which normally comes from the HTTP cache. Add each to `upload-release.js`'s census.

## Acceptance

1. `/1904/` phone ArrayBuffers fall by ≥ 45 MB in `tools/measure_memory.mjs`, and `memory_ceilings.json` comes down by what was measured.
2. A detail switch on the phone profile still works (smoke) and draws the same frame.
3. Picking, the confidence view and the card still work at both viewports, with zero page errors. Invisible, under exemption 1 (owner-reported bug); state it in the PR.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

