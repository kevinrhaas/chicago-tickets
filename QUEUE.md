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

# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
T-2462 — 1620 Prairie's upper street windows off their bays' centres from the 1874 engraving (over the door v 5.5, over the bay window v 2.5), the pavilion's stone corner strip and the bay window's pilaster strips
T-2464 — Prairie Avenue 1904 opens on an iPhone again: houses share their identical stone, brick and wood images instead of each decoding its own copy
T-2463 — 1620 Prairie's door from the 1874 engraving: drawn at v 5.4-6.45, south of the stoop whose strings both pictures put at about v 5.85-7.65, so K07 learns a stoop off its door's axis; and both match records brought to matches (after the piece before it)
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).

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
T-2216 — Glessner: complete the main entry oak door and iron grille
T-2457 — 1638 Prairie's gable and bay from its photograph, the differences left open: the broad moulded bargeboard, the apex's three pinnacles, the hood's cusped tracery and volute stops, the apex height, the bay's blunter heads and their dark stops (after the piece before it)
T-2468 — Dev's smoke stage 14 is red: #771 placed forsyth_house_1635_prairie in 1904 but the 1904 roster (PLACED_1904) was never given it, so every PR off dev refuses on smoke (mobile, 14)
T-2458 — 1638 Prairie's entrance, tower and south block from its photograph, and its match record brought to matches: the narrower opening, the steps' run to grade, the pale gabled shape over the door, the tower's smooth upper stage and the two-storey block south of the gable (after the two pieces before it)
T-2460 — 1619 Prairie's moulded stone cornice at the bow's top from the drawing: the bow carried up to it, in place of K10's bracketed timber cornice (after the piece before it)
T-2422 — 1619 Prairie's entrance, balcony and basement from the drawing: the recessed round-arched door under its carved panel, the side stoop, the bow's balcony rail and the grilled basement arches, and the match record brought to matches
T-2440 — Move Hamline's drawing build from 1619 to 1621: the K01 house and its Building Budget camera re-solved on 1621's own bay and the passage south of it, carrying T-2420's and T-2428's work, and 1619 handed back to its own front
T-2434 — The group's third house (1621 or 1623, whichever is not Farwell's) without a picture: a bounded brick front on K01 at the light well the 1911 sheet draws, its own and not a copy of either neighbour
T-2435 — Bring the 1621-1625 match records to matches: what the McBirney photograph and the Building Budget drawing still show differently, and the image gate (after the three pieces before it)
T-2465 — 1637 Prairie's wing from the engraving: carried up to the cornice under its own steep hip, its ridge running back into the main roof as high as it, with the wing's stack at the ridge
T-2466 — 1637 Prairie's swell bay carried up to the cornice, and the stacks' panelled shafts and caps (K15 on a mansard) from the engraving (after the piece before it)
T-2467 — 1637 Prairie's wing cornice from the engraving: a band as deep as the main cornice's (y 232-262 px) with its block over the window, where the hipped crown carries K05's 0.2 m fascia and no K10 brackets
T-2449 — 1637 Prairie's windows from the engraving and its c. 1870 photograph weighed: the principal storey's tall sashes, the basement lights, the Grosvenor photograph's source, camera and match record as evidence of its own date, and both match records brought to matches (after the two pieces before it)
T-1871 — Refine 1700-1706 Glessner family townhouses
T-1872 — Refine 1708 and 1712 townhouse fronts
T-1873 — Refine 1720 Walker frame villa
T-1874 — Refine 1726, 1730 and 1736 replacement/altered houses
T-1875 — Refine 1701 Hibbard house and rear veranda envelope
T-1876 — Finish 1701 Hibbard house and rear veranda architecture
T-1877 — Refine 1709 Palmer Kellogg successor
T-1878 — Refine 1719-1721 Dexter address and altered house envelope
T-1879 — Finish 1719-1721 Dexter address and altered house architecture
T-1880 — Refine 1729 Pullman main house envelope
T-1881 — Finish 1729 Pullman main house architecture
T-1882 — Refine 1808 Keith-Field neighbour of Glessner envelope
T-1883 — Finish 1808 Keith-Field neighbour of Glessner architecture
T-1884 — Refine 1812 Wheeler shaped-gable house envelope
T-1885 — Finish 1812 Wheeler shaped-gable house architecture
T-1886 — Refine 1816 Henderson mansard house
T-1887 — Refine 1824 Marsh altered front and 1828 neighbour
T-1888 — Refine 1834 Jones post-1886 mansard
T-1889 — Refine 1801 Kimball corner mansion envelope
T-1890 — Finish 1801 Kimball corner mansion architecture
T-1891 — Refine 1811 Coleman-Ames Romanesque house envelope
T-1892 — Finish 1811 Coleman-Ames Romanesque house architecture
T-1893 — Refine 1815 Sears-Meeker altered house
T-1894 — Refine 1823 Dent house
T-1895 — Refine 1827 Doane twin-tower mansion envelope
T-1896 — Finish 1827 Doane twin-tower mansion architecture
T-1897 — Refine 1900 Elbridge Keith corner house
T-1898 — Refine 1906 Edson Keith and attached 1908
T-1899 — Refine 1912 Moulton-Lowden Chateauesque house envelope
T-1900 — Finish 1912 Moulton-Lowden Chateauesque house architecture
T-1901 — Refine 1916-1930 identity and 1936 Allerton estate envelope
T-1902 — Finish 1916-1930 identity and 1936 Allerton estate architecture
T-1903 — Refine 1901 Ream post-fire house
T-1904 — Refine 1905 Marshall Field Sr. mansion envelope
T-1905 — Finish 1905 Marshall Field Sr. mansion architecture
T-1906 — Refine 1919 Field Jr. post-1902 enlargement envelope
T-1907 — Finish 1919 Field Jr. post-1902 enlargement architecture
T-1908 — Refine 1923 Kellogg and 1945 Armour-Corwith corner
T-1909 — Refine 2000 and 2010 detached frame houses
T-1910 — Refine 2018 and 2026 masonry houses
T-1911 — Refine 2036 Buckingham corner house
T-1912 — Refine 2001, 2003 and 2005 attached row
T-1913 — Refine 2009 Mayer-Meyer French Gothic house envelope
T-1914 — Finish 2009 Mayer-Meyer French Gothic house architecture
T-1915 — Refine 2011 Romanesque house beside Mayer
T-1916 — Refine 2013 Reid classical house
T-1917 — Refine 2017, 2021 High and 2027 Cobb-associated group
T-1918 — Refine 2031, 2033 and 2035 limestone row
T-1919 — Refine 2100 Sherman Victorian Gothic house envelope
T-1920 — Finish 2100 Sherman Victorian Gothic house architecture
T-1921 — Refine 2108 Mark Kimball and 2112 Rothschild
T-1922 — Refine 2110 Rees at its historical site envelope
T-1923 — Finish 2110 Rees at its historical site architecture
T-1924 — Refine 2101 and 2109 Roloson neighbours
T-1925 — Refine 2115 Armour Second Empire house
T-1926 — Refine 2120 and the 2126 Robbins construction phase
T-1927 — Refine 2130 Murdoch rounded-bay house
T-1928 — Refine 2140 Tucker-Smith corner mansion envelope
T-1929 — Finish 2140 Tucker-Smith corner mansion architecture
T-1930 — Refine 2123 masonry and 2125 frame neighbours
T-1931 — Refine 2127-2129 flats and 2141 non-building frontage
T-1932 — Refine north-west alley coach houses and service courts
T-1933 — Refine north-east rear service buildings
T-1934 — Refine Pullman stable, additions and conservatory estate
T-1935 — Refine west 1800-1900 service buildings and Glessner boundary
T-1936 — Refine east 1800-1900 service buildings
T-1937 — Refine south-west service buildings and shared Rees coach house
T-1938 — Refine south-east service buildings
T-1939 — Refine 213, 215 and 217 East Twentieth Street context
T-1940 — Refine 2008 Calumet Hanford exterior
T-1941 — Refine 2018 Calumet Wheeler-Kohn exterior
T-1942 — Refine Second Presbyterian post-1900 exterior skyline
T-1943 — Finish north-block boundaries, gardens and frontage fittings
T-1944 — Finish 18th-20th block boundaries, gardens and frontage fittings
T-1945 — Finish 20th-22nd block boundaries, gardens and frontage fittings
T-1946 — Close side-street and rail-side background gaps
T-1947 — Verify the completed 16th-18th Prairie streetscape
T-1948 — Verify the completed 18th-20th Prairie streetscape
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
# BLOCKED-TECH T-2217 (opened 2026-10-09, SOUTH_TIME) — Glessner: finish both porte-cochere leaves, hardware and passage
#     waits: T-2216 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2218 (opened 2026-10-09, SOUTH_TIME) — Glessner: reconstruct the curved courtyard hall steps and cheek wall
#     waits: T-2217 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2219 (opened 2026-10-09, SOUTH_TIME) — Glessner: audit basement grilles, light wells and service openings
#     waits: T-2218 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2220 (opened 2026-10-09, SOUTH_TIME) — Glessner: refine copper roof panels, seams and weathering
#     waits: T-2219 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2221 (opened 2026-10-09, SOUTH_TIME) — Glessner: complete gutters, rainwater heads, downpipes and attachments
#     waits: T-2220 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2222 (opened 2026-10-09, SOUTH_TIME) — Glessner: resolve chimney phase and finish stack/cap detail
#     waits: T-2221 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2223 (opened 2026-10-09, SOUTH_TIME) — Glessner: date and finish courtyard service stairs, rails and rear gate
#     waits: T-2222 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2224 (opened 2026-10-09, SOUTH_TIME) — Glessner: finish courtyard paths, edging, lawn and drainage
#     waits: T-2223 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2225 (opened 2026-10-09, SOUTH_TIME) — Glessner: add restrained, dated courtyard vines and exterior planting
#     waits: T-2224 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2226 (opened 2026-10-09, SOUTH_TIME) — Glessner: balance lighting, contact shadows and restrained surface aging
#     waits: T-2225 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2227 (opened 2026-10-09, SOUTH_TIME) — Glessner: validate full/light browser quality and controlled performance
#     waits: T-2226 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
# BLOCKED-TECH T-2228 (opened 2026-10-09, SOUTH_TIME) — Glessner: run final photographic comparison and evidence sign-off
#     waits: T-2227 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
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
