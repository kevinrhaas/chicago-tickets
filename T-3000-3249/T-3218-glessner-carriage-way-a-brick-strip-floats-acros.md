---
id: T-3218
title: Glessner carriage way: a brick strip floats across the court mouth over the sunk floor
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-27
closed: null
pr: 1393
claimed_by: run 10/27/2026, 7:12:42 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-28T00:12:43.691Z
decision: null
decision_answer: null
---

Glessner carriage way: a brick strip floats across the court mouth over the sunk floor.

Owner, 2026-10-27, with a dev screenshot from the court looking east (1820 Prairie): "there is a weird brick line in the carriageway of glessner".

Cause (measured in the committed master GLB): the court face's underpass exit opening is written at z 0.0 on the `ng` datum, which T-2955 put 0.2 ft over the model's grade, while the court wall starts at model grade. So the wall's bottom brick course (model z 0.004-0.061 m) and its mortar backing run uncut across the mouth, and since T-2976/T-2978 sank the passage floor to -2.45 ft ng that course hangs about 2.25 ft over the floor as a thin floating brick bar.

**Acceptance:**
- The court wall's hole for the through passage reaches the passage floor, so no brick or mortar crosses the mouth between the reveals; the opening's recorded z (sheet 4's lawn line) is unchanged.
- Glessner rebaked (master + web + light), K01/opening schedule/source use refreshed, gate green.
- Before/after stills from the owner's viewpoint, desktop and phone.
