---
id: T-3096
title: Glessner's stable E-W ridge rebuilt to the ruling: the north slope kept at 42.5 degrees with its ridge brought down to about 36.5 ft over north grade and north to about S 12.3 (T-3094's first piece), the alley gable's coping standing proud over the lowered roof to its unmoved apex, the ridge's run into the cupola and the north range's skewed junction rebuilt, rebaked, and the prints' course count (41.7-43.9 and 40.6-42.9) and roll foot re-read through the measured cameras on the new GLB
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: T-3094
opened: 2026-10-23
closed: 2026-10-24
pr: 1272
claimed_by: run 10/23/2026, 11:51:05 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-24T09:43:19Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/40063665042
claimed_at: 2026-10-24T04:51:06.223Z
decision: null
decision_answer: null
---

Glessner's stable E-W ridge rebuilt to the ruling: the north slope kept at 42.5 degrees with its ridge brought down to about 36.5 ft over north grade and north to about S 12.3 (T-3094's first piece), the alley gable's coping standing proud over the lowered roof to its unmoved apex, the ridge's run into the cupola and the north range's skewed junction rebuilt, rebaked, and the prints' course count (41.7-43.9 and 40.6-42.9) and roll foot re-read through the measured cameras on the new GLB.

Piece 2 of 2 of **T-3094 — Glessner's roof slope over the stable's alley end carries about 51 courses where the early prints show about 43 (found by T-3080): the north slope of the E-W ridge from the turret to the alley gable runs 21.4 ft from its 7.65 m eave to its 12.05 m ridge at 42.5 degrees, but the Cornell c. 1887 print counts 41.7-43.9 courses between the foot of the cresting and the eave and HABS photograph 1 counts 40.6-42.9, about 17.5-18.3 ft at HABS's 5 in; through T-2758's measured-control cameras the print's eave lands on the model's (0.0-0.4 m) and the cresting's foot 0.3-1.1 m below the model's ridge; read the ridge's height and plan line, the plane's pitch and the alley gable's coping against both prints and the sheets, and rebuild the roof or rule (docs/RESEARCH/glessner-roof-slope-camera-T-3080)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3094 was split (2026-10-24T02:58:48.778Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 12m ago, run 10/23/2026, 9:46:51 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/40054619913) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/40054619913) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

Stated by T-3095 (docs/RESEARCH/glessner-stable-ridge-T-3095/README.md § 4): on the rebaked GLB, `read_slope.py` (T-3080) and `read_ridge.py` (T-3095), run unchanged, give 41-44 courses between the model's eave and roll foot on the plane over the alley end; the roll foot lies within 0.3 m of the model's in every measured-control fit and the eave within 0.4 m; the alley gable's coping stands proud of the tiles to an apex within T-2758's 38.75-40.63 ft; and no other Glessner match record gets worse. Keep the cupola on the crossing or rule where it moves; check the south slope (about 47 to 41 degrees) against the courtyard records.

**Follow T-3065 (PR #1261) rather than race it:** it rebakes the same GLB recovery package and edits the same two match records. Sized M with a bake (one structure, `bake.sh --only glessner_house`).
