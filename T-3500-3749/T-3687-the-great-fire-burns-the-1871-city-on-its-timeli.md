---
id: T-3687
title: The Great Fire burns the 1871 city on its timeline: fire front, flames, smoke, glow, char and ash at each hour
state: done
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: 2026-11-19
pr: 2228
claimed_by: run 11/19/2026, 10:51:52 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-19T21:17:10Z
claimed_run: null
claimed_at: 2026-11-19T16:51:53.252Z
decision: null
decision_answer: null
---

The Great Fire burns the 1871 city on its own timeline: a fire front that advances through the city from the O'Leary barn (Sunday 8 October, about 9 p.m.) to its end at Fullerton Avenue (the rain, late Monday 9 to early Tuesday 10 October), with flames, smoke, sparks and brands, a red night sky, and blackened shells, ash and chimneys behind it, all set by the hour a jaunt stop names.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- The burnt district is the mapped one (Sheahan and Upton 1871's map of the burnt district; Andreas 1885 vol. 2 where it is clearer), stored as data with its source, and the fire front's hour at each place comes from the accounts (O'Leary barn ~21:00 Sun; St. Paul's church and the West Side mills by ~22:30; the South Side first lit at the Parmelee stables and the gas works ~23:30-00:00; Court House ~01:30, its bell falls ~02:00; across the main river ~01:30-02:00; the Water Works roof ~03:20; State Street, the Palmer House, Field and Leiter, Crosby's through the small hours; the Tribune ~07:00 Mon; the North Side through Monday; rain ~23:00 Mon; out at Fullerton). Each hour is a cited claim or a declared inferred one (interpolated between cited hours along the wind, SW to NE). Survivors stand: the Water Tower, the O'Leary cottage, the Ogden house, St. Michael's walls, and the West Side south and west of the barn.
- At any fire time t, a building is unburnt, burning (flames from windows and roof, smoke column leaning NE with the gale, sparks and brands blowing), collapsing or burnt (charred walls for masonry, a chimney and ash heap for frame); the context city and every named building take part. Burning frontage near the visitor looks photographic (reuse and extend fort-fire.js: noise flame cards, lit smoke, per-instance char/collapse, ash heaps; its traps are in its header). Far fire is a cheap glow, smoke plume and sky tint so the whole burning city reads from a stop.
- A jaunt stop (or `api.fire.set(t)` for QA) sets t; the night sky, the fire's light on faces and walls, and the smoke follow it. Free walk outside a jaunt shows the pre-fire city (scene date 8 Oct 16:00) unchanged.
- Performance: desktop holds its 1871 frame budget with a whole block burning in view; the phone gets fewer flame cards and a simpler plume, never no fire.
- Before/after pictures inline in the PR: DeKoven Street at 21:30, the Court House at 01:45, State Street at 03:00, the North Side at noon Monday, a burnt block after; desktop and phone. Gate green, merged to dev.

## Notes

- Sources in data/sources: sheahan_upton_1871_great_conflagration, colbert_chamberlin_1871 (on dev via T-3683 if merged), andreas_1884_v1 (vol. 1; add vol. 2 for the fire chapter if used), chicago_public_works_1871. The Board of Police and Fire Commissioners' inquiry testimony (Nov-Dec 1871) is the record of the first hour.
- The fire engine is shared by T-3691 (the jaunt), T-3688 and T-3689 (the landmarks burn with it), T-3690 (crowds fleeing ahead of the front).

## Left after PR #2228

- **Masonry roofs.** A burnt masonry block keeps its roof, because the 1871 context kit is one mesh per template and can't drop a roof per instance. Gutted shells would need either a roofless near-template variant chosen at burn time or a roof-hole decal.
- **Named landmarks.** city-fire.js burns any instance in the buildings layer that lies inside the district, using `fateOf(id)` from data/fire/1871.json (walls_stand, roof_burns or collapses; survivors never burn). This has not been seen yet on the landmark models; check it once T-3688 and T-3689 merge. Pieces in the upper 28% of a structure's height count as its roof.
- **Jaunt stops (T-3691).** A stop burns only if it carries both `hour` and `date` (date YYYY-MM-DD, hour HH:MM). An `ambience` hour has no date, so it never sets the fire.
- **Smoke.** main.js changed, so `smoke_budget --for-diff` asks for the whole body. The body was not run locally, because the shared runner was overloaded. CI's gate ran on the PR.
- **Interpolation.** Between timed places the hours are linear on a per-division triangulation. More timed places from Colbert & Chamberlin or Sheahan & Upton would sharpen the front; add each to data/fire/1871.json's controls and run `tools/fire_1871.py --write`.

## Owner request

Kevin, 2026-11-19, thread "Build the 1871 Great Fire jaunt and streetscapes" (verbatim): "for 1871 what i would like to start with is a few jaunt scenes and build out the areas around that. i definitiely want a follow the chicago fire like a timeline and you follow the start of the fire and you see it engulf an area and then you move to the next stop and see that, through burning the north side, etc. you shoul be sure to make it seasonal time of day etc, so we will want to build out the jaunt and the scene areas around that, its ok and good if we look at the main landmarks and watch them burn along with the whole streetscape, consider and propose at least 2 more jaunts also for 1871, ideally you can be fairly efficient with this and design and create streetscapes and building and a reuse many of the elements and structures and components and designs from 1904 to jump start your work. In general those structures in 1871 appear to be much more modern than I would anticipate, there are no walkways or entries and the streets, I am concerned about the streets because they look to be all grey brick, I would have thought dirt? Or maybe it was cobblestone in certain areas and with a plank walk against it and a large green fronts downtown that do not appear to look like an 1817 streetscape so get some images and build improve from that the context city, and the buildings all have gaps between them, I think when you look at the density of downtown they would have built more next to each other, and your then marker for this does not show the current intersection, and also many of the streets are janky and do not connect like that recent image and there are lots of places where they go around curves and they do not look like a reasonable curve, review some of the other time periods like 1835 for elements to add for realism and you can keep it reasonably inexpensive to render all that except for around the jaunt sites which should be fully photographic realistic, you can add a chunk of tickets below the south through time and start working them in parallel"

Band 7B (1871). Siblings: T-3684 streets and names, T-3685 surfaces and walks, T-3686 dense downtown, T-3687 the fire, T-3688 South Side landmarks, T-3689 West and North Side places, T-3690 people and vehicles, T-3691 the Great Fire jaunt. Related, worked elsewhere: T-3683 (frame vs masonry mix, PR 2220) and T-3682 (Today window offset and the Illinois Central trestle). Don't duplicate those; build on them once merged.

Standing rules that bind every ticket here: people, horses, carriages and wagons are core on every device (lower resolution, never dropped); photographic quality around the jaunt sites, cheap elsewhere; reuse 1835 and 1904 components first; reconstructed is a tier to build at, recorded in docs/LIBERTIES.md; one PR per ticket into dev, pictures inline and rendered in the PR body, before and after, desktop and phone (390x780).
