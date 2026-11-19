---
id: T-3691
title: The Great Chicago Fire jaunt: follow the fire from the O'Leary barn to the North Side, stop by stop, at its hours
state: review
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: null
pr: 2243
claimed_by: run 11/19/2026, 10:51:56 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T16:51:57.713Z
decision: null
decision_answer: null
---

The Great Chicago Fire jaunt: you follow the fire from the O'Leary barn on Sunday night to the North Side and the rain, stop by stop at its hours, watching each area and its landmarks catch and burn, with the people who were there.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- A jaunt (data/jaunts/the-great-fire*.json) of 10 to 12 stops in fire order, each with its date and hour (`hour`, `date`, `hour_evidence`) set by the accounts: the O'Leary barn (Sun 8 Oct ~21:00); the West Side spreading NE (St. Paul's church, the mills, ~22:30); the brands crossing the South Branch to the Parmelee stables and the gas works (~23:30); the Court House and its bell (~01:30-02:00 Mon 9 Oct); the Sherman House and the river's south bank; State Street and Field and Leiter / the Palmer House; Crosby's Opera House; across the main river to the North Side (~02:00); the Water Works roof (~03:20) and the Water Tower; the North Side through Monday (the Ogden house, St. Michael's); the refugees on the lake shore and in Lincoln Park; the rain and the end at Fullerton Avenue (late Monday). Its default season is autumn, its weather dry with a SW gale; night stops are night.
- Told like the 1812 jaunts: engaging, every person introduced on first mention, each stop ending on a hook, "according to legend" for the cow, no hedging, no technical talk; opening narration on the way to stop 1 and a closing scene before Outing complete. Stop text inside the compile limits; `long_form` as the 1812 tellings.
- Staged scenes in the manner of the burning of Fort Dearborn (fort-fire.js, jaunt-stage.js): the fire is burning in front of you (T-3687), the landmark is the one from its pictures (T-3688, T-3689), and the people of the hour are there (T-3690): Catherine and Patrick O'Leary, Daniel "Peg Leg" Sullivan, the watchman Mathias Schaffer in the Court House tower, Mayor Roswell B. Mason, Potter Palmer, Joseph Medill at the Tribune, crowds fleeing.
- `menu_group`, `menu_rank`, a measured `grade_band`, and every band via versions.py (3-5, 6-8, 9-10, 11-12) plus an adults (18+) telling. Students: no one shown burning or dying; the adults telling may tell and show the dead from the accounts. Narration direction written for the voice pipeline (record only when Kevin asks).
- Every quotation verbatim from a cited source; every hour cited or declared inferred; staging recorded under its own liberty.
- Pictures of every stop inline in the PR, desktop and phone, and the jaunt played end to end in the app (QA run). Gate green, merged to dev.

## Notes

- Depends on T-3687 for the fire and T-3688/T-3689 for the landmarks; the text, stops, anchors and versions can land first with the fire following. docs/JAUNTS-AUTHORING.md is the contract; the 1812 battle jaunt and the 1904 story jaunts (docs/RESEARCH/jaunt-stories-1904/) are the models.

## Owner request

Kevin, 2026-11-19, thread "Build the 1871 Great Fire jaunt and streetscapes" (verbatim): "for 1871 what i would like to start with is a few jaunt scenes and build out the areas around that. i definitiely want a follow the chicago fire like a timeline and you follow the start of the fire and you see it engulf an area and then you move to the next stop and see that, through burning the north side, etc. you shoul be sure to make it seasonal time of day etc, so we will want to build out the jaunt and the scene areas around that, its ok and good if we look at the main landmarks and watch them burn along with the whole streetscape, consider and propose at least 2 more jaunts also for 1871, ideally you can be fairly efficient with this and design and create streetscapes and building and a reuse many of the elements and structures and components and designs from 1904 to jump start your work. In general those structures in 1871 appear to be much more modern than I would anticipate, there are no walkways or entries and the streets, I am concerned about the streets because they look to be all grey brick, I would have thought dirt? Or maybe it was cobblestone in certain areas and with a plank walk against it and a large green fronts downtown that do not appear to look like an 1817 streetscape so get some images and build improve from that the context city, and the buildings all have gaps between them, I think when you look at the density of downtown they would have built more next to each other, and your then marker for this does not show the current intersection, and also many of the streets are janky and do not connect like that recent image and there are lots of places where they go around curves and they do not look like a reasonable curve, review some of the other time periods like 1835 for elements to add for realism and you can keep it reasonably inexpensive to render all that except for around the jaunt sites which should be fully photographic realistic, you can add a chunk of tickets below the south through time and start working them in parallel"

Band 7B (1871). Siblings: T-3684 streets and names, T-3685 surfaces and walks, T-3686 dense downtown, T-3687 the fire, T-3688 South Side landmarks, T-3689 West and North Side places, T-3690 people and vehicles, T-3691 the Great Fire jaunt. Related, worked elsewhere: T-3683 (frame vs masonry mix, PR 2220) and T-3682 (Today window offset and the Illinois Central trestle). Don't duplicate those; build on them once merged.

Standing rules that bind every ticket here: people, horses, carriages and wagons are core on every device (lower resolution, never dropped); photographic quality around the jaunt sites, cheap elsewhere; reuse 1835 and 1904 components first; reconstructed is a tier to build at, recorded in docs/LIBERTIES.md; one PR per ticket into dev, pictures inline and rendered in the PR body, before and after, desktop and phone (390x780).
