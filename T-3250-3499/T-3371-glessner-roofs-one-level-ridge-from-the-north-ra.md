---
id: T-3371
title: Glessner roofs: one level ridge from the north range into the stable cupola, alley gable sat on its roof
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-04
closed: null
pr: 1711
claimed_by: run 11/4/2026, 11:19:43 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-11-05T05:19:45.095Z
decision: null
decision_answer: null
---

Glessner roofs: one level ridge from the north range into the stable cupola, alley gable sat on its roof.

Owner, 2026-11-05 (thread "Correct Glessner roofs and window stone"), with marked Google Earth and in-app screenshots: "Please create multiple tickets as needed for this and work through these as a priority #1 ... don't over correct to the google earth images given they are of lower quality". HABS drawings and archival photographs govern; Google Earth shows the roof lines. Four tickets, grouped by what moves together, chained one at a time (same Glessner bake): T-3371 -> T-3372 -> T-3373 -> T-3374.

## The ask (items 1, 6, 7 and the east-wing check)

1. North wing ridge too low: on Google Earth it runs level into the stable's cupola with the ridge west of it; the model steps 2.07 ft (north range 34.1 ft ng at S 14.6, stable cross ridge 36.17 at S 12.31).
6. West (alley) face: the model's stone gable stands as a tall fin over the roof.
7. The elevation difference between the west and east parts of that ridge (same step as item 1).
East wing ridge "seems tall": validate it.

## Evidence read before working

- HABS photograph 1 (1963), camera-free: the north range's cresting and the stable cross ridge's cresting lie on one straight line in the print (cross crest 4 px off the north crest's extension over 260-420 px); the model's render puts the cross ridge 36-42 px above that line. Two ridges on one line at about the same plan line are one height.
- HABS 1, eave-to-roll gap on the north range at the same columns, print over render: 103/97 and 120/104 px, so the print's ridge stands about 0.7-1.7 ft over the built 34.1 ft.
- HABS sheet 4 (section at W 51.3) draws the north range ridge 11.0 ft over its north eave (34.1 ft ng). The ruling departs from it by 2.07 ft on the two photographs and the owner's direction; recorded as a liberty.
- The alley gable IS stone: HABS photograph 1 and the c. 1887 Cornell print both show a stone gable on the alley face. Both draw its coping apex barely over the cresting; the model's wall line apex (38.6 ft) stands 2.4 ft over the 36.17-ft cross ridge, so its coping reads as a fin.
- East wing ridge 45.7 ft door: sheet 6 (photogrammetric), Taylor 2135 (1887-89), HABS 16 and 17 all match the built ridge; no change.

**Acceptance:**
- `ridge_north_range.ridge` is 36.17 ft ng at S 14.6 (the stable cross ridge's height), eaves unchanged (north 23.1, courtyard 25.63 at the wall, overhang edge 24.0); the ridge meets the cupola level from both sides.
- The alley gable stays stone; its wall-line apex comes down to the cross ridge (36.17 at S 12.31) so the coping stands about 1 ft over the roof, as on the stable's 18th Street gable.
- East wing ridge unchanged, with the validation written into its record.
- Glessner rebaked; k01_contract, opening schedule and source-use regenerated; every Glessner match record re-rendered with no verdict worse; gate green.
- Before/after renders from the owner's Google Earth and in-app viewpoints posted in the thread.
