---
id: T-3684
title: 1871 streets carry their 1871 names, meet cleanly and curve smoothly; the THEN card names the intersection you stand at
state: claimed
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: null
pr: null
claimed_by: run 11/19/2026, 10:49:48 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T16:49:49.442Z
decision: null
decision_answer: null
---

Every 1871 street carries its 1871 name, meets its neighbours at clean junctions and bends on real curves; the THEN card names the intersection or block you stand at.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- No street in the 1871 scene is named "Reconstructed north–south street" or "Reconstructed east–west street" where the 1870 Mitchell map (or the 1871 Edwards directory's street list) gives its name. Downtown and the near North and West Sides carry their 1871 names (Fifth Avenue for Wells, Market, Franklin, Griswold, Pacific Avenue, Third and Fourth Avenues, Sherman, Custom House Place, DeKoven, Jefferson, Clinton, Canal, Kinzie, Illinois, Erie, Huron, Superior, Pine, Cass, Rush and the rest), read from the map's own lettering; a grid line the map leaves unnamed keeps a plain reconstructed name and says so in data.
- The downtown block grid sits on the platted streets (original town and its additions, as the 1835 scene already draws the original town), not on a uniform generic pitch. Where the generic lattice and a mapped street disagree, the mapped street wins and the lattice line is dropped, not doubled.
- No dead-end stub, overlapping parallel pair, or "continuation beyond mapped street" connector that reads as a broken road: every street either meets another at a junction, ends at water, a park or the city limit, or is cut by a mapped feature. A junction is one surface, with the walks wrapping its corners.
- Curving streets (Clybourn, Milwaukee, Blue Island, Ogden, North Clark, the river-bank streets) are smooth: no visible kink over about 10°, built from a spline through the traced points, with the walks and the lot frontage following the curve.
- The THEN line of the where card shows the intersection when you stand within about 25 m of one ("State and Madison streets") and the street with its nearest cross streets otherwise ("Clark Street, between Washington and Randolph"); Kevin's two screenshots (148 E Wacker Dr) read a named 1871 place.
- Before/after pictures inline in the PR, desktop and phone, from Kevin's two camera stands (the river looking west from near Michigan Avenue, and the lake-front blocks north of the river). Gate green, merged to dev.

## Notes

- Files: generators/city_1871_emit.py (grid(), the connectors block, infrastructure()), data/context/1871/plan.json (streets), renderers/web/js/where.js (the THEN line). PR 2220 (T-3683) also edits city_1871_emit.py; merge dev in after it lands. Any edit to city_1871_emit.py re-stamps the terrain GLBs: update assets/manifest.json inputs_sha256 and run tools/web_derivatives.sh --only terrain__e1871_prefire.glb,water__e1871_prefire.glb.
- The 1835 scene's data/streets/1835.json already carries the original-town plat; the 1904 street grid (data/street_grid/1904.json) carries later names; use both as cross-checks for line and name, never as a substitute for the 1870 map.

## Owner request

Kevin, 2026-11-19, thread "Build the 1871 Great Fire jaunt and streetscapes" (verbatim): "for 1871 what i would like to start with is a few jaunt scenes and build out the areas around that. i definitiely want a follow the chicago fire like a timeline and you follow the start of the fire and you see it engulf an area and then you move to the next stop and see that, through burning the north side, etc. you shoul be sure to make it seasonal time of day etc, so we will want to build out the jaunt and the scene areas around that, its ok and good if we look at the main landmarks and watch them burn along with the whole streetscape, consider and propose at least 2 more jaunts also for 1871, ideally you can be fairly efficient with this and design and create streetscapes and building and a reuse many of the elements and structures and components and designs from 1904 to jump start your work. In general those structures in 1871 appear to be much more modern than I would anticipate, there are no walkways or entries and the streets, I am concerned about the streets because they look to be all grey brick, I would have thought dirt? Or maybe it was cobblestone in certain areas and with a plank walk against it and a large green fronts downtown that do not appear to look like an 1817 streetscape so get some images and build improve from that the context city, and the buildings all have gaps between them, I think when you look at the density of downtown they would have built more next to each other, and your then marker for this does not show the current intersection, and also many of the streets are janky and do not connect like that recent image and there are lots of places where they go around curves and they do not look like a reasonable curve, review some of the other time periods like 1835 for elements to add for realism and you can keep it reasonably inexpensive to render all that except for around the jaunt sites which should be fully photographic realistic, you can add a chunk of tickets below the south through time and start working them in parallel"

Band 7B (1871). Siblings: T-3684 streets and names, T-3685 surfaces and walks, T-3686 dense downtown, T-3687 the fire, T-3688 South Side landmarks, T-3689 West and North Side places, T-3690 people and vehicles, T-3691 the Great Fire jaunt. Related, worked elsewhere: T-3683 (frame vs masonry mix, PR 2220) and T-3682 (Today window offset and the Illinois Central trestle). Don't duplicate those; build on them once merged.

Standing rules that bind every ticket here: people, horses, carriages and wagons are core on every device (lower resolution, never dropped); photographic quality around the jaunt sites, cheap elsewhere; reuse 1835 and 1904 components first; reconstructed is a tier to build at, recorded in docs/LIBERTIES.md; one PR per ticket into dev, pictures inline and rendered in the PR body, before and after, desktop and phone (390x780).
