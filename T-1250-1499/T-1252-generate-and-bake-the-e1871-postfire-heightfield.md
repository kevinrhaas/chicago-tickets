---
id: T-1252
title: Generate and bake the e1871_postfire heightfield over the Prairie Avenue reach
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

The owner, working with Glessner House (William Tyre), set **1904** as the year of the Prairie Avenue model. This supersedes the "1880s" framing and T-1249's 1 July 1888 date *for the Prairie Avenue scene*. T-1249's epoch record and `data/terrain/1880s_scene_date_constraints.json` may stay as they are; the owner said "you can leave the 1888 scene if you need to". Nothing here needs to delete them, but nothing Prairie Avenue builds is dated 1888. The scene date defaults to **1904-07-01** (the project's day-of-year convention, as 1835-07-01); a run may argue another day in writing.

**Sources, committed at `chicago/reference/prairie-avenue/sanborn-1911-and-robinson-1886/`** (read its README first): the Sanborn **1911** Chicago vol. 3 **key** and **sheets 20, 28 and 35** (E. 16th to E. 22nd St., Indiana Av. to the IC tracks and Lake Michigan), and **Robinson's 1886 atlas, plate 10** (16th to 18th St.). Glessner House's reading is that on these sheets only two things changed between 1904 and 1911: **1609–1611 Prairie** (two rowhouses in 1904, a commercial building by 1911) and **1620 Prairie** (a house in 1904, an empty lot by 1911). For both, the 1886 Robinson outlines stand in. Each ticket that spends a sheet writes its own `data/sources/*.json` record, in the house format, before citing it.

**For this ticket:** write the Prairie Avenue scene as **`data/scenes/1904.json`** (`target_date: "1904-07-01"` unless argued otherwise), on `e1871_postfire`, with its own anchors and 1 July lighting. `1888.json` is not required. If a run finds the 1888 scene already written, it may stay, and the Prairie Avenue content targets 1904.
