---
id: T-2371
title: Match the 1812 Prairie (Wheeler) coach house to the street views looking south from 18th Street
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-11
closed: null
pr: null
claimed_by: run 10/12/2026, 12:24:56 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38207533029
claimed_at: 2026-10-12T05:24:56.691Z
decision: null
decision_answer: null
---

Match the 1812 Prairie (Wheeler) coach house to the street views looking south from 18th Street.

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing"; "redo any work already done to meet this high standard"; "you don't wrap the case until it matches the photo".

This building was built without being checked against its pictures (inventory of 2026-10-11, T-2368). Open every picture listed here and read the building off the picture itself. Solve each one's camera into `data/reference_views/<structure_id>/<view>.json`, render with `node tools/photo_match.mjs`, and rebuild until the side-by-side shows nothing the picture shows differently: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone (AGENTS.md rule 11; `data/reference_views/README.md`). What the picture does not show stays reconstructed and recorded in `docs/LIBERTIES.md`.

Pictures:
  picture: a18-rba-taylor-9974-prairie-south-from-18th (photograph, street view, undated (before 1908: a colourised version was published as a postcard postmarked 1908); mature trees suggest c. 1895–1907) — `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/a18-rba-taylor-9974-prairie-south-from-18th.jpg`
  picture: st-flinn-1892-looking-south-prairie-from-18th (publication plate, street view, 1892 (publication; photograph 1887–92)) — `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/st-flinn-1892-looking-south-prairie-from-18th.jpg`
  picture: st-ghm-postcard-1908-prairie-south-at-18th (postcard, street view, postmarked 1908 (photograph published by 1892)) — `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/st-ghm-postcard-1908-prairie-south-at-18th.jpg`
  picture: st-picturesque-chicago-1892-prairie-avenue-p199 (publication plate, street view, 1892 (publication)) — `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/st-picturesque-chicago-1892-prairie-avenue-p199.jpg`

**Acceptance:** every reference view of the building(s) below has its camera, its side-by-side from the GLB in the tree, and a match record with verdict `matches` and nothing open. The PR carries the before and after side-by-sides, plus desktop and 390x780 in-app shots with no page errors.

## Image gate
- wheeler_house_1812_prairie_coach_house

