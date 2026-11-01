---
id: T-3289
title: K08: a segmental bow's cone is wound inward and culled from above — fix the quad path in _cone and rebake the bow-capped houses
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-01
closed: 2026-11-01
pr: 1563
claimed_by: run 11/1/2026, 3:07:31 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-01T11:02:02Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41290799363
claimed_at: 2026-11-01T09:07:31.667Z
decision: null
decision_answer: null
---

K08: a segmental bow's cone is wound inward and culled from above — fix the quad path in _cone and rebake the bow-capped houses.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Found by T-3288 (2026-11-01)

`generators/archetypes/k08_bays.py` `Bay._cone` builds a bow's cone two ways. Where the bow is a full
half round (its centre exactly on the wall plane, `cz == 0`) every slice is a triangle from the apex,
`add_poly(pr, [q[0], q[3], q[2]][::-1], …)`, and those are wound outward. Where the bow is SEGMENTAL
(`rise_m < chord_m / 2`, centre behind the wall) every slice is a quad,
`add_poly(pr, q[::-1], …)`, whose ring edge runs the other way: wound INWARD, against the normals the
kit writes. The renderer culls back faces, so such a cone is invisible from above and seen from below
as its underside.

Measured on the committed GLBs (triangles whose geometric normal agrees with the stored normal):
1721 Prairie's bow caps 2 agree / 122 disagree; 1600 Prairie's half-round bow 48 / 0; 1912's tower 48 / 0.
A trial 1912 turret on a segmental bow (chord 2.0, rise 0.8, pitch 2.8) drew no cone at all; T-3288
built its turret as an exact half round (chord 1.8 → 1.4, rise half of it) to stay on the correct path.
Note `cz` must be exactly 0: chord 1.6 / rise 0.8 computes `cz = -1.1e-16` and takes the quad path.

Bow cones on the quad path today (record, bay, pitch): 1721 north_bow / south_bow 0.05; 1619 front_swell
0.05; 1621 front_swell 0.05; 1801 sw_round, front_bow, flank_round, gable_oriel 0.05; 1637 north_swell
0.05; 1808 south_front_bow 0; 1828 south_round 0; 1905 south_conservatory 0.0 (pitch 0 caps may be flat
roofs whose winding matters only from above).

**Acceptance:** `_cone`'s quad slices wound outward (and the `cz` test made tolerant of rounding);
`tools/check_bay_kit.py` asserting every roof face's winding against its normal; the affected K01
houses re-emitted, their derivatives rebuilt, and each photo-gated house's views re-run with
`photo_match.mjs` (their GLB hashes move).
