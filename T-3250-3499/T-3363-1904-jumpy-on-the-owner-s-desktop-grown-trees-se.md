---
id: T-3363
title: 1904 jumpy on the owner's desktop: grown trees send one draw per tree, Light's building cells one per cell
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-03
closed: null
pr: 1689
claimed_by: run 11/3/2026, 4:01:19 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-03T22:01:20.758Z
decision: null
decision_answer: null
---

1904 jumpy on the owner's desktop: grown trees send one draw per tree, Light's building cells one per cell.

The owner, 2026-11-03, on his Mac desktop (Chrome 156, 1381x819 at ratio 1.1, Scene detail Light, Sharpness Low), Read frame pacing in 1904: walk 65-90 ms mean with ~5,000 driver draws, turn 35-48 ms, flight 141-157 ms with ~5,300 draws; Adaptive did not help ("1904 seems a bit jumpy"). He asked whether Light skips something the GPU does.

Measured (tools/measure_pose_draws.mjs, his viewport, dev's published data): at the flight pose Full sends 4,583 GL draws, 2,028 of them the parkway elms (2 % of the triangles: one multi-draw entry per tree, wood and leaves, view and sun); Light sends 4,192, 4,076 of them structures (Light cuts every 1904 structure into 4 m x 2 m cells for Glessner's inspection model, T-2219, and one blended batch alone is 1,215 draws for 13k triangles).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- Grown-tree batches (street elms, front yards, 1835/1812 timber) draw every copy of one template as one instanced multi-draw entry; the stems drawn, their per-stem cull in view and sun, matrices and dissolve are unchanged; renderer.info triangles still count every instance.
- Light's structure cells send fewer draws at the flight and walk poses where that does not change what is drawn.
- Driver draws before/after at the owner's viewport (walk, turn, flight; Light and Full) recorded in docs/measurements, with screenshots showing no visible change.
