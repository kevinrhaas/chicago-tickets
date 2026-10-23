---
id: T-3065
title: Glessner's 18th Street stack reads about 8.7 px wider than Taylor 2135 through T-3058's camera (found by T-3058): with the principal point free and the stacks' centres fitted, the south and middle stacks' widths match the photograph within 0.4 px but the north stack's record box (W 15.25-22.35, T-2873's 7.1 ft from HABS 14) is 8.7 px wider than the photograph's 74 px, and the render's 1886 device and cross stand proud past the photograph's right edge; read the stack's E-W depth and the device's projection against HABS 14 and Taylor 2135 together and rule or rebuild
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-23
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Glessner's 18th Street stack reads about 8.7 px wider than Taylor 2135 through T-3058's camera (found by T-3058): with the principal point free and the stacks' centres fitted, the south and middle stacks' widths match the photograph within 0.4 px but the north stack's record box (W 15.25-22.35, T-2873's 7.1 ft from HABS 14) is 8.7 px wider than the photograph's 74 px, and the render's 1886 device and cross stand proud past the photograph's right edge; read the stack's E-W depth and the device's projection against HABS 14 and Taylor 2135 together and rule or rebuild.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Released 2026-10-23** (claim of run 10/23/2026, 10:09:52 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/39974840069): Readings taken, not finished: a rebuild needs a full Glessner rebake and does not fit beside T-3058's camera. Through T-3058's camera (PR on branch steward/t3065-t3058-glessner-north-stack-taylor-camera), the north stack's box is 82.6 px across against the photograph's 74 (picks) / about 77 (rows 200-216). Magnified, the photograph's NE corner (where the courses change direction) stands at x ~1035: east face 991-1035 = 44 px (3.14 ft at the built 14 px/ft, so sheet 6's 3.1-ft N-S depth stands); north face 1035-1068 = 34 px against the built 39 (5.5 px/ft), about 6.2 ft against T-2873's 7.1. A first look at HABS 17's side-by-side (also from the NE) agrees: north face ~18 px against the render's ~23, east face ~30 against ~29; HABS 01 read ~6.3 (T-2873). HABS 14, square to the face, still reads 127 px against the render's 128 at the cap row, so the frontal view and the three obliques disagree, and a plain box cannot satisfy both: narrowing to ~6.2 ft breaks HABS 14 by ~16 px. Next: check HABS 14's scale at the stack (its camera is solved on the wall plane; the stack top is 15 m up at the frame's top) and whether the face has a step or chamfer at its east end that a frontal view sees full-width; the GLB also reads ~7 px wider than the box on the east side 0.5-1.0 m below the cap (read_caps.py with DROP 1.0), i.e. the shaft's rock faces. Device: the render's right-hand cross stands proud past the photograph's edge; HABS 14 shows the crosses incised, not raised.
