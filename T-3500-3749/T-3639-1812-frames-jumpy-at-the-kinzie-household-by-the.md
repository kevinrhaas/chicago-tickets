---
id: T-3639
title: 1812 frames jumpy at the Kinzie household by the boat
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-17
closed: 2026-11-17
pr: 2154
claimed_by: run 11/17/2026, 9:44:22 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-17T22:36:59Z
claimed_run: null
claimed_at: 2026-11-17T15:44:23.934Z
decision: null
decision_answer: null
---

1812 frames jumpy at the Kinzie household by the boat.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Result (PR #2154)

At the Kinzie stand, each person's skinned pieces now share one skeleton. Skeletons drawn a frame went from 448 to 63 and texture uploads from 682 to 130 (3.48 MB to 1.04 MB). The black box's 3 s stall of 10 to 37 ms is gone. The same people are drawn before and after. The numbers are in `docs/measurements/T-3639-frames.json`.

Desktop 1280x800, before | after (249 to 46 skeletons):

![Kinzie household, desktop, before and after](https://github.com/kevinrhaas/chicago-evidence/blob/08c928cdc0661c791d16c5a327814536c3a68af7/evidence/2026-11-17-t3639-frames/kinzie-desktop-before-after.jpg?raw=true)

Phone 390x780, before | after (736 to 94 skeletons, the same 47 people):

![Kinzie household, phone, before and after](https://github.com/kevinrhaas/chicago-evidence/blob/08c928cdc0661c791d16c5a327814536c3a68af7/evidence/2026-11-17-t3639-frames/kinzie-phone-before-after.jpg?raw=true)
