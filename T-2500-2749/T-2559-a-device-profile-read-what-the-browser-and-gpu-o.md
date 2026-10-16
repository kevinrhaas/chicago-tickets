---
id: T-2559
title: A device profile: read what the browser and GPU offer (WebGPU, compressed formats, cores, memory) and a one-second benchmark, then choose tier, sharpness, textures and workers per device
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
claimed_by: run 10/15/2026, 11:24:51 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38850138289
claimed_at: 2026-10-16T04:24:51.689Z
decision: null
decision_answer: null
---

A device profile: read what the browser and GPU offer (WebGPU, compressed formats, cores, memory) and a one-second benchmark, then choose tier, sharpness, textures and workers per device.

## Why

Owner, 2026-10-16: *"if there is a way to tap into local computing resources for rendering based on the browser and platform"*. Today the renderer knows exactly one thing about the device: whether it has a touch screen (`prefersTouch()` in `main.js` `boot`). A 2026 iPad Pro and a five-year-old Android phone both boot `light` at Sharpness Low, and a weak laptop boots `full`. Nothing reads what the browser will tell it.

## What

`renderers/web/js/device-profile.js`, run once at boot before the scene is fetched:

- **Read what the platform offers:** `navigator.gpu` (WebGPU present, and its adapter's limits and `info`), the WebGL2 renderer string (`WEBGL_debug_renderer_info` where exposed), `MAX_TEXTURE_SIZE`, which compressed formats are supported (ASTC / ETC2 / BC7, which T-2551 also needs), `hardwareConcurrency`, `deviceMemory` (Chromium only, so treat it as a hint), screen pixels and `devicePixelRatio`.
- **Measure briefly:** a ≤ 1 s GPU micro-benchmark (fill and vertex throughput on an offscreen target) behind the loading screen, timed with `EXT_disjoint_timer_query_webgl2` where present.
- **Decide:** a device class → the boot detail tier, Sharpness, texture tier (T-2551 / T-2553), worker count (T-2556) and whether WebGPU is available for a later renderer (T-2558). Cache the result per device in `localStorage`, keyed by the renderer string and build, so a repeat visit skips the benchmark.
- **The visitor keeps the last word:** Settings shows "Your device: <class>, chosen <tier>", and any setting they choose overrides the profile. T-2547's crash marker steps a class down. Doctrine 5 holds: a class changes flora, resolution and texture tier, never the reconstruction.

## Acceptance

1. The smoke boots the phone and desktop profiles and asserts the profile's choices and the Settings line, with zero page errors.
2. A forced "weak" and "strong" profile (`?device=weak|strong`, harness only) boot the expected tiers.
3. The benchmark's cost to time-to-ready is measured and stated (≤ 1 s cold, 0 warm).

## The group

Part of the owner's mobile performance and memory group of 2026-10-16 (T-2546 measures; see its reading). Added on the owner's follow-up the same day: *"if there is a way to tap into local computing resources for rendering based on the browser and platform or if there can be a big package app download that happens up front so the app is lightning fast rendering when you are walking or flying"*. T-2559 chooses per device, T-2560 ships the town prebuilt, and T-2561 puts it on disk. Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug), and its PR says so.

