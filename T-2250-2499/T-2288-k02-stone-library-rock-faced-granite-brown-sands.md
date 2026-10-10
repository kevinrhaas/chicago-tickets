---
id: T-2288
title: K02 stone library: rock-faced granite, brown sandstone, Lemont and Bedford limestone, dressed trim and foundation rubble as metric PBR fabrics with joint and edge profiles, studied in raking and diffuse light
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1844
opened: 2026-10-09
closed: null
pr: 624
claimed_by: run 10/9/2026, 11:41:02 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38024571632
claimed_at: 2026-10-10T04:41:02.610Z
decision: null
decision_answer: null
---

K02 stone library: rock-faced granite, brown sandstone, Lemont and Bedford limestone, dressed trim and foundation rubble as metric PBR fabrics with joint and edge profiles, studied in raking and diffuse light.

Piece 1 of 2 of **T-1844 — Stone, mortar and dressed masonry materials**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Acceptance (stated before work):**

1. A deterministic generator (numpy/scipy/Pillow, no photograph sampled) writes a K02 stone library: rock-faced granite, warm brown sandstone, pale Lemont limestone, pale Bedford (Indiana) limestone, smooth dressed trim and foundation rubble — each with seamless sRGB albedo, OpenGL normal and linear roughness, web JPEGs, and a `material.json` giving its metric tile in metres so it registers under K01's UV rule (TEXCOORD_0 = surface metres / tile_m).
2. Joint and edge profiles are DATA, not pixels: per fabric, the mortar joint width and recess depth, bed/course height ranges, arris bevel and chip parameters, in an engine-neutral `profiles.json` that T-2289's components read. No mortar line is baked into a stone map.
3. Granite is not the default: the library records, per fabric, the uses it is for (granite: rock-faced bases and the landmark it is attested on; sandstone, limestone: the brownstone/greystone fronts the study's register names), so nothing paints granite on every mansion.
4. A repeatable study renders each fabric on a sample panel in raking and diffuse light at metric scale, committed under docs/RESEARCH with its texture byte and pixel costs; asset licences recorded in assets/LICENSES.md; the reconstruction recorded as one liberty.
