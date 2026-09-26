---
id: T-0474
title: Reconstruct the 1904 Prairie Avenue street, parcel and service grid
state: open
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
opened: 2026-09-01
closed: null
pr: null
claimed_by: null
blocked_on: T-1252
needs_bake: true
---

Build the urban framework the mansion records must sit on: Prairie, Calumet and Michigan-area streets and the east-west tiers from roughly 16th through 22nd/Cermak, with period widths, sidewalks, alleys, lots, curbs and service access appropriate to the chosen 1880s scene date.

Derive geometry from period plats, atlases and fire-insurance maps; do not back-project today's curb lines where the period maps disagree. Include the Illinois Central/lakefront edge where it affects access or sightlines. Treat modern address numbers as cross-references, not primary period geometry.

Acceptance: each Prairie Avenue landmark ticket can cite a stable period parcel/lot and street face; major streets and alleys render on the correct terrain; lot boundaries have source/tier metadata; and the grid reaches the whole 16th-to-22nd corridor without relying on modern OSM as the historical source.

**Blocker repointed 2026-09-17 (T-1249).** T-0473 was split into T-1249 (the representative scene
date and the epoch record), T-1250 (the lake edge), T-1251 (the terrain spec) and T-1252 (the
heightfield, the bake and the scene file). This ticket's dependency was never on the parent as
such — it is on the GROUND, which is T-1252's, so `blocked_on` now names that piece. The date it
resolves against is settled: **1 July 1888**, `data/terrain/1880s_scene_date_constraints.json`.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket:** the Sanborn sheets give street widths ("66'" on Prairie Av. Blvd., Calumet, Indiana, 16th, 18th, 20th and 22nd), alleys, lot lines and **1904-era addresses** along both faces of Prairie from 16th to 22nd. Robinson plate 10 gives the subdivision and lot numbers for 16th–18th. Period geometry comes from these, not from modern OSM.
