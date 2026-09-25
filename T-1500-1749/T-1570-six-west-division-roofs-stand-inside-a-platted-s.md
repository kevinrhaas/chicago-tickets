---
id: T-1570
title: Six West Division roofs stand inside a platted street corridor the corridor gate cannot see: two in Jefferson, two in Fulton, two in Des Plaines, west_046 12.08 m in
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
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

Six West Division roofs stand inside a platted street corridor the corridor gate cannot see: two in Jefferson, two in Fulton, two in Des Plaines, west_046 12.08 m in.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Measured working T-1545, 2026-09-25, and filed because that ticket released two slots off
the same street and would otherwise have looked like it had settled the question.

**What the gate cannot see.** `plat_corridors.corridors()` builds its corridor layer from
`generate_plat_lots.CORRIDOR_EW` + `CORRIDOR_NS` — the Original Town block grid plus the
north bank. `data/streets/1835.json` draws **79** streets; **33** are in that layer and
**46** are not, `jefferson` among them. So the corridor check every structure generator
runs is silent about 46 drawn streets, and that is how T-1490 came to measure two West
Division placements 11.9 m and 9.7 m inside Jefferson BY HAND after the gate had passed
them for as long as they stood.

**The six, measured against each omitted street's own declared `corridor_width_m`,
footprint sampled at 0.5 m:**

| structure | street | depth into the corridor |
|---|---|---|
| `recon_1835_west_046` | Des Plaines | 12.08 m |
| `recon_1835_west_006` | Fulton | 4.61 m |
| `recon_1835_west_033` | Jefferson | 3.80 m |
| `recon_1835_west_005` | Fulton | 3.72 m |
| `recon_1835_west_030` | Jefferson | 3.28 m |
| `recon_1835_west_039` | Des Plaines | 2.37 m |

`recon_1835_west_046` stands DEEPER into a drawn roadway than either of the two slots the
Jefferson hold refused to build at all, which is the inconsistency this ticket owns.

**What T-1545 did and deliberately did not do.** It re-dealt the two unbuilt slots clear
(12.25 m and 10.00 m east, `STREET_ADJUSTMENTS`) and FROZE the occupancy as
`WEST_DIVISION_CORRIDOR_OCCUPANTS` in `tools/generate_west_infill.py`, asserted on every
run, so a seventh cannot arrive unremarked and a roof that leaves is recorded as a release.
It did not move the six: each was dealt, reviewed and baked on its present seat, and
re-seating six committed roofs is a different act from releasing two that were never built.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. The six are re-measured from committed files, not read from this table.
2. Each is either re-dealt clear by `STREET_ADJUSTMENTS` — same rule, same search, the
   move recorded on its own record — or the corridor is refused in writing for it, with
   the reading that refuses it. `west_046` at 12.08 m is the one a refusal has to argue
   hardest for.
3. Whichever way each goes, the frozen set shrinks to match and the gate still fires.
4. The two OUTSIDE this parcel's generator are named and handed on rather than silently
   left (they were `west_039` and `west_046` at filing; confirm the ownership).
5. Whether the corridor LAYER itself should reach the 46 omitted streets is a separate and
   larger question — name it, do not answer it here. A blanket gate goes red on records
   this ticket has not adjudicated.
