---
id: T-3286
title: Full's far views of the Prairie district read up to 7.30 M against Glessner's 4.7 M inspection ceiling: the sun's pass draws every house whole at any distance (3.33 M of 7.30 M at Prairie 60 m E / 120 m S of Glessner, 2.0 M of it the neighbours'), so the far-view allowance T-3285 declared (7,325,000 triangles / 8,500 draws) needs a far shadow level of detail for structures to retire it
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-31
closed: 2026-10-31
pr: 1553
claimed_by: run 10/31/2026, 9:00:43 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-01T04:47:37Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41263117039
claimed_at: 2026-11-01T02:00:44.507Z
decision: null
decision_answer: null
---

Full's far views of the Prairie district read up to 7.30 M against Glessner's 4.7 M inspection ceiling: the sun's pass draws every house whole at any distance (3.33 M of 7.30 M at Prairie 60 m E / 120 m S of Glessner, 2.0 M of it the neighbours'), so the far-view allowance T-3285 declared (7,325,000 triangles / 8,500 draws) needs a far shadow level of detail for structures to retire it.

**Acceptance:** (stated 2026-11-01 before the implementation was final, by the run that claimed it)

1. Full's sun pass casts each heavy structure piece from a vertex-clustered **shadow twin** (renderer only; no GLB or contract change) wherever the twin's worst-case shadow-edge movement projects to at most 1 px at the nearest view depth the piece's shadow can land on. Nearer than that, or with the sun too low to bound the sweep, the piece casts whole. `?farshadow=0` turns it off.
2. `tools/qa_t3286_far_shadow.mjs` on the published 1904 app at Full, at 1280x800 AND 390x780, at T-3285's far stands (alley from the north, 18th 150 m W, Prairie 60 m E / 120 m S) plus the near stands as controls: the twins change at most 1 pixel in 1,000 of each held frame and at most 1 in 10,000 by more than 8 levels, never add triangles, add at most one sub-draw per twin cast, and the page raises no error. A positive control (no structure casting) has to change each frame, or the pixel count proves nothing.
3. The far-view allowance in main.js (`GLESSNER_V4_FULL_FAR_TRIANGLES` / `_DRAWS`) is re-based DOWN to the new measured worst far stand by the rule it was set with. The 4.7 M / 7,800 ceiling is not touched. Any far stand still over 4.7 M is named in the PR with what carries it; the allowance is called retired only if no stand needs it.
4. The cost is measured and said: twin count, triangles and vertices added to the GPU buffers, and the boot-time change.
