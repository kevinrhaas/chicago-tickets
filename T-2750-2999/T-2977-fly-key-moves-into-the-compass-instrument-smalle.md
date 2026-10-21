---
id: T-2977
title: Fly key moves into the compass instrument, smaller; the Inspect key fades in and out; nothing on the right edge overlaps in phone landscape
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-21
closed: 2026-10-21
pr: 1173
claimed_by: run 10/21/2026, 9:51:44 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-21T16:30:09Z
claimed_run: null
claimed_at: 2026-10-21T14:51:45.865Z
decision: null
decision_answer: null
---

Fly key moves into the compass instrument, smaller; the Inspect key fades in and out; nothing on the right edge overlaps in phone landscape.

Owner, 2026-10-21 (iPhone, Chrome iOS), with a screenshot of the right-edge quick column: *"the show details button is nice but it keeps appearing and it shifts the fly button up, could you move the fly button to the navigator panel on the upper right, near the map, you can make it smaller tuck it into that panel somewhere sensible and usable and then for the house display panel details button make that fade in and out reasonably quickly so come in is nicely and it's not so jarring"*. Then, with a phone-landscape screenshot where Fly and Inspect sit over the heading and the street readout: *"And pay attention that button Overlaps on mobile landscape"*.

**Acceptance:**
- The Walk/Fly key (`#btn-fly`, F still toggles it) sits in the compass instrument's heading row beside the street switch, a small round key with a touch target of at least 44 px on a touch device, and its pressed state still reads Walk/Fly.
- The quick column holds only the Inspect key; it fades in and out (about 200 ms in, 250 ms out, none under reduced motion) instead of popping, and nothing else moves when it does.
- At 390x780, 844x390 (phone landscape) and 1280x800, in all four appearances, the Inspect key does not overlap the instrument, the heading row or the street readout.
- check.sh green; test_navigator and the smoke's T-2627 check updated to the new home of the Fly key.
