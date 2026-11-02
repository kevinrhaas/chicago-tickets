---
id: T-3319
title: Fort Dearborn: walk inside in 1812 and 1835 through gates an Interact key opens and shuts
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-02
closed: 2026-11-02
pr: 1624
claimed_by: run 11/2/2026, 11:54:12 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-02T23:19:47Z
claimed_run: null
claimed_at: 2026-11-02T17:54:13.206Z
decision: null
decision_answer: null
---

Fort Dearborn: walk inside in 1812 and 1835 through gates an Interact key opens and shuts.

The owner, 2026-11-02 (project thread "Add interactable fort gates"): *"you should be able to enter the fort in both 1812 and 1835, be able to walk through the gate, ideally if you can have like with inspect an interact button and the gate by default is closed and you can click on interact and for the gate where there is only two settings open and closed then you should be able to interact and otherwise for future there may be some kind of interaction sequence on how or a move to do something to interact with objects across the scenes, but start here with the fort gates"*

Found before work: the walker treats each stockade as one solid footprint (so the whole fort is a block you are pushed out of), the parade ground is a solid footprint too, and the 1812 gates are baked at the middle of the south rows while Whistler's draught puts the passage ~2.6-2.8 m west, where the barracks leave their gap (both picket records say so in their gate_sides notes).

**Acceptance:**
- 1835 and 1812: a visitor on foot can walk through a gate, round the parade and the buildings inside, and back out; the stockade itself still stops them; the buildings inside stay solid.
- 1812: the main gate in both picket rows stands at the draught's passage (E -11.1..-4.9 ft), not the archetype's centre; rebaked.
- An Interact key in the quick column beside Inspect (and a keyboard key) appears near a gate; gates start closed; Interact opens or closes them with a swing; a closed gate blocks, an open one lets you through.
- Built as a generic interaction (states + a sequence of steps per action) so later objects can carry multi-step sequences; only the fort gates ship.
- Phone (390x780) and desktop checked; gate check green.
