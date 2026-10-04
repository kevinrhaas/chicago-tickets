---
id: T-2103
title: The far treeline still draws a moving blob down South Water and a slab from the air
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/4/2026, 2:03:03 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-04T19:03:03.275Z
decision: null
decision_answer: null
---

The far treeline still draws a moving blob down South Water and a slab from the air.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 190 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The owner reported it again on 2026-10-04 with screenshots from South Water facing west and from 55 ft up over La Salle; T-1978 is closed, and this is the end-on and aerial cases it did not cover.

**The owner, 2026-10-04, on dev at /4d/dev/1835/:** *"we are back withe the problem with the tree
line you can see massive moving up and down blobs, you fixed this before but it appears to be back"*
(South Water Street facing W 275°), and *"i found another when flying"* (55 ft up over La Salle at
Lake, facing WSW 251°: a flat dark slab with sheer ends on the left horizon).

The band code T-1978 shipped is unchanged on dev. Both views are cases it did not cover:
- **End-on.** `main_stem_belt_east` runs along South Water's south side, so looking down the street
  its near edge points at the eye. Every sample along it lands in the same few bearings, and the
  bin keeps the angularly tallest — the nearest one past the 330 m cut. That draws a tall narrow
  blob at the street's end whose height follows the cut as you walk.
- **From the air.** The band's foot is a fixed 12 m below the eye. Walking, the near ground hides
  it; from 15 m up it does not, so the band reads as a slab standing on the far ground, its run
  ends sheer.

**Acceptance:**
1. Down South Water facing west, no blob: the band's peak at the street end is under a third of
   dev's, and changes by under 2 px per 20 m walked.
2. From 15 m up and higher, no band is drawn (the modelled trees carry the aerial view); walking,
   wagon and horse heights unchanged in kind.
3. A run of the band ends in a shoulder, not a sheer edge.
4. A smoke check in part 10 that fails on dev's band and passes on the fix: the band's height at the
   South Water end stand, and that it is absent from a flying stand.
5. Lake & Clark, the forks and spawn re-captured; `check.sh` and smoke by parts as for T-1978.
