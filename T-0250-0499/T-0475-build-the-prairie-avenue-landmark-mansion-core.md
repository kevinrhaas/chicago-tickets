---
id: T-0475
title: Build the 1904 Prairie Avenue landmark mansion core
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

Add the highest-evidence, most visually important Prairie Avenue residences present on the chosen 1880s scene date as individually researched structures rather than generic mansion archetypes. Start with surviving or exceptionally well-documented houses such as the Glessner House and Clarke House when the selected date includes them, then include other major documented residences whose construction predates the scene.

For each structure, establish construction/alteration dates, architect where known, period address/lot, footprint, height/stories, roof form, primary materials, setbacks, carriage/service buildings and photo/map sources. A house built after the selected scene date belongs in exclusions or a later phase, not in the scene.

Research starting points: Glessner House research collections; Chicago Landmarks documentation; National Register/Prairie Avenue historic-district material; Art Institute/Ryerson & Burnham architectural collections; Chicago History Museum photographs and atlases.

Acceptance: the first landmark batch is visibly recognizable from period sources, correctly dated and placed, each attribute is tiered, no post-date mansion leaks in, and the run that closes this ticket files the next landmark-batch ticket if documented high-priority houses remain.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket (1904 landmark core):** on sheet 28, **1800 Prairie** (SW corner at 18th) is drawn in stone (blue) with its courtyard plan and coach house, which is the Glessner House (HABS record `habs_glessner_house_il_1015` is already committed). **1801 Prairie** opposite is also stone. Check every candidate's construction date against 1904: a house built after 1904 is excluded, and the 1911 sheet alone never proves a building stood in 1904. **The Clarke House is believed to have stood at 45th and Wabash in 1904** (moved 1872, returned to Prairie Avenue only in 1977). Verify that against a source before relying on it; if it holds, the Clarke House is not in a 1904 corridor.
