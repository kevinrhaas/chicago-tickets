---
id: T-2050
title: Seat the first fort in the 1812 scene with the factor's house, gardens and outbuildings the draught places, gate that the 1803 and 1816 forts never resolve into one scene, and move the 1812-only features out of exclusions-only
state: done
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-0469
opened: 2026-10-03
closed: 2026-10-04
pr: 383
claimed_by: run 10/3/2026, 10:12:49 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T05:25:48Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37173285313
claimed_at: 2026-10-04T03:12:49.201Z
decision: null
decision_answer: null
---

Seat the first fort in the 1812 scene with the factor's house, gardens and outbuildings the draught places, gate that the 1803 and 1816 forts never resolve into one scene, and move the 1812-only features out of exclusions-only.

Piece 3 of 3 of **T-0469 — Reconstruct the first Fort Dearborn complex as it stood in August 1812**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding from T-2049 (2026-10-04): the bake is this ticket's now

T-2049 wrote the first fort's fourteen records (`data/structures/first_fort_dearborn_*.json`,
PR #379) but could not bake them: `generators/build.py` builds only phases some committed
scene resolves (T-1732), and no scene resolves 1803-08-17..1812-08-16 until this ticket seats
the fort in one. So seating carries the bake: `./tools/bake.sh --only` the fourteen ids once the
1812 scene exists.

- Every record has `utm_e`/`utm_n` null and its box in the draught's own frame in
  `symbolic_location` (feet E/N of the flagstaff's foot; "east" is the sheet's right). Seating is
  one origin + one bearing for all fourteen; footprints are anchored at their own (0, 0) corner
  per GLB-CONTRACT, so each position is the box's corner after the frame's rotation.
- `tools/read_whistler_1808.py --check` refuses any scene date that resolves these records while
  no `data/scenes/1812.json` exists. Create the scene and that rule stands aside by itself.
- Two things to look at in the first bake: the palisade archetype centres a gate on its side, but
  the draught's passage is at E -11.1..-4.9 ft, about 8 ft west of the rows' centre; and the inward
  row's closed loop stands against the ranges' back walls, where the draught draws it only between
  the buildings.
