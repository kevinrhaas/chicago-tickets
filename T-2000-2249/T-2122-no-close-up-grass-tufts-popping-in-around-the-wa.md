---
id: T-2122
title: No close-up grass tufts popping in around the walker in town: drop the near tufts on short turf, keep only fence-line weeds and draw them on the full forb ring
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: 449
claimed_by: run 10/5/2026, 7:11:17 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37307506107
claimed_at: 2026-10-05T12:11:17.876Z
decision: null
decision_answer: null
---

No close-up grass tufts popping in around the walker in town: drop the near tufts on short turf, keep only fence-line weeds and draw them on the full forb ring.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 184 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner-reported in the project thread 2026-10-05, being fixed in the same run

## The report

Owner, 2026-10-05, from a screenshot near Randolph Street in 1835 with spiky grass tufts and a
few weeds standing around the camera: "the near field grass animation sucks like things
constantly pop up ... i think that it probably is best to remove those close up grass animations
in town and when you can render them outside in fields where it makes sense lets do that but
they are jarring in how they come into the scene now."

Cause: T-2085 draws the settled town's short turf as near tufts and weeds on a ring of its own
(7.6 m Full, 4.8 m Balanced, 3.4 m Light) over the turf texture. On bare and trodden town
ground nothing stands behind that ring's edge, so every step grows plants up out of open ground
a few metres ahead. In the prairie the near tufts hand over inside a standing mid-card sward,
so nothing is seen to grow out of bare ground there.

**Acceptance:**
- On short turf (`isTurfCommunity`) no near tuft is drawn at any Scene detail tier.
- Weeds on turf stand only where a kept lot re-seats them along its line (T-2086), on the
  ordinary forb ring, so they arrive at its ragged edge ~20 m out, not at the walker's feet.
- Prairie, trees, shrubs and flowers outside the town are unchanged.
- Before/after captures at the in-town stands; flora triangles do not rise.
