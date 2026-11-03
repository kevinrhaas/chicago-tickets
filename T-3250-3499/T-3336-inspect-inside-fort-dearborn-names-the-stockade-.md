---
id: T-3336
title: Inspect inside Fort Dearborn names the stockade, not the building looked at (phone box pick)
state: done
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-11-02
closed: 2026-11-02
pr: 1639
claimed_by: run 11/2/2026, 9:32:03 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-03T04:07:00Z
claimed_run: null
claimed_at: 2026-11-03T03:32:04.203Z
decision: null
decision_answer: null
---

Inspect inside Fort Dearborn names the stockade, not the building looked at (phone box pick).

Owner, 2026-11-03: "When walking inside the fort and looking at a building in 1812 and maybe in 1835 if inspect I get an inside row of pickets not the building I am looking at."

Cause: on a phone the Inspect probe answers from building parts' boxes (gpu-pick.js boxPick, T-2827). A stockade is one part whose box holds the whole fort, and a ray that starts inside a box was answered at 0 m, so from anywhere inside the walls the pickets won.

**Acceptance:** standing inside either fort on a phone (390×780), Inspect names the building in front of the eye (the same one a tap opens); with nothing nearer ahead it still names the stockade; tools/test_pick_boxes.mjs covers both.
