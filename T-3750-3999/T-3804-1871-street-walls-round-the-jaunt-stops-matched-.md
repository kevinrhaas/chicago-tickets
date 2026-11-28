---
id: T-3804
title: 1871 street walls round the jaunt stops matched to the period street views: Lake, Clark, LaSalle, State and Washington
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: null
claimed_by: run 11/27/2026, 11:46:45 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-28T05:46:46.371Z
decision: null
decision_answer: null
---

Kevin, 2026-11-27 (thread "Make 1871 jaunt streets photo-accurate"): *"I would like you to do more street improvements to the areas around the jaunt stops, the most historic and important areas. Do what research you can on the surrounding areas of the jaunts and photo match the best you can to the surrounding street. If you need to, use period photos to infer and reconstruct the street scape, businessess, street furniture etc. the signs above stores must need to be varied and be more specific based on your research of the citizens and people and businesses in 1871, build and extend a group of tickets to improve 1871, and claim and start to work them in parallel to make it photographic match perfect with 1871, add whatever is needed to make it shockingly accurate"*

**Where:** the streets round every 1871 jaunt stop (The Great Chicago Fire, The Last Sunday, A Message for the Opera House, Who Started the Fire?): the detail rings in `data/context/1871/detail-rings.json` (Court House square, State Street Lake to Monroe, Dearborn and Madison, Washington State to Dearborn, Lake and Clark, DeKoven at Jefferson, Chicago Avenue at Pine, the Clark and State bridges), extended where a stop looks down a street the rings miss. Photographic only round the stops, cheap elsewhere; Bill Tyre's UHD 630 and the phone stay smooth (light tier inside its ceiling); site storage budget respected.

**References:** `/mnt/project-files/1871-references/` (Lake Street stereoview late 1860s, Kurz LaSalle from Court House square 1865, from the Court House cupola c1858, State Street horse cars, Library Hall), the LOC stereographs already in `data/sources/` (1s12325 Court House, 1s12371 Sherman House, 1s47902 Crosby's, 1s47905 Tremont), Andreas vol. 2 plates, and `edwards_chicago_directory_1871` (full text: archive.org edwardsannualdir141871chic, djvu.txt).

**What:** the street walls round the stops are generic kit fronts. Match them, block by block, to what the period street views show.

- Solve a camera on each usable street view (Lake Street stereoview, Kurz LaSalle 1865, the State Street views, the Court House cupola panorama for roofs) into `data/reference_views/`, render with `tools/photo_match.mjs`, and work the differences down (AGENTS.md rules 11 and 12, the stopping rule's good-enough bar).
- What to match: storey counts and heights, Italianate stone fronts with hooded arched windows, mansard roofs and dormers, iron balconies, cast-iron storefront arcades, stoops and areaways, raised entrances, party walls stepping, chimney rows, roof signs; frame fronts with false fronts where the photos show them.
- Named blocks from the directory (Cobb's Block, Link's Block, Dickey's Building, the Honore Block ...) where they stand on a stop's faces.

**Acceptance:** each solved view has a match record; the visible differences (over the bar) are closed or written down; before/after side-by-sides, desktop and phone.
