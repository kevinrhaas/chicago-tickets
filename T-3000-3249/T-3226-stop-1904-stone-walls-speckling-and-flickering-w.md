---
id: T-3226
title: Stop 1904 stone walls speckling and flickering where the mortar floor fights the stone face
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-27
closed: 2026-10-28
pr: 1404
claimed_by: run 10/27/2026, 11:45:35 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-28T06:13:05Z
claimed_run: null
claimed_at: 2026-10-28T04:45:36.931Z
decision: null
decision_answer: null
---

Stop 1904 stone walls speckling and flickering where the mortar floor fights the stone face.

The owner, 2026-10-28, on the 1904 dev preview (desktop Chrome): the stone flanks of 1827 and 1801 Prairie are "speckled and flicker when you walk around them", and houses down the street flicker "until you get close".

**Cause (measured).** Not the sun's shadow, the trees or the textures: with the sun's shadow off, the trees hidden and the normal maps removed the patches stay. K02's `stone()` lays a `mortar` floor under each stone's whole cell, the fabric's joint recess (Bedford 2 mm, Lemont 5 mm, dressed trim 1 mm) behind the face; the web derivative's 14-bit lattice is 2.8 mm a rung on 1801 Prairie, so the floor lands on the face's own plane (decoded: both at z -10.99933) and the two fight. 587 m² of 1801 and 415 m² of 1827 are face-over-floor; 24 shipped houses carry the floor.

**Acceptance:** the mortar floor draws behind the stone faces lying on it at any distance and on any lattice, in every shipped house, with no new draw call, no extra memory and no change to a joint's look; a gate holds it; before/after stills from the owner's viewpoints show the speckle gone.
