---
id: T-0477
title: Build the 1904 Prairie Avenue streetscape, vegetation and urban furniture
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
blocked_on: T-0474
needs_bake: true
---

Make the 1880s district read as an inhabited elite residential street rather than mansion models on bare lots. Add period-appropriate sidewalks, boulevard/parkway treatment where documented, street and yard trees, fences/gates, hitching infrastructure, lamps where dated, carriage drives, service access and parcel landscaping.

Use photographs, fire-insurance maps, city improvement records and surviving-house research to separate attested parcel details from reconstructed neighborhood texture. Avoid importing 1890s/World's Fair improvements into an earlier 1880s date unless the selected scene date supports them.

Acceptance: the corridor has a coherent period streetscape from at least 16th through 22nd; landscape/furniture respects parcel and street geometry; date-sensitive items have existence ranges; reconstructed texture is recorded in LIBERTIES; and the result remains distinct from both the open 1812 landscape and the sparse 1835 south prairie.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket:** "avoid importing later improvements" now means **nothing after 1904**. World's Fair-era (1893) improvements that survived to 1904 belong in the scene. The sheets give hydrants, water mains and street widths but no trees, lamps or fences: those need photographs or city records, or they are reconstructed texture recorded in LIBERTIES.
