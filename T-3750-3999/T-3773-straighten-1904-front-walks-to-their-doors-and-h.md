---
id: T-3773
title: Straighten 1904 front walks to their doors and hinge the frame houses' front doors
state: review
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-26
closed: null
pr: 2370
claimed_by: run 11/26/2026, 2:18:16 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-26T20:18:17.564Z
decision: null
decision_answer: null
---

Straighten 1904 front walks to their doors and hinge the frame houses' front doors.

The owner, 2026-11-26, at 2010 Prairie (the Greys'), with a phone screenshot: *"In 1904 looking at the grey house and lots of others don't have the walkway straight to the door from the sidewalk, it's not straight can you fix this and any others whose door does not align and also the door itself does not seem to open like Glessner does any door that a person can come in and out of should swing like a real door on hinges"*.

Measured on dev (every worked 1904 house's built walk against its hung front door, data/humans/doors_1904.json):
- 2010 Prairie: walk on s 1.50, stair and door on s 0.36 (1.14 m off). 2000 Prairie: 1.60 vs 1.17. Cause: `k16_yard.dress` laid the walk on the porch stair's `centre_m` read from s 0, not from the porch's front block corner (the stair itself is built from the block).
- 2011 Prairie: the walk jogged 0.3 m south through its reconstructed coping wall's opening (2.2 m), too narrow for the 1.6 m walk with K14's 0.05 m spare.
- Left as built, photo-gated: Keith 1808, Wheeler 1812, Law 1620, 1736, the 1700/1706 pair (stair stood off the door by `stoop_v_m`, read off their pictures; the walk runs straight to the stair), Dent 1823 and 1621 (side stoops), Jones 1834 and Shortall 1638 (turned walks the photographs draw).
- Doors that did not swing: the frame houses' front doors (2000, 2010, 1720 Walker) were `leafless` (built into the wall). Every other 1904 front door with a plan, and every back door, already swings.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- 2000, 2010 and 2011 Prairie's walks run straight out on their stair and door's line; `check_house_walks.py` refuses a walk off that line (rule 4), with self-tests.
- The three frame houses' front doors are hung passages whose leaf swings (no `leafless`), with no "baked leaf was not found" problem on desktop or phone.
- Before/after pictures, desktop and phone, in the PR and the close note.
