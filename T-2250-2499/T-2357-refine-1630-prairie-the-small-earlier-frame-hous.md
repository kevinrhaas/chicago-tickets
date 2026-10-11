---
id: T-2357
title: Refine 1630 Prairie, the small earlier frame house between masonry neighbours, on a frame kit
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1862
opened: 2026-10-11
closed: null
pr: 699
claimed_by: run 10/11/2026, 8:07:37 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38141688283
claimed_at: 2026-10-11T13:07:37.041Z
decision: null
decision_answer: null
---

Refine 1630 Prairie, the small earlier frame house between masonry neighbours, on a frame kit.

Piece 3 of 3 of **T-1862 — Refine 1626, 1628 and small frame 1630**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

No picture of this building was found by address in the Prairie library on 2026-10-11. Before building, search the library (every record, street views and neighbours' plates included) and `data/sources/`. If one turns up, add an `## Image gate` section here naming the structure id as a bullet.
