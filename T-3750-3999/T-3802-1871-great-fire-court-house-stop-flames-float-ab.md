---
id: T-3802
title: 1871 Great Fire Court House stop: flames float above the building instead of sitting on it
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Kevin, 2026-11-27 (thread "Make 1871 jaunt streets photo-accurate"): *"I would like you to do more street improvements to the areas around the jaunt stops, the most historic and important areas. Do what research you can on the surrounding areas of the jaunts and photo match the best you can to the surrounding street. If you need to, use period photos to infer and reconstruct the street scape, businessess, street furniture etc. the signs above stores must need to be varied and be more specific based on your research of the citizens and people and businesses in 1871, build and extend a group of tickets to improve 1871, and claim and start to work them in parallel to make it photographic match perfect with 1871, add whatever is needed to make it shockingly accurate"*

And, the same day: *"one note on 1871 the fire when the court house is on fire that the fires sometimes appear above the building"*.

**Cause (first read):** `renderers/web/js/city-fire.js` builds a named structure's fire record from the bounding box of ALL its pieces, so the Court House's cupola sets `top`, and `h = 0.8 × H` puts the storey count and the roof flames (`rec.base + rec.h * 0.97`) far above the wings' roofs; roof and window emitters are also spread over the whole box, so on a building that is not a box (the centre block and two wings, the square round it) they stand in empty air.

**Acceptance:**
1. Named-structure flames sit on the building: roof flames on a roof under them, window flames on a wall up to that wall's own height, never in air beside or above the building (cupola flames only on the cupola).
2. A check that fails a flame emitter more than ~1 m clear of every piece of its structure, run over every named 1871 structure that burns, in the gate.
3. Before/after at the Court House stop (Great Fire stop 4, 01:30 and the Sherman House stop's view of it), desktop and phone.
