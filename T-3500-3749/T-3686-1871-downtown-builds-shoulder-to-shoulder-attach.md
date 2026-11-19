---
id: T-3686
title: 1871 downtown builds shoulder to shoulder: attached period fronts with doors, stoops, steps and signs, full detail near the jaunt sites
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
claimed_by: run 11/19/2026, 10:52:27 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T16:52:28.663Z
decision: null
decision_answer: null
---

Downtown 1871 builds shoulder to shoulder: attached commercial rows with period fronts (no pale-green modern blocks), and every building has its doors, stoops, steps and signs; full detail near the jaunt sites, cheap elsewhere.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- In the business district (and the commercial strips of Lake, Randolph, Clark, Wells, Madison, Canal, Milwaukee, North Clark) buildings stand wall to wall along the frontage: no side gaps, shared party walls, varied widths (20 to 80 ft) and heights (3 to 5 storeys downtown, 2 to 3 on the strips). Residential streets keep their yards and side gaps.
- Fronts look like 1860s Chicago from the pictures, not like a 20th-century block: Italianate and commercial-palace fronts with heavy bracketed cornices, tall segmental or round-arched windows with hoods, cast-iron storefronts with large plate glass at ground floor, painted signboards and lettering, awnings; stone (Athens marble, the cream Joliet limestone), brick and painted brick. Nothing reads as the current pale green. Built from photographs: the Chicagology pre-fire views already in data/sources (chicagology_prefire_*), the Ruger 1868 panorama, and any period stereographs the hunt finds (save their source records first).
- Every building has an entrance: a door in each storefront; houses get a stoop or steps up to a door, a porch on frame houses, and a gate in the fence where a yard has one. Reuse the 1835 store fronts, doors, steps and fences and the 1904 K01 house kit parts (cornices, window hoods, stoops) rather than drawing new ones.
- Within about 200 m of a jaunt stop, full detail (photographic textures, modelled cornices and openings); beyond, the cheap instanced stand-in with the same silhouette and colour. Phone keeps the full ring smaller. The 1871 scene's frame time at its stands stays inside its budget.
- Before/after pictures inline in the PR: State and Madison, Lake Street, Clark Street at the Court House, and a North Side residential street, desktop and phone. Gate green, merged to dev.

## Notes

- Builds on T-3683 (PR 2220, frame vs masonry mix): start after it merges. Files: generators/city_1871_emit.py buildings(), renderers/web/js/city-context.js. The jaunt stops are T-3691's; until they are fixed, use the fire's landmark sites (Court House square, State and Washington, DeKoven Street, Chicago Avenue at Pine).

## Owner request

Kevin, 2026-11-19, thread "Build the 1871 Great Fire jaunt and streetscapes" (verbatim): "for 1871 what i would like to start with is a few jaunt scenes and build out the areas around that. i definitiely want a follow the chicago fire like a timeline and you follow the start of the fire and you see it engulf an area and then you move to the next stop and see that, through burning the north side, etc. you shoul be sure to make it seasonal time of day etc, so we will want to build out the jaunt and the scene areas around that, its ok and good if we look at the main landmarks and watch them burn along with the whole streetscape, consider and propose at least 2 more jaunts also for 1871, ideally you can be fairly efficient with this and design and create streetscapes and building and a reuse many of the elements and structures and components and designs from 1904 to jump start your work. In general those structures in 1871 appear to be much more modern than I would anticipate, there are no walkways or entries and the streets, I am concerned about the streets because they look to be all grey brick, I would have thought dirt? Or maybe it was cobblestone in certain areas and with a plank walk against it and a large green fronts downtown that do not appear to look like an 1817 streetscape so get some images and build improve from that the context city, and the buildings all have gaps between them, I think when you look at the density of downtown they would have built more next to each other, and your then marker for this does not show the current intersection, and also many of the streets are janky and do not connect like that recent image and there are lots of places where they go around curves and they do not look like a reasonable curve, review some of the other time periods like 1835 for elements to add for realism and you can keep it reasonably inexpensive to render all that except for around the jaunt sites which should be fully photographic realistic, you can add a chunk of tickets below the south through time and start working them in parallel"

Band 7B (1871). Siblings: T-3684 streets and names, T-3685 surfaces and walks, T-3686 dense downtown, T-3687 the fire, T-3688 South Side landmarks, T-3689 West and North Side places, T-3690 people and vehicles, T-3691 the Great Fire jaunt. Related, worked elsewhere: T-3683 (frame vs masonry mix, PR 2220) and T-3682 (Today window offset and the Illinois Central trestle). Don't duplicate those; build on them once merged.

Standing rules that bind every ticket here: people, horses, carriages and wagons are core on every device (lower resolution, never dropped); photographic quality around the jaunt sites, cheap elsewhere; reuse 1835 and 1904 components first; reconstructed is a tier to build at, recorded in docs/LIBERTIES.md; one PR per ticket into dev, pictures inline and rendered in the PR body, before and after, desktop and phone (390x780).
