---
id: T-1252
title: Generate and bake the e1871_postfire heightfield over the Prairie Avenue reach
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-0473
opened: 2026-09-17
closed: null
pr: null
claimed_by: run 9/28/2026, 1:04:43 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-28T18:04:43.827Z
decision: null
decision_answer: null
---

Generate and bake the e1871_postfire heightfield over the Prairie Avenue reach.

Piece 4 of 4 of **T-0473 — Create an 1880s South Side terrain and urban-ground epoch**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Settled upstream by T-1249, and binding here:** the scene stands at **1 July 1888** on
`e1871_postfire`. This ticket carries the scene file, which T-1249 deliberately did not write —
a scene must stand on a heightfield and there was none.

1. Generate `data/terrain/epochs/e1871_postfire/heightfield.json` + `.bin` from T-1251's spec,
   over a reach that covers Prairie Avenue — the 1835 box already reaches Cermak Road at local
   N -3800, which is the extent an 1880s Prairie Avenue scene needs.
2. **Bake** (`./tools/bake.sh`), because ground geometry moves. `validate.py --stale` hard-fails a
   record that stops matching its committed mesh, so the bake is in the same commit.
3. Write `data/scenes/1888.json`: `target_date: "1888-07-01"`, `terrain_epoch: "e1871_postfire"`,
   its **own** anchors — the 1835 scene's anchors are not inherited, which is the mechanism that
   keeps an 1880s mansion out of an 1812 label — and lighting for 1 July at this latitude.
4. `tools/measure_anchors.mjs` holds every new anchor against the heightfield it stands on, the
   ground-contact and publish gates pass for the second epoch, and the frame budget is measured
   before the push.

**Sized as more than the other three pieces.** If the bake plus a measured before/after does not
fit in one run, `ticket.mjs split` it rather than shipping a self-invented half.

## Owner ruling, 2026-09-26: Prairie Avenue is centred on 1904

The owner, working with Glessner House, set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket:** write the Prairie Avenue scene as **`data/scenes/1904.json`** (`target_date: "1904-07-01"` unless argued otherwise), on `e1871_postfire`, with its own anchors and 1 July lighting. `1888.json` is not required. If a run finds the 1888 scene already written, it may stay, and the Prairie Avenue content targets 1904.

## Owner, 2026-09-28: the Prairie Avenue 1904 research library is a source here

The research library committed with T-1633 (#82), **`chicago/prairie_1904_v1/`**, can be browsed at
**https://chicago.polecat.live/prairie-1904/viewer/** (dev mirror `/4d/dev/prairie-1904/viewer/`).
Read its `README.md` and `docs/research-gaps.md` before starting. It holds `data/buildings.csv`,
`building_events.csv`, `assertions.csv`, `sources.csv`, `map_frontages.csv` (1911 frontage
readings, 91 of them still tentative), `measurements.csv` and `address_crosswalk.csv`; the five
original map JPEGs with checksums under `maps/originals/`; and dossiers under `research/`
(`glessner-dossier.json`, `glessner-chronology-supplement.json`, `civic-dossier.json`,
`dimensional-claims.json`, `map-inventory.json`). It **supports** this ticket and does not close
its acceptance. A tentative reading stays tentative until this ticket resolves it against the
sheets, and every value taken from the library cites the library row or dossier entry it came from.

**For this ticket: where a visitor lands (owner, 2026-09-28).** The 1904 scene's **spawn** stands on
Prairie Avenue at E. 18th Street, at eye height on the east sidewalk, **facing the south-west corner
lot, 1800 Prairie**, where the Glessner House stands (Sanborn 1911 sheet 28; library
`glessner-dossier.json`). So `/4d/1904/` and `/4d/dev/1904/` open looking at that ground. The scene
also carries a named anchor **`glessner_house`** at the same pose (`?year=1904&anchor=glessner_house`).
The house itself belongs to T-1729; the view is this ticket's.

**Added acceptance:** loading `/4d/dev/1904/` at 390×780 and at 1280×800 lands facing the 1800 Prairie
lot, held by a smoke assertion on the spawn bearing and the lot centroid's screen position.
