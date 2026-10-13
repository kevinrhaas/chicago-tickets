---
id: T-2475
title: Soft edges where the 1904 street surfaces meet each other and the lawns, instead of hard jagged cuts
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: 791
claimed_by: run 10/13/2026, 3:00:03 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-13T20:00:03.623Z
decision: null
decision_answer: null
---

Soft edges where the 1904 street surfaces meet each other and the lawns, instead of hard jagged cuts.

## The owner's ask (2026-10-13, project thread "Prairie Avenue streetscape")

> Something else that would be nice, I am looking at this street scape and we want to emulate this. Look at the curb height and make sure we are correct on that, with correct carriage walk ways, and add street foliage trees correctly, would be nice to in options to be able to hide trees or make them spring trees barely blooming so you can see the house with the trees shown but you can still see the house, default should have the correct trees, you should be able to use the models from 1835 for flora as a base. If it's easy to add some correct bushes or other foliage with the houses please do, but you will have that as part of the house passes to add the correct flora for each. Also when flying or walking over street areas that are transitional between surfaces it's looks jagged and harsh, that should fade, in some way there should be a transition

"This image" is the Holzman postcard postmarked 1908, the library's `st-ghm-postcard-1908-prairie-south-at-18th`: the west sidewalk at 18th Street beside Glessner, looking south. The same negative is `st-picturesque-chicago-1892-prairie-avenue-p199`, `st-flinn-1892-looking-south-prairie-from-18th` and `st-flinn-1891-a-bit-of-prairie-avenue`, so the photograph dates Dec. 1887 to 1891, 13-17 years before the scene date. Supporting views: `st-views-of-chicago-1905-prairie-and-michigan-avenues` (a single row of closely spaced elms in the parkway, dressed-stone carriage blocks along the parkway edge), `st-chicagology-prairie-avenue-about-1890-photo` (carriage blocks at the curb, bare parkway elms), `st-ghm-ward-1887-prairie-north-from-20th` (a continuous row of parkway trees on both sides), `st-ghm-1700-1706-under-construction-1901` (a freshly planted sapling in the parkway), `st-randmcnally-1910-pullman-corner-18th` (young parkway trees on the 18th Street corner), and HABS Glessner nos. 2 and 3 (c. 1923: a paved crossing from the door to the curb, a young parkway tree).

Worked interactively in that thread; the three tickets T-2473, T-2474 and T-2475 are its pieces, one PR each into dev.

## What to build

Where the 1904 street surfaces meet each other and the ground (walk to turf, turf to curb, curb to roadway, roadway to alley, the corner squares, the margin to the lawns, the grid's turf to the terrain's lawn), the edges are hard straight cuts between differently coloured and textured materials, and from the air or at a walk the turf of the parkway and the lawn of the lots do not match. Soften them: a short blended fringe where turf meets paving (grass creeping over the edge, dirt and wear along the curb and walk joints), the parkway turf and the lot lawn brought to one colour so the margin does not read as a stripe, and a feathered fade where a grid surface meets the terrain's own ground. Hard edges stay where they are real (a dressed curb face, a cut stone joint).

## Acceptance

1. Before/after captures from the air (8 m and 30 m) and at a walk, desktop and phone, showing the transitions faded with no jagged or shimmering edge.
2. No z-fighting or depth artefact introduced (the T-1805 and T-2098 depth lessons kept).
3. Phone budget held; gate and smoke by parts green; changelog entry.
