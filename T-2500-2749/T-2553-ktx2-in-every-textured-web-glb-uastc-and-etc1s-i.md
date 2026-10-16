---
id: T-2553
title: KTX2 in every textured web GLB: UASTC and ETC1S in web_derivatives.sh, the light tier capped at 1024, Glessner v4 repacked, and every photo-match still matches
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: null
claimed_by: run 10/16/2026, 8:34:14 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38908068294
claimed_at: 2026-10-16T13:34:14.499Z
decision: null
decision_answer: null
---

KTX2 in every textured web GLB: UASTC and ETC1S in web_derivatives.sh, the light tier capped at 1024, Glessner v4 repacked, and every photo-match still matches.

## Why

The textured 1904 GLBs carry their images as JPEG/PNG inside the GLB. The phone's Glessner light tier alone is 24.4 MB of images, ~282 MB once decoded to RGBA8 + mips. The 17 textured Prairie houses hold 26 distinct images (~128 MB decoded) (the reading in T-2546). As the owner's photographic Prairie programme refines house after house, this total grows with every house, and it is what kills a phone on `/1904/`.

## What (bake side; needs the `ktx` binary the bake runner already installs, decision 5)

- `tools/web_derivatives.sh`: run gltf-transform's KTX2 encode on every derivative with images. Use **UASTC (+ RDO, zstd)** for normal / ORM / occlusion, **ETC1S** for basecolor unless it fails the photo-match, `KHR_texture_basisu` in `extensionsRequired`. Keep `EXT_meshopt_compression` + quantization as today.
- **Cap the light tier's resolution at 1024²** (it is the phone's), and 2048² at full. The 2048² JPEGs in the light Glessner are the largest single item on the phone.
- The Glessner v4 three-file package (`tools/recover_glessner_v4.py`) gets re-packed KTX2 derivatives with their hashes. The master stays untouched.
- `tools/measure_web_derivatives.py` learns the new assertion: no PNG/JPEG image in a web derivative.

Depends on the renderer half (T-2551) landing first.

## Acceptance

1. No web derivative carries a PNG/JPEG image. `/1904/` phone GPU texture bytes fall ≥ 4× in `measure_memory.mjs`, and the ceiling comes down.
2. `node tools/photo_match.mjs` on every house with a `matches` reference view still reads `matches` (AGENTS rule 11). Name any material moved from ETC1S to UASTC to get there.
3. The published payload is re-measured, and it should fall. The bytes are stated.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

