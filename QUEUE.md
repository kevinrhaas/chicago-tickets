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
# - Order (owner, 2026-11-05: "finish prairie Ave first and keep the rest of the tickets in sections where they can be
#   worked by separate agents later"; "Pullman should def be finished next"): performance and GPU (band 1), loop operations
#   (band 9), Prairie Avenue 1904 in progress: Pullman, 1801, Glessner and the owner's photo reworks (band 2), the balance of
#   Prairie Avenue 1904, nearest Glessner first (band 7), the Navigator (band 3), then one band per area, each workable by its
#   own agent: 1835 (band 4), 1812 (band 5), portable humans (8C), carriages (8D), horses (8E); 8C-8E consolidated 2026-11-12. The Unreal holds and the
#   playtests are commented out, by hand only. A bare `ticket.mjs new` or `unblock` lands at the foot of this file, under 8b,
#   where no lane reaches it: pass --after, or move the line into its area's band at once.

# --- 1. PERFORMANCE AND GPU — the whole optimization group, cleared first (owner, 2026-10-16: "move all of those gpu and performance
# ---    tickets above all of the house tickets let's clear those first"; earlier the same day: "clear all of the optimization tickets").
# Owner, 2026-10-16: "in a browser on mobile we get memory crashes and it's getting jittery ... keep it simple and lightweight ... rely on the local cpu gpu". Mobile performance and memory group T-2546..T-2558 (not T-2552), dependency order: measure, cut CPU/geometry, cut textures, smooth frames, then the WebGPU spike (T-2558, ruled (a) 2026-10-16). Same day: "tap into local computing resources ... based on the browser and platform or ... a big package app download that happens up front" added T-2559 (device profile), T-2560 (prebuilt town), T-2561 (download the year to disk).
# Owner, 2026-11-05 re-rank: dev's red content-build smoke and the phone's shadow-caster cut, moved up from 8b's foot and band 7.


# --- 9. LOOP IMPROVEMENTS — operations: the loop's own tooling (lap, claims, merge, gates, tickets). Owner, 2026-10-20: right under
# ---    the performance band, and GPU or performance follow-ups go to band 1, a building's to its own band, not here.

# --- 2. PRAIRIE AVENUE 1904 IN PROGRESS — every Prairie Avenue house already begun, finished next (owner, 2026-10-16: "finish any
# ---    existing in progress buildings in 1904"): Keith (1808), Glessner's sign-off, 1621-1625, 1637, then 1801, 1812 and 1811,
# ---    whose K01 massing pieces have merged.
# Owner, 2026-10-13: "Sure" (move T-1882 to the top) — 1808 Prairie rebuilt to its photographs, thread "Keith house vs photos"; T-1883 waits on it and takes this line when it merges.
# Owner, 2026-10-12: "Can you move these up to top you started most of this house finish it" (T-2369 is worked interactively; T-2370, T-2371 for the loop).
# Owner, 2026-10-13, with the 1887-91 Prairie Avenue sidewalk postcard: "we want to emulate this" (curbs and carriage walks, parkway trees with a Trees setting, soft surface edges). T-2473..T-2475, worked interactively in thread "Prairie Avenue streetscape", one PR each.
# Owner, 2026-10-13, thread "1812 structures": "For 1812 did I ask you to build the other buildings from that era ... all known structures from history"; card answer "After Prairie group"; "You can include native lodges as documented" (T-2490); card answer "Move to 14 August" (T-2490 moves the 1812 scene date first). T-2485 and T-2486 wait on T-2484 (same site) and take its line in turn.
# Owner, 2026-10-12, with photographs of the Prairie Avenue door: "the front door arch on the east also has the same stone treatment and should stand out more ... refer to the photos in the reference to make it photographic perfect" (T-2416 + T-2215, one PR, worked interactively; T-2212 waits on them).
# Owner, 2026-11-05, thread "Correct Glessner roofs and window stone": "Please create multiple tickets as needed for this and work through these as a priority #1". Worked interactively, chained one at a time (same bake): T-3371 -> T-3372 -> T-3373 -> T-3374.
# Owner, 2026-11-05, thread "Reorder queue to finish Prairie Avenue first": Pullman first ("Pullman should def be finished next"), then 1801
# reopened, Glessner, then the owner's photo reworks already in hand. T-3273 (the Pullman conservatory, filed 2026-10-31) came up from 8b's foot.
# Owner, 2026-10-28, thread "Rework Pullman estate photo match": 1729 Prairie "is still way off from a photographic match ... you need to reenter the photographic match". Reopened in place (they had closed through split pieces without their image gate, T-3235); worked interactively, one PR each.
# Owner, 2026-11-05: "1801 prairie should also reenter photo matching the facade on prairie is still way off". Reopened in place (its ## Reopened section).
T-1890 — Finish 1801 Kimball corner mansion architecture
T-3567 — Fort Dearborn Massacre monument standing in 1904 on 18th Street by Calumet: granite pedestal and bronze group from its photographs, with its card
T-3568 — Fort Dearborn Massacre monument worked to its pictures: cameras on ICHi-19208, Taylor 1893 and Detroit 4a08066, side-by-sides to matches, and the Pullman house's 4a08066 and 4a08065 records showing it
# Glessner (owner photo markup, 2026-11-05), up from 8b's foot.
# The owner's photo reworks of 1919, 1936 and 2009 Prairie (2026-11-03/04), already claimed, up from band 7.
T-3370 — 1936 Prairie worked on to its photograph: re-solve the Chicagology camera with more points (the 1886 Andreas engraving and the 1874 Land Owner vignette as cross-checks), settle where the photograph's south-east corner stands on the plan and the front's composition between the photograph and the 1911 sheet, and set the verandah's place along the front, the stacks' places and the deck's height against the photograph
T-3365 — 2009 Prairie's remaining front detailing to its pictures: the oriel's carved apron, the windows' hoods and the gable's pendant, the north corner's quoins, the gable's carved crest, the basement's three lights, the door's pinnacles, the near stack's place, and a camera solved on Monroe's 1896 plate

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
# Owner, 2026-11-05 re-rank: nearest Glessner first by street-front distance from 1800 Prairie. The houses reopened 2026-10-28 lead,
# ordered by distance (1816, 1824-1828, 1815, 1708-1712, 1823, 1827), then 1916-1936, then 1613-1619 and the 20th-22nd block in its
# existing order; T-2163 (the district grounds and walk, unblocked 2026-11-05: T-2983's pieces have all merged) goes before the verifies.
# Owner, 2026-10-28 (decision card "Reopen them below Pullman"): eight houses that had closed through split pieces without their image gate, reopened in place (T-3235).
T-1886 — Refine 1816 Henderson mansard house
T-1887 — Refine 1824 Marsh altered front and 1828 neighbour
T-3562 — 1815 Prairie's remaining photograph differences: the pavilion's full 4 m width with the door in it, its dentil band and shoulders, the corner bay's set-out past the flank, the rock-faced south flank, the door's pedimented hood, the stoop's newels, arched underside and basement doorway, the mansard's curb height, cresting, finials and south-flank dormer, the north stack's place, and which front stood in 1904 (after the piece before it)
T-1872 — Refine 1708 and 1712 townhouse fronts
T-1894 — Refine 1823 Dent house
T-1896 — Finish 1827 Doane twin-tower mansion architecture
T-1902 — Finish 1916-1930 identity and 1936 Allerton estate architecture
T-1935 — Refine west 1800-1900 service buildings and Glessner boundary
T-1868 — Refine 1613, 1615 and 1619 east row
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
T-2163 — Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all three blocks, measured on a phone
T-1948 — Verify the completed 18th-20th Prairie streetscape
T-1947 — Verify the completed 16th-18th Prairie streetscape
T-1949 — Verify the completed 20th-22nd Prairie streetscape
# Glessner look research (owner, 2026-10-29), evidence only, up from 8b's foot.
T-3246 — Marble look target for Glessner: one photo-generated world beside our render, evidence only

# --- 3. THE NAVIGATOR — the interface work from the owner's Navigator design doc (owner, 2026-10-16: "then we do all of this
# ---    interface work, follow that with the balance of buildings in 1904"). Filed into this band in dependency order.
# Order: the two card bugs from the review and the gold/silver/bronze grade colors, then E1 arrival, E2 the Navigator shell, the string table, E3 HUD, E4 Jaunts, E5 the
# building dossier (summary record, Glessner pilot, Inspect), E6 Confidence view, E7 Move, E9 Map/Jump/Settings with Researcher
# mode, sound and the field log (owner rulings 2026-10-16), E8 Guide and Tour, then the E10 content gates. Each ticket names what
# it waits on under "Depends on"; take the next workable one while a dependency is open. Spec: chicago-tickets
# evidence/navigator-mk2-2026-10-16/DESIGN.md. NAV-1006 (student playtest, T-2670) is held in band 8F.
# Owner, 2026-10-20: sound off by default; the gaze tag to the right nav under the address, smaller, fading by default (T-2941, T-2942, one PR).
# Owner, 2026-11-05 re-rank: band 3 moves below the balance of Prairie Avenue ("finish prairie Ave first"); T-3043 came up from 8b's foot.
T-3043 — Guide's glossary tap check finds no locked term on Home since its Confidence view tile became a button

# --- 4. 1835 — the 1835 town's open work, one band for its own agent (owner, 2026-11-05: "keep the rest of the tickets in sections where
# ---    they can be worked by separate agents later").
# The picture-match redos parked at 8b's foot since 2026-10-22 come up here, with the seating remainder and the brick ticket, so
# nothing workable is left under the blocked band (owner, 2026-11-05: "make sure we are not leaving things at the bottom").
# T-3341 covers 1812's brick too; it is here because the 1835 brick library is its source.
# Owner, 2026-11-12, thread "Consolidate ticket queue": Mark Beaubien is one of all the 1835 people given days, as 1812 and 1904 were, not his own tickets (T-2673..T-2675 folded in).
T-3556 — Put everyone of 1835 in the town with a day, as 1812 and 1904 have: the carded townspeople drawn at their homes and work, Mark Beaubien at the Sauganash among them, and the rest asked for at their doors

# --- 5. 1812 — the 1812 scene's open work, one band for its own agent (owner, 2026-11-05).
# Owner, 2026-10-13, thread "1812 structures": build every documented 1812 structure. T-2484 came down from the foot of band 7.
# Owner, 2026-11-07, thread "Research and place 1812 people": "maybe you should do a multi agent research sweep to identify and place and fill in any possible people, and do reconstructions for the balance in 1812 since we dont have many". T-3461 cards first; T-3462..T-3467 place each group.

# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-11-12, thread "Consolidate ticket queue": "a lot has been done and there probably are only a few items left ... consolidated
# into a limited number of tickets that will be faster to complete". 8C, 8D and 8E were pulled into the eight tickets below
# (T-3553..T-3560); each lists what dev already has, to reuse, and a short acceptance. Add findings to them; don't file per-person tickets.
T-3553 — Finish people's clothing: no breakthrough in motion, better collars and seats, the six-role wardrobe reviewed beside period photographs, coat tails that sway
T-3554 — Everyday motion for people: exported talk, gesture, carry and work clips on the shared rig, sweeping and leaning with their props, and contact shadows under feet and hat brims
T-3555 — A living town at a phone's cost: far people as impostor cards, middle-distance people instanced, and horse-drawn traffic moving on distant streets, inside measured budgets

# --- 8D. PERIOD CARRIAGES AND WAGONS — the Glessner carriage ride first (owner, 2026-11-09), then the photographic vehicles (epic T-2791)
# T-2795 and T-2801 are done (the waiting Glessner team, #1908) and leave the queue when settle reads the merge.
T-3557 — Ride the Glessner carriage: ask the coachman, board, ride a short round with Mr. Glessner aboard, stop and get down, by keyboard and touch
T-3558 — Finish the photographic wagons and Brougham: the farm-box master qualified, the covered wagons upgraded but kept distinct, and the Brougham matched to its 1893 plate and qualified in town

# --- 8E. PERIOD HORSES AND GEAR — the photographic horse and its trot, then riding (epic T-2798)
T-3559 — Finish the photographic horse: near anatomy and coat against cleared views, near, mid and far exports, and a grounded trot beside the delivered walk
T-3560 — Ride a horse: period saddle and bridle, a fitted rider at walk and trot, and mount, steer and dismount by keyboard and touch

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
# BLOCKED-TECH T-2365 (opened 2026-10-11, SOUTH_TIME) — K14 compared beside a newer neighbour: 1708 Prairie, an empty lot on the 1886 Robinson plate, takes the kit at its own …
#     waits: T-1872
T-3502 — dev's content-build smoke is red on three legs (dev c891a26d7 + PR #1873's 1904-only diff, run 42469167608): 1835 boot payload 43.017 MB over its 40.2 MB budget, 1835 'balanced' detail at West prairie 2,654,960 tris over its 2,625,000 ceiling, and the Glessner People card's why reading 'Face reconstructed after a stand-in' where the T-3265 check wants 'Inferred…'
T-3563 — Settings card: icon tabs, mouse sensitivity, What's new and Research at the end
T-3564 — Glessner to Kevin's 2026-11-10 photos: coach-house doors and drive, Prairie arch roll, alley dormer, court wall, 35 plaque and green sash, varied granite
T-3566 — 1721 Prairie: the 1863 frame Dexter house standing behind Arthur Little's brick front, built to the 1891 plate and the Detroit print
T-3569 — Replace 1904 music with Kevin's ten-track ragtime playlist on shuffle
T-3570 — Meet the Glessner House: owner's edits to the opening text
T-3571 — Navigator mute all sound and mute music toggles; softer lit state on every appearance
