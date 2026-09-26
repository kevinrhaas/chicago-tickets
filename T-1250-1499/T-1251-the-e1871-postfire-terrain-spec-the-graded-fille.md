---
id: T-1251
title: The e1871_postfire terrain spec: the graded, filled and raised South Side ground as an authored zone table
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

The e1871_postfire terrain spec: the graded, filled and raised South Side ground as an authored zone table.

Piece 3 of 4 of **T-0473 — Create an 1880s South Side terrain and urban-ground epoch**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Settled upstream by T-1249, and binding here:** the epoch's representative date is
**1 July 1888**, and `e1871_postfire.layer_status.terrain_spec` names this ticket as owing the
zone table.

1. An authored zone table at `data/terrain/epochs/e1871_postfire/terrain_spec.json` in the shape
   `e1834_harbor_cut`'s already uses, **every elevation citing a numbered zone in a research
   doc** — graded street crowns, the sewer-era fill, the railroad earthworks, the made ground
   along the lake, and the original prairie surface where it still shows.
2. The relationship to the 1835 surface is stated as a claim and not assumed: the grade raise of
   the 1850s–60s buried that ground, so the two epochs' heightfields are **not** offsets of one
   another, and anywhere this ticket cannot source a depth it says `conjectural` and says why.
3. An `evidence_limit` of its own. The 1835 spec carries one at local N -2149.4 because no source
   it holds describes the land below Twelfth Street; this epoch's limit will fall somewhere else
   and must be derived, not inherited.
4. `tools/check.sh` green, with the spec's own re-derivation gated the way the 1835 one is.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket:** the zone table must serve a **1904** scene. The epoch id `e1871_postfire` may stay, since it names the post-fire grade, not the scene year. Where the ground at 1904 differs from 1888 (lakefront fill, the IC embankment, street grades), say which date each zone describes.
