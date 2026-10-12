---
id: T-2369
title: Finish 1612 Prairie against its photograph: paired cornice brackets on a dark frieze, the south wall's canted bay, the stoop between iron rails, the portico's depth
state: review
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-11
closed: null
pr: 728
claimed_by: run 10/11/2026, 11:57:58 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-12T04:57:58.114Z
decision: null
decision_answer: null
---

Finish 1612 Prairie against its photograph: paired cornice brackets on a dark frieze, the south wall's canted bay, the stoop between iron rails, the portico's depth.

Owner, 2026-10-11: "it should look exactly perfectly like the image or drawing" and "you don't wrap the case until it matches the photo". T-2366 rebuilt the front from the photograph (`data/reference_views/goodman_house_1612_prairie/front_from_southeast.json`); its match record lists what the side-by-side still shows differently, and this ticket closes those:

1. **Cornice:** the print's brackets are paired, deeper and closer, over a frieze that reads dark end to end. The build has single brackets, evenly spaced, over a light band.
2. **South wall:** the print shows a canted bay on the brick side wall behind the front. The build's side is flat.
3. **Stoop:** the print has fewer, narrower steps between iron hand-rails. The build has a long stone flight with stone cheeks.
4. **Portico:** the print's porch stands closer to the wall and reads flatter. The build's projects further, with deep open sides.

Look again for anything else the photograph shows differently. Read the image itself (`data/sources/assets/goodman_1612_photo_owner_2026_10/`), and find any other picture of the house in the Prairie library, solving each one's camera too.

**Acceptance:** for every reference view of 1612, `node tools/photo_match.mjs` renders from the GLB in the tree, every difference is `fixed` or `not shown`, and the verdict is `matches`. The PR carries the side-by-sides, and the desktop and 390x780 in-app shots have no page errors.

## Image gate
- goodman_house_1612_prairie

**Unblocked 2026-10-11:** T-2366 merged (PR #706); this took its place in the queue. The block read: T-2366 — same house; lands after T-2366's PR
