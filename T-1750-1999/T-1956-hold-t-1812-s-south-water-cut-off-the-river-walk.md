---
id: T-1956
title: Hold T-1812's South Water cut off the river walk: the bank under its south half fell up to 0.19 m, and its edge stands 0.191 m over grade
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Hold T-1812's South Water cut off the river walk: the bank under its south half fell up to 0.19 m, and its edge stands 0.191 m over grade.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 250 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> dev's gate stays red on it after T-1955, and T-1812, which caused it, has merged and closed, so nothing else owns the fix

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: mobile part 2, 'the plank decks tie into the ground they cross', highest flat-ground deck vertex 0.191 m against 0.18, still red after T-1955 fixed the crossings and the inn pick

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
The river walk stands on the level bank it had before T-1812 (its board stations within 0.04 m of their pre-T-1812 ground), and mobile part 2's 'the plank decks tie into the ground they cross' is green with its 0.18 m band and 0.12 m threshold unchanged.

## What T-1955 measured (2026-10-02)

- **Cause.** T-1812's `street_sections` cut lowers South Water out to its worked
  half-width less `shelf_clear_m`, which is wider than the travelled track that
  `_audit_river_reach` keeps the river walk clear of. So the river walk (north of
  the track, N ≈ 13–15 between E ≈ 640 and 805) lies inside the worked width, and
  the cut reaches under it. Heightfield before T-1812 (353f7898^) against dev:

  | E | N 12.5 | N 13.0 | N 13.9 | N 14.8 |
  |---|---|---|---|---|
  | 689.25 | 0.374 → 0.100 | 0.362 → 0.140 | 0.340 → 0.219 | 0.318 → 0.296 |
  | 712.06 | 0.414 → 0.176 | 0.410 → 0.217 | 0.403 → 0.298 | 0.396 → 0.377 |
  | 715.18 | 0.426 → 0.201 | 0.420 → 0.238 | 0.409 → 0.310 | 0.397 → 0.380 |

  The walk was on level ground; it now sits on a bank tilting 0.16 m across its
  1.83 m width, so a board seated on its centre stands 0.19 m over grade at its
  south edge (`river_plank_walk_east_reach`, `_west_reach`, `_wharf_reach_1`).
- **Why the smoke's relief allowance does not excuse it.** The probe's ring
  (±0.95 m round the vertex) reads 0.105–0.119 there, under the 0.12 tilted-ground
  threshold. Measuring the relief across the walk's own width instead still leaves
  0.190 at the wharf reach; only a rule that takes the larger of the two passes,
  and that rule only ever loosens the band. So T-1955 left the instrument alone.
- **The fix is the ground.** Keep the cut off the river walk's footprint (a
  `keep_clear` that follows a line, or the walk's own edge as the worked edge on
  that side), regenerate the heightfield, rebake the ground and re-derive what
  reads it — T-1812's own chain. T-1771 (riverfront ground) is shaping the same
  bank; read its branch first.
