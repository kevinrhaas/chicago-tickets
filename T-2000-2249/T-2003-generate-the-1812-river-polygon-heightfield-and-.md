---
id: T-2003
title: Generate the 1812 river polygon, heightfield and ground and water meshes from the e1830_natural spec across the Fort-to-Eighteenth-Street corridor, and bake them
state: open
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1243
opened: 2026-10-02
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

Generate the 1812 river polygon, heightfield and ground and water meshes from the e1830_natural spec across the Fort-to-Eighteenth-Street corridor, and bake them.

Piece 2 of 2 of **T-1243 — Author the e1830_natural terrain spec and generate the 1812 heightfield and the ground and water meshes across the Fort-to-Eighteenth-Street corridor**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. Import `resolve()` from `tools/check_terrain_e1830.py` (PR #312, T-2002) for the effective 1812 zone table; do not copy the 1834 spec.
2. Write `e1830_natural/river.geojson` from `water_bodies_1812.mouth`: the 1834 harbour reach less `isthmus_1812` and `spit_1812`, opening between the adopted outlet station and the bar tip. Write the `north_lake_shore_1812` run (a chord from 1834 index 29 to 39, then the 1834 line). All of it is generated, none drawn by hand.
3. Generate `heightfield.json/.bin` and `terrain__e1830_natural.glb` / `water__e1830_natural.glb` on the 1834 grid. Every vertex is emitted conjectural south of Twelfth Street, and in the west-bank band (`channel_west_bank_ruling`: N −426.75 to −69, the channel plus 157 m west); no land vertex is documented.
4. Wire the 1812 blocks into `compile_scene.GROUND_GROUPS` and `terrain_inputs.CONSUMED` in the same PR, with `mesh:` declarations and LIBERTIES `Covers:` tokens for L361–L363. Then relax the GROUND_GROUPS-collision refusal in check_terrain_e1830.py.
5. `validate.py --stale`, `measure_terrain_fit.mjs --epoch e1830_natural --gate`, and check.sh all pass. Set the epoch's layer_status to generated. This closes T-1243, which unblocks T-0469/T-0470/T-0471.
