---
id: T-3683
title: 1871 city is mostly wood frame: fewer brick and stone stand-ins outside downtown, frame houses that read as painted clapboard
state: review
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: null
pr: 2220
claimed_by: run 11/19/2026, 10:08:20 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T16:08:21.768Z
decision: null
decision_answer: null
---

1871 city is mostly wood frame: fewer brick and stone stand-ins outside downtown, frame houses that read as painted clapboard.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Outside the central business district, the generic 1871 stand-ins are overwhelmingly wood frame: West Side and outer settlement at least 90% frame, North Side and mixed neighbourhoods at least 80%, the affluent South Side still mixed. Downtown stays masonry. Citywide, frame is well above two-thirds of buildings.
- Every footprint stays where it is (only the building type and facade change), so no street, bridge, quay or walk moves.
- Frame houses read as painted or weathered clapboard, not as cream stone: lighter, narrower weatherboards and a varied paint per house. A two-storey frame shop replaces the brick shop block outside downtown.
- The sources are recorded on the kit (Colbert & Chamberlin 1871 on the burned West Side being nearly all frame; the U.S. Census Bureau on up to 90% of people living in frame houses; Murphy on more than two-thirds of structures being wood), and the paint colours are recorded as a reconstruction in LIBERTIES.md.
- Before/after pictures, desktop and phone, inline in the PR. Gate green, merged to dev.

## Owner request

Kevin, 2026-11-19, looking at the 1871 baseline on the dev preview: "in looking at it i was surprised to see so many brick and apparently stone surfaces among all of the buildings in 1871".

Measured on dev (data/context/1871.json): by count 62% of the main buildings were frame (68% with yard stables), but West Side 33% brick, North Side 40%, mixed neighbourhoods 50%, river 67%; and the frame wall colour (180,168,139) is almost the stone colour (181,163,132), so frame houses read as stone.

## Result (PR #2220)

Masonry stand-ins fell from 10,770 to 2,942 of 33,580 footprints (about one house or shop in ten, matching Colbert and Chamberlin's 1868 count of 35,654 wooden to 3,712 brick and stone). Downtown stays masonry, and no footprint moved. Frame houses are pale weatherboard with a per-house reconstructed paint, and a new two-storey frame store form serves the neighbourhood shops.

West Side from 60 m, desktop (before | after)
<img src="https://github.com/kevinrhaas/chicago-evidence/blob/0c0e92407e1e63e5c9c6541898ededd00322ca71/evidence/t3683-1871-materials/desktop-west-side-low-aerial-before-after.jpg?raw=true" width="900">

City from 450 m, desktop
<img src="https://github.com/kevinrhaas/chicago-evidence/blob/0c0e92407e1e63e5c9c6541898ededd00322ca71/evidence/t3683-1871-materials/desktop-city-aerial-before-after.jpg?raw=true" width="900">

North Side street, desktop
<img src="https://github.com/kevinrhaas/chicago-evidence/blob/0c0e92407e1e63e5c9c6541898ededd00322ca71/evidence/t3683-1871-materials/desktop-north-side-street-before-after.jpg?raw=true" width="900">

Phone, West Side from 60 m
<img src="https://github.com/kevinrhaas/chicago-evidence/blob/0c0e92407e1e63e5c9c6541898ededd00322ca71/evidence/t3683-1871-materials/phone-west-side-low-aerial-before-after.jpg?raw=true" width="400">
