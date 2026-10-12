---
id: T-2370
title: Match 1620 Prairie (Law) to its pictures: the 1874 landowner engraving and the 1898 Tribune view
state: split
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-11
closed: 2026-10-12
pr: null
claimed_by: run 10/12/2026, 12:18:18 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-12T05:42:46.792Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38206913932
claimed_at: 2026-10-12T05:18:18.142Z
decision: null
decision_answer: null
---

Match 1620 Prairie (Law) to its pictures: the 1874 landowner engraving and the 1898 Tribune view.

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing"; "redo any work already done to meet this high standard"; "you don't wrap the case until it matches the photo".

This building was built without being checked against its pictures (inventory of 2026-10-11, T-2368). Open every picture listed here and read the building off the picture itself. Solve each one's camera into `data/reference_views/<structure_id>/<view>.json`, render with `node tools/photo_match.mjs`, and rebuild until the side-by-side shows nothing the picture shows differently: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone (AGENTS.md rule 11; `data/reference_views/README.md`). What the picture does not show stays reconstructed and recorded in `docs/LIBERTIES.md`.

Pictures:
  picture: a16-cgy-landowner-1874-1620-law (publication plate, oblique front, May 1874) — `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/a16-cgy-landowner-1874-1620-law.jpg`
  picture: a16-cgy-tribune-1898-prairie-widows (newspaper item, front elevation, January 9, 1898) — `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/a16-cgy-tribune-1898-prairie-widows.jpg`

**Acceptance:** every reference view of the building(s) below has its camera, its side-by-side from the GLB in the tree, and a match record with verdict `matches` and nothing open. The PR carries the before and after side-by-sides, plus desktop and 390x780 in-app shots with no page errors.

## Image gate
- law_house_1620_prairie

