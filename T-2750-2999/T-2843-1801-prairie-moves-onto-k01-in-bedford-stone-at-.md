---
id: T-2843
title: 1801 Prairie moves onto K01 in Bedford stone at T-2538's massing (after the two kit pieces before it): the main block's mansard, the south pavilion and the flank section on K08 projections, the round tower on a K08 tower on the north wall, the gabled section and east range as roofed K01 wings, the north-east turret on the east range, compared with the draft from the Taylor camera, the draft builder's copy retired
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2789
opened: 2026-10-19
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

1801 Prairie moves onto K01 in Bedford stone at T-2538's massing (after the two kit pieces before it): the main block's mansard, the south pavilion and the flank section on K08 projections, the round tower on a K08 tower on the north wall, the gabled section and east range as roofed K01 wings, the north-east turret on the east range, compared with the draft from the Taylor camera, the draft builder's copy retired.

Piece 3 of 3 of **T-2789 — 1801 Prairie moves onto K01 in Bedford stone at T-2538's massing: the main block, south pavilion, flank section, gabled section and east range, its round tower and north-east turret on K08 towers with their cones over the main roof, compared with the draft from the Taylor camera, the draft builder's copy retired**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2789 was split (2026-10-19T07:51:49.196Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 10/19/2026, 2:48:34 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39217831963) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39217831963) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Found when T-2789 was sized (2026-10-19, the run that split it)

T-2789 was claimed as an S and turned out to need kit that does not exist, so it was split before any code was written. What stands in the way, read in `generators/archetypes/k01_frontage_params.py` on dev at 5a06b89c5:

- `_rear_wings` refuses any wing roof but `flat` ("a K01 wing is decked flat"). The draft's r3 (u -8.5..0, v 0.5..5.5, three storeys, hipped, apex about 16.3 m in the Taylor print) and r2 (u -17..-8.5, v 0..17.25, two storeys, hipped, eaves about 8.2 m) cannot be laid as flat decks without a regression the Taylor camera shows: the gabled section on the flank is one of the photograph's main masses. T-2841 is that kit.
- `rear_section` (1625's) stands only beside a hipped main roof, and 1801's main block is a mansard, so it is not the route.
- `_bays` places K08 bays and towers on the main walls only; the north-east turret (draft feature at u -16.6, v 0.7, r 1.3 m, eaves 8.0 m, cone to 12.7 m) stands on r2's north wall. T-2842 is that kit.
- What K01 already does for this house: `construction: "stone"` (T-2788, the all-stone house; `coleman_ames_house_1811_prairie` is one of its fixtures), a mansard main roof (1637 is the template, `mansard.variant` k05.roof.mansard_convex), K08 `projection.full_height` bays on the street front (1812's `south_projection` is the template for p_south) and on a side wall (p_flank), and a K08 tower on `k01.wall.side.north` past the eave (T-2787; `tools/test_k01_tower.py` builds one on 1637's mansard). The tower's draft numbers: axis u 12.6, 1.1 m proud of the north wall, r 1.45 m, eaves 12.9 m, cone 5.8 m to 18.7 m.
- Still open: K08's projection roofs are hip, cone or spire. The south pavilion's coped stone gable (apex about 17 m) has no K08 roof yet; carry it hipped with a liberty and leave the gable to T-2540, or extend K08.
- Template commits: T-2543 (#855, 1812 Prairie draft → K01 in place under the draft's id: the draft register's skip line, the match record re-rendered, the old `__draft_1904.glb` removed).
