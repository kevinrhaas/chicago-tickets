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
# - Below the 1835 work: Prairie Avenue 1904 (band 7, with the Glessner photographic-finish group released into it
#   2026-10-11 and run one at a time), then the portable humans (8C). The Unreal holds are commented out, by hand only.

# --- 1. THE 1835 TOWN — the owed roofs raised, households seated and dealt, signs and cards a visitor reads, the
# ---    household-record retirement, then the research readings (owner, 2026-10-10: held tickets that can now be
# ---    worked go to the top with the core 1835 loop and research tickets)

# Owner, 2026-10-13: "Sure" (move T-1882 to the top) — 1808 Prairie rebuilt to its photographs, thread "Keith house vs photos"; T-1883 waits on it and takes this line when it merges.
# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
# Owner, 2026-10-13, with the 1887-91 Prairie Avenue sidewalk postcard: "we want to emulate this" (curbs and carriage walks, parkway trees with a Trees setting, soft surface edges). T-2473..T-2475, worked interactively in thread "Prairie Avenue streetscape", one PR each.
# Owner, 2026-10-13, thread "1812 structures": "For 1812 did I ask you to build the other buildings from that era ... all known structures from history"; card answer "After Prairie group"; "You can include native lodges as documented" (T-2490); card answer "Move to 14 August" (T-2490 moves the 1812 scene date first). T-2485 and T-2486 wait on T-2484 (same site) and take its line in turn.
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).

T-1883 — Finish 1808 Keith-Field neighbour of Glessner architecture
T-2546 — A memory meter and ceilings: resident JS heap, ArrayBuffers and GPU geometry and texture bytes per year, viewport and layer, gated like frame time (phone memory crashes, owner 2026-10-16)
T-2547 — Crash-aware boot: a phone that ran out of memory last session boots one tier lower and says so, and a lost WebGL context never reload-loops
T-2548 — 1904 phone: stop holding what it never reads again: the 26.5 MB Glessner GLB in assetBytes, the source glTF beside its batch copy, and decoded images after upload
T-2549 — Compact vertex formats in the batch: keep the quantization the bake paid for, about 52 to at most 24 bytes a vertex for structures, frontage, enclosures and yard, with pixel parity
T-2550 — GPU picking from a 1x1 id pass, so frontage, enclosures, yard and structures release their CPU triangles (about 188 MB on the 1835 phone) and weathering becomes a uniform
T-2551 — KTX2 in the renderer: vendor KTX2Loader and the Basis transcoder from the pinned three tarball, and ship the runtime library sheets GPU-compressed with mip 0 skipped on light
T-2553 — KTX2 in every textured web GLB: UASTC and ETC1S in web_derivatives.sh, the light tier capped at 1024, Glessner v4 repacked, and every photo-match still matches
T-2554 — 1904 texture residency: textured houses resident by distance under a per-tier texture budget, uploads paced per frame, and the boot fetch bounded

# --- 9. LOOP IMPROVEMENTS — a follow-up a run files lands at this band's foot (owner, 2026-09-27)

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
T-2228 — Glessner: run final photographic comparison and evidence sign-off
T-2531 — 1621 Prairie's last drawn differences — the entrance arch's curved extrados and deeper recess, the light's shelf over the panel, the basement lights' voussoir heads — and the Building Budget match record brought to matches (after the piece before it)
T-2435 — Bring the 1621-1625 match records to matches: what the McBirney photograph and the Building Budget drawing still show differently, and the image gate (after the three pieces before it)
T-2534 — 1637 Prairie's principal storey from the engraving: its sashes about 2.9 m tall on the front, the swell bay and the wing, and the wing's French window to its floor over a bowed balcony about 0.9 m high
T-2536 — 1637 Prairie's c. 1870 Grosvenor photograph weighed as evidence of its own date: its source record, camera and match record, and both match records brought to matches (after the two pieces before it)
T-2538 — 1801 Prairie's massing from J. W. Taylor's c. 1895 photograph: its camera solved and match record written, and the draft's heights, corner tower and cone, south gable and 18th Street flank with its east turret rebuilt in place to what the photograph shows
T-2539 — 1801 Prairie onto K01 in Bedford stone: the kit lays an all-stone house and carries a round corner tower whose cone stands over the main roof, and the Kimball house moves onto it with the photograph's openings, entrance arches and curved stair (after the piece before it)
T-2540 — 1801 Prairie's roof and 18th Street flank from the Taylor, 1929 and HABS photographs: the front's stone gable, the dormers, the cresting deck, the stacks and the rear elevation, and the envelope's match records brought to matches (after the pieces before it)
T-1890 — Finish 1801 Kimball corner mansion architecture
T-2543 — 1812 Prairie onto K01 from the Levy photograph: the plan re-read from sheet 28, three storeys over the raised basement at the photograph's heights, the arched entrance and stair, the south projection, and the street front's shaped Flemish gable with its grid attic light and finial; its camera solved and match record written
T-2544 — 1812 Prairie's front detail from the Levy photograph: the balcony over the projection, the third storey's arched windows and fanlight, the stone lower storeys under the brick upper wall with its stone bands, and whatever the first piece's match record left open on the front (after the piece before it)
T-2545 — 1812 Prairie's flanks, rear and the roof behind the gable, and the Levy, c. 1955 and 1915 Tribune match records brought to matches (after the pieces before it)
T-1885 — Finish 1812 Wheeler shaped-gable house architecture
T-2541 — 1811 Prairie onto K01 from the Coleman/Ames photograph: its camera solved and match record written, and the draft rebuilt in place as three storeys of rock-faced brown stone — the square front bay carried to the third storey, the entrance block with its deep round arch and broad stair, the oriel over it, and the brick north flank
T-2542 — 1811 Prairie's roofs from the photograph and the Inland Architect plate: the front bay's stone gable with its arched lights and fretwork balcony, the entrance block's pyramid and finial, the main slate roof, the north flank's stepped brick gable and the stacks; the plate's camera and match record, and the envelope's match records brought to matches (after the piece before it)
T-1892 — Finish 1811 Coleman-Ames Romanesque house architecture
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
T-2552 — Prairie from the air: break the ground's even plaid with a world-scale variation map and a distance fade (owner, 2026-10-16)
