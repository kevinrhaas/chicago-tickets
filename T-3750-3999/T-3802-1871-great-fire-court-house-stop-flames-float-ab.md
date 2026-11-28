---
id: T-3802
title: 1871 Great Fire Court House stop: flames float above the building instead of sitting on it
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2417
claimed_by: run 11/27/2026, 1:25:33 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T19:25:35.061Z
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

## Done — PR 2417 (2026-11-28)

Named structures in the fire now burn on their mass (fire-mass.js): the composition's blocks and towers where the sidecar has one, else the pieces' boxes through a median. The Court House's flames stand on its roofs and at its windows, wing by wing; the cupola burns only on its stages. qa_city_fire_1871 fails any flame more than 2 m off a building's plan or 1 m over its roof.

![desktop-court-house-stop-before-after](https://github.com/kevinrhaas/chicago-evidence/blob/1881521a0efe3eca9f5c39898e731f7aee310fba/evidence/1871-streets/T-3802/desktop-court-house-stop-before-after.jpg?raw=true)

![desktop-clark-washington-0145-before-after](https://github.com/kevinrhaas/chicago-evidence/blob/1881521a0efe3eca9f5c39898e731f7aee310fba/evidence/1871-streets/T-3802/desktop-clark-washington-0145-before-after.jpg?raw=true)

![phone-court-house-stop-before-after](https://github.com/kevinrhaas/chicago-evidence/blob/1881521a0efe3eca9f5c39898e731f7aee310fba/evidence/1871-streets/T-3802/phone-court-house-stop-before-after.jpg?raw=true)

![phone-clark-washington-0145-before-after](https://github.com/kevinrhaas/chicago-evidence/blob/1881521a0efe3eca9f5c39898e731f7aee310fba/evidence/1871-streets/T-3802/phone-clark-washington-0145-before-after.jpg?raw=true)

