---
id: T-1250
title: Trace the Illinois Central lake edge for the 1904 Prairie Avenue scene and fill shore_1880s_ic_edge, from the Sanborn 1911 sheets and the Robinson 1886 plate
state: open
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-0473
opened: 2026-09-17
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
---

Trace the 1880s Illinois Central lake edge and fill shore_1880s_ic_edge from a sourced period sheet.

Piece 2 of 4 of **T-0473 — Create an 1880s South Side terrain and urban-ground epoch**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Settled upstream by T-1249, and binding here:** the state addresses **1 July 1888**
(`data/terrain/1880s_scene_date_constraints.json`). Trace the edge that date asks for.

1. Identify a **period sheet** that draws the lake edge, the Illinois Central corridor and the
   post-fire fill on the South Side, commit it as a source, and georeference it the way
   `rees_rucker_1849` was (GCP file, fitted affine, stated RMS). **No sheet has been identified
   yet** — that search is part of this ticket.
2. `shore_1880s_ic_edge` gets its own `geometry`, with `dated_lines` naming the sheet and the
   feature. It may not alias `shore_1835_harbor_cut` or `shore_1812_pre_cut`; a sheet of the
   wrong date **bounds** the line and does not become it, the same rule the 1849 lower bound
   already runs under.
3. **Rule on the 1852 trestle claim.** The epoch's placeholder note used to assert that "the
   Illinois Central trestle line already fixed the shore in 1852" and nothing in this corpus says
   so. T-1249 removed the sentence without deciding it. Either source it or record the refusal.
4. `tools/check_shoreline_states.py` extends to cover the new active geometry, and the 1812/1835
   separation assertions still fire.

**Retrieval notes (measured 2026-09-17, T-1249):** LOC *item* endpoints answer 200 but rate-limit
to 403 under a burst — `curl --retry 4 --retry-delay 15` recovered every time; LOC *search* with
`fo=json` answered 403 outright, so reach HABS and map records by item id. And
`www.encyclopedia.chicagohistory.org` did not resolve from the runner at all.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket:** the Sanborn 1911 sheets 20 and 28 draw the Illinois Central / Michigan Central right-of-way and the lake edge along exactly this reach. That answers "no sheet has been identified yet" for 16th–20th St. A 1911 sheet **bounds** a 1904 edge from after and Robinson 1886 bounds it from before, the rule already written above. Trace the edge the **1904** scene stands on.
