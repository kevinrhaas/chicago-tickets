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
T-3070 — The PR and dev gate (Chicago 4D — gate) dies with 'The runner has received a shutdown signal' (exit 143) about 6 minutes into check.sh, right after publish, on every run since about 12:15Z on 2026-10-23: dev's own run 39953163716, T-3046's 39951182314 and T-3019's 39951882275 (both attempts) all stop at the same line, so no PR can merge; find what kills the runner there (memory or disk after the ~640 MB of scene packs, or a step that grew) and bring the gate back to a verdict
# ---    tickets above all of the house tickets let's clear those first"; earlier the same day: "clear all of the optimization tickets").
# Owner, 2026-10-16: "in a browser on mobile we get memory crashes and it's getting jittery ... keep it simple and lightweight ... rely on the local cpu gpu". Mobile performance and memory group T-2546..T-2558 (not T-2552), dependency order: measure, cut CPU/geometry, cut textures, smooth frames, then the WebGPU spike (T-2558, ruled (a) 2026-10-16). Same day: "tap into local computing resources ... based on the browser and platform or ... a big package app download that happens up front" added T-2559 (device profile), T-2560 (prebuilt town), T-2561 (download the year to disk).



# --- 9. LOOP IMPROVEMENTS — operations: the loop's own tooling (lap, claims, merge, gates, tickets). Owner, 2026-10-20: right under
# ---    the performance band, and GPU or performance follow-ups go to band 1, a building's to its own band, not here.

# --- 2. 1904 STRUCTURES IN PROGRESS — every Prairie Avenue house already begun, finished next (owner, 2026-10-16: "finish any
# ---    existing in progress buildings in 1904"): Keith (1808), Glessner's sign-off, 1621-1625, 1637, then 1801, 1812 and 1811,
# ---    whose K01 massing pieces have merged.
# Owner, 2026-10-13: "Sure" (move T-1882 to the top) — 1808 Prairie rebuilt to its photographs, thread "Keith house vs photos"; T-1883 waits on it and takes this line when it merges.
# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
# Owner, 2026-10-13, with the 1887-91 Prairie Avenue sidewalk postcard: "we want to emulate this" (curbs and carriage walks, parkway trees with a Trees setting, soft surface edges). T-2473..T-2475, worked interactively in thread "Prairie Avenue streetscape", one PR each.
# Owner, 2026-10-13, thread "1812 structures": "For 1812 did I ask you to build the other buildings from that era ... all known structures from history"; card answer "After Prairie group"; "You can include native lodges as documented" (T-2490); card answer "Move to 14 August" (T-2490 moves the 1812 scene date first). T-2485 and T-2486 wait on T-2484 (same site) and take its line in turn.
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).

T-3024 — Glessner's 18th Street stack's vertical layout from HABS 14, photograph 4 and HABS 01: the gable's coping meeting the stack about 1.5 ft lower than built, the 1886 stone about 0.6 ft lower under the device's stone, and the two crosses level or stepped, each ruled, built or argued, rebaked, and HABS 14's stack-layout item closed
T-3065 — Glessner's 18th Street stack reads about 8.7 px wider than Taylor 2135 through T-3058's camera (found by T-3058): with the principal point free and the stacks' centres fitted, the south and middle stacks' widths match the photograph within 0.4 px but the north stack's record box (W 15.25-22.35, T-2873's 7.1 ft from HABS 14) is 8.7 px wider than the photograph's 74 px, and the render's 1886 device and cross stand proud past the photograph's right edge; read the stack's E-W depth and the device's projection against HABS 14 and Taylor 2135 together and rule or rebuild
T-3025 — Glessner's roof covering: every print reads the roofs, the stable cupola's pyramid included, slate-grey where the model lays red tile house-wide; find what the roof was laid in (contract, specification, description or a colour view) and rule it, rebaking if it changes
T-3072 — Glessner's roof course module from the c. 1887 Cornell print (found by T-3025): the print's stable-roof courses read about 6.4 in (1.28 times the render's, three column bands, docs/RESEARCH/glessner-roof-covering-T-3025) where the model lays HABS's 1963 5 in exposure (L-glessner-roof-tiles-2203, carried to 1904 as inferred); measure the render's course where its texture is not near its sampling limit, read a second early picture (Taylor 2135 or the 1888 plate), find whether the roof was relaid between 1887 and 1963, and rule the 1904 module, rebaking if it changes
T-3058 — Taylor 2135's camera with its principal point freed (found by T-3027): the south stack stands where sheets 6 and 4 put it, and T-2858's camera, whose principal point is held at T-2221's value, cannot reach it even with the stacks admitted (-13 px); freed, the withheld south stack reads -7.3 px and all three stacks fitted read within 5 px (jambs within 3.1 px), but the solve has several minima. Find the camera (principal point, the cap-overhang correction carried from T-2221's render, the picks) that fits the jambs and the stacks together, re-render, re-read T-3045's courses through it, and close the camera item on the taylor-2135-ne match record
T-3028 — Glessner's photographic sign-off: every match record reading matches with nothing open, the discrepancy register's final acceptance written with what is attested against inferred, and every courtyard and rear face reviewed, sheet 4's datum (T-2978) included (after the pieces before it)
T-3060 — 1801 Prairie's Taylor camera re-solved with its south-west bearing on the chamfer's near end (u 20.6, v 10.56), where T-2538 laid it on the chamfer's back (u 20.1, v 11.2), which the camera cannot see: the pavilion renders about 15 px south of the print across its whole face (its corner at x 1356 against 1335-1343, its north cheek from 1247 against 1232-1250); refit the eye, yaw and focal length to the four bearings and the scale lengths, re-read every height read through the camera, and bring the corner within about 5 px of the print's
T-3073 — 1801 Prairie's south pavilion's gable against T-3060's re-solved Taylor camera (found by T-3060): its finial's axis renders at x 1280 against the print's 1268 and its top at y 237 against 218, and T-2538's readings carried through the camera put the gable's springing at about 14.1 m and its apex at 17.7 m where the build stands 13.9 and 17.45 m; read the gable's rows and the face's place off the print through the new camera and rebuild or rule
T-3074 — 1801 Prairie's 18th Street flank against T-3060's re-solved Taylor camera (found by T-3060): the tower's finial renders about 16 px east of the print's (x 684 against 700) and no camera that fits the front fits it, the flank's string course across x 370-650 falls about 12 px less on the print than the camera draws a level line on the 18th Street wall, and T-2538's far-flank readings carried through the camera fall about 9 % (the east range's eaves 7.5 m against the build's 8.2, the turret's 7.3, 11.6 and 13.8 m against 8.0, 12.7 and 15.1); re-pick the flank's rows and the tower's axis off the print, decide whether the flank's sections or the camera's flank is wrong, and rebuild or rule
T-3001 — 1801 Prairie's 18th Street flank from the Taylor photograph: the gabled section's gable facing 18th Street with its balcony at about 11.5 m where the build has a hip, and the flank section's width (about 7.8 m in the photograph, built 6.0 m, K08's widest pavilion)
T-3002 — 1801 Prairie's carved stone from the Taylor photograph: the heavy moulded main cornice under the mansard's faces (the build's eave is K05's plain fascia; K10's moulded cornice stands only under a flat or gable roof) and the carved panel filling the south pavilion's gable
T-3003 — 1801 Prairie's south and east sides and its rear from the 1929 and HABS photographs: find each picture, solve its camera into data/reference_views/kimball_house_1801_prairie/, and bring the faces the Taylor camera cannot see to them
T-1890 — Finish 1801 Kimball corner mansion architecture
T-3061 — 1812 Prairie's south side-wall parapet and the stack on its outer face (found by T-3034): K01 learns a mansard house's side wall carried up past the curb as a coped parapet and a stack standing on the wall's outer face in the gap to the neighbour (both 1812 photographs put it 0.3-0.9 m outside the wall line, at u 12.75-13.75), every other K01 house re-emitting byte-identical; rebake and bring the Levy and c. 1955 match records' parapet and stack items to fixed
T-3035 — 1812 Prairie's open front items in the Levy and c. 1955 match records (the shoulder panels, the grid window's surround and hood, the balcony's stone panel and the projection's top, the third storey's lights and voussoirs, the entrance arch's ring, transom and place, the stair's cheeks and newels, the carving and the tone), the rear from the 1911 sheet, and both records brought to matches (after the pieces before it)
T-1885 — Finish 1812 Wheeler shaped-gable house architecture
T-3063 — 1811 Prairie's south gable's rear fall: behind the tall stack the 1888 plate's coping runs about 30-48 px under the render's (x 528-571), near level at about 11.0 m by the camera where the build's coped rake falls from the ridge + 0.3 m at 22.4 degrees, so the second stack shows 35 px over it in the plate and barely clears it in the render; read the flank's wall head and the rear slope against the Chicagology print (cgn-1811-coleman-ames-photo, whose camera T-3052 solves) and build it (K01's coped parapet follows the roof's slopes only)
T-3064 — 1811 Prairie's north pinnacle's shaft and scaled cap from the 1888 plate (found by T-3062): the plate's shaft stops at a band about y 342 px, a scaled pyramid over it to about y 320 under the moulded block, where K01 carries every engaged shaft past the wall gable's eave (11.10 m), so the build's cap stands about 20 px (0.4 m) high and its pyramid is plain; let a shaft under a block stop below the face's eave with the block taking the eave's end, and check the inland_architect_plate match record
T-3052 — 1811 Prairie's other pictures: the Chicagology print, the a18 photograph and the 1965 HABS photograph each ingested where missing, its camera solved into data/reference_views/coleman_ames_house_1811_prairie/ and its match record written, the Building Budget sketch kept to its phase guard, and every 1811 match record brought to matches (after the pieces before it)
T-2991 — 1811 Prairie's porch south arcade from the 1888 plate: three round-arched lights on colonnettes (x 476, 490 and 501 px, capitals y 680-690, crowns y 647-660) on a face receding from the front at about v 9.4-9.5 by the camera, where the solve puts the entrance block's south corner at v 10.40 (x 510); read the block's south return and the porch's side wall, then build it (K01's loggia side arch opens only an end wall)
T-2486 — 1812: build Antoine Ouilmette's house and garden close behind the Kinzie house, and Pettell's small cabin near it
T-3075 — 1812 Prairie's south wall line (found by T-3061): Levy's print puts the main front's south corner (its downpipe at x 293-300 px against the build's 320), the parapet's end (x 277-293) and the outside stack (26 px) about 0.26-0.31 m south of sheet 28's traced wall, and the c. 1955 photograph puts the stack 14 px (about 0.34 m) south too, where the permit's 30 ft (9.14 m) is wider than the traced 8.5 m; read the front's south corner through both cameras and rule the wall's line, moving the footprint's south side (and the 1.41 m gap to 1816) or ruling the trace, with every front feature measured from the south corner checked

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
T-3013 — The 1904 state of five Indiana-side fronts sheet 35 draws with 1911 commercial uses (found by T-3009): the printing works at 2001-2003 Indiana, the motor garages at 2101-2105 and 2129-2131, the auto repair and blacksmith shop at 215-217 E. 21st with the open lot beside it, and the five-storey branch post office at 2133 Indiana with 202-212 E. 22nd; find what stood on each lot on 1 July 1904 (a 1904 directory, a building permit, a dated photograph or an earlier Sanborn) and draft it, or record the ground open, on the 35w census rows the trace already carries
T-3066 — First Presbyterian Church at 2029 Indiana sourced and its massing refined to the Otis 1913 plate: the 1870-1873 church its congregation used until its last service in December 1912, the gable to Indiana Avenue, the tower's stages and its spire to the photograph's heights, the plate's camera solved and a match record written
T-3067 — First Presbyterian Church at 2029 Indiana worked to the Otis 1913 plate until it matches: the 21st Street flank's pinnacled buttresses and corbel table, the tower's angle buttresses, gabled lucarnes and broach spire, the west front's traceried window and gabled porch, the roof's dormers, every open difference in the match record fixed or ruled
T-3019 — Indiana Avenue's east frontage, 16th to 18th Street, with East 16th Street's lot, drafted from sheet 20 as the background census ranks them (12 of 17 lots seen, 1623 from 13 stands; e16th_209 from 6)
T-3068 — The 1904 state of the seven Indiana-side lots where sheet 20 and Robinson 1886 disagree (found by T-3019): the office and tin shop at 1601-1603, the ice-cream factory at 1605-1613 and the photographic-supply factory at 1727-1737 (1886 houses, 1911 works), 1619's 1886 frame house against its 1911 brick one with the frame shed both draw, and the 1886 brick houses on 1637 and 1641 that are gone by 1911; find what stood on each lot on 1 July 1904 (a 1904 directory, a building permit, a dated photograph or the 1894-97 Rascher plan) and draft it, or record the ground open, on the 20w census rows the trace already carries
T-3011 — The background ground no 1904 lot covers, drafted as bounded masses or recorded open: the Indiana half of the 18th-20th block (the census's most-seen target, 48 Prairie stands; lots from T-1745 or a bounded mass) and the Illinois Central strip behind Prairie's 16th-18th east lots; then the views west to Indiana, east to Calumet and down every cross street captured at 1280x800 and 390x780 with 1904's load, heap and frame time against the pre-background baseline
T-3012 — 1904's desktop full-detail triangle budget on Calumet's east walk at 20th looking north (found by T-3008): 4.63 M against 4.6 M, where the fifteen Calumet 18th-20th drafts add only 30,476, so the view stood at the budget before them; find what carries the weight (the Prairie east-side K01 houses, the trees or the IC apron) and bring the stand inside without cutting the background
T-2995 — 1736 Prairie's roof behind its curb, the rear and the coach house: the 1911 sheet draws the mansard's dashed curb only along the street front and the 18th Street flank back to the brick bay (u about 9.9), none along the north wall or over the rear 9.9 m; read the wall figures ('12 12 8' on the north, '14 12 12' on the south) and rule whether the north side and the rear rise as a straight brick third storey (the service wing), build it where K01's mansard is four-sided today, declare every closed face, and refine house_1736_prairie_coach_house from its draft (the sheet's '2', 'GARAGE', walls '12 8')
T-2964 — 1816 Prairie's photograph worked to matches: the raised mansard crown over the front bay, the south bay's own mansard and dormers, the iron cresting, the carved window hoods, the iron front fence, the 1874 Land Owner engraving's camera solved, and every 1816 match record brought to matches (after the piece before it)
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
T-2794 — Build one photographic period passenger-carriage master
T-2795 — Animate vehicle running gear and matched draft-horse hitches
T-2796 — Move horse-drawn traffic through distant streets with measured LOD budgets
T-2797 — Board, ride and leave a carriage or wagon with accessible controls

# --- 8E. PERIOD HORSES AND GEAR — photographic animals, tack, riders, then mounting/riding (epic T-2798)
# Horse master and gear supply both wagon/carriage teams and mounted riders; reuse portable-human rig/wardrobe.
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
T-3055 — Frame-tavern picture controls preserve legacy geometry
T-2377 — Match Hogan's store, the first post office to its pictures
T-2378 — Match J. B. Beaubien's homestead to its pictures
T-2379 — Match the Lake House under construction to its pictures
T-2380 — Match the log jail to its pictures
T-2381 — Match the Miller House to its pictures
T-2382 — Match Philo Carpenter's log shop (the Sauganash's log wing) to its pictures
T-2383 — Match the Sauganash Hotel to its pictures
T-2384 — Match St Mary's church to its pictures
T-3056 — Correct early-building image credits and evidence limits
T-2385 — Match the first Tremont House to its pictures
T-2386 — Match the Wolf Point Tavern to its pictures
T-3041 — Match the first Fort Dearborn buildings against every reference picture
T-2388 — Match the second Fort Dearborn (1835) to its pictures, every building in it
# BLOCKED-TECH T-2163 (opened 2026-10-08, SOUTH_TIME) — Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all thre…
#     waits: T-2983 — the grounds and the whole-district walk need every draft standing; T-2162 split into T-2982 (named context buildings, #1180, merged) and T-2983 (the background census), so this waits on T-2983
T-3043 — Guide's glossary tap check finds no locked term on Home since its Confidence view tile became a button
