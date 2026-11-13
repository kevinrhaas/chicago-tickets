---
id: T-3583
title: Fort Dearborn monument's figures modelled past their poses (faces, hair, drapery, ornaments and weapons as sculpted), the inscription cut, the front panel's c. 1900 tone, and its match records to matches
state: split
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-3568
opened: 2026-11-13
closed: 2026-11-13
pr: null
claimed_by: run 11/13/2026, 3:38:36 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-13T21:45:22.784Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43511249978
claimed_at: 2026-11-13T21:38:37.634Z
decision: null
decision_answer: null
---

Fort Dearborn monument's figures modelled past their poses (faces, hair, drapery, ornaments and weapons as sculpted), the inscription cut, the front panel's c. 1900 tone, and its match records to matches.

Piece 2 of 2 of **T-3568 — Fort Dearborn Massacre monument worked to its pictures: cameras on ICHi-19208, Taylor 1893 and Detroit 4a08066, side-by-sides to matches, and the Pullman house's 4a08066 and 4a08065 records showing it**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3568 was split (2026-11-13T17:24:49.574Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 11/13/2026, 11:24:35 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/43470026646) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/43470026646) may be working one of the pieces now.

## Image gate stays on T-3568

T-3568 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Owner's suggestion (Kevin, 2026-11-13): build the figures on the people harness

> if there are a bumch of people in that monument maybe you can use some of the existing people harness maybe you arelady thought of that and are doing that but i wanted to suggest that for that ticket

**Not done yet, and not planned in this ticket's text.** T-3565's ruling already allows the portable-human rigs "only as an armature", but nothing built so far uses them: `generators/archetypes/monument.py` (T-3567, poses by T-3582, PR #2005) joins each figure from tapered limbs and balls in pure Python, with no human asset, face, hair or cloth. That is where the "modelled past their poses" gap in this ticket comes from. Take Kevin's suggestion as the starting route for this ticket:

- **Bodies from the existing rigs** (`assets/humans/`, MakeHuman hm08, LOD0-3): the warrior and Black Partridge from `potawatomi_man_1812`, Margaret Helm from `lady_1812`, the fallen post surgeon from `surgeons_mate_first_infantry_1812`, the child from `child_boy_1812` / `child_girl_1812` (whichever the photographs read). Bodies and armatures only: dress, undress, ornaments, feathers, hair and weapons are re-made to the sculpture, and the project's Native dress / variation rules (`dress_1812_native.json`) still do not apply (T-3565 ruling).
- **Pose** each skeleton to the joints T-3582 already read (`FIGURES` in `monument.py`, ICHi-19208 + Taylor 1893), then bake the skinned mesh to a static mesh in the monument's frame.
- **Faces** from the hm08 variation kit (`hm08_variation_kit`, `tools/fit_portrait_face.py`) fitted to the sculpted faces as the photographs show them, not to portraits of the real people.
- **Hair, feathers and drapery** from the strand-hair and cloth systems (`human-skirt.js` bell for Mrs. Helm's skirt; the fabric fold work) as starting shapes, solidified and baked as cast bronze.
- **Render as bronze**: one bronze material shared with the rock (no skin, hair or fabric shaders), merged into the monument's GLB, one draw call per LOD; LODs from the rigs' own lod0-3 so Light and phones get the reduced group (T-3565 budget ruling: `measure_detail_ceilings.mjs --deal` before raising anything).
- **Watch-outs**: `monument.py` writes its glTF in pure Python with no Blender, while the human GLBs are KHR-quantised and meshopt-reordered (see `human-variation.js` and the skin notes), so posing and baking them needs either a Python GLB skin-and-bake step or a Blender bake (set `needs_bake` if so). Update the monument's liberty in `docs/LIBERTIES.md` to say the figures stand on the people rigs, and every figure still has to read as Rohl-Smith's sculpture in each match record ("no generic stand-ins").
