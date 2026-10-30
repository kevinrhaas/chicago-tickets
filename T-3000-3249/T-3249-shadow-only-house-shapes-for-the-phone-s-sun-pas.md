---
id: T-3249
title: Shadow-only house shapes for the phone's sun pass: simplified casters made at bake time
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-29
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Owner, 2026-10-30 (project thread "Assess other 3D project for reuse"), answering whether to file it: *"sure simpler shadow-only house shapes"*. Follows T-3247 (PR 1460), where the owner chose to aim the phone speed-up at the railway and the sun's shadow pass.

**What was measured (T-3247, 1904, phone 390x780, `light`, stand 1801 Prairie looking south).** Frame 1,670,535 triangles, of which the sun's shadow pass is 633,756. Structures are 591,979 of that: 366 casters, each at its full rendered detail, inside the `light` shadow box (+-120 m, 1024 map, about 23 cm a texel). Street trees are 34,168 and the street grid 7,510. `castersTowardView` (T-2529) already drops casters whose shadow cannot reach the view, so what is left is the houses whose shadows are on screen. At 23 cm a texel, cornices, window reveals, mullions, sash and carved trim are below the shadow map's resolution: they cost triangles in the pass and change no texel.

**What:** at bake time, give each building GLB a shadow-caster stand-in: its walls, roofs, towers, chimneys, porches and stairs as closed simplified solids, with detail smaller than about a shadow texel removed. At `light`, the sun's pass draws the stand-in and the colour pass draws the building as now. `full` and `balanced` are unchanged unless measured as a free win. The stand-in is not visible and is not a level of detail of the picture.

**Acceptance:**
- At the T-3247 stands (south from 1801, Prairie & 18th, lakeside, air over Indiana Ave), the `light` sun pass's structure triangles fall by at least half. Report before and after per stand.
- Shadows on screen agree with the full casters at those stands. Report the pixel difference with shadows from the stand-ins against shadows from the full models, and show the pictures. No missing or floating shadow edges at eaves, towers or porches.
- Phone memory stays inside `tools/memory_ceilings.json` for every year. Read it with `measure_memory.mjs --only mobile`. Stand-ins that cost more than they save in memory are a fail.
- No shadow acne (`tools/check_shadow_bias.mjs`, T-3054) and no light leaks at wall and roof joins.
- Gate green; smoke by parts on the structures and shadow parts, both viewports.
- The bake contract, manifests and derivative checks (K36 to K39) cover the new stand-ins.
