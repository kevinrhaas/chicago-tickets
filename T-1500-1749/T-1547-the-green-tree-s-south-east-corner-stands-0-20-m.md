---
id: T-1547
title: The Green Tree's south-east corner stands 0.20 m INSIDE the West Water track, and the street's trace ends at that corner: re-seat it clear, carry the trace past it, or refuse the corridor in writing
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
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

The Green Tree's south-east corner stands 0.20 m INSIDE the West Water track, and the street's trace ends at that corner: re-seat it clear, carry the trace past it, or refuse the corridor in writing.

Measured on the t0141 branch (the move of T-0141), against
`data/streets/1835.json` `west_water`, whose track is 5.80 m wide:

| footprint corner (local ENU m) | distance to centreline | verdict |
| --- | ---: | --- |
| (-18.90, -96.19) | 2.70 m | **INSIDE the track by 0.20 m** |
| (-18.90, -88.57) | 10.02 m | clear by 7.12 m |
| (-31.09, -88.57) | 14.64 m | clear by 11.74 m |
| (-31.09, -96.19) | 11.01 m | clear by 8.11 m |

Two facts compound. First, West Water's traced centreline does not run past the
inn at all — it climbs from (-20.21, -404.02) and TERMINATES at (-20.32, -98.49),
which is 2.70 m from the inn's south-east corner. The street the placement names
as the front's street ends at the building. Second, the corner is inside what
corridor there is.

This is why the frontage works collapsed to one walk and no board. The front
wall faces west and West Water lies east of it, so `_street_facing` reads the
street as BEHIND the front (outward -10.77 m) and refuses it; only the long
south elevation on Lake keeps its walk. The corner post needs the corner two
walks make, so it goes too, and with it the GREEN TREE lettering — the first
lettering this project ever drew. Nothing in the frontage rule is at fault:
`FRONTAGE_DOMINANCE`, the T-0090 guard against laying a walk down a building's
flank, is doing exactly its job.

The post cannot simply be re-seated at that corner either: a post offset into
the verge there measures 2.40 m from the West Water centreline against a 2.90 m
half-width, so it would stand in the roadway.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. One of the three is chosen and written down with its reason:
   a. the inn is re-seated clear of the corridor by the recipe that placed it
      (not nudged by hand), or
   b. West Water's trace is carried north past the inn on a source, so the inn
      has a real second frontage and the works regenerate, or
   c. the corridor is refused in writing at this point, stating what is known
      about where West Water ran north of Lake and why no corridor is drawn.
2. No footprint corner of `green_tree_tavern` lies inside a street track, or the
   intrusion is the stated, argued consequence of (c).
3. `tools/generate_frontage_works.py --check` re-derives, and the refusals it
   states are true of the geometry that ships.
4. The GREEN TREE board exists somewhere in the town — on its post at the corner
   if the corner can carry one, on the wall if it cannot. It is never silently
   absent (see the companion fix in `generate_business_signboards.py`).
