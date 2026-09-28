---
id: T-1739
title: Write data/scenes/1904.json on e1871_postfire and land /4d/1904/ at Prairie and 18th facing the Glessner lot, with the glessner_house anchor and a smoke assertion at 390x780 and 1280x800
state: done
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1252
opened: 2026-09-28
closed: 2026-09-28
pr: 175
claimed_by: run 9/28/2026, 2:18:33 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-28T22:33:09Z
claimed_run: null
claimed_at: 2026-09-28T19:18:33.447Z
decision: null
decision_answer: null
---

Write data/scenes/1904.json on e1871_postfire and land /4d/1904/ at Prairie and 18th facing the Glessner lot, with the glessner_house anchor and a smoke assertion at 390x780 and 1280x800.

Piece 2 of 2 of **T-1252 — Generate and bake the e1871_postfire heightfield over the Prairie Avenue reach**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The owner's requirement (2026-09-28, carried from T-1252): the 1904 scene's **spawn** stands on
Prairie Avenue at E. 18th Street, at eye height on the east sidewalk, **facing the south-west corner
lot, 1800 Prairie** (the Glessner House lot; Sanborn 1911 sheet 28). `/4d/1904/` and `/4d/dev/1904/`
open looking at that ground, and the scene carries a named anchor **`glessner_house`** at the same pose
(`?year=1904&anchor=glessner_house`). The house itself is T-1729's; the view is this ticket's.

1. `data/scenes/1904.json`: `target_date: "1904-07-01"`, `terrain_epoch: "e1871_postfire"`, its **own**
   anchors (the 1835 scene's are not inherited), lighting for 1 July at this latitude; the spawn and
   `glessner_house` at the pose above, placed from the T-1250 georeference of sheet 28 and T-1731's lot
   frame, never from a round number.
2. The renderer boots the 1904 scene on its own ground and draws none of the 1835 layers into it (no
   1835 street, fence, flora, sign or building); `/4d/1904/` is written as a front door.
3. `tools/measure_anchors.mjs` holds the new anchors against the e1871 heightfield; the ground-contact
   and publish gates pass for the second epoch; the frame budget is measured at the spawn.
4. **A smoke assertion at 390x780 and at 1280x800** that loading `/4d/dev/1904/` lands facing the 1800
   Prairie lot: the spawn bearing, and the lot centroid's screen position (on screen, left of centre,
   in front of the camera).

Split out of T-1252 on 2026-09-28. Depends on T-1738 (the heightfield it stands on).
