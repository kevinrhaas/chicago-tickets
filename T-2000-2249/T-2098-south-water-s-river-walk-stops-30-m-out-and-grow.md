---
id: T-2098
title: South Water's river walk stops ~30 m out and grows back as you approach: the working bank's biased depth hides its boards
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-04
closed: 2026-10-04
pr: 415
claimed_by: run 10/4/2026, 12:25:46 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T18:39:12Z
claimed_run: null
claimed_at: 2026-10-04T17:25:46.395Z
decision: null
decision_answer: null
---

South Water's river walk stops ~30 m out and grows back as you approach: the working bank's biased depth hides its boards.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 189 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner reports the river walk still vanishing in the distance on dev after T-2037, with screenshots at South Water and La Salle

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:**

- From South Water at La Salle looking west and at Dearborn looking east, at walking height, the river walk is drawn to its recorded end, and the frame near the visitor is unchanged.
- The cause is repaired where it lives (the working bank's decal depth), not with a counter-bias on the timber: T-2037's `material.polygonOffset === false` checks stay as they are.
- No added geometry, draw call or shader program.

## Cause (2026-10-04)

The working bank (working-bank.js) was an OPAQUE decal with `polygonOffset -2/-2`. Opaque, it wrote that offset depth before the timber drew, and the slope term of the offset grows with distance at a grazing view. Past ~30 m from a walking eye the biased bank stood in front of the boards 0.11 m above it, so the walk ended short and its end crept toward the visitor while walking. Hiding the terrain, the street ribbon, the street grid or the yard ground changed nothing; hiding only the working bank brought the whole walk back.
