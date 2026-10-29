# QUEUE — top is next. The parser reads only uncommented T-NNNN lines; ticket files hold evidence and acceptance.
# The owner sets the order; every re-rank is logged in QUEUE_ORDER.md. Work top-down, skipping a blocked ticket or a
# LIVE claim (a claim past the 3h run window is a dead run, and `claim` takes it). Read each ticket before you claim it.
#
# STANDING RULES
# - Add a finding to the ticket it was found in before filing a new one. `ticket.mjs new` refuses at 140 queue lines
#   (T-1295) unless `--anyway --why "<reason>"`.
# - A follow-up goes to the band of its KIND (owner, 2026-10-20): performance, GPU, memory and frame-time work to the foot of
#   band 1; a building's to that building's band, beside its own tickets; loop operations (tooling, lap, claims, bake and
#   rederive faults, measurement gaps) to the foot of band 9 (owner, 2026-09-27), unless dev's gate is red or the build in
#   hand cannot finish without them.
# - A decision only the owner can make: `ticket.mjs ask`. The ticket keeps its place and runs skip it until answered.
# - Human figures are drawn once the portable-humans tickets (8C) render them, and Native and Metis people may be depicted
#   on informed, evidence-bounded judgement (owner, 2026-10-16; T-2672 updates the standing constraint).
#   Keep review flags and reasons; they do not veto release. The August gathering is excluded from 1 July 1835.
#   Black residents, families and businesses stay identified. Respect needs_bake and every ticket-level blocker.
# - Order (owner, 2026-10-16; band 9 moved up 2026-10-20): the performance and GPU group (band 1), loop operations (band 9),
#   1904 structures already in progress (band 2), the Navigator interface (band 3), then the balance of Prairie Avenue
#   1904 (band 7, nearest Glessner first), then the portable humans (8C). The Unreal holds are commented out, by hand only.

# --- 1. PERFORMANCE AND GPU — the whole optimization group, cleared first (owner, 2026-10-16: "move all of those gpu and performance
# ---    tickets above all of the house tickets let's clear those first"; earlier the same day: "clear all of the optimization tickets").
# Owner, 2026-10-16: "in a browser on mobile we get memory crashes and it's getting jittery ... keep it simple and lightweight ... rely on the local cpu gpu". Mobile performance and memory group T-2546..T-2558 (not T-2552), dependency order: measure, cut CPU/geometry, cut textures, smooth frames, then the WebGPU spike (T-2558, ruled (a) 2026-10-16). Same day: "tap into local computing resources ... based on the browser and platform or ... a big package app download that happens up front" added T-2559 (device profile), T-2560 (prebuilt town), T-2561 (download the year to disk).



# --- 9. LOOP IMPROVEMENTS — operations: the loop's own tooling (lap, claims, merge, gates, tickets). Owner, 2026-10-20: right under
T-3173 — 1904 desktop memory 1171.2 MB over its 1125 MiB ceiling: unmeasured since 2026-10-24 while the frame-time nightly died installing Playwright on ubuntu-26.04 (T-3169 un-blinded it on PR #1339); bring the 1904 scene down or argue a new ceiling in tools/memory_ceilings.json with its reading
# ---    the performance band, and GPU or performance follow-ups go to band 1, a building's to its own band, not here.

# --- 2. 1904 STRUCTURES IN PROGRESS — every Prairie Avenue house already begun, finished next (owner, 2026-10-16: "finish any
# ---    existing in progress buildings in 1904"): Keith (1808), Glessner's sign-off, 1621-1625, 1637, then 1801, 1812 and 1811,
# ---    whose K01 massing pieces have merged.
# Owner, 2026-10-13: "Sure" (move T-1882 to the top) — 1808 Prairie rebuilt to its photographs, thread "Keith house vs photos"; T-1883 waits on it and takes this line when it merges.
# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
# Owner, 2026-10-13, with the 1887-91 Prairie Avenue sidewalk postcard: "we want to emulate this" (curbs and carriage walks, parkway trees with a Trees setting, soft surface edges). T-2473..T-2475, worked interactively in thread "Prairie Avenue streetscape", one PR each.
# Owner, 2026-10-13, thread "1812 structures": "For 1812 did I ask you to build the other buildings from that era ... all known structures from history"; card answer "After Prairie group"; "You can include native lodges as documented" (T-2490); card answer "Move to 14 August" (T-2490 moves the 1812 scene date first). T-2485 and T-2486 wait on T-2484 (same site) and take its line in turn.
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).

T-1890 — Finish 1801 Kimball corner mansion architecture
# Owner, 2026-10-28, thread "Rework Pullman estate photo match": 1729 Prairie "is still way off from a photographic match ... you need to reenter the photographic match". Reopened in place (they had closed through split pieces without their image gate, T-3235); worked interactively, one PR each.
T-1881 — Finish 1729 Pullman main house architecture
T-1934 — Refine Pullman stable, additions and conservatory estate
T-3164 — Pullman's glasshouses and lodge across 18th Street: the north-south and east-west GREEN HO. ranges traced off Sanborn sheet 28 and stood from the K13 kit's span form, the east range's rounded end, and the two-storey brick lodge at their angle

# --- 3. THE NAVIGATOR — the interface work from the owner's Navigator design doc (owner, 2026-10-16: "then we do all of this
# ---    interface work, follow that with the balance of buildings in 1904"). Filed into this band in dependency order.
# Order: the two card bugs from the review and the gold/silver/bronze grade colors, then E1 arrival, E2 the Navigator shell, the string table, E3 HUD, E4 Jaunts, E5 the
# building dossier (summary record, Glessner pilot, Inspect), E6 Confidence view, E7 Move, E9 Map/Jump/Settings with Researcher
# mode, sound and the field log (owner rulings 2026-10-16), E8 Guide and Tour, then the E10 content gates. Each ticket names what
# it waits on under "Depends on"; take the next workable one while a dependency is open. Spec: chicago-tickets
# evidence/navigator-mk2-2026-10-16/DESIGN.md. NAV-1006 (student playtest, T-2670) is held in band 8F.
# Owner, 2026-10-20: sound off by default; the gaze tag to the right nav under the address, smaller, fading by default (T-2941, T-2942, one PR).

# --- 7. SOUTH THROUGH TIME — PRAIRIE AVENUE 1904, ARCHITECTURAL ASSET PROGRAMME (T-1837)
# Umbrellas T-0475, T-0476 and T-0477 were closed as split into the T-1837 children below (2026-10-16); their files keep the scope.
# Owner, 2026-10-01: “Go”; “Push the tickets to dev queue in one group below”.
# One contiguous group below all existing work. Dependencies first; individual dependency and needs_bake gates remain in each ticket.
# Owner, 2026-10-08: "a controlled set of tickets to do an initial pass of the whole district ... then the tickets later for each building can refine
# your initial serviceable good draft model layer". Order: reconciliations, components, then the DISTRICT DRAFT PASS (T-2159 the 18th-20th block and the
# draft builder, T-2160 16th-18th, T-2161 20th-22nd, T-2162 the edges, T-2163 the grounds and the whole-district phone walk), then the per-building
# REFINEMENT tickets ("Build ..." retitled "Refine ..."), each depending on its block's draft. The draft pass is capped at five; it splits only in halves.
# Owner, 2026-10-11: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". The Glessner group (T-2201, T-2207..T-2228, audit order) runs here one at a time: each later
# ticket waits in 8b on the one before it and takes this line when that PR merges (same house, owner 2026-10-10 "one at a time").
# Owner, 2026-10-14: "can you move the tickets up that are the building around Glessner, like build out from Glessner north and south, where we refine each building". Below the Glessner line, the two bake faults and the structures already in progress (owner, 2026-10-14: "Keep anything near the top of that prairie queue that is already a structure in progress, finish those and move on to the stuff nearest Glessner": 1638, 1619-1625, 1637), the refine work runs nearest-first by distance from 1800 Prairie, both sides of the street and both directions; a house's Refine before its Finish, back-lot service tickets after their side of the block, boundaries after those, edges and block checks last.
T-3239 — 1906 Prairie's pictures worked to matches: the mansard photograph's 1900-or-1906 attribution settled against the register, the 1896 lakeshore item set aside as no view of the house, the c.1914 west-side elevation drawing's 1906 front found and weighed, the 1898 strip's panel solved, and every 1906 match record brought to matches (after the piece before it)
T-3242 — 1701 Prairie's two-level columned rear veranda with its balustrades and garden steps, and the rear range's corbelled oriel, against the rear photograph
T-1876 — Finish 1701 Hibbard house and rear veranda architecture
T-1904 — Refine 1905 Marshall Field Sr. mansion envelope
T-1905 — Finish 1905 Marshall Field Sr. mansion architecture
T-1932 — Refine north-west alley coach houses and service courts
T-1899 — Refine 1912 Moulton-Lowden Chateauesque house envelope
T-1900 — Finish 1912 Moulton-Lowden Chateauesque house architecture
T-1906 — Refine 1919 Field Jr. post-1902 enlargement envelope
T-1907 — Finish 1919 Field Jr. post-1902 enlargement architecture
T-1908 — Refine 1923 Kellogg and 1945 Armour-Corwith corner
T-1936 — Refine east 1800-1900 service buildings
T-1933 — Refine north-east rear service buildings
T-1943 — Finish north-block boundaries, gardens and frontage fittings
T-1901 — Refine 1916-1930 identity and 1936 Allerton estate envelope
T-1902 — Finish 1916-1930 identity and 1936 Allerton estate architecture
T-1935 — Refine west 1800-1900 service buildings and Glessner boundary
T-1944 — Finish 18th-20th block boundaries, gardens and frontage fittings
T-1912 — Refine 2001, 2003 and 2005 attached row
T-1913 — Refine 2009 Mayer-Meyer French Gothic house envelope
T-1914 — Finish 2009 Mayer-Meyer French Gothic house architecture
T-1909 — Refine 2000 and 2010 detached frame houses
T-1910 — Refine 2018 and 2026 masonry houses
T-1915 — Refine 2011 Romanesque house beside Mayer
T-1916 — Refine 2013 Reid classical house
T-1917 — Refine 2017, 2021 High and 2027 Cobb-associated group
T-1918 — Refine 2031, 2033 and 2035 limestone row
T-1911 — Refine 2036 Buckingham corner house
T-1919 — Refine 2100 Sherman Victorian Gothic house envelope
T-1920 — Finish 2100 Sherman Victorian Gothic house architecture
T-1924 — Refine 2101 and 2109 Roloson neighbours
T-1921 — Refine 2108 Mark Kimball and 2112 Rothschild
T-1922 — Refine 2110 Rees at its historical site envelope
T-1923 — Finish 2110 Rees at its historical site architecture
T-1925 — Refine 2115 Armour Second Empire house
T-1926 — Refine 2120 and the 2126 Robbins construction phase
T-1930 — Refine 2123 masonry and 2125 frame neighbours
T-1931 — Refine 2127-2129 flats and 2141 non-building frontage
T-1938 — Refine south-east service buildings
T-1927 — Refine 2130 Murdoch rounded-bay house
T-1928 — Refine 2140 Tucker-Smith corner mansion envelope
T-1929 — Finish 2140 Tucker-Smith corner mansion architecture
T-1937 — Refine south-west service buildings and shared Rees coach house
T-1945 — Finish 20th-22nd block boundaries, gardens and frontage fittings
T-1939 — Refine 213, 215 and 217 East Twentieth Street context
T-1940 — Refine 2008 Calumet Hanford exterior
T-1941 — Refine 2018 Calumet Wheeler-Kohn exterior
T-1942 — Refine Second Presbyterian post-1900 exterior skyline
T-1946 — Close side-street and rail-side background gaps
T-1948 — Verify the completed 18th-20th Prairie streetscape
T-1947 — Verify the completed 16th-18th Prairie streetscape
T-1949 — Verify the completed 20th-22nd Prairie streetscape
# Owner, 2026-10-28 (decision card "Reopen them below Pullman"): eight houses that had closed through split pieces without their image gate, reopened in place (T-3235).
T-1868 — Refine 1613, 1615 and 1619 east row
T-1872 — Refine 1708 and 1712 townhouse fronts
T-1886 — Refine 1816 Henderson mansard house
T-1887 — Refine 1824 Marsh altered front and 1828 neighbour
T-1893 — Refine 1815 Sears-Meeker altered house
T-1894 — Refine 1823 Dent house
T-1896 — Finish 1827 Doane twin-tower mansion architecture
T-2484 — 1812: build the Kinzie house, the former Point du Sable house on the north bank opposite the fort, with its piazza, fenced green, Lombardy poplars and two cottonwoods, matched to its pictures

# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-10-08: "move the portable people tickets after the south through time tickets" — moved here, below the whole Prairie Avenue 1904 programme (draft pass, refinements, block checks, Glessner repair).
# Owner, 2026-10-03: had moved it to sit directly above the Prairie Avenue 1904 architectural programme.
# Owner, 2026-09-30: build the human library and browser rendering path before loop optimization; Mark Beaubien is the first end-to-end historical example.
T-1789 — Build the first modular 1835 human library in Blender on the shared portable rig
T-1790 — Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
T-2673 — Mark Beaubien's evidence sheet and Blender master: dated likeness evidence with attested likeness, period analogy and reconstruction kept apart, the figure assembled from the T-1789 library on the shared rig, inspected front, three-quarter and profile renders, and LODs exported through T-1787
T-2674 — Mark Beaubien in the browser: the actor bound to the existing beaubien_mark person at his authored place, idling, walking when driven, greeting, selectable, and handing off to his card
T-2675 — Mark Beaubien inspected and measured in the real 1835 scene at desktop and mobile: close, conversation and street distances checked for contact, scale, shadows, foot slide and LOD popping, with shipped size, triangles, draw calls, texture memory and frame cost recorded and defects fixed
T-1792 — Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly

# --- 8D. PERIOD CARRIAGES AND WAGONS — photographic models, then motion, then boarding/riding (epic T-2791)
# Owner, 2026-10-18: "build tickets for these, place them in the queue in bands below the portable humans";
# first review existing assets and dated photographic evidence, then models, moving distant traffic and interaction.
# T-2792 and T-2799 completed through PR #1174; retain each remaining model's rights, date and needs_bake gates.
T-2793 — Build one articulated period wagon master from the existing wagon families
T-2980 — Upgrade selected covered wagons while preserving their distinct finishes
# Owner 2026-10-21: upgrade covered wagons as ready; preserve their existing visual variety so they do not become clones (follow-up recorded in T-2793).
T-3084 — Match the Brougham body and materials to the 1893 catalogue
T-3085 — Qualify Brougham interfaces and portable distance delivery in town
T-2795 — Animate vehicle running gear and matched draft-horse hitches
T-2796 — Move horse-drawn traffic through distant streets with measured LOD budgets
T-2797 — Board, ride and leave a carriage or wagon with accessible controls

# --- 8E. PERIOD HORSES AND GEAR — photographic animals, tack, riders, then mounting/riding (epic T-2798)
# Horse master and gear supply both wagon/carriage teams and mounted riders; reuse portable-human rig/wardrobe.
T-3088 — Refine the horse anatomy and near silhouette against cleared views
T-3089 — Qualify horse surface materials and portable distance exports
T-2801 — Build period draft harnesses and vehicle hitch assemblies
T-2802 — Build period riding saddles, bridles and horse gear
T-2803 — Rig the horse and author grounded idle, walk and trot clips
T-2804 — Fit portable-human riders and drivers to horses and vehicles
T-2805 — Mount, ride, steer and dismount a horse with accessible controls

# --- 8. UNREAL DELIVERY — LOCAL / QUALIFIED UNREAL ONLY, NOT WORKABLE BY THE REMOTE WEB WORKER (programme T-1356)
# Commented holds, never claimable. Unblock only when every dependency AND a capable executor are proven.
# HOLD T-1472 — on-demand latest-validated Mac build/release; qualified Mac + release access.
# HOLD T-1473 — sinking buildings/terrain contact; qualified Unreal + matched web/source views.
# HOLD T-1358 — after T-1357 and current Unreal/GPU capability receipt.
# HOLD T-1360 — after T-0252, T-1357, T-1358; Unreal visual/collision receipt required.
# HOLD T-1474 — flora corridor; after shared exports/import and placement, Unreal visual/performance proof.
# HOLD T-1475 — map/search/place inspection; runtime provenance and Unreal input/route validation.
# HOLD T-1359 — streaming corruption; affected Mac/Unreal/browser access, after native priorities.
# HOLD T-1361 — after T-1358/T-1359, approved licensed build runner, GPU host, budget and credentials.

# --- 8F. PLAYTESTS — HELD (owner, 2026-10-19: "Let's put all of those playtest tickets in a common band below unreal and hold
# ---     them for now"). Commented holds, never claimable; a run does not prepare their materials until the owner lifts the hold.
# HOLD T-2670 — Student playtest (NAV-1006): 6-8 students aged 14-16, three tasks (find a house, learn who lived there, tell
#     Attested from Reconstructed), 80 % unaided. Needs the owner to arrange the students; T-2663 (tour) and T-2637 (Glessner
#     pilot) have merged, so the task cards and observer sheet can be prepared once the hold is lifted.

# --- 8b. BLOCKED AND WAITING — every ticket that is not workable and not finished
# Commented on purpose: visible to the owner, never claimable. `ticket.mjs block` writes these lines and `check`
# refuses a blocked ticket that is missing from this band (T-1518, T-1541).
# BLOCKED-TECH T-1407 (opened 2026-09-19, META) — The crews of the vessels in port and the harbour-works gang seated, once a committed source gives a schooner her comp…
#     waits: a committed source giving an 1830s Great Lakes schooner her complement, and the Chief Engineer's 1835 harbour-works report. Neither is in the corpus.
T-2023 — Seat the lodging remainder as lodging roofs rise: 7 West adults the book orders with no free bed, and 44 boarding-house and inn households waiting on roofs. T-1538's frozen top-up deals new roofs to them automatically
# BLOCKED-TECH T-2365 (opened 2026-10-11, SOUTH_TIME) — K14 compared beside a newer neighbour: 1708 Prairie, an empty lot on the 1886 Robinson plate, takes the kit at its own …
#     waits: T-1872
T-2372 — Match Eliza Chappel's infant school to its pictures
T-2373 — Match the 1832 lighthouse to its pictures
T-2374 — Match Cobweb Castle to its pictures
T-2375 — Match the Dearborn Street drawbridge to its pictures
T-2376 — Match the Green Tree Tavern to its pictures
T-2377 — Match Hogan's store, the first post office to its pictures
T-2378 — Match J. B. Beaubien's homestead to its pictures
T-2379 — Match the Lake House under construction to its pictures
T-2380 — Match the log jail to its pictures
T-2381 — Match the Miller House to its pictures
T-2382 — Match Philo Carpenter's log shop (the Sauganash's log wing) to its pictures
T-2383 — Match the Sauganash Hotel to its pictures
T-2384 — Match St Mary's church to its pictures
T-2386 — Match the Wolf Point Tavern to its pictures
T-3041 — Match the first Fort Dearborn buildings against every reference picture
T-2388 — Match the second Fort Dearborn (1835) to its pictures, every building in it
# BLOCKED-TECH T-2163 (opened 2026-10-08, SOUTH_TIME) — Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all thre…
#     waits: T-2983 — the grounds and the whole-district walk need every draft standing; T-2162 split into T-2982 (named context buildings, #1180, merged) and T-2983 (the background census), so this waits on T-2983
T-3043 — Guide's glossary tap check finds no locked term on Home since its Confidence view tile became a button
T-3246 — Marble look target for Glessner: one photo-generated world beside our render, evidence only
T-3247 — Budget-filled detail for trees and furniture: per-device instance budget, nearest and view-centre first
