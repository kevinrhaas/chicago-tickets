# QUEUE — top is next. The parser reads only uncommented T-NNNN lines; ticket files hold evidence and acceptance.
# The owner sets the order; every re-rank is logged in QUEUE_ORDER.md. Work top-down, skipping a blocked ticket or a
# LIVE claim (a claim past the 3h run window is a dead run, and `claim` takes it). Read each ticket before you claim it.
#
# STANDING RULES
# - Add a finding to the ticket it was found in before filing a new one. `ticket.mjs new` refuses at 140 queue lines
#   (T-1295) unless `--anyway --why "<reason>"`.
# - Loop follow-ups (tooling, lap, bake and rederive faults, deal and seating refinements, measurement gaps) go to the
#   foot of band 9 (owner, 2026-09-27), unless dev's gate is red or the build in hand cannot finish without them.
# - A decision only the owner can make: `ticket.mjs ask`. The ticket keeps its place and runs skip it until answered.
# - No human figure is drawn. Native, Metis and Black residents, families and businesses are reconstructed in the data
#   layer, review_required (AGENTS.md, standing constraint). Respect needs_bake and every ticket-level blocker.
# - Order (owner, 2026-10-16): the performance and GPU group (band 1), 1904 structures already in progress (band 2), the
#   Navigator interface (band 3), loop follow-ups (band 9), then the balance of Prairie Avenue 1904 (band 7, nearest
#   Glessner first), then the portable humans (8C). The Unreal holds are commented out, by hand only.

# --- 1. PERFORMANCE AND GPU — the whole optimization group, cleared first (owner, 2026-10-16: "move all of those gpu and performance
# ---    tickets above all of the house tickets let's clear those first"; earlier the same day: "clear all of the optimization tickets").
# Owner, 2026-10-16: "in a browser on mobile we get memory crashes and it's getting jittery ... keep it simple and lightweight ... rely on the local cpu gpu". Mobile performance and memory group T-2546..T-2558 (not T-2552), dependency order: measure, cut CPU/geometry, cut textures, smooth frames, then the WebGPU spike (T-2558 waits on a ruling). Same day: "tap into local computing resources ... based on the browser and platform or ... a big package app download that happens up front" added T-2559 (device profile), T-2560 (prebuilt town), T-2561 (download the year to disk).
T-2596 — Glessner v4 in KTX2: the full and light derivatives re-encoded, the light tier capped at 1024, the three-file package repacked with its hashes, the baseline page and report reading the new files, and every Glessner photo-match still matching
T-2592 — Frame governor's moving reading: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read where a frame costs inside the governor's range (the steward runner's SwiftShader draws one in 2.3 to 3.6 s)
T-2600 — Every other spatialBatch caller through the job pool: streets, yards, railway, building cells and terrain's re-batch of the distant ground, each awaiting it with identical output
T-2604 — The flora lattice walk in the job pool: scatter's cells, cone cull, deal ranks and jitter as a three-free kernel a spread pass awaits on a worker, slot for slot the in-frame walk (a check.sh gate), with the spread pass's main-thread milliseconds quoted before and after at the throttled phone profile
T-2605 — The rest of the flora re-deal off the main thread (zones, water, floors, verges and heights read in the worker), double-buffered so the old lattice draws until the new one arrives, with measure_walk_frames at the throttled phone profile: no flora or spatial-batch long task over 50 ms in walk and turn, moving p95 down, boot to ready quoted before and after
T-2560 — Ship the town prebuilt: run the layer builders at publish and ship frontage and spatial-batch buffers as compressed binaries, so a phone uploads the town instead of building it at every boot
T-2561 — Download the year to the device: a service worker installs a versioned per-year pack to disk with progress, boots offline, updates only changed files, installs to the home screen, and has a kill switch
T-2557 — GPU-procedural near grass: the near ring dealt in the vertex shader from the lattice's own hash, the heightfield and the ground masks, with no CPU lattice and no re-deal on move
T-2558 — H0, the WebGPU bake-off RENDERING.md planned and never started: three WebGPURenderer and TSL on the Glessner block from the same GLBs, kill criteria written first
#   ? T-2558 DECISION: RENDERING.md section 8 keeps Track 2 (the WebGPU renderer) gated. May a run start H0, the no-build WebGPU bake-off on the Glessner block, with its kill criteria written into section 8 first? — (a) Yes, once T-2546's memory meter has landed, so walk/ and the spike are compared on the same instrument  (b) Yes, now, in parallel with the memory group  (c) Not yet: finish the memory and smoothness group first and ask again — recommended: (a)
T-2576 — Quantized positions in frontage, enclosures and yard: Int16x4 relative to each chunk with the offset and scale in its matrix, every probe and spatialBatch reader made to apply it, so the four layers reach T-2549's 40 %
T-2602 — T-2598's remaining readings: captures at glessner-aloft-ne and the three street-eye stands (measure_memory --walk prairie --captures), the moving p95 at phone profile on a GPU, and the 1904 memory ceilings re-read with residency

# --- 2. 1904 STRUCTURES IN PROGRESS — every Prairie Avenue house already begun, finished next (owner, 2026-10-16: "finish any
# ---    existing in progress buildings in 1904"): Keith (1808), Glessner's sign-off, 1621-1625, 1637, then 1801, 1812 and 1811,
# ---    whose K01 massing pieces have merged.
# Owner, 2026-10-13: "Sure" (move T-1882 to the top) — 1808 Prairie rebuilt to its photographs, thread "Keith house vs photos"; T-1883 waits on it and takes this line when it merges.
# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
# Owner, 2026-10-13, with the 1887-91 Prairie Avenue sidewalk postcard: "we want to emulate this" (curbs and carriage walks, parkway trees with a Trees setting, soft surface edges). T-2473..T-2475, worked interactively in thread "Prairie Avenue streetscape", one PR each.
# Owner, 2026-10-13, thread "1812 structures": "For 1812 did I ask you to build the other buildings from that era ... all known structures from history"; card answer "After Prairie group"; "You can include native lodges as documented" (T-2490); card answer "Move to 14 August" (T-2490 moves the 1812 scene date first). T-2485 and T-2486 wait on T-2484 (same site) and take its line in turn.
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).

T-2586 — Keith's image gate closed: every reference view of keith_house_1808_prairie reads matches, and T-1883's acceptance checked off
T-2587 — Keith's crown and loggia from the re-fitted cameras: the diamond-point band under the lattice, the north-east boss, a wider north-east pier, taller loggia columns
T-2228 — Glessner: run final photographic comparison and evidence sign-off
T-2435 — Bring the 1621-1625 match records to matches: what the McBirney photograph and the Building Budget drawing still show differently, and the image gate (after the three pieces before it)
T-2536 — 1637 Prairie's c. 1870 Grosvenor photograph weighed as evidence of its own date: its source record, camera and match record, and both match records brought to matches (after the two pieces before it)
T-2539 — 1801 Prairie onto K01 in Bedford stone: the kit lays an all-stone house and carries a round corner tower whose cone stands over the main roof, and the Kimball house moves onto it with the photograph's openings, entrance arches and curved stair (after the piece before it)
T-2540 — 1801 Prairie's roof and 18th Street flank from the Taylor, 1929 and HABS photographs: the front's stone gable, the dormers, the cresting deck, the stacks and the rear elevation, and the envelope's match records brought to matches (after the pieces before it)
T-1890 — Finish 1801 Kimball corner mansion architecture
T-2544 — 1812 Prairie's front detail from the Levy photograph: the balcony over the projection, the third storey's arched windows and fanlight, the stone lower storeys under the brick upper wall with its stone bands, and whatever the first piece's match record left open on the front (after the piece before it)
T-2545 — 1812 Prairie's flanks, rear and the roof behind the gable, and the Levy, c. 1955 and 1915 Tribune match records brought to matches (after the pieces before it)
T-1885 — Finish 1812 Wheeler shaped-gable house architecture
T-2542 — 1811 Prairie's roofs from the photograph and the Inland Architect plate: the front bay's stone gable with its arched lights and fretwork balcony, the entrance block's pyramid and finial, the main slate roof, the north flank's stepped brick gable and the stacks; the plate's camera and match record, and the envelope's match records brought to matches (after the piece before it)
T-1892 — Finish 1811 Coleman-Ames Romanesque house architecture

# --- 3. THE NAVIGATOR — the interface work from the owner's Navigator design doc (owner, 2026-10-16: "then we do all of this
# ---    interface work, follow that with the balance of buildings in 1904"). Filed into this band in dependency order.

# --- 9. LOOP IMPROVEMENTS — a follow-up a run files lands at this band's foot (owner, 2026-09-27)
T-2606 — The yards' sward test indexed: suppressesSward scans every fenced interior's bounding box for every lattice slot (2.3 s of a 7.5 s flora profile at 4x/390x780, the largest single flora cost), so a cell grid like flora's circleGrid answers it with identical answers at every slot

# --- 7. SOUTH THROUGH TIME — PRAIRIE AVENUE 1904, ARCHITECTURAL ASSET PROGRAMME (T-1837)
# Umbrellas T-0475, T-0476 and T-0477 are references only; their execution is delegated to the T-1837 children below.
# Owner, 2026-10-01: “Go”; “Push the tickets to dev queue in one group below”.
# One contiguous group below all existing work. Dependencies first; individual dependency and needs_bake gates remain in each ticket.
# Owner, 2026-10-08: "a controlled set of tickets to do an initial pass of the whole district ... then the tickets later for each building can refine
# your initial serviceable good draft model layer". Order: reconciliations, components, then the DISTRICT DRAFT PASS (T-2159 the 18th-20th block and the
# draft builder, T-2160 16th-18th, T-2161 20th-22nd, T-2162 the edges, T-2163 the grounds and the whole-district phone walk), then the per-building
# REFINEMENT tickets ("Build ..." retitled "Refine ..."), each depending on its block's draft. The draft pass is capped at five; it splits only in halves.
# Owner, 2026-10-11: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". The Glessner group (T-2201, T-2207..T-2228, audit order) runs here one at a time: each later
# ticket waits in 8b on the one before it and takes this line when that PR merges (same house, owner 2026-10-10 "one at a time").
# Owner, 2026-10-14: "can you move the tickets up that are the building around Glessner, like build out from Glessner north and south, where we refine each building". Below the Glessner line, the two bake faults and the structures already in progress (owner, 2026-10-14: "Keep anything near the top of that prairie queue that is already a structure in progress, finish those and move on to the stuff nearest Glessner": 1638, 1619-1625, 1637), the refine work runs nearest-first by distance from 1800 Prairie, both sides of the street and both directions; a house's Refine before its Finish, back-lot service tickets after their side of the block, boundaries after those, edges and block checks last.
T-1874 — Refine 1726, 1730 and 1736 replacement/altered houses
T-1886 — Refine 1816 Henderson mansard house
T-1893 — Refine 1815 Sears-Meeker altered house
T-1880 — Refine 1729 Pullman main house envelope
T-1881 — Finish 1729 Pullman main house architecture
T-1934 — Refine Pullman stable, additions and conservatory estate
T-1894 — Refine 1823 Dent house
T-1887 — Refine 1824 Marsh altered front and 1828 neighbour
T-1895 — Refine 1827 Doane twin-tower mansion envelope
T-1896 — Finish 1827 Doane twin-tower mansion architecture
T-1873 — Refine 1720 Walker frame villa
T-1878 — Refine 1719-1721 Dexter address and altered house envelope
T-1879 — Finish 1719-1721 Dexter address and altered house architecture
T-1888 — Refine 1834 Jones post-1886 mansard
T-1903 — Refine 1901 Ream post-fire house
T-1872 — Refine 1708 and 1712 townhouse fronts
T-1877 — Refine 1709 Palmer Kellogg successor
T-1897 — Refine 1900 Elbridge Keith corner house
T-1871 — Refine 1700-1706 Glessner family townhouses
T-1898 — Refine 1906 Edson Keith and attached 1908
T-1875 — Refine 1701 Hibbard house and rear veranda envelope
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

# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-10-08: "move the portable people tickets after the south through time tickets" — moved here, below the whole Prairie Avenue 1904 programme (draft pass, refinements, block checks, Glessner repair).
# Owner, 2026-10-03: had moved it to sit directly above the Prairie Avenue 1904 architectural programme.
# Owner, 2026-09-30: build the human library and browser rendering path before loop optimization; Mark Beaubien is the first end-to-end historical example.
T-1789 — Build the first modular 1835 human library in Blender on the shared portable rig
T-1790 — Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
T-1791 — Build Mark Beaubien as Chicago 4D's first historical portable human, from Blender master to interactive browser actor
T-1792 — Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly

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

# --- 8b. BLOCKED AND WAITING — every ticket that is not workable and not finished
# Commented on purpose: visible to the owner, never claimable. `ticket.mjs block` writes these lines and `check`
# refuses a blocked ticket that is missing from this band (T-1518, T-1541).
# BLOCKED-TECH T-1407 (opened 2026-09-19, META) — The crews of the vessels in port and the harbour-works gang seated, once a committed source gives a schooner her comp…
#     waits: a committed source giving an 1830s Great Lakes schooner her complement, and the Chief Engineer's 1835 harbour-works report. Neither is in the corpus.
T-2023 — Seat the lodging remainder as lodging roofs rise: 7 West adults the book orders with no free bed, and 44 boarding-house and inn households waiting on roofs. T-1538's frozen top-up deals new roofs to them automatically
# BLOCKED-TECH T-2162 (opened 2026-10-08, SOUTH_TIME) — Draft the district's edges: East Twentieth Street, Calumet, Second Presbyterian and the side-street and rail-side backg…
#     waits: T-2161 — every building this ticket names except Second Presbyterian (213/215/217 East Twentieth: parcels e20th south of blk_indiana_prairie_20_21; 2008 and 2018 Calumet: calumet west of blk_prairie_calumet_20_21) stands on Sanborn 1911 sheet 35, which has never been traced: tools/trace_prairie_1904_footprints.py SHEETS holds only 20 and 28, and no data/traces/prairie_1904_footprints_s35.json exists. T-2161 (20th-22nd Prairie, claimed by a live sibling run on 2026-10-11) must add the sheet-35 SHEETS entry, tune the tracer for that sheet's 1602x2000 raster and add sheet 35 to the draft rules. Drafting these edges beside it would write the same SHEETS key, the same s35 trace file and the same rules block twice. Second Presbyterian (1936 S Michigan) is on no committed sheet at all and will need its own footprint source. Chained so settle reopens this in T-2161's queue line when T-2161 merges; if T-2161 is split instead, unblock this when the piece that traces sheet 35 lands.
# BLOCKED-TECH T-2163 (opened 2026-10-08, SOUTH_TIME) — Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all thre…
#     waits: T-2162 — the grounds and the whole-district walk need every draft standing: T-2161 (20th-22nd, blocked on T-2340's sheet-35 trace) and T-2162 (edges, blocked on T-2161) have not landed, and T-2335 (16th-18th east) is in flight; chained so settle reopens this in T-2162's queue line when it merges
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
T-2385 — Match the first Tremont House to its pictures
T-2386 — Match the Wolf Point Tavern to its pictures
T-2387 — Match the first Fort Dearborn (1812) to its pictures, every building in it
T-2388 — Match the second Fort Dearborn (1835) to its pictures, every building in it
# BLOCKED-TECH T-2485 (opened 2026-10-13, SOUTH_TIME) — 1812: build the Kinzie establishment behind the house: dairy, bake-house, the Frenchmen's lodging house, stables, garde…
#     waits: T-2484 — same site, one PR at a time (owner, 2026-10-10): the Kinzie establishment is sited around the house T-2484 builds
# BLOCKED-TECH T-2486 (opened 2026-10-13, SOUTH_TIME) — 1812: build Antoine Ouilmette's house and garden close behind the Kinzie house, and Pettell's small cabin near it
#     waits: T-2485 — same site, one PR at a time (owner, 2026-10-10): Ouilmette's and Pettell's houses stand behind the Kinzie establishment
T-2608 — Navigator arrival: a two-line year readout, DESTINATION 1904 · PRAIRIE AVE above the ticker from first paint and the ticker rolling from the present year down to the destination, with the 'Destination year' label removed
T-2609 — Navigator: the building card's two review bugs fixed now: 'bay dining [object Object]' under Attributes, and the 1835 fire-limit by-law shown on a 1904 building
T-2610 — Navigator arrival: a two-line year readout, DESTINATION 1904 · PRAIRIE AVE above the ticker from first paint and the ticker rolling from the present year down to the destination, with the 'Destination year' label removed
T-2611 — Navigator arrival: time-stream captions, a graded and sourced deck of 8-12 landmark years per destination shown as the ticker passes each one (at most 3 on fast loads, 8 on slow)
T-2612 — Navigator arrival telemetry: Payload, Link and ETA kept, a YEARS TO GO counter added, the six lamps regrouped as STREETS, BUILDINGS, TREES and PEOPLE on the real boot phases, and log lines from the destination deck
T-2613 — Navigator landing replaces Tap to enter: the last digit clunks into place, an ARRIVED flash, the device flips to Navigator Home and the scene un-blurs, with #gate-btn and the Welcome card retired behind a small js/journey.js state machine
T-2614 — Navigator gesture gating without a gate: audio and pointer lock start on the first Home choice, canvas tap or Navigator control, desktop shows CLICK TO ENGAGE LOOK until lock, and iOS Safari logs no autoplay errors
T-2615 — Navigator portal continuity: an arrival within 10 s of the Observatory's transfer opens with the ring's tail still expanding, so the jump reads as one shot
T-2616 — Navigator arrival failure state: 'The jump stalled somewhere around 1950.' with TRY AGAIN and BACK TO THE OBSERVATORY, and the error detail collapsed under 'Details for your teacher'
T-2617 — Navigator device: the handheld that replaces the drawer, a phone bottom sheet with DOCK, HALF and FULL detents, a 400 px desktop panel that collapses to its rail, the bezel and screen-code header, and the Home app
T-2618 — Navigator app registry and contextual rail: navigator.register with when(ctx) and badge(ctx), icons that slide in and out within 240 ms with a lamp-amber first-appearance dot, at most 10 icons
T-2619 — Navigator dock: when closed it always shows a status lamp, the NAVIGATOR label, the year and the current app's icon, and one tap or swipe up opens the last app at HALF
T-2620 — Navigator: the drawer's panels move into Navigator apps, goto, people, businesses, evidence and settings mounted inside apps with every element id the smoke reads intact, and the hamburger drawer retired
T-2621 — Navigator deep links and back: ?nav=app[:id]&tab= opens that app after landing, and the browser back button closes the current app before leaving the page
T-2622 — Navigator keyboard and accessibility: N toggles it, 1-9 select rail apps, Esc closes, the rail is a tablist of tabpanels, focus moves into the app on open and is always visible
T-2623 — Navigator telemetry strip: a phosphor footer ticking every 800 ms with FIELD, DRIFT, SIG and a RECALL lamp, reusing portal.js drift, aria-hidden, paused when hidden and still under reduced motion
T-2624 — Navigator string table and glossary terms: every Navigator, HUD and arrival string in one table, the locked terms enforced and the renamed terms of §03 applied
T-2625 — HUD declutter: Start/Jaunts, the Confidence chip and caret, pace, theme and menu leave the HUD's top row, each reachable in the Navigator, and the street readout becomes a 2 s toast
T-2626 — HUD year chip and compass-map instrument: an amber LED year chip top left that opens Jump, and the compass and mini map merged into one round instrument top right that opens Map
T-2627 — HUD target tag and quick column: a 400 ms reticle dwell shows the building's name and distance, tap or E opens Inspect, and the quick column holds Walk/Fly plus a contextual Inspect key, never more than two
T-2628 — HUD footprint budget: the HUD covers 10 % or less of a 390x844 viewport and respects safe areas, measured by the smoke
T-2629 — Dev chrome off the phone screen: the DEV pill and build stamp move to Settings › About on phones
T-2630 — Navigator Jaunts app: Jaunts · Go to · Free roam segments, opened from the Home choices and the rail, the Welcome card's three choices kept permanently
T-2631 — Navigator Jaunt cards: plate, title, premise, minutes, stops and keepsake state for each route, with a Jaunt in progress pinned on top with Continue that survives a reload
T-2632 — Navigator Go to cleanup: zero-result chips hidden, titles wrapping to two lines, every row showing distance and bearing, filters Places · People · Shops & work · Viewpoints
T-2633 — Navigator Go to follows the Confidence view: the 'Include reconstructed roofs' checkbox removed, and results of a hidden grade shown dimmed with the reason
T-2634 — Navigator Free roam: docks the Navigator and shows the one-time tip 'Tap any building to inspect it.'
T-2635 — Building summary record: the data/summaries/<id>.json schema, its compiler into what the Inspect app reads, and a gate refusing a fact with no grade, an Attested fact with no source, a string over its length or an id or path in a string
T-2636 — Building fallback summary: a building with no summary record gets one templated from its sidecar, never raw fields, never ids, paths or snake_case
T-2637 — Glessner House summary record, the pilot: every line mapped to a graded fact in the Glessner research or a source record, fact-checked, and approved by the owner as the pattern for every other building
T-2638 — Navigator Inspect app, the Overview front page: plate, address, name, status chips, summary, key facts, residents, Look for, Notable facts and the Confidence meter, replacing the floating building card
T-2639 — Navigator Inspect tabs: Overview · People · Design · Story · Photos · Sources, a new building always opening on Overview, and the People tab listing who lived, worked or visited in the scene year, then before and after
T-2640 — Navigator Inspect 'Show me': each Look for feature turns the camera to it in 900 ms and pulses an outline for 2 s, moving to a viewpoint first in fly mode
T-2641 — Navigator Inspect Design tab: the style card, numbered 'On this house' hotspots with grades replacing the attribute table, Compare styles, and the Richardsonian Romanesque module for Glessner House
T-2642 — Navigator style library: Greek Revival, Italianate, Second Empire, Queen Anne and Chicago School modules, each with four sourced 'how to spot it' cues and a credited reference plate
T-2643 — Navigator Inspect Story tab: BUILT, YOU ARE HERE and TODAY on a timeline from design to today, filtered by the scene's era
T-2644 — Navigator Inspect Sources tab: facts grouped by Attested, Inferred and Reconstructed with a Liberties section, human source titles, and full citations collapsed under each fact
T-2645 — Navigator Inspect Photos tab: images sorted by date with year, caption and 'from this spot', the 12 best first and the rest behind 'All N'
T-2646 — Confidence view renderer: per-grade color, mode and opacity uniforms on the batched materials, Ghost sorted last with depthWrite off, Dither reusing the Reconstructed path, 60 fps held at the mid-tier phone profile
T-2647 — Navigator Confidence view app with presets NORMAL, BY GRADE, ATTESTED ONLY and X-RAY, replacing the HUD chip, caret and checkbox menu, with the C hotkey still toggling BY GRADE
T-2648 — Navigator Confidence view per-grade rows: a show toggle, four curated swatches with a color-blind-safe set, Look (Tint, Ghost, Dither), opacity 0-100 % and a live count per grade
T-2649 — Confidence view persists and shows a HUD legend: choices saved to localStorage chicago4d.confidence and carried across destinations, and a legend chip under the year chip while the view is on
T-2650 — Confidence view overlays: street names, building labels, people pins and the Jaunt route, each with its own toggle at the foot of the app
T-2651 — Navigator Move app: one mode picker, Walk, Run, Wagon, Horse or Fly, replacing #s-travel and #s-pace, with one slider for the active mode that keeps the named speeds
T-2652 — Navigator getting-there style: Teleport, Ride there or Fly over, one choice that Go to, Map and Jaunts all use
T-2653 — Navigator Move comfort: head bob, eye height (keeping the researched default and its 'Why?') and snap-turn on touch
T-2654 — Navigator Map app: the whole field inside the device with your arrow, tap a building to preview it then Go, Jaunt routes dotted, and a legend in the Confidence view colors
T-2655 — Navigator Jump app: the destinations as era mini-cards with HERE on the current one, an in-world jump (ring, time-stream, landing) to another, and RECALL to the Observatory as the screen's only signal-red key
T-2656 — Navigator Settings app: Display (brightness, field of view, road visibility, labels, light/dark, text size 100-140 %), the machine skins as preview tiles, Performance with Auto, Sound, Units, and About & What's new
T-2657 — Researcher mode: a Settings › About switch, off by default, that brings back the order book, ticket references, source ids, file paths and the full 'Why this default' essays the visitor UI no longer carries
T-2658 — Short 'Why?': every 'Why this default' essay becomes a one-line hint plus a popover of 40 words or fewer, with the full text shown in Researcher mode
T-2659 — Navigator sound, on by default: the ticker's flap ticks capped at 12 a second, the landing clunk, relay clicks and a hum while the Navigator is open, per-destination ambience, and Settings › Sound with master, effects and ambience
T-2660 — Field log on the device: landed, first inspect, tabs opened, Show me, Jaunts started and finished, Tour steps and Confidence presets counted in localStorage only, shown in Settings › About with a Clear button, never sent
T-2661 — Navigator Guide controls sheet: device-aware touch or keyboard controls from controls/intent.js, replacing the control-help popover
T-2662 — Navigator Guide glossary and FAQ: the locked terms with one-line meanings, 'Is this real?' and 'What does Reconstructed mean?' in 60 words or fewer each, and a locked term's first appearance on a screen showing its meaning on tap
T-2663 — Navigator Tour mode: the seven-step Field Check, each step completing on the real action, a spotlight cut-out with 55 % dim, Skip always visible, resume after reload and replay from Guide
T-2664 — Navigator first-landing tour offer: offered once per device after landing, declining never re-prompts, and one-time hints after it for the first Jaunt, first Jump and first Reconstructed building
T-2665 — Navigator License keepsake: awarded on finishing the tour and shown with the Jaunt keepsakes in the Jaunts app
T-2666 — Navigator teacher handout: Guide › For teachers prints the seven tour steps on one page with three suggested Jaunts per destination
T-2667 — Evidence hub becomes Guide › About this destination: ten topics folded into four cards, How we grade, Sources, Liberties and What lived and grew here, with the order book behind Researcher mode
T-2668 — Visitor-UI lint: check.sh fails on file paths, ids, snake_case, 'tier', 'ticket' or 'order book' in visitor strings, with Researcher-mode strings exempt
