---
id: T-2104
title: Storefront header boards flicker as you turn: the fascia, pilasters and sills are built with their street face missing
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: 422
claimed_by: run 10/4/2026, 2:05:55 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-04T19:05:55.873Z
decision: null
decision_answer: null
---

Storefront header boards flicker as you turn: the fascia, pilasters and sills are built with their street face missing.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 191 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-reported bug (2026-10-04, Rockwell's on South Water): the header over every shopfront flickers as the view turns

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:**

- Turning in front of any shopfront in the 1835 town (Rockwell's cabinet warehouse on South Water is the owner's case), the header board over the door and windows is one steady painted board: no stipple, no wall siding showing through it.
- Fixed where it lives, in the generator, for every building that carries the header (every `frame_storefront` with a shopfront), and the same face mistake on the house stoops (`frame_dwelling`) fixed with it.
- A gate builds every frame storefront, frame dwelling and frame tavern in the town and refuses a trim board whose only face along a wall lies on that wall's plane, with a self-test that re-introduces the fault.
- The structures rebaked (needs_bake: the cloud runner has no Blender, so the bake workflow's branch bake carries the GLBs).

## Cause (2026-10-04)

`MeshBuilder.add_box` names its faces by axis: `front` is the y0 face and `back` the y1 face. On the +y street facade a board runs from the wall at `y` out to `y + t`, so `front` is the face nailed to the wall and `back` is the face the street sees. `frame_storefront._shopfront` built the fascia, the two pilasters, the mullion boards and the counter sills with `skip=("bottom", "back")`: no street face, and a face lying exactly on the wall plane behind it. The renderer draws buildings double-sided, so that face and the wall panel behind the fascia (head to plate, `_front_wall`) fought for the same depth, and the winner changed pixel by pixel as the view turned. Confirmed in the page by raycasting through Rockwell's header from 3.6 m: two hits at the same distance (3.6979 m), the trim face at the wall plane and the wall face. The fascia ends and top were built, which is why it still read as a board with siding showing through it. `_sign` and `frame_dwelling._porch` (the stoop's landing and step) had the same inverted skip.

