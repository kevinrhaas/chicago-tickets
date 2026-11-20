---
id: T-3685
title: 1871 street surfaces: dirt in most streets, Nicholson wood block downtown, stone at the wharves, raised plank walks with crossings
state: done
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: 2026-11-19
pr: 2240
claimed_by: run 11/19/2026, 2:34:59 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-20T03:18:21Z
claimed_run: null
claimed_at: 2026-11-19T20:35:02.671Z
decision: null
decision_answer: null
---

1871 street surfaces read as 1871: dirt in most streets, Nicholson wood block on the paved downtown and avenue streets, stone at the wharves and river streets, and raised plank walks with crossings and steps.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- The paving map comes from a source, not a guess: the Board of Public Works' 1871 report (chicago_public_works_1871, its tables of streets paved by kind and mile) and the period accounts. Streets the report lists as wood-block (Nicholson) paved draw as wood block; streets it lists as macadam or gravel draw as such; every other street is dirt. Whatever the report does not reach is a declared reconstruction (LIBERTIES.md) bounded by the report's mileage per kind.
- Wood block reads as weathered end-grain wooden blocks (brown-grey, irregular, tar-joined), not as grey brick; dirt reads as packed earth with wheel ruts and puddle stains (reuse the 1835 `rough_road` ruts mode and textures); stone setts at the wharf streets reuse the 1904 street material. No street anywhere reads as the current uniform pale grey.
- Plank walks are raised wooden sidewalks with a visible edge or curb plank and steps down at crossings, wider downtown, with plank crossings over the dirt streets at junctions (reuse the 1835 plank walk and crossing pieces). Where the street was raised to the new grade and the lot was not, the walk steps; a visitor walking stays on the walk.
- Nearer than about 150 m the surfaces are photographic (textured, with normal detail); beyond, a cheap tinted surface. Phone (390x780) keeps the same colours with smaller textures; frame time at the 1871 stands no worse than before.
- Before/after pictures inline in the PR, desktop and phone, at street level downtown, on a West Side dirt street and at a river wharf. Gate green, merged to dev.

## Notes

- Files: generators/city_1871_emit.py (the `mat` choice per segment, `woodblock`/`dirt`/`plank`), renderers/web/js/city-context.js (materials). Coordinate with T-3684, which reshapes the same streets: land after it or merge it in. The 1835 ground and road materials and the 1904 street surfaces are the parts to reuse.

## Owner request

Kevin, 2026-11-19, thread "Build the 1871 Great Fire jaunt and streetscapes" (verbatim): "for 1871 what i would like to start with is a few jaunt scenes and build out the areas around that. i definitiely want a follow the chicago fire like a timeline and you follow the start of the fire and you see it engulf an area and then you move to the next stop and see that, through burning the north side, etc. you shoul be sure to make it seasonal time of day etc, so we will want to build out the jaunt and the scene areas around that, its ok and good if we look at the main landmarks and watch them burn along with the whole streetscape, consider and propose at least 2 more jaunts also for 1871, ideally you can be fairly efficient with this and design and create streetscapes and building and a reuse many of the elements and structures and components and designs from 1904 to jump start your work. In general those structures in 1871 appear to be much more modern than I would anticipate, there are no walkways or entries and the streets, I am concerned about the streets because they look to be all grey brick, I would have thought dirt? Or maybe it was cobblestone in certain areas and with a plank walk against it and a large green fronts downtown that do not appear to look like an 1817 streetscape so get some images and build improve from that the context city, and the buildings all have gaps between them, I think when you look at the density of downtown they would have built more next to each other, and your then marker for this does not show the current intersection, and also many of the streets are janky and do not connect like that recent image and there are lots of places where they go around curves and they do not look like a reasonable curve, review some of the other time periods like 1835 for elements to add for realism and you can keep it reasonably inexpensive to render all that except for around the jaunt sites which should be fully photographic realistic, you can add a chunk of tickets below the south through time and start working them in parallel"

Band 7B (1871). Siblings: T-3684 streets and names, T-3685 surfaces and walks, T-3686 dense downtown, T-3687 the fire, T-3688 South Side landmarks, T-3689 West and North Side places, T-3690 people and vehicles, T-3691 the Great Fire jaunt. Related, worked elsewhere: T-3683 (frame vs masonry mix, PR 2220) and T-3682 (Today window offset and the Illinois Central trestle). Don't duplicate those; build on them once merged.

Standing rules that bind every ticket here: people, horses, carriages and wagons are core on every device (lower resolution, never dropped); photographic quality around the jaunt sites, cheap elsewhere; reuse 1835 and 1904 components first; reconstructed is a tier to build at, recorded in docs/LIBERTIES.md; one PR per ticket into dev, pictures inline and rendered in the PR body, before and after, desktop and phone (390x780).
