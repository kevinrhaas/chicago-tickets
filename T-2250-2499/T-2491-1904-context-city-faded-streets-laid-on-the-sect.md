---
id: T-2491
title: 1904 context city: faded streets laid on the section grid and the city carried out to the haze's reach
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-13
pr: 788
claimed_by: run 10/13/2026, 2:28:19 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-13T21:29:18Z
claimed_run: null
claimed_at: 2026-10-13T19:28:19.740Z
decision: null
decision_answer: null
---

1904 context city: faded streets laid on the section grid and the city carried out to the haze's reach.

Owner, 2026-10-13 19:22 UTC, thread "Faded placeholder city around Prairie Ave", after seeing T-2477: "we should have some streets where they should be based on maps, you can continue it to the end of the visible map based on your analysis and then render appropriate continued to the end of the city publishes map land area".

**Acceptance:**
1. The 1904 context layer draws faded streets (carriageways, desaturated like the stand-ins) for the city's grid as far as the city reaches. They're placed from what is in hand: the school-section corners (State, Halsted, Madison, Roosevelt), the OSM crossings already committed for 16th, 18th, 21st and Cermak at Indiana, Prairie and Calumet, and Michigan at 16th. Streets between those anchors are laid at the pitch the anchors give, and that fill is a recorded liberty. No faded street overlaps a carriageway, alley or parcel of `data/street_grid/1904.json`, and the build tool's `--check` refuses one that does.
2. The stand-in city is carried out to the haze's reach (the distance at which the 1904 fog is total, read from `world.js`) past the modelled box on every land side. Nothing is drawn on water.
3. Land use is appropriate rather than one residential pattern everywhere. Robinson 1886 plate 10 (already georeferenced) is traced where it reaches north of 16th Street: its buildings stand, and its Illinois Central yard stays clear of projected houses. Any other zone (business blocks, railway lands) is recorded as a liberty with its reasoning and how to resolve it.
4. Phone (390×780, light detail): boot peak memory no more than 25 MB over the T-2477 build, triangles and draw calls within budget. Desktop stays under its triangle budget.
5. The liberty is recorded in docs/LIBERTIES.md, the gate is green, and the 1904 smoke passes on phone and desktop.
