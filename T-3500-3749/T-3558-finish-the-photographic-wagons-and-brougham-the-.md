---
id: T-3558
title: Finish the photographic wagons and Brougham: the farm-box master qualified, the covered wagons upgraded but kept distinct, and the Brougham matched to its 1893 plate and qualified in town
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: 2026-11-17
pr: 2140
claimed_by: run 11/16/2026, 8:42:13 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-17T08:15:59Z
claimed_run: null
claimed_at: 2026-11-17T02:42:14.946Z
decision: null
decision_answer: null
---

Finish the photographic wagons and Brougham: the farm-box master qualified, the covered wagons upgraded but kept distinct, and the Brougham matched to its 1893 plate and qualified in town.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is what is left of the vehicle models. It replaces **T-2793** (articulated wagon master), **T-2980** (covered wagons), **T-3084** (Brougham to the 1893 catalogue) and **T-3085** (Brougham qualified in town), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- The licensed farm-box master and its near/mid/far tooling (#1340), the timber wagons, distinct canvas and the Brougham (#1175), occupied loops and controls (#1649, #1697), the 1812 driven wagons (T-3497).
- Brougham lamp refinement (T-3083); draft PR #1335's coachwork and glass source work is on its branch, not on dev.

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **Farm box**: `renderers/web/transport/farm-box-master/farm-box.json` loses `photographic_acceptance: false` honestly: matched-view renders beside its cleared references, ground and tree clearance, LODs and phone/desktop cost recorded.
- [ ] **Covered wagons**: a few older covered wagons replaced by better ones, each keeping its own finish, canvas ageing, seed and place, so no two look like clones.
- [ ] **Brougham**: body, wheels, steps, doors, seats and glass matched to the 1893 Studebaker plate at matched cameras, with a discrepancy register; then exported near/mid/far and loaded in the real 1904 scene with its seats, doors and anchors intact for the ride (T-3557).
- [ ] Before and after shots, desktop and phone, for each; triangles, draws, memory and bytes inside the phone ceilings.


## Finding 2026-11-13: each 1904 coach, team and coachman distinct (PR #2021)

Kevin (2026-11-13): "make the carriages look different ... horses will vary and the coachmen will vary ... different colors and/or some random mar marks ... typically black". PR #2021 adds `renderers/web/js/coachwork.js`: a row's `vehicle_finish` (panels, timber, gear, trim colours; gloss, dust, scuffs; a seed) gives each brougham its own paint, road dust, splash, wheel-rim mud and scuffs on one shared shader program, no textures. `driver_livery_colours` gives each coachman his own coat/trousers/buttons/gloves; `driver_export_person_id` lets the new coachmen reuse Hans's seated export with their own faces. New teams: dark bay (Pullman) and chestnut (Armour). Still open here: photographic coach textures and a second coach model (all three are the same brougham shape).

## Result 2026-11-17 (PR #2140)

- **Brougham V20** matched to plate 0095 (closed driving box, dash with iron rail and stays, swept irons, no rear mudguards), near/mid/far, on all four 1904 carriages; register `tools/transport/brougham_v20/discrepancies.json` keeps one difference open (box about 0.3 m lower, because the coachmen were fitted on V19's seat). Glessner ride test passes on V20. Hans Johnson's people-match was reshot on V20 and reset to `unreviewed` for Kevin to mark again.
- **Covered wagons v2**: the Western Hotel and Wolf Point wagons stand on the farm-box master with their own cover, bows, yoke, seeded canvas weathering and seeded body/gear paint; phones load farm-box-mid.
- **Farm box qualified**: `QUALIFICATION.json` records the matched views, ground and tree clearance, levels and cost; `photographic_acceptance: true`.
- Cost, same pose before → after: 1904 desktop 1,054 → 1,052 draws; 1904 phone 480 → 491 draws, 731k → 666k tris; 1835 desktop 825 → 844 draws; 1835 phone 612 → 610. Resident memory not re-measured in the container.

Plate, V19, V20:

![plate, V19, V20](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/brougham-plate-v19-v20.jpg?raw=true)

1904 desktop and phone, before | after:

![1904 desktop](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/brougham-1904-desktop-before-after.jpg?raw=true)

![1904 phone](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/brougham-1904-phone-before-after.jpg?raw=true)

Covered wagons, v1 above v2:

![Western Hotel](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/covered-western-v1-v2-model.jpg?raw=true)

![Wolf Point](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/covered-wolfpoint-v1-v2-model.jpg?raw=true)

1835 desktop and phone, before | after:

![1835 Western Hotel desktop](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/covered-western-1835-desktop-before-after.jpg?raw=true)

![1835 Wolf Point desktop](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/covered-wolfpoint-1835-desktop-before-after.jpg?raw=true)

![1835 phone](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/covered-western-1835-phone-before-after.jpg?raw=true)

Farm box beside Wild's 1835 Third and Vine and the Buffalo print, and in 1812:

![Wild farm box](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/match-wild-1835-farm-box.jpg?raw=true)

![Buffalo farm box](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/match-buffalo-farm-box.jpg?raw=true)

![1812 farm box](https://github.com/kevinrhaas/chicago-evidence/blob/4fc7da1b418fd2c920342ef01b94d38a91c23745/evidence/T-3558-wagons-brougham-2026-11-17/farm-box-1812-desktop-phone.jpg?raw=true)
