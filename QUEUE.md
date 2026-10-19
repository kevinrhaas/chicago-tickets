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
# - Human figures are drawn once the portable-humans tickets (8C) render them, and Native and Metis people may be depicted
#   on informed, evidence-bounded judgement (owner, 2026-10-16; T-2672 updates the standing constraint).
#   Keep review flags and reasons; they do not veto release. The August gathering is excluded from 1 July 1835.
#   Black residents, families and businesses stay identified. Respect needs_bake and every ticket-level blocker.
# - Order (owner, 2026-10-16): the performance and GPU group (band 1), 1904 structures already in progress (band 2), the
#   Navigator interface (band 3), loop follow-ups (band 9), then the balance of Prairie Avenue 1904 (band 7, nearest
#   Glessner first), then the portable humans (8C). The Unreal holds are commented out, by hand only.

# --- 1. PERFORMANCE AND GPU — the whole optimization group, cleared first (owner, 2026-10-16: "move all of those gpu and performance
# ---    tickets above all of the house tickets let's clear those first"; earlier the same day: "clear all of the optimization tickets").
# Owner, 2026-10-16: "in a browser on mobile we get memory crashes and it's getting jittery ... keep it simple and lightweight ... rely on the local cpu gpu". Mobile performance and memory group T-2546..T-2558 (not T-2552), dependency order: measure, cut CPU/geometry, cut textures, smooth frames, then the WebGPU spike (T-2558, ruled (a) 2026-10-16). Same day: "tap into local computing resources ... based on the browser and platform or ... a big package app download that happens up front" added T-2559 (device profile), T-2560 (prebuilt town), T-2561 (download the year to disk).
T-2828 — 1904 on the owner's iPhone dies walking up to the Glessner front at Light and Sharpness 1: the tab was killed about 5 s into a walk from the 18th Street spawn across Prairie Avenue (last at 1390,-3220, 741 textures, 550k triangles), found and fixed against the phone memory ceiling
T-2733 — The frame governor's moving reading off the owner's phone: the Read frame pacing result copied back and filed, sd and p95 fallen (or not) for walk, turn and flight under Adaptive against Fixed
T-2719 — T-2598's Prairie walk moving p95 at phone profile on a real GPU (SwiftShader draws a frame in seconds, so the steward runner cannot read it)

# --- 2. 1904 STRUCTURES IN PROGRESS — every Prairie Avenue house already begun, finished next (owner, 2026-10-16: "finish any
# ---    existing in progress buildings in 1904"): Keith (1808), Glessner's sign-off, 1621-1625, 1637, then 1801, 1812 and 1811,
# ---    whose K01 massing pieces have merged.
# Owner, 2026-10-13: "Sure" (move T-1882 to the top) — 1808 Prairie rebuilt to its photographs, thread "Keith house vs photos"; T-1883 waits on it and takes this line when it merges.
# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
# Owner, 2026-10-13, with the 1887-91 Prairie Avenue sidewalk postcard: "we want to emulate this" (curbs and carriage walks, parkway trees with a Trees setting, soft surface edges). T-2473..T-2475, worked interactively in thread "Prairie Avenue streetscape", one PR each.
# Owner, 2026-10-13, thread "1812 structures": "For 1812 did I ask you to build the other buildings from that era ... all known structures from history"; card answer "After Prairie group"; "You can include native lodges as documented" (T-2490); card answer "Move to 14 August" (T-2490 moves the 1812 scene date first). T-2485 and T-2486 wait on T-2484 (same site) and take its line in turn.
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).

T-2813 — Keith's crown stack: about 0.1-0.17 m out between the lattice's foot and the head band (a shallower K10 moulded course first), rebaked, the Glessner-front and Florian cameras re-solved and tools/keith_crown_stack.py re-run, closing the Glessner-front lattice item
T-2830 — Keith's 1965 porch view: the slide's 1.25-1.35 factor at the loggia tested by fit against the slide's optics (pitch, lens distortion, principal point), the bow's heights and the loggia's plan, and Nickel 1967 read as a third picture of the loggia beside the bow
T-2831 — Keith's loggia column ruled between the 1888 plate, Nickel 1967 and the 1965 slide (about 0.78, 0.95 and 1.11 of the bow's principal opening), the late pictures' principal openings read for blinded transoms, built or argued, and porch-1965 brought to matches
T-2815 — Keith's 1888 plate items built: the south pedestal's bordered side field, the bow's principal lights in three tiers between stone bars, and the bow cap's carved band under its light top, rebaked and inland-1888 brought to matches
T-2816 — Keith's image gate closed: every reference view of keith_house_1808_prairie re-reviewed from the GLB in the tree and reading matches with nothing open, and T-1883's full acceptance (close street, corner and aerial views; liberties, licences and compressed assets) checked off
T-2760 — Glessner's west-court access levels: the west-wing courtyard door's 1.77 m sill and the descending areaway on HABS sheet 2 reconciled with the sections and the dated alterations, and the courtyard views reviewed
T-2761 — Glessner's photographic sign-off: the remaining opening, ornament, material and lighting differences in every canonical view resolved or accepted with a reason, a discrepancy register, and every match record brought to matches
T-2817 — 1623's entrance porch: the entrance arch as broad as the window's (about 1.85 m) springing from about 3.4 m, the door and stoop about 1.3 m north of its axis at the back of the porch, and the landing's iron guard; K01 rebaked and the match record's entrance and guard rows closed
T-2819 — 1623's stone and the oriel's front: the smoother coursed stone beside the oriel above the arches' springing and the carved band across both arches, and the oriel front's place along the wall ruled; K01 rebaked and 1623's match record brought to matches
T-2821 — 1625's plinth, door height and segmental heads to the McBirney photograph, whatever the rear section's piece left open, and 1625's match record brought to matches (the group's image gate)
T-2781 — 1637's south flank finished from the Grosvenor photograph: the bay's columns and carved dress, the pale band along the wall's foot read as water table or coping and built, and the panelled stack at about u 6.0 weighed against the engraving's wing stack and the one the evidence holds built; rebaked, and the Grosvenor record brought to matches
T-2782 — 1637's engraving brought to matches: the main cornice's band over the swell bay, the stacks' hooded crowns and the garden wall's run before 1635 built or argued, and both of 1637's match records reading matches with nothing open (the image gate)
T-2787 — K01 carries a K08 tower: a round or octagonal tower on grade against a wall, standing past the main eave with its cap over the main roof, its back closed in the wall's plane above the eave, and the main eave, cornice and gutter stopped against it; refused where it would sit under the eave, and held by the contract check (the kit piece 1801 Prairie's move needs)
T-2788 — K01 lays an all-stone house: a stone construction whose K02 coursed stone goes round every face (flanks, rear and wings), with stone dressings where a brick house has brick, so a Bedford-stone house is not a stone front on a brick box (the kit piece 1801 Prairie's move needs)
T-2789 — 1801 Prairie moves onto K01 in Bedford stone at T-2538's massing: the main block, south pavilion, flank section, gabled section and east range, its round tower and north-east turret on K08 towers with their cones over the main roof, compared with the draft from the Taylor camera, the draft builder's copy retired
T-2790 — 1801 Prairie's openings, entrance arches and curved stair on K01 from the Taylor photograph and the Inland Architect entrance plate, and the Taylor match record's opening and entrance items closed
T-2540 — 1801 Prairie's roof and 18th Street flank from the Taylor, 1929 and HABS photographs: the front's stone gable, the dormers, the cresting deck, the stacks and the rear elevation, and the envelope's match records brought to matches (after the pieces before it)
T-1890 — Finish 1801 Kimball corner mansion architecture
T-2544 — 1812 Prairie's front detail from the Levy photograph: the balcony over the projection, the third storey's arched windows and fanlight, the stone lower storeys under the brick upper wall with its stone bands, and whatever the first piece's match record left open on the front (after the piece before it)
T-2545 — 1812 Prairie's flanks, rear and the roof behind the gable, and the Levy, c. 1955 and 1915 Tribune match records brought to matches (after the pieces before it)
T-1885 — Finish 1812 Wheeler shaped-gable house architecture
T-2542 — 1811 Prairie's roofs from the photograph and the Inland Architect plate: the front bay's stone gable with its arched lights and fretwork balcony, the entrance block's pyramid and finial, the main slate roof, the north flank's stepped brick gable and the stacks; the plate's camera and match record, and the envelope's match records brought to matches (after the piece before it)
T-1892 — Finish 1811 Coleman-Ames Romanesque house architecture

# --- 3. THE NAVIGATOR — the interface work from the owner's Navigator design doc (owner, 2026-10-16: "then we do all of this
# ---    interface work, follow that with the balance of buildings in 1904"). Filed into this band in dependency order.
# Order: the two card bugs from the review and the gold/silver/bronze grade colors, then E1 arrival, E2 the Navigator shell, the string table, E3 HUD, E4 Jaunts, E5 the
# building dossier (summary record, Glessner pilot, Inspect), E6 Confidence view, E7 Move, E9 Map/Jump/Settings with Researcher
# mode, sound and the field log (owner rulings 2026-10-16), E8 Guide and Tour, then the E10 content gates. Each ticket names what
# it waits on under "Depends on"; take the next workable one while a dependency is open. Spec: chicago-tickets
# evidence/navigator-mk2-2026-10-16/DESIGN.md. NAV-1006 (student playtest) waits on the owner in 8b.
T-2642 — Navigator style library: Greek Revival, Italianate, Second Empire, Queen Anne and Chicago School modules, each with four sourced 'how to spot it' cues and a credited reference plate
T-2649 — Confidence view persists and shows a HUD legend: choices saved to localStorage chicago4d.confidence and carried across destinations, and a legend chip under the year chip while the view is on
T-2825 — Visitor-readable research records: liberties, ground, open questions, people and source details name no internal ticket number or record id, in any mode
T-2658 — Short 'Why?': every 'Why this default' essay becomes a one-line hint plus a popover of 40 words or fewer, with the full text shown in Researcher mode
T-2659 — Navigator sound, on by default: the ticker's flap ticks capped at 12 a second, the landing clunk, relay clicks and a hum while the Navigator is open, per-destination ambience, and Settings › Sound with master, effects and ambience
T-2660 — Field log on the device: landed, first inspect, tabs opened, Show me, Jaunts started and finished, Tour steps and Confidence presets counted in localStorage only, shown in Settings › About with a Clear button, never sent

# --- 9. LOOP IMPROVEMENTS — a follow-up a run files lands at this band's foot (owner, 2026-09-27)
T-2606 — The yards' sward test indexed: suppressesSward scans every fenced interior's bounding box for every lattice slot (2.3 s of a 7.5 s flora profile at 4x/390x780, the largest single flora cost), so a cell grid like flora's circleGrid answers it with identical answers at every slot
T-2723 — The gaze target's GPU pick stops stalling the frame: target.js's look reads back asynchronously (or raycasts on the CPU while moving) instead of a synchronous readPixels on the main thread every 500 ms of movement, with the moving p95 read before and after
T-2774 — The near ring's remaining sets on the GPU, so the near re-deal reaches zero: the heads hung from the GPU's deal and the CPU near walk retired (T-2717 read it unchanged at 2.6-3.4 ms a pass, because it still deals every near slot for the heads), then mid, forbs and far shrubs, each read with measure_walk_frames.mjs's near re-deal line at the throttled phone profile
T-2829 — Why Adaptive pacing makes turning less steady on the owner's phone (turn sd 4.7 to 6.5 ms, max 44 to 73 ms in T-2733's reading), and whether Adaptive stays the default until it does not
T-2832 — Shops & work: the 94 authored firms' cards fetch businesses/<id>.json, which 404s; the record lives under businesses/authored/

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
T-2672 — AGENTS.md's standing constraint rewritten to the owner's 2026-10-16 rulings: human figures drawn once the portable-humans pipeline renders them, and Native and Metis people depicted on informed, evidence-bounded judgement
T-2823 — Anonymous adult fallback role identities: period-qualified profiles and actor selection without invented residents
T-1789 — Build the first modular 1835 human library in Blender on the shared portable rig
T-1790 — Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
T-2673 — Mark Beaubien's evidence sheet and Blender master: dated likeness evidence with attested likeness, period analogy and reconstruction kept apart, the figure assembled from the T-1789 library on the shared rig, inspected front, three-quarter and profile renders, and LODs exported through T-1787
T-2674 — Mark Beaubien in the browser: the actor bound to the existing beaubien_mark person at his authored place, idling, walking when driven, greeting, selectable, and handing off to his card
T-2675 — Mark Beaubien inspected and measured in the real 1835 scene at desktop and mobile: close, conversation and street distances checked for contact, scale, shadows, foot slide and LOD popping, with shipped size, triangles, draw calls, texture memory and frame cost recorded and defects fixed
T-1792 — Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly

# --- 8D. PERIOD CARRIAGES AND WAGONS — photographic models, then motion, then boarding/riding (epic T-2791)
# Owner, 2026-10-18: "build tickets for these, place them in the queue in bands below the portable humans";
# first review existing assets and dated photographic evidence, then models, moving distant traffic and interaction.
# T-2792 and T-2799 begin in parallel by explicit owner instruction; respect every model's rights/date/needs_bake gates.
T-2792 — Carriages and wagons: evidence register and first master specification
T-2793 — Build one articulated period wagon master from the existing wagon families
T-2794 — Build one photographic period passenger-carriage master
T-2795 — Animate vehicle running gear and matched draft-horse hitches
T-2796 — Move horse-drawn traffic through distant streets with measured LOD budgets
T-2797 — Board, ride and leave a carriage or wagon with accessible controls

# --- 8E. PERIOD HORSES AND GEAR — photographic animals, tack, riders, then mounting/riding (epic T-2798)
# Horse master and gear supply both wagon/carriage teams and mounted riders; reuse portable-human rig/wardrobe.
T-2799 — Horses and gear: dated reference dossier and first master specification
T-2800 — Build the first anatomically grounded photographic horse master
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
# BLOCKED-OWNER T-2670 (opened 2026-10-16, META) — Student playtest: 6-8 students, three tasks (find a house, learn who lived there, tell Attested from Reconstructed), 80…
#     waits: needs the owner to arrange 6-8 students aged 14-16; a run can prepare the task cards and observer sheet once T-2663 (tour) and T-2637 (Glessner pilot) have merged
# BLOCKED-TECH T-2745 (opened 2026-10-17, META) — 1812 trees from the research: North Side woods run east to the sand hills, wooded forks, the young 16th-18th Street gro…
#     waits: T-2744 (the 1835 placement tools and grove records it reuses)
T-2809 — 1835 fruit trees: the fort's company-garden fruit trees and currants, and Dr. Harmon's young sod-fenced orchard by the lake
T-2810 — 1835 river woods: wild grape curtains on the river-facing edge, and a few snags and fallen logs in the wet woods and gallery
T-2783 — 1835 and 1812 prairie, part 1: the far prairie past flora.js's near ring reads as flat paint; add a mid ring of cheap grass cards and a grass-coloured, streaked ground so the near ring has no visible edge, held in every tier's ceiling and the 1835 frame
T-2784 — 1835 and 1812 prairie, part 2: woody plants of the open plain from the ecology analysis: prairie rose, New Jersey tea and leadplant scattered, pussy and slender willow clumps and buttonbush at slough edges, and a few lone bur oaks and cottonwoods in the fire shadow just east of sloughs and the river; ecology inferred, positions reconstructed under a liberty
T-2824 — Phone boot upload pass: draws rejected before the first shadow map (sampler2DShadow on unit 0)
