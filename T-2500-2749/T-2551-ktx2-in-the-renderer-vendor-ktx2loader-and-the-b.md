---
id: T-2551
title: KTX2 in the renderer: vendor KTX2Loader and the Basis transcoder from the pinned three tarball, and ship the runtime library sheets GPU-compressed with mip 0 skipped on light
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
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T09:48:11.791Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

KTX2 in the renderer: vendor KTX2Loader and the Basis transcoder from the pinned three tarball, and ship the runtime library sheets GPU-compressed with mip 0 skipped on light.

## Why

Every texture in the renderer ships as JPEG, PNG or WebP, so each one is decoded on the CPU and uploaded as **uncompressed RGBA8**, 4 bytes a texel plus a third again for mips, plus three's retained ImageBitmap. GPU-compressed formats (ASTC/ETC2 on phones, BC7/BC1 on desktop) are 0.5 to 1 byte a texel, are uploaded with no decode, and stay compressed in GPU memory. This is the single change that lets the town carry photographic texture without running a phone out of memory. `/1904/` phone holds ~367 MB of decoded textures today (the reading in T-2546). The owner approved KTX-Software on the bake runner on 2026-08-14 (RENDERING.md §8 decision 5), for exactly this. The renderer half was never built.

## What (renderer side: no Blender, no bake)

- Vendor `KTX2Loader` and the Basis Universal transcoder (`basis_transcoder.js` + `.wasm`) from **the same pinned three 0.185.1 tarball**, with `vendor/MANIFEST` + `MANIFEST.sha256` lines (doctrine 8: no CDN, no runtime-fetched code). Call `detectSupport(renderer)` once, and register the loader on every `GLTFLoader` (`scene-loader.js`, `terrain.js`).
- Convert the **runtime library sheets** loaded by URL (`frontage.js`, `wall-relief.js`, `roof-relief.js`, `signage.js`, `street-grid.js`, `ground-strip.js`: the `*_basecolor`, `*_normal_gl`, `*_orm` sheets) to `.ktx2`. Use UASTC (+ RDO + zstd) for normal and ORM maps and ETC1S for basecolor. A converter script under `tools/` writes them next to the sources, and every output gets its `assets/LICENSES.md` line, inherited from its source.
- **Tiered residency from one file:** on `light`, skip transcoding mip 0 (load from mip 1), which quarters a sheet's memory with no second asset.
- Keep the WebP/PNG path as the fallback where a device's transcode target is unsupported.

## Acceptance

1. Every runtime sheet loads as KTX2 on desktop and phone profiles. `renderer.info` and `measure_memory.mjs` show GPU texture bytes for the sheets down ≥ 4× on phone and the ceiling lowered.
2. Captures at the anchors are within the photo-match tolerance the frontage/wall work already uses. Name any sheet whose ETC1S loss is visible and move it to UASTC.
3. The published byte budget (`SITE-BUDGET.md`) is re-measured. The transcoder's ~0.5 MB is accounted for, not waved through.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

