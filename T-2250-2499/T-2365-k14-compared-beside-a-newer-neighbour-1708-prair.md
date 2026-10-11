---
id: T-2365
title: K14 compared beside a newer neighbour: 1708 Prairie, an empty lot on the 1886 Robinson plate, takes the kit at its own age once T-1872 stands it on K01, shown beside 1808 under the same light, front and oblique at both viewports, with costs
state: blocked-tech
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2361
opened: 2026-10-11
closed: null
pr: null
claimed_by: null
blocked_on: T-1872
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

K14 compared beside a newer neighbour: 1708 Prairie, an empty lot on the 1886 Robinson plate, takes the kit at its own age once T-1872 stands it on K01, shown beside 1808 under the same light, front and oblique at both viewports, with costs.

Piece 2 of 2 of **T-2361 — K14 compared beside a newer neighbour: the kit applied to a Prairie Avenue 1904 house built later than 1808 (1886) and shown beside it under the same light, front and oblique at both viewports, with costs**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2361 was split (2026-10-11T17:55:20.957Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 10/11/2026, 12:52:19 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38160651430) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38160651430) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding (T-2364's run, 2026-10-11): which houses are newer than 1808

Read off Robinson 1886 plate 10 (`robinson_1886_chicago_plate_10`) through its committed fit
(`data/traces/gcp/robinson_1886_plate_10_gcps.json`, 4.54 m RMS), with each structure's position
projected onto the raster:

- **1600, 1608, 1612, 1616, 1620 and 1626/1628** all have a building drawn on their lots in 1886,
  so no house now on K01 can be the newer neighbour. That is why this ticket was split.
- **1708** is an **empty lot** on the plate, between the mansion at 1700-1706 and the house at
  1712: built after 1886 and standing by 1904 (T-1840 census). It is the nearest newer neighbour
  that a K01 refinement (T-1872) will build.
- **1700 and 1706** are drawn as ONE older stone-fronted mansion in 1886; the Glessner family
  townhouses replaced it later (T-1871), so they are newer too, if T-1871 lands first.
- All three are brick (register `map_material: brick`), so this piece also needs T-2364's
  brick-front support in the kit.

## Image gate (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

Pictures:
  `house_1708_prairie`: a16-cgy-1700-1706-townhouses (photograph, front elevation, undated (after 1902)), a16-ghm-blog-1700-1706-construction-1901 (photograph, oblique front, 1901), a16-ghm-blog-1708-1706-1700-christmas (photograph, oblique front, undated (after 1902; blog context is Christmas 1911)), st-ghm-1700-1706-under-construction-1901 (photograph, oblique front, 1901)

- house_1708_prairie
