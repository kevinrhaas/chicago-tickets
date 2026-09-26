# QUEUE — top is next. The parser reads only T-NNNN lines; ticket files hold evidence and acceptance.
# The owner sets the order. Work top-down, skipping a blocked or already-claimed ticket.
# Add findings to an existing ticket first. Put new one-run work beside its dependency;
# add new research readings to RESEARCH COMPLETION so the spend band can drain.
# Split multi-run epics into bounded tickets when reached; do not create a refill at the top.
# Research spend: fix identity/date/mint gates before deriving cards. THE LETTER-LIST
# RULING IS MADE (owner, 2026-09-18: option (c) on T-0660) — refusals 7 and 8 are
# mint-time rules and do not un-mint a standing record; nothing is retired, rank() is
# unchanged, and the pass SAYS a collision instead of acting on it. T-1144 is no longer
# waiting on anything and is the queue's second row; the line that told runs to skip it
# is gone with this. T-0691 shrinks to wiring its --check into check.sh.
# South Through Time: 1812 depiction follows AGENTS.md Indigenous-history review;
# ship no human figures. T-0469/T-0470/T-0471 depend on T-0468; T-0472 on T-0470.
# Prairie Avenue: T-0474 follows T-0473; T-0475/T-0477 follow T-0474;
# T-0476 follows T-0475. Respect needs_bake and other ticket-level blockers.
# Completion: preserve explicit refusals and later/out-of-town evidence; zero
# unclassified research does not mean forcing uncertain people or locations into 1835.
# T-1027 is the one-letter identity epic; Newberry and 1840 deposit work follow
# their lower resident yield. Read each ticket before splitting or claiming.
# Reconstruction (owner, 2026-09-17): BAND 2 IS OPEN NOW — it reads the layer and writes
# reports, models and an order book, and it needs no sign-off to do that. Bands 3-5 WRITE
# reconstructed people, businesses and roofs, and those wait for T-1157 to say GO.
#   The first cut gated 2-5 together, and it starved the top: band 1's rows were all in
#   flight or self-blocked, so runs fell past 59 gated tickets into SOUTH THROUGH TIME and
#   LOOP IMPROVEMENTS (T-0467, T-1154, 2026-09-17). A gate that empties the top of the
#   queue sends the loop to the bottom of it.
# Every reconstructed value carries tier, basis, seed and replaceable_by (T-1158); the order
# book (T-1166) is the quota; docs/RESEARCH/1835_reconstruction_plan.md is the map.
# Sub-bands (3A/3B/3C, 5A-5E) may be taken by different agents; within a sub-band, top first.
# Build tickets in 5C are needs_bake and hand on a successor. Native, Métis and Black residents,
# families and businesses ARE reconstructed (owner, 2026-09-17; T-1177), review_required, no figures.
# Owner, 2026-09-17: THE CITY COMES FIRST. Bands 6 (arrival and jaunts) and 7 (south
# through time) are PARKED BEHIND IT — jaunts first, then south through time. They were
# numbered 5F-5J, which read as part of the 5A-5E structures programme and is why they
# looked like city work; they are band 6 now so the ordering says what it means.
#   AND A RUN MAY NOT FALL INTO THEM. While any row in bands 1-5 is workable, that row is
# the work. If the top is gated or every row is in flight, the run SAYS SO and stops — it
# does not walk down to bands 6–9. That fall-through is how T-0467 and T-1154 were
# picked up out of the bottom of a 148-line queue on 2026-09-17 while the city waited.
# TICKET BUDGET (T-1295, owner 2026-09-17: "I don't want too many tickets and not making
# any progress"). `ticket.mjs new` REFUSES at 140 queue lines, and refuses a branch its
# fourth new ticket. Override is `--anyway --why "<reason>"` and the reason is written into
# the file. Filing is free and working is not — add a finding to the ticket it was found in
# first, which is what the line above already asks for. `split` is exempt: it replaces a
# ticket rather than adding one. An EPIC states its own cap in children (T-1236: three).
# STANDING RULE (owner, 2026-09-25): A NEW TICKET GOES BELOW THE NEXT BUILD TICKET (5C) UNLESS dev's GATE IS RED.
# Band 0 is for what blocks EVERY run — a red dev gate, a merge that cannot land — and nothing else. A finding
# that only improves the loop goes to band 9; a new research reading goes below the first district builds.
# "Put it beside its dependency" (--after) still applies, but never above T-1199 / the next 5C row for loop work.
# --- 0. BLOCKING THE QUEUE (owner, 2026-09-20). These rows are first because the loop
# --- cannot judge its own work until they are done. THREE assertions have been standing
# --- red on dev for days, and because they are red, smoke_budget reports every leg that
# --- covers them as 'already red on dev' and runs skip it — so a real regression in those
# --- parts would look exactly like the reds already there. The gate is not measuring.
# --- Below them: the deadlock that needed hands on four PRs in one evening, and the two
# --- derivation faults that cost cycles on every branch that re-derives.
# --- The old note here described the terrain fossil on #1521/#1518, cleared 2026-09-19.
# --- FOUR was the count until 2026-09-21, and it is THREE because T-1369 closed, not
# --- because its leg went green: the fix landed on #1605 and is proved on dev by the
# --- stage's own 25 rules and by the layer on disk, but desktop part 3 can no longer be
# --- RUN inside the foreground ceiling — it is killed in the block before the assertion,
# --- which has therefore been unevaluated since 2026-09-18. That is T-1501, directly below.
# --- 2026-09-25 (owner): two derivation/lap faults every resident-layer branch pays for,
# --- ahead of the re-family and seating work that is about to touch that layer.

# --- 1. RESEARCH SPEND — truth, safe derivation, roles, profiles, and locations
# --- 2. 1835 TOWN ANALYSIS — the known population profiled, the town modelled, the order book (OPEN NOW)
# --- 3A. RECONSTRUCT RESIDENTS — programme, then complete the known people (attributes, arrival, families, re-admissions)
# --- 3B. RECONSTRUCT RESIDENTS — fill the model: trades, women and children, lodgers, garrison, cohorts, transients
# --- 3C. RECONSTRUCT RESIDENTS — converge
# --- 4. BUSINESSES — the authored layer and view, the audit, staffing model, five reconstruction groups, staff, converge

# --- 5A. STRUCTURES — ground: north and west streets and alleys, terrain extent, the lot grid beyond the river

# --- 5B. STRUCTURES — seating: placement policy, roof programme re-derived, anonymous roofs redealt, everyone seated
# Owner, 2026-09-25: the register's four R6 people come into the town BEFORE anyone is seated, so seating is dealt once.
# Owner, 2026-09-25: the ten named-building corroborations are written onto the structure layer BEFORE seating, so seating adopts them.
T-1623 — The four roofs the platted deal asked of blk_south_water_dearborn and blk_south_water_wells stand on the one lot each block's schedule sizing reserves open: a ruling on whether a block may be dealt out of its open lot
T-1626 — The street-face adoption policy takes a roof raised in answer to a household's slot request before the household can adopt it: T-1622 raised the D3 and D4 blk_south_water_franklin asked for and two documented firms took both, so the two tradesmen came back owed — decide whether that precedence should hold for a roof the seating itself requested
T-1627 — T-1622 re-dealt blk_south_water_franklin out from under the agencies smoke fixture: mobile part 3 asks recon_1835_blk_south_water_franklin_d5_01 for its REFUSED agency holding and 1835_agencies.json no longer names that roof at all
# Owner, 2026-09-25: the frame ceiling is read at the worst stand BEFORE the districts are built.
# --- 5C. STRUCTURES — build, one district per run, baked, successor handed on (frame budget measured before every push)
T-1200 — Build the South Water Street river front to its seats: the forwarding houses, warehouses, stores and store-residences on the party lines from Market to State, the freight sheds and landings behind, every roof with its firm and its keeper
T-1201 — Build the Lake Street and Dearborn–Clark–LaSalle core to its seats: the store fronts and store-residences, the hotels' neighbours, the professional offices over shops, the mechanics' shops on State and Dearborn, the cottages behind them
T-1202 — Build the Randolph–Washington tier and the public square's neighbours to their seats: the professional and merchant houses (H1/H2), the churches and schools the civic band established, the log jail and the estray pen as they stand, the dwellings falling southward
# --- AFTER THE FIRST THREE DISTRICTS (owner, 2026-09-25): the research readings, the staffing division axis and the
# --- re-family end state come here, below T-1200..T-1202. They add evidence to buildings already documented or
# --- settle accounting; none of them decides where a South Division building stands.
T-1624 — The 23 pre-scene-date building placements the Chicago Democrat gives on the plat: T-1599's lot-and-block, named-corner and held-neighbour readings of 1833-34 carried forward to 1835-07-01 or refused, with the plat and the block recipes in front of them
T-1625 — The six prose building placements the books and Norris give by corner, cross street and neighbour: the First Baptist meeting house, Hamilton's own house, Mark Beaubien's frame building by Noble's, Tippecanoe Hall, the Dearborn and South Water log building with the block 14 building, and Owings's house south of the Fur Company's — each carried forward to 1835-07-01 or refused
T-1591 — The 79 INFRASTRUCTURE readings in the Chicago Democrat and the Chicago American: the river works, the fort's supply and the ordinances' town geography, each one asserted, limited or refused
T-1592 — The 13 INFRASTRUCTURE readings in the books, directories and civic corpora: Hubbard's river and portage works, Fergus, Andreas and Norris, each one asserted, limited or refused
T-1587 — Spend the 19 unasserted STREET readings: the trails, roads and street lines the papers, Hubbard and Norris name that reach no corridor in the street layer, each one asserted onto the corridor it names, limited to the division it reaches, or refused in writing
T-1588 — Spend the two landholding enrichments T-1301 routed to T-1198: wright_john_s's Chicago land purchases and original-town lots and kingston_paul's Chicago landholding, written onto the held cards by a field that says what a person held — the same shape as T-1315, T-1335 and T-1569 for the births, the kin and the posts
T-1566 — The staffing mint's payment never prices the DIVISION axis: a north lodging slot pays for a hand in a south shop, and for 19 of the 26 the register places no premises at all
T-1597 — The re-family rule has reached its fixpoint with 395 of the 523 held people still held in 44 refused buckets: the order book's programme step needs a live owner for them, and the owner's ruling of 2026-09-24 that they are re-familied and never retired needs somewhere to land
T-1203 — Build the South Division's outer ground to its seats: the Fort Dearborn Addition and Michigan Street tract dwellings, the Clark–State cottages south of Washington where the ground allows, the packing and slaughter yards on the South Branch, the country places outside the plat
T-1204 — Build the fort reach and the lakefront to their seats: the sutler's, the garrison's outbuildings and the Agency establishment as the dossiers allow, the lighthouse keeper's, the pier-works yard at the river mouth, the Lake House's neighbours on the north bank east end
T-1205 — Build the North Division's Kinzie band to its seats: the Kinzie properties' neighbours, the North Water bank's forwarding and heavy trades, the Wolcott–Kinzie core's stores and taverns, the brickyard and the school, the dwellings between Kinzie and Michigan
T-1206 — Build Kinzie's Addition and the north tier to their seats: the labourers' and mechanics' cabins, shanties and small cottages on the addition's small lots, the scattered better houses on the Rush–Pine fringe, the open ground left honestly open
# West Division ground (owner, 2026-09-25): moved here from 5A — they matter for the West builds below, not for the South districts above.
T-1479 — Move blk_lake_clinton and blk_randolph_clinton onto the West Division grid: blocks 28 and 45 re-cut in the sheet's own arrangement, with the structures seated on their lots re-seated
T-1570 — Six West Division roofs stand inside a platted street corridor the corridor gate cannot see: two in Jefferson, two in Fulton, two in Des Plaines, west_046 12.08 m in
T-1544 — Carry Jefferson Street the last 288 m from Hubbard to Ohio: modern Jefferson does not survive north of Hubbard, so the corporate boundary's west leg wants a sheet and not a node
T-1460 — The two conjectural west-prairie swales now start in open ground at E -320 and swale_a's corridor covers eight West Division roofs: review the invented alignments the terrain extension stranded
T-1207 — Build the West Division's Wolf Point and Canal Street approach to their seats: the taverns' yards and stables, the grocery and blacksmith on the approach, the ferry and the bridge heads, the cabins and boarding houses of the forks
T-1208 — Build the West Division's outer clusters and Wabansia to their seats: the three looser clusters toward the Des Plaines edge, the Wabansia cabins on the North Branch, the farms and barns on the prairie edge, the held 35 slots released on the extended ground
T-1209 — Build the boarding houses to their beds: the H1–H3 houses the lodging model sized, each with the window rhythm, service wing and stovepipes its capacity implies, its stable and privies, on the seats near the landings and approaches — and re-size the named hotels' outbuildings to their guests
# --- 5D. STRUCTURES — finish: fabric by household, plank walks, yards, signs, camps
T-1210 — Deal building fabric, finish and weathering by who lived and worked there: a physician's or forwarder's house painted and glazed, a tradesman's cottage weathered clapboard, a labourer's cabin unpainted and patched — the rule set on the material sheet, applied to every dwelling and business, no attested finish moved
T-1211 — Plank sidewalks, stoops, hitching posts and street crossings for every business face, varied by the business — a forwarding house's wide decked walk, a store's board walk and stoop, a smithy's bare ground and rail, a tavern's posts and mounting block — extended to the new fronts town-wide
T-1212 — Yards for every household: lot-line and dooryard fences, gardens, woodpiles, wells, privies and stables assigned by household type, wagons and barrels and trade goods at the shops by trade — the enclosure, yard and outbuilding layers extended to the reconstructed town
T-1213 — Signboards for every business that would have hung one: the reconstructed firms' names and trades in period lettering and forms, the attested signs untouched, the signless trades left signless by rule
T-1214 — Build the camps of the summer of 1835: a tent and wagon-camp archetype, the encampments on the grounds the transient ticket evidenced — the land-sale crowd south of the fort, the immigrants' wagons at the west approach, the pier gang at the river mouth — bounded, labelled, and empty of figures
T-0772 — Twelve dooryard gardens went with the retired households: should a garden follow the house or the household?
T-1547 — The Green Tree's south-east corner stands 0.20 m INSIDE the West Water track, and the street's trace ends at that corner: re-seat it clear, carry the trace past it, or refuse the corridor in writing
# --- 5E. STRUCTURES — converge: every person housed, every business roofed, the town complete
T-1215 — Converge the reconstructed town: every person housed, every business roofed, every roof occupied or its use stated, the census's dwellings ratio met, the programme reconciled, the budgets re-measured and set — the completion report a visitor can open
# Arrival/jaunts: read docs/ARRIVAL-JAUNTS-EXECUTION.md; honor ticket dependencies.
# Finish each subsection; unavoidable successors stay beside their dependency, not at the tail.
# --- 6A. ARRIVAL AND SOURCES — measured loading, time rollback, source library, free start
T-1247 — Roll the year back into a restrained time-machine arrival
T-1248 — Compile the sources used and their reconstruction backlinks
T-1275 — Give the loading journey 160 varied source and reconstruction statuses
T-1276 — Browse every source the reconstruction used, with its counts and used-for links
T-1277 — Share one destination search for Go to and Explore Myself
T-1278 — Land on a warm mobile welcome with Jaunts and Explore Myself
# --- 6B. JAUNTS ENGINE — content contract, navigation, travel, choices, history and menu
T-1253 — Define validated jaunt JSON and render a real pilot preview
T-1279 — Make the pilot jaunt playable with persistent stop navigation
T-1280 — Offer live jaunt travel modes and honest quick-play estimates
T-1256 — Support bounded choices, inventory and alternate jaunt endings
T-1257 — Connect jaunt stops and travel to optional historical context
T-1258 — Collect era-themed keepsakes in a five-family Chicago daybook
T-1259 — Finish the scalable Jaunts Menu and integrated start experience
# --- 6C. PRIORITY JAUNTS — six short stories, fully authored and playable
T-1260 — Publish Outfit for the West as a five-minute jaunt
T-1261 — Publish Taverns of Chicago as a five-minute jaunt
T-1262 — Publish New in Chicago as a five-minute jaunt
T-1263 — Publish Shopping South Water Street as a five-minute jaunt
T-1264 — Publish Across Wolf Point as a five-minute jaunt
T-1265 — Publish Fort Dearborn Errand as a five-minute jaunt
# --- 6D. EVERYDAY JAUNTS — nineteen additional outings in five bounded content batches
T-1266 — Publish news, mail, lodging and work jaunts
T-1267 — Publish land, freight, household supplies and clothing jaunts
T-1268 — Publish harness, candles, building materials and leather jaunts
T-1269 — Publish schooling, social visits and careful news reading jaunts
T-1270 — Publish harbor, prairie arrival and a quiet stroll jaunts
# --- 6E. ARRIVAL AND JAUNTS COMPLETE — content convergence and published mobile acceptance
T-1271 — Reconcile and time the complete 25-jaunt library
T-1272 — Verify arrival, jaunts and source browsing on the published mobile app
# --- 7. SOUTH THROUGH TIME — Prairie Avenue 1904 first (owner, 2026-09-26, with Glessner House), then Fort Dearborn and 1812
T-1250 — Trace the Illinois Central lake edge for the 1904 Prairie Avenue scene and fill shore_1880s_ic_edge, from the Sanborn 1911 sheets and the Robinson 1886 plate
T-1251 — The e1871_postfire terrain spec: the graded, filled and raised South Side ground as an authored zone table
T-1252 — Generate and bake the e1871_postfire heightfield over the Prairie Avenue reach
T-0474 — Reconstruct the 1904 Prairie Avenue street, parcel and service grid
T-0475 — Build the 1904 Prairie Avenue landmark mansion core
T-0476 — Fill the 1904 Prairie Avenue corridor with documented residences and outbuildings
T-0477 — Build the 1904 Prairie Avenue streetscape, vegetation and urban furniture
T-1286 — Cross-check the derived 1812 pre-cut shore against the Harrison 1830 trace, and record what the two readings disagree about
T-1243 — Author the e1830_natural terrain spec and generate the 1812 heightfield and the ground and water meshes across the Fort-to-Eighteenth-Street corridor
T-0469 — Reconstruct the first Fort Dearborn complex as it stood in August 1812
T-0470 — Map the 15 August 1812 evacuation route and battle-location confidence zone
T-0471 — Build the 1812 lakeshore prairie, vegetation and landscape features
T-0472 — Build the 1812 interpretive scene with Indigenous-history review gates
# --- 8. UNREAL DELIVERY — repeatable native builds, web parity, then streaming
# Programme: T-1356; docs/unreal/README.md. Owner-ranked here on 2026-09-18.
# Remote-workable preparation (still subject to the city-first ordering above):
T-1357 — Publish a versioned Chicago scene bundle from every successful scheduled asset bake
T-0252 — Decide once whether a baked town carries the nine renderer-drawn layers, or none of them
# LOCAL / QUALIFIED UNREAL ONLY — NOT WORKABLE BY THE REMOTE WEB WORKER.
# HOLD references below are comments, not claimable queue entries. Tickets are blocked-tech.
# HOLD T-1472 — on-demand latest-validated Mac build/release; qualified Mac + release access.
# HOLD T-1473 — sinking buildings/terrain contact; qualified Unreal + matched web/source views.
# HOLD T-1358 — after T-1357 and current Unreal/GPU capability receipt.
# HOLD T-1360 — after T-0252, T-1357, T-1358; Unreal visual/collision receipt required.
# HOLD T-1474 — flora corridor; after shared exports/import and placement, Unreal visual/performance proof.
# HOLD T-1475 — map/search/place inspection; runtime provenance and Unreal input/route validation.
# HOLD T-1359 — streaming corruption; affected Mac/Unreal/browser access, after native priorities.
# HOLD T-1361 — after T-1358/T-1359, approved licensed build runner, GPU host, budget and credentials.
# Coordinator: unblock only when all dependencies AND current executor capability are proven;
# immediately assign/claim on that eligible executor; otherwise retain blocked-tech.
# Return unblocked work to this band in the displayed order; do not leave local work open
# for the general loop. The held epic is a tracker, never a claimable task.
# --- 8b. BLOCKED AND WAITING — every ticket that is not workable and not finished
#
# WHY THIS BAND EXISTS (T-1518). A ticket in `blocked-owner` or `blocked-tech` is
# deliberately outside the workable set — ticket.mjs excludes both states from
# `list --workable`, and QUEUE.md carries the workable states. The consequence was
# never decided: they fell out of this file entirely. Measured 2026-09-21 on dev:
# NINETEEN live tickets appeared in no band at all, thirteen of them waiting on an
# owner ruling, the oldest opened 2026-08-21 and unseen for a month. The one class
# of ticket that most needs the owner's eyes was the one class the owner could not
# see, which is the fault this band ends.
#
# THE LINES ARE COMMENTED ON PURPOSE, exactly as band 8's HOLD list is. The parser
# reads only uncommented T-NNNN lines, so nothing here is offered as work — a
# blocked ticket is visible and still not claimable, which is the whole point.
# `ticket.mjs check` refuses a blocked ticket that is missing from this band, so it
# cannot silently re-accumulate: that gate is what makes this durable rather than
# a snapshot somebody tidied once.
#
# WAITING ON AN OWNER RULING — each names the question it waits on in its own
# `blocked_on`; the one-liners here are the ask, not the ticket.
#
# BLOCKED ON TOOLING OR ANOTHER TICKET — no owner decision is wanted; each waits on
# a capability or a sibling, and unblocks without a ruling when that arrives.
# BLOCKED-TECH T-0192 (opened 2026-08-24, TOWN) — The cross streets' own frontages get the street edge
#     waits: the frame budget: all three scene-detail ceilings go over with the seven cross streets in (full +145,639, balanced +122,299, light +15,372 at T-0135'…
# BLOCKED-TECH T-0193 (opened 2026-08-24, TOWN) — blk_lake_clinton, the West Division block T-0069 refused
#     waits: T-0190 — a second street tier for the street edge. Built and measured: both faces generate cleanly (+192.2 m of walk) but desktop 'balanced' reads 1,…
# BLOCKED-TECH T-0386 (opened 2026-08-29, META) — W. Montgomery's new auction and commission room takes David Carver's old stand on South Water Street
#     waits: T-0414 first (the street-face adoption refuses W. Montgomery for being L. W. Montgomery, against identity.json's own two_houses ruling), which in tur…
# BLOCKED-TECH T-0841 (opened 2026-09-05, META) — The keeper of the St Cyr register is graded G5, not G2c: may the officiant of a parish register be graded on it?
#     waits: T-1525 — the owner RULED on 2026-09-21 and the ladder half is written, measured and parked on PR kevinrhaas/chicago#8 (G2c 34→172, the priest off G5); the…
# BLOCKED-TECH T-1171 (opened 2026-09-16, META) — Give the remaining attested and inferred heads reconstructed families from the household model: wives, children, serv…
#     waits: T-1179's convergence must re-house T-1174's 856 and T-1347's 308 women and children into the 310 married houses the household model drew; until it do…
# BLOCKED-TECH T-1407 (opened 2026-09-19, META) — The crews of the vessels in port and the harbour-works gang seated, once a committed source gives a schooner her comp…
#     waits: a committed source giving an 1830s Great Lakes schooner her complement (an enrolment or registry return, a shipping article, or a marine list that pr…
# BLOCKED-TECH T-1414 (opened 2026-09-19, GROUND) — Seat the West Division's and Wabansia's streets and alleys as platted corridors with the small lots the sheets draw,…
#     waits: T-1193 — the modelled ground ends at local east -320 m and Jefferson, Des Plaines and the whole Wabansia grid lie west of it; docs/RESEARCH/west_divi…
# BLOCKED-TECH T-1536 (opened 2026-09-24, META) — Seat the other 76 under-tens the book orders into lodging households: the children of DOCUMENTED keepers, and of the 37 boarding houses nobody has built
#     waits: T-1537 and T-1538, with T-1209's roofs — all 76 are under_10 children of lodging households that do not exist; every documented keeper's family is already drawn or source-ruled, and the rest belong to the 37 unbuilt boarding houses.
# BLOCKED-TECH T-1532 (opened 2026-09-24, META) — Deal the 61 working lodgers the boarders stage left open: the book's 30 persons/*/lodging/trade cells, w…
#     waits: NEW BEDS. Every one of the 144 ordinary night beds is slept in since T-1535, so this ticket gained no room from it; the 61 working lodgers wai…
# BLOCKED-TECH T-1529 (opened 2026-09-24, META) — Build the tenth physician the re-cut bracket now orders: businesses/physician stands at 9 of 10 since the parish r…
#     waits: T-1525 has not landed. On dev the bracket still reads scene_date_population_low 2353, so businesses/physician orders target 9, known 8, to_reconstruct …
# BLOCKED-TECH T-1532 (opened 2026-09-24, META) — Deal the 61 working lodgers the boarders stage left open: the book's 30 persons/*/lodging/trade cells, whose m…
#     waits: THE BEDS ARE NOT THERE. All 144 ordinary night beds are slept in since T-1535, so this ticket gained no room from it; refusal 2 still forbids the stag…
# BLOCKED-TECH T-1536 (opened 2026-09-24, META) — Seat the other 76 under-tens the book orders into lodging households: the children of DOCUMENTED keepers, and …
#     waits: T-1537 and T-1538 (with T-1209's roofs): all 76 are under_10 children of lodging households that do not exist. Every documented keeper's family is already…
# BLOCKED-TECH T-1524 (opened 2026-09-23, META) — A row carrying a printing's controlled word and a row carrying the same printing without one are two rows on the…
#     waits: T-1515 — on dev, derive_resident_roles reads only the 1839 REGISTER crosswalk, so William Jones carries ONE 1839 row and the pair this ticket rules on…
#     waits: T-1540 — the owner ruled on 2026-09-21 (question 1 of 3) that the Clinton-to-Canal successor is FILED BEFORE blocks 28 and 45 move; re-cutting 32 lots against a grid short of the plat module would bake the error into everything seated on them. T-1540 is filed. Unblock when it lands.
# BLOCKED-TECH T-1536 (opened 2026-09-24, META) — Seat the other 76 under-tens the book orders into lodging households: the children of DOCUMENTED keepers, an…
#     waits: T-1537 and T-1538 (with T-1209's roofs): all 76 are under_10 children of lodging households that do not exist. Every documented keeper's family is alr…
# BLOCKED-TECH T-1530 (opened 2026-09-24, META) — Retire the 25 surplus reconstructed tradesmen in the south-side 20-29 band: persons/male/20_29/south/family/tr…
#     waits: T-1556 — the owner ANSWERED on 2026-09-24 with option (c): the surplus is re-familied, never retired, and as ONE unit for all 523 across the 48 refu…
#
# --- 9. LOOP IMPROVEMENTS — scene budgets, gates, build cost, and rendering
T-1617 — settle reads every ticket's pr: as a kevinrhaas/chicago PR, so a ticket whose PR is in polecat-platform never settles, and will be settled by an unrelated chicago PR once the numbers meet
T-1601 — The claim check reads a MINT lock as work in flight, so every freshly filed ticket looks already taken and the only way past is --force
T-1612 — A dead claim parks a queue row for days: list --workable prints 'claimed' without saying the claim is three hours stale, and the picking rule says skip anything claimed
T-1582 — The re-family programme's second and third rounds are spent but nothing says a fourth cannot appear: assert the fixpoint rather than reaching it by hand
T-1602 — rederive.mjs --run leaves the town model stale on any branch that adds residents: model_town_1835.py reads the sidecar compile_scene rebuilds after it, and the second pass does not carry it, so a clean full rebuild still fails check.sh
T-1510 — The stuck reporter cannot see a red gate: a PR whose gate failed and whose owning run has finished is the one state no automation in this repo owns
T-1520 — A cancelled non-required check leaves a PR unstable for ever: gate green, merge-ready passes over it, and the stuck reporter calls it moving — pr-stuck's third shape
T-1519 — smoke_budget --for-diff maps renderers/web/js/people.js to part 13, but the People directory's checks are guarded by stageOn(12), so a run that trusts the mapping runs the wrong leg
T-1518 — Every blocked ticket is invisible: 19 live tickets appear in no band of QUEUE.md, 13 of them waiting on an owner ruling, the oldest for a month
T-1541 — The blocked band accumulates duplicate lines: T-1532 and T-1536 each stand twice in QUEUE.md band 8b, and T-1479 stood nowhere at all until a run's gate caught it
T-1222 — Read the letter-list mint's 798-file drift and give the pass a check the gate can run at its own place in the pipeline
T-1341 — ticket.mjs --check REPAIRS the mirror it is checking, so on any branch that adds a ticket the gate's queue step mutates tickets.json while the pool reads it — the T-0856 check-that-repairs fault, one tool over
T-1344 — Splitting a ticket that has a live branch puts two runs on one acceptance: the in-flight run retargets onto a child while the child also enters the queue for a fresh claim, and neither claim contends with the other
T-1345 — step_isolation exempts gitignored build products by a hand-kept path list, when git check-ignore can classify them: a write to an ignored path is a build product and a write to a tracked one is a tree mutation, and the gate should ask rather than be told
T-1355 — The four derived research reports conflict on every merge: decide whether they come off the PR surface the way T-0937 and T-0938 took the board and the mirror, with the reading written down
T-1362 — The lap re-derives only when it merges, so a branch already current with dev stays stale against a gate dev just added: #1487 sat red on four manifest-owned files while the lap said 'already current — nothing to lap'
T-1380 — A squash merge dropped a shipped release note and re-used its version: v971 named 'Six dates that would not stick' on dev at 06:06 and names 'How many people each tavern and boarding house could sleep' at 06:31, and the first entry is gone from the file the launcher and Manager parse
T-1282 — The lap cannot re-derive a resident household card, so any PR that conflicts on hh_*.json is refused whole
T-1118 — A bake whose ref merged mid-run still spends the whole bake before the PR is withheld
T-0231 — T-0229's expiry was blocked on a flora ticket, so the raised ceilings would never have come down
T-0673 — The triangle-budget fork was never filed as a ticket, so the owner's answer had nothing to land against: record the ruling and spend it only where a breach is measured
T-0672 — The three ceilings were raised for one parcel on 2026-09-03 and light's floor was spent: re-measure once #432 lands and take every tier back down
T-0237 — The full ceiling has 1,145 triangles clear on the published mirror, twelve hours after T-0229 raised it
T-0438 — The letter-list cohort is 2.54 MiB of the published tree, and it is now the largest single item in it
T-0777 — assets/manifest.web.json's $note is rewritten with escaped em-dashes, so its own generator does not reproduce what dev committed
T-0776 — A full tools/web_derivatives.sh rewrites 348 derivatives with identical byte counts: the derivative step is not reproducible
T-0829 — A repeated string in a provenance or coverage list is the same merge artefact as a repeated id, and nothing asserts it
T-0239 — Nothing tests the party-line note's prose against the placement it describes
T-0253 — May an invented building stand on the river margin of a platted street corridor
T-0190 — A second street tier for the street edge, and the ceiling that refuses it
T-0285 — An asset carrying its own AO map cannot batch with the town: +2 draw calls for one building
T-0286 — The AO unwrap leaves 68.9 per cent of every atlas empty, and the map is priced as if it were full
T-0364 — Two byte-identical copies of changelog.js are 7.2 per cent of the published payload, and they grow on every release
T-0053 — A patched lit material silently inherits another layer's shader program
T-0371 — The lattice path's block rotation is dead code that measure_rank_bias.mjs's drift guard pins in place
T-0433 — T-0346's measured costs for the new desktop parts 4, 5 and 6 were never filed, and the two places they are written down disagree
T-0030 — A queue card in Manager reading tickets.json
# --- 10. RESEARCH COMPLETION — remaining readings, identity epics, and deposit closeout
T-1335 — Spend the kin the church registers, the papers' family columns and the completed resident enrichments state — the 166 units T-1320's book pass was never scoped for, plus the two book relatives it left unruled: ties written onto held cards, nobody minted
T-1553 — Land the 61 stated kin ties the register's 120 minted residents made landable: St Mary's parentage with both ends now in the town, reciprocal rows on both cards
T-1273 — Write every committed home and workplace reconciliation row as an associated_with row on the record it belongs to, changing no value, confidence or source
T-1274 — Move the renderers and tools off the singular lives_at/works_at once the plural rows carry every claim, and retire the pair
T-0909 — The Chappel shore drawing has no candidate left: the cheapest question is the depositor's, and it has never been asked
T-1551 — Own the 1830 census and directory residue T-1297 left behind: the unasserted name-on-a-roll units that reach no ruling now the register's 120 residents are minted
T-1552 — Own the remainder units T-1298 left behind: the reserved resident-pass people, the church register entries and the surviving letter-list name suspicions that reach no ruling
# Single-person identity, spelling and date readings: kept LAST (owner, 2026-09-25) —
# small and card-local, they do not move the city.
T-1219 — The three re-spelled cards still say in prose that the papers print the reading T-1139 overturned: hh_fraser_wm_h reads 'Wm. H. Frazer' and its own note says the papers print 'Wm. H. Fraser'
T-1281 — Is the Democrat's 'A. Sweet' of 4 June 1834 Alanson Sweet or the Alon[s]on Sweet of the same column
T-1315 — Spend the three dated birth and age enrichments T-1301 routed to T-1168: robinson_alexander, kimberly_edmund_s and maxwell_philip each carry a sourced birth date or age no field held when the reading was made, and both fields exist now
T-1569 — Spend the twelve civic, church, school and garrison post enrichments T-1301 routed to T-1188 and then T-1189: the county offices, trusteeships, ministries, schools kept and the fort clerkship written onto the held cards by the fields that now exist
T-1543 — Spend the Fergus annotation of Silas W Sherman's 1834 and 1836 sheriff elections onto the dated office T-1299 put on his card
T-1550 — Read the page for Charles Beaubien: is the St Mary's register's Charles the Charles H the voter lists and Fergus 1839 carry, or a second Beaubien of that forename
T-1554 — Read St Cyr's 1834 marriage witness against St Mary's 1833 sponsor: is L Franchere Louis Franchere
T-1606 — The two research reports embed live ticket state from a separate repository, so a sibling run claiming a ticket turns every code branch's gate red on a diff that cannot touch it
T-1628 — The La Salle slough runs inland to Randolph off Conley/Stelzer, and the owner rules it to Wright and Hathaway: in from the river just past South Water Street and into the lot, no deeper
T-1629 — Two notches enter the main stem near the foot of State Street and Wright and Hathaway draw one: the State Street slough enters at Wright's re-entrant just east of State, and the second notch goes
