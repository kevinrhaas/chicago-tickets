---
id: T-2394
title: Glessner granite relief in shade at the stone scale: bake occlusion for joints, drafted margins and pitched faces onto BakeUV (TEXCOORD_1), the light LOD included
state: split
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2390
opened: 2026-10-11
closed: 2026-10-11
pr: null
claimed_by: run 10/11/2026, 10:34:48 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-12T04:04:52.426Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38199969400
claimed_at: 2026-10-12T03:34:48.492Z
decision: null
decision_answer: null
---

Glessner granite relief in shade at the stone scale: bake occlusion for joints, drafted margins and pitched faces onto BakeUV (TEXCOORD_1), the light LOD included.

Piece 2 of 2 of **T-2390 — Glessner granite relief in shade: an occlusion channel for the rock faces (generators/ao_export.py), so shaded north/west faces show their relief without changing the light**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2390 was split (2026-10-12T02:19:06.065Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 19m ago, run 10/11/2026, 9:00:29 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38193697523) — held by the run that split it
- branch `steward/t2390-granite-occlusion` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38193697523) may be working one of the pieces now.

## What T-2393 measured, and why this piece exists

T-2393 gave the granite a material occlusion map from its own height field (horizon-based, 16
directions to 8 cm, tangent-biased; mean 0.932, min 0.678). On the T-2209 stands, same cameras,
desktop: shade luminance fell 1.7-5.4 % and the mean |Laplacian| fell with it, so the relief metric
did not rise; crease-scale contrast relative to luminance rose only 1-6 %. The split face's
texture relief is millimetres deep, and a tiling map cannot know where a stone's joints, drafted
margins and pitched face are. That stone-scale occlusion is what reads as relief in shade, and
it has to be baked per asset: `emit.bake_ao` onto the smart-UV `BakeUV` layer, which the v4
detail builder currently strips at export (`masonry_house_v4_detail.py`), exported as
TEXCOORD_1, with `baked_ao: true` and `ao_export.assert_ao_survived_export`. The light LOD
(`structure_versions.py build-light`) copies materials onto a different mesh, so it needs its
own UVs or its own bake. Budget the bake time and the web bytes before claiming.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
