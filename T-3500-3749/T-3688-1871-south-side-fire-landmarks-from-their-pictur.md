---
id: T-3688
title: 1871 South Side fire landmarks from their pictures: Court House, Sherman and Tremont Houses, Chamber of Commerce, Crosby's, Field and Leiter, Palmer House, Tribune
state: open
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
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

The South Side's fire landmarks stand in 1871 built from their pictures, ready to burn: the Court House and City Hall on its square, the Sherman House, the Tremont House, the Chamber of Commerce (Board of Trade), Crosby's Opera House, Field, Leiter and Co. at State and Washington, the new Palmer House at State and Quincy, and the Tribune building at Dearborn and Madison.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Each is a named structure in the 1871 scene (added to its structure_ids), on its documented lot from the 1870 map and the directory, built to its photographs, prints and drawings under the image gate (AGENTS.md rule 11: every picture found, cameras solved into data/reference_views/<id>/, photo_match until the side-by-side shows nothing a visitor would notice; the stopping rule binds). The pre-fire research site (chicago/pre_fire_v1: buildings.csv, media.csv, research_1871.json, the Carbutt Chamber stereograph) and the Chicagology pre-fire views are the first places to look.
- Each has a card: what it was, who built it, what happened to it on 9 October (cited), and its grade (attested where a picture shows it whole).
- Each takes part in T-3687's fire (burning, then its burnt shell: the Court House's walls and fallen cupola, the Tribune's "fireproof" shell), so the jaunt can stop before it and watch it burn.
- The blocks round each (Court House square's four fronts, State Street from Lake to Monroe, Dearborn at Madison) are full-detail streetscape per T-3686.
- Phone keeps every landmark (lower detail, never dropped). Before/after pictures inline in the PR, desktop and phone. Gate green, merged to dev.

## Image gate

- cook_county_court_house_1871
- chamber_of_commerce_1871
- sherman_house_1871

## Progress (2026-11-19, first PR: the Court House square group)

This ticket grew past one run, so its first PR ships the Court House square group, as the Notes allow, and the rest is recorded here rather than split.

- **Shipped:** the Court House, the Chamber of Commerce and the Sherman House stand in the 1871 scene on a new pure-Python archetype, `landmark_1871` (blocks, faces, openings, cornices, mansards, towers, crests; K02/K03/K04 materials). Each has a record, a card with its fire hour and sources, a camera on its photograph and a match record. The GLB node's extras carry `fire.roles` (roof, glazing, walls, trim, iron mapped to material names) and `fire.shell` (what stood after: fate, walls left, hour) as the hook for T-3687.
- **Image gate, still `differs`:** the Chamber of Commerce (the balcony over the entrance; the upper windows' curved pediments), the Sherman House (the second-storey balcony's railing; the attic's balustrade; the Clark Street portico), the Court House (its camera is not fitted because no dimension of the 1870 wings was found; the wings are a storey short; the great cupola is low and lacks its clock stage). Each item is in its view's match record.
- **Remaining, not started:** the Tremont House (SE corner of Lake and Dearborn, 140 ft on Lake by 180 on Dearborn, five and a half storeys, Van Osdel, 1850: Andreas vol. 2, pp. 501-502), Crosby's Opera House, Field, Leiter and Co., the Palmer House and the Tribune building, and the full-detail blocks round each (T-3686).

## Notes

- Reuse the 1904 K01 kit and Glessner-era masonry materials (cornices, window hoods, rusticated stone). If one landmark grows past a run, ship the others and record the rest in this ticket; ask Kevin before splitting it into per-building tickets (owner, 2026-10-25 ticket restraint).

## Owner request

Kevin, 2026-11-19, thread "Build the 1871 Great Fire jaunt and streetscapes" (verbatim): "for 1871 what i would like to start with is a few jaunt scenes and build out the areas around that. i definitiely want a follow the chicago fire like a timeline and you follow the start of the fire and you see it engulf an area and then you move to the next stop and see that, through burning the north side, etc. you shoul be sure to make it seasonal time of day etc, so we will want to build out the jaunt and the scene areas around that, its ok and good if we look at the main landmarks and watch them burn along with the whole streetscape, consider and propose at least 2 more jaunts also for 1871, ideally you can be fairly efficient with this and design and create streetscapes and building and a reuse many of the elements and structures and components and designs from 1904 to jump start your work. In general those structures in 1871 appear to be much more modern than I would anticipate, there are no walkways or entries and the streets, I am concerned about the streets because they look to be all grey brick, I would have thought dirt? Or maybe it was cobblestone in certain areas and with a plank walk against it and a large green fronts downtown that do not appear to look like an 1817 streetscape so get some images and build improve from that the context city, and the buildings all have gaps between them, I think when you look at the density of downtown they would have built more next to each other, and your then marker for this does not show the current intersection, and also many of the streets are janky and do not connect like that recent image and there are lots of places where they go around curves and they do not look like a reasonable curve, review some of the other time periods like 1835 for elements to add for realism and you can keep it reasonably inexpensive to render all that except for around the jaunt sites which should be fully photographic realistic, you can add a chunk of tickets below the south through time and start working them in parallel"

Band 7B (1871). Siblings: T-3684 streets and names, T-3685 surfaces and walks, T-3686 dense downtown, T-3687 the fire, T-3688 South Side landmarks, T-3689 West and North Side places, T-3690 people and vehicles, T-3691 the Great Fire jaunt. Related, worked elsewhere: T-3683 (frame vs masonry mix, PR 2220) and T-3682 (Today window offset and the Illinois Central trestle). Don't duplicate those; build on them once merged.

Standing rules that bind every ticket here: people, horses, carriages and wagons are core on every device (lower resolution, never dropped); photographic quality around the jaunt sites, cheap elsewhere; reuse 1835 and 1904 components first; reconstructed is a tier to build at, recorded in docs/LIBERTIES.md; one PR per ticket into dev, pictures inline and rendered in the PR body, before and after, desktop and phone (390x780).

**Released 2026-11-20** (claim of run 11/19/2026, 10:51:49 AM CT): no reason given
