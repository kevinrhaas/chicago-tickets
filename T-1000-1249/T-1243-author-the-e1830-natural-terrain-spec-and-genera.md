---
id: T-1243
title: Author the e1830_natural terrain spec and generate the 1812 heightfield and the ground and water meshes across the Fort-to-Eighteenth-Street corridor
state: open
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: T-0468
opened: 2026-09-17
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
---

Author the e1830_natural terrain spec and generate the 1812 heightfield and the ground and water meshes across the Fort-to-Eighteenth-Street corridor.

Piece 2 of 2 of **T-0468 — Create an e1812 natural terrain epoch for the Fort Dearborn battle landscape**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

Starts from the planform T-1242 committed at `data/terrain/epochs/e1830_natural/shoreline.geojson`,
which claims NO elevation anywhere.

1. `data/terrain/epochs/e1830_natural/terrain_spec.json` is authored to the standard the
   `e1834_harbor_cut` spec sets: every elevation traces to a numbered zone in the terrain
   research, and no land elevation is graded better than `inferred`.
2. The spit's isthmus gets a surface and a height, or is written down as absent — it is
   `docs/LIBERTIES.md` L240 and `spit_attachment_gap_1812` is the feature that names the hole.
3. The 1812 river polygon and its banks follow from the spec; the heightfield and the ground
   and water meshes are generated, not hand-authored, and the Fort-to-Eighteenth-Street
   corridor is modelled ground.
4. The fit and provenance gates pass, including `validate.py --stale`; `./tools/publish.sh`
   runs in the same commit. This ticket is `needs_bake`.
5. T-0469, T-0470 and T-0471 are blocked on this ticket and unblock when it closes.

## Finding from T-1286 (2026-10-02): the only pre-cut sheet disagrees down the old channel

`data/terrain/1812_harrison_cross_check.json` measures Harrison 1830 (the one pre-cut sheet,
traced by `tools/trace_shoreline_1830.py`) against the derived `shore_1812_pre_cut`. Near the
fort they agree (median 9 m, worst 31 m within 100 m), and Harrison draws the bar attached to
the mainland where L240 attached it (median 7 m). **Down the old southward channel they do
not**: Harrison's west bank is 40 m west of Wright's at 150 m from the fort, 71 m at 200 m,
then a median 120 m and worst 157 m; he letters "Old Mouth of River very shallow" at local
N −69, **357 m north of the adopted station**. Wright still carries the line by the owner's
ruling of 2026-09-17, and nothing was moved.

**Before this ticket lays ground along the old channel, say which of these it is**, in the
spec: (a) the single-anchor transform failing away from the fort (though a 25° rotation would
also throw the main stem out by ~85 m, where it agrees to ~20); (b) the plate's admitted memory
additions; or (c) a mouth that really moved — Harrison calls his the *old* mouth and letters a
channel the soldiers cut in 1828, so the outlet of 1830 need not be that of 1812. If it cannot
be decided from what is held, the channel's ground between N −69 and N −427 is the stretch to
grade lowest. `docs/RESEARCH/shore_1812_pre_cut.md` § 6 has the full reading.
