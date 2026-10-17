---
id: T-2602
title: T-2598's remaining readings: captures at glessner-aloft-ne and the three street-eye stands (measure_memory --walk prairie --captures), the moving p95 at phone profile on a GPU, and the 1904 memory ceilings re-read with residency
state: split
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: null
claimed_by: run 10/17/2026, 11:59:01 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T16:59:41.127Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39051423277
claimed_at: 2026-10-17T16:59:01.436Z
decision: null
decision_answer: null
---

T-2598's remaining readings: captures at glessner-aloft-ne and the three street-eye stands (measure_memory --walk prairie --captures), the moving p95 at phone profile on a GPU, and the 1904 memory ceilings re-read with residency.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (T-2558's H0 run, 2026-10-16) — the GL meter may read WebGL textures low

Read this before re-reading the 1904 ceilings: they stand on the same meter. On the H0
bake-off's Glessner block (`renderers/web-hd/classic.html`, three's WebGLRenderer with every
block texture made resident by `initTexture`), `measure_memory.mjs`'s own GL meter
(`installGlMeter`, which `tools/measure_hd_spike.mjs` reads out of that file) put the page's
whole texture total at **359.1 MiB**. three's arithmetic for what that page asked WebGL for is
at least **398.6 MiB**: 46 mip-filtered RGBA8 image maps at their own sizes (354.6 MiB, the
figure the WebGPU meter reads for the same 46 maps to 0.1 MiB), 27 BPTC maps (28.0 MiB) and
a 2048² shadow depth (16 MiB). So the meter reads **39.5 MiB low** there — or WebGL holds
less than three asked for. Either answer moves `tools/memory_ceilings.json`. A reading of
`window.__memoryMeter()` per texture against the page's own texture list on that page is the
shortest way in (`node tools/measure_hd_spike.mjs --dir <d> --pages classic --only phone`).
The full table is `docs/RENDERING.md` § 8, "H0 — the bake-off memo".
