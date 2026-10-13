---
id: T-2474
title: Prairie Avenue 1904 curb with its reveal, the walk and parkway at curb height, carriage blocks and carriage walks across the parkway
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
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

Prairie Avenue 1904 curb with its reveal, the walk and parkway at curb height, carriage blocks and carriage walks across the parkway.

## The owner's ask (2026-10-13, project thread "Prairie Avenue streetscape")

> Something else that would be nice, I am looking at this street scape and we want to emulate this. Look at the curb height and make sure we are correct on that, with correct carriage walk ways, and add street foliage trees correctly, would be nice to in options to be able to hide trees or make them spring trees barely blooming so you can see the house with the trees shown but you can still see the house, default should have the correct trees, you should be able to use the models from 1835 for flora as a base. If it's easy to add some correct bushes or other foliage with the houses please do, but you will have that as part of the house passes to add the correct flora for each. Also when flying or walking over street areas that are transitional between surfaces it's looks jagged and harsh, that should fade, in some way there should be a transition

"This image" is the Holzman postcard postmarked 1908, the library's `st-ghm-postcard-1908-prairie-south-at-18th`: the west sidewalk at 18th Street beside Glessner, looking south. The same negative is `st-picturesque-chicago-1892-prairie-avenue-p199`, `st-flinn-1892-looking-south-prairie-from-18th` and `st-flinn-1891-a-bit-of-prairie-avenue`, so the photograph dates Dec. 1887 to 1891, 13-17 years before the scene date. Supporting views: `st-views-of-chicago-1905-prairie-and-michigan-avenues` (a single row of closely spaced elms in the parkway, dressed-stone carriage blocks along the parkway edge), `st-chicagology-prairie-avenue-about-1890-photo` (carriage blocks at the curb, bare parkway elms), `st-ghm-ward-1887-prairie-north-from-20th` (a continuous row of parkway trees on both sides), `st-ghm-1700-1706-under-construction-1901` (a freshly planted sapling in the parkway), `st-randmcnally-1910-pullman-corner-18th` (young parkway trees on the 18th Street corner), and HABS Glessner nos. 2 and 3 (c. 1923: a paved crossing from the door to the curb, a young parkway tree).

Worked interactively in that thread; the three tickets T-2473, T-2474 and T-2475 are its pieces, one PR each into dev.

## What to build

T-0474 / T-1728 lay the walk, parkway and curb flat on the ground with no reveal (L293: "no crown, gutter or curb reveal ... because no source read so far gives either"). The 1887-91 photograph and the c. 1923 HABS views show a stone curb standing proud of the roadway.

1. **The curb reveal.** Raise the sidewalk space (curb top, parkway, walk) above the carriageway by a curb reveal argued from period practice (city specifications or engineering texts of 1890-1905 if one can be read; otherwise a bounded reconstruction, recorded as a liberty), with a dressed vertical curb face down to the roadway and the code's cross-fall (1 in in 3 ft toward the curb, 1905 code "Slope" sections). The walker stands on it; nothing floats or sinks at the lot line.
2. **Carriage blocks.** Dressed stone carriage (mounting) blocks at the curb in front of the houses, as the 1905 and c. 1890 views show.
3. **Carriage walks.** A paved crossing over the parkway from the walk to the curb at each house entrance (HABS no. 2 shows one at Glessner c. 1923), reconstructed for 1904 and recorded as such.

## Acceptance

1. A street-eye render at the curb shows the reveal, the curb face and a carriage block, side by side with the 1887-91 photograph in the PR.
2. No z-fighting, floating or buried edge at the curb, the lot line or the corners at street-eye level; walking onto and off the walk is smooth.
3. L293 updated (the reveal is now drawn, with its basis); cards for the curb, carriage blocks and carriage walks.
4. Phone budget held; gate and smoke by parts green; changelog entry.

## Owner's second picture (2026-10-13, 17:10 UTC)

"Found this also you may already have bit it shows the curbs nicely": a black-and-white street
photograph of a Prairie Avenue block face in winter (bare parkway elms, high stoops with stone
balustrades, a stone curb standing proud of a light roadway, the walk and parkway level with the
curb), 482 x 328 px, sha256 12b9f8ca6c1b0e76bcd07d34aab116de6f7d2da08baab3f2d92213b7c96d5872.
It looks like the library's `st-chicagology-prairie-avenue-about-1890-photo` (bare elms, high
stoops, stone balustrades); confirm against that record before citing it. Commit it beside the
postcard under `data/sources/assets/` and read the curb reveal off it against a known riser height.
