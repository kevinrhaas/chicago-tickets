---
id: T-0476
title: Fill the 1904 Prairie Avenue corridor with documented residences and outbuildings
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
blocked_on: T-0475
needs_bake: true
---

After the landmark core, populate the rest of the chosen 1880s Prairie Avenue corridor with the documented residences, carriage houses, stables, fences and other parcel structures visible in period atlases/fire-insurance maps. The goal is a historically dense residential district, not a few isolated hero houses in empty blocks.

Use a one-run batch sized to the available evidence and geometry budget. Where a footprint is documented but architecture is not, build a period-bounded reconstructed massing and label it honestly rather than omitting the building. Preserve parcel-level distinctions between documented, inferred and reconstructed components.

Acceptance: one coherent multi-parcel batch visibly increases the corridor's density; every added structure is dated to the chosen scene and tied to a parcel/source; reconstructed forms carry their liberty; and closing this ticket creates the next corridor-infill batch if the period map still contains unbuilt occupied parcels.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket (1904 corridor infill):** every dwelling, barn, stable, green house and garage on sheets 20, 28 and 35 is a footprint candidate, with material from the key's colours and stories from the sheet ("2B", "3SB"). Two corrections to 1911: **1609–1611** are two rowhouses in 1904 (Robinson outlines), not the 1911 commercial building; **1620** has a house in 1904 (Robinson outline), not the 1911 empty lot. **The 1911 "Garage" labels:** rule each one as a 1904 carriage house or stable, or as a post-1904 build, in writing. A 1911 motor garage is not built into 1904 by default.
