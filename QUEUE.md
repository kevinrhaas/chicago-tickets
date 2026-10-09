# QUEUE — top is next. The parser reads only T-NNNN lines; ticket files hold evidence and acceptance.
# The owner sets the order. Work top-down, skipping a blocked ticket or a LIVE claim. A claim
# past the 3h run window is a dead run: `list --workable` prints it TAKEABLE and `claim` steals it.
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
# STANDING RULE (owner, 2026-09-27): LOOP FOLLOW-UPS GO TO THE FOOT OF BAND 9, NOT BESIDE THE BUILD. A ticket a run files
# while working — tooling, lap, bake and rederive faults, deal and seating refinements, measurement gaps — is filed
# `--after` the LAST band-9 row. Two exceptions only, stated in the ticket's first line: (a) dev's gate is red, or
# (b) the build ticket being worked, or the next 5C/5D row, cannot be finished without it — then it goes directly above
# that row. Add a finding to the ticket being worked before filing anything. Owner: "move loop follow-ups to band 9".
# --- TOP (owner, 2026-10-04): the town's ground reads as kept, lived-in ground, not wet prairie, and the town costs fewer
# --- triangles for it. In order: the ground carried over the built town, the turf drawn cheaply with Scene detail,
# --- every grass and land texture rebuilt the road's way (owner, same day), kept lots, then road shoulders, alleys,
# --- frontages and paths. Trees and the prairie outside the town are kept.
# Owner, 2026-10-04 17:18Z: "when you walk it is laggy now ... some focused effort on that" — lag first: T-2096 while moving, T-2099 in still frames (widened 17:26Z: "that lag is all over not just walking").

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
# Owner, 2026-10-02: dev's two smoke reds first — the river walk (mobile part 2) and the boot payload over 12 MB (desktop part 1). #258 and every baked PR wait on them.


# --- 0B. UNBLOCKED — previously blocked tickets whose blockers have landed (owner, 2026-10-03: "move those up")
# Visible builds first, then the lodging/resident layer they feed, then the one ruling. Each ticket's own
# "Queue cleanup 2026-10-03" section names what landed. T-1953 stays blocked on T-1414 (band 8b).
# Owner, 2026-10-03: T-2017 first. PR #329 (T-2012) cannot merge until its terrain is rebaked.

# --- 1. RESEARCH SPEND — truth, safe derivation, roles, profiles, and locations
# --- 2. 1835 TOWN ANALYSIS — the known population profiled, the town modelled, the order book (OPEN NOW)
# --- 3A. RECONSTRUCT RESIDENTS — programme, then complete the known people (attributes, arrival, families, re-admissions)
# --- 3B. RECONSTRUCT RESIDENTS — fill the model: trades, women and children, lodgers, garrison, cohorts, transients
# --- 3C. RECONSTRUCT RESIDENTS — converge
# --- 4. BUSINESSES — the authored layer and view, the audit, staffing model, five reconstruction groups, staff, converge

# --- 5A. STRUCTURES — ground: north and west streets and alleys, terrain extent, the lot grid beyond the river
# Owner, 2026-09-26: the river front's own bank first. He flew it against Wright and Hathaway, and T-1200 builds on this waterline.

# --- 5B. STRUCTURES — seating: placement policy, roof programme re-derived, anonymous roofs redealt, everyone seated
# Owner, 2026-09-25: the register's four R6 people come into the town BEFORE anyone is seated, so seating is dealt once.
# Owner, 2026-09-25: the ten named-building corroborations are written onto the structure layer BEFORE seating, so seating adopts them.
# Owner, 2026-09-25: the frame ceiling is read at the worst stand BEFORE the districts are built.
# --- 5C. STRUCTURES — build, one district per run, baked, successor handed on (frame budget measured before every push)
# --- AFTER THE FIRST THREE DISTRICTS (owner, 2026-09-25): the research readings, the staffing division axis and the
# --- re-family end state come here, below T-1200..T-1202. They add evidence to buildings already documented or
# --- settle accounting; none of them decides where a South Division building stands.
# West Division ground (owner, 2026-09-25): moved here from 5A — they matter for the West builds below, not for the South districts above.
# --- 5D. STRUCTURES — finish: fabric by household, plank walks, yards, signs, camps
# Owner, 2026-09-30: photographic quality; T-1769 prepares the Glessner v4 methods and textures before T-1210–T-1213 can close.
# Owner, 2026-09-30: full dirt streets, working river ramps, grey sand-to-prairie transitions and worn owner-varied plank colours; consume T-1769, coordinate T-1211.
# --- 5E. STRUCTURES — converge: every person housed, every business roofed, the town complete
# Arrival/jaunts: read docs/ARRIVAL-JAUNTS-EXECUTION.md; honor ticket dependencies.
# Finish each subsection; unavoidable successors stay beside their dependency, not at the tail.
# --- 6A. ARRIVAL AND SOURCES — measured loading, time rollback, source library, free start
# --- 6B. JAUNTS ENGINE — content contract, navigation, travel, choices, history and menu
# --- 6C. PRIORITY JAUNTS — six short stories, fully authored and playable
# --- 6D. EVERYDAY JAUNTS — nineteen additional outings in five bounded content batches
# --- 6E. ARRIVAL AND JAUNTS COMPLETE — content convergence and published mobile acceptance
# --- 7. SOUTH THROUGH TIME — Prairie Avenue 1904 first (owner, 2026-09-26, with Glessner House), then Fort Dearborn and 1812
# --- 2026-09-28 (owner): in render order — ground and the 1904 landing (T-1250..T-1252), structure versions by URL (T-1727), streets then their materials (T-0474, T-1728), the Glessner House and its compared versions (T-1729, T-1730), then the rest of the district.
# RESUMED — owner, 2026-10-01: Go; enqueue the complete T-1837 implementation programme as one group below the existing queue. Legacy umbrellas remain references; work the 110 child tickets at the bottom.
# UMBRELLA T-0475 — Build the 1904 Prairie Avenue landmark mansion core — execution delegated to T-1837 children below
# UMBRELLA T-0476 — Fill the 1904 Prairie Avenue corridor with documented residences and outbuildings — execution delegated to T-1837 children below
# UMBRELLA T-0477 — Build the 1904 Prairie Avenue streetscape, vegetation and urban furniture — execution delegated to T-1837 children below
# Architectural decomposition: T-1837; T-1840..T-1949 are open in one dependency-ordered group at the bottom. See evidence/T-1837-prairie-1904-architectural-study/README.md.
# DRAFT PASS FIRST (owner, 2026-10-08): after the reconciliations and shared components (T-1840..T-1858), five tickets T-2159..T-2163 draft the whole district; every per-building ticket refines that draft and depends on it. No new per-building tickets.
# --- 8. UNREAL DELIVERY — repeatable native builds, web parity, then streaming
# Programme: T-1356; docs/unreal/README.md. Owner-ranked here on 2026-09-18.
# Remote-workable preparation (still subject to the city-first ordering above):
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
# 2026-10-03 (owner-directed scan): T-0192, T-0193, T-0386, T-1171, T-1205, T-1414, T-1524, T-1529, T-1532, T-1536, T-1538 unblocked
#     and moved to band 0B; T-0841 and T-1530 withdrawn (their work landed); T-1566 merged into T-1532.
# BLOCKED-TECH T-1407 (opened 2026-09-19, META) — The crews of the vessels in port and the harbour-works gang seated, once a committed source gives a schooner her comp…
#     waits: a committed source giving an 1830s Great Lakes schooner her complement, and the Chief Engineer's 1835 harbour-works report. Neither is in the corpus.
# BLOCKED-TECH T-1953 (opened 2026-10-01, TOWN) — The West's three H3 boarding houses the book orders, on the platted ground T-1414 seats
#     waits: T-1414 (now open in band 0B). Unblock when T-1414 lands.
# BLOCKED-TECH T-2153 (opened 2026-10-06, META) — Measure T-1711's fix: name the first steward-improve run cancelled at its cap after polecat-platform#190, and the stewa…
#     waits: the first steward-improve run cancelled at its 150-minute cap after polecat-platform#190 (2026-10-06T19:59:48Z): none in the 61 runs to 2026-10-08T04:04Z — the lane hit its weekly usage limit at 22:17Z and no run could reach the cap; the read is ~6 tool calls, see the ticket's 2026-10-08 reading
# BLOCKED-TECH T-2023 (opened 2026-10-03, META) — Seat the lodging remainder as lodging roofs rise: 7 West adults the book orders with no free bed, and 44 boarding-house…
#     waits: T-1953 — the 7 West adults need a West lodging roof and T-1953 (blocked on T-1414) is the only ticket that raises one; the division axis prices an empty purse (0 slots outstanding) and the 24 unordered beds ride with those roofs. Re-measured 2026-10-08, see the ticket.
#
# --- 9. LOOP IMPROVEMENTS — scene budgets, gates, build cost, and rendering
T-2196 — Raise the South's two owed boarding houses on the Market wedge's new lots, re-freezing the lodger basis first so seat_lodgers_1835 seats their lodgers
T-2250 — A boarding house its platted keeper fills from the layer alone gets no lodging card, so the business layer raises no firm for it: Mark Beaubien keeps the Market wedge's H3 (recon_1835_blk_south_water_market_h3_02) and rcb_beaubien_boarding_house retired with T-2196
T-2252 — Cut the School Section's second tier (Monroe to Adams, east of the South Branch) into the lots the October 1833 register witnesses, as T-1477 cut Madison to Monroe — owner ruling (b) on T-2247
T-2253 — Join the Monroe-to-Adams tier to the platted grid and the roof schedule, as T-2144 joined Madison to Monroe, with the South's six gated roofs (D2, D2, D4, D4, D5, H3) dealt to it
T-2254 — Raise the South's six gated roofs (D2, D2, D4, D4, D5 and the H3 boarding house) on the Monroe-to-Adams tier's lots
#   ? T-1957 DECISION: The 668-roof schedule still deals 8 roofs (D2, D4, D5, D6, F3, F4 and these two H3 boarding houses) onto blk_south_water_market, the Market-and-South-Water wedge your 2026-08-29 closure ruling could not cut: the ground leaves 2.8 m of block depth at Market against a 24.4 m lot, so the block stays 'gated' and T-1957, T-2175 and T-2182 all wait on it. What should happen to those 8 roofs? — (a) Re-deal them onto the School Section's Madison–Monroe tier, extending your 2026-10-05 ruling on T-1755 (b) from the 40 dwellings to the wedge's 8 roofs  (b) Build on the wedge's eastern two-thirds only: cut reconstructed lots where the block has depth (about 5 of its 8 lots) and re-deal the rest, recorded in LIBERTIES  (c) Return them: cut the South's targets by these 8 and re-close the order book (folds into T-1983) — recommended: (b)
T-2249 — The housing deal counts 31 present households as housed by a workplace row alone (hh_harmon_brothers, hh_calhoun_john, hh_dole_george_w, hh_clybourne_archibald…): they sleep under no roof in the scene; seat them or rule where they slept
# --- 10. RESEARCH COMPLETION — remaining readings, identity epics, and deposit closeout
T-2233 — Seat Mary Noble as George Bickerdyke's printed wife (Democrat 3 Dec 1833, c007): his house is one the order book refused a wife, so seating her takes him out of T-2020's wife match, which re-pairs about ten houses after him (measured 2026-10-09: hh_rc_ryan_bridget moves to hh_boardman_harry, and so on down to hh_markle_joseph_w; hh_rc_crandall_clarissa stands alone again). Carry that through the fixpoint, or rule that the pairs stay and only his own wife changes
T-1274 — Move the renderers and tools off the singular lives_at/works_at once the plural rows carry every claim, and retire the pair
# Single-person identity, spelling and date readings: kept LAST (owner, 2026-09-25) —
# small and card-local, they do not move the city.
T-1550 — Read the page for Charles Beaubien: is the St Mary's register's Charles the Charles H the voter lists and Fergus 1839 carry, or a second Beaubien of that forename
T-1554 — Read St Cyr's 1834 marriage witness against St Mary's 1833 sponsor: is L Franchere Louis Franchere
T-2251 — Deposit and read the marriage leaves of St Mary's register — the book Father Rouges bound in 1880 with the baptisms already deposited — for the forename of the 1834 witness every printing sets as 'L. Franchere'
T-1645 — The platted deal seats 60 letter-list households on roofs the ruling of 2026-08-30 refuses them: the deal and T-0379 disagree about 60 roofs, and one of them has to move
T-2256 — The South's family_dwelling order has 2 households no held head fills: once T-1645 stopped dealing roofs to letter-list households, count_held_head_dwellings_1835.py finds 165 heads under South dwellings against room for 167, and T-2193, which owned the order, is done
T-2255 — The off-plat deal seats 55 letter-list households on roofs the ruling of 2026-08-30 (T-0379) refuses them: T-1645 made the platted deal owe that cohort, and the off-plat deal (tools/seat_off_plat_ground_1835.py) still deals from the rows it hands on without reading the ruling
T-2175 — The street line's other three warehouses: the F3 the schedule deals to blk_south_water_wells, which generate_block_infill refuses on a platted lot for want of river access (T-0275), and the F3 and F4 on gated blk_south_water_market

# --- PRAIRIE AVENUE 1904 — ARCHITECTURAL ASSET PROGRAMME (T-1837; 110 tickets)
# Owner, 2026-10-01: “Go”; “Push the tickets to dev queue in one group below”.
# One contiguous group below all existing work. Dependencies first; individual dependency and needs_bake gates remain in each ticket.
# Owner, 2026-10-08: "a controlled set of tickets to do an initial pass of the whole district ... then the tickets later for each building can refine
# your initial serviceable good draft model layer". Order: reconciliations, components, then the DISTRICT DRAFT PASS (T-2159 the 18th-20th block and the
# draft builder, T-2160 16th-18th, T-2161 20th-22nd, T-2162 the edges, T-2163 the grounds and the whole-district phone walk), then the per-building
# REFINEMENT tickets ("Build ..." retitled "Refine ..."), each depending on its block's draft. The draft pass is capped at five; it splits only in halves.
T-1840 — Reconcile sheet 20 building entities for 1904
T-1841 — Reconcile sheet 28 building entities for 1904
T-1842 — Reconcile sheet 35 building entities for 1904
T-1843 — Metric asset contract and Glessner comparison slice
T-1844 — Stone, mortar and dressed masonry materials
T-1845 — Pressed, common and rough brick materials
T-1846 — Period roof coverings and drainage
T-1847 — Mansard, hip, gable and tower roof construction
T-1848 — Windows, glazing and visible interior depth
T-1849 — Entrances, stoops, porches and carriage doors
T-1850 — Bays, oriels and towers
T-1851 — Carved entrances and classical or Gothic trim
T-1852 — Cornices, parapets, dormer faces and cresting
T-1853 — Ironwork, gates, canopies and boundary walls
T-1854 — Coach houses, stable fittings and service wings
T-1855 — Conservatory and greenhouse assemblies
T-1857 — Chimneys, flues and roof service details
T-1858 — Frame cladding and exterior timber construction
T-1856 — Age, surface variation and ground contact
T-2159 — Draft the 18th-20th Prairie block around Glessner: a serviceable kit-built house on every frontage, and the draft builder the other blocks reuse
T-2160 — Draft the 16th-18th Prairie block with the draft builder: every frontage and its rear service buildings
T-2161 — Draft the 20th-22nd Prairie block with the draft builder: every frontage and its rear service buildings
T-2162 — Draft the district's edges: East Twentieth Street, Calumet, Second Presbyterian and the side-street and rail-side background
T-2163 — Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all three blocks, measured on a phone
T-1859 — Refine 1600, 1604 and 1608 north-west frontage
T-1860 — Refine 1612 Goodman and 1616 neighbour
T-1861 — Refine 1620 Law house restored for 1904
T-1862 — Refine 1626, 1628 and small frame 1630
T-1863 — Refine 1634 and 1636 stone-front pair
T-1864 — Refine 1638 Shortall-Gregory Gothic house envelope
T-1865 — Finish 1638 Shortall-Gregory Gothic house architecture
T-1866 — Refine 1601 house and 1603 station-side envelope
T-1867 — Refine 1609-1611 lost pair and 1607 association
T-1868 — Refine 1613, 1615 and 1619 east row
T-1869 — Refine 1621, 1623 and 1625 east row
T-1870 — Refine 1635 unresolved site and 1637 Spalding remodel
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
T-2135 — The smoke's plant panel still asserts ten communities and 155 species, and dev has served eleven and 166 since #460 (T-2101's vacant-lot prairie): part 13 is red on dev at mobile, three checks

# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-10-08: "move the portable people tickets after the south through time tickets" — moved here, below the whole Prairie Avenue 1904 programme (draft pass, refinements, block checks, Glessner repair).
# Owner, 2026-10-03: had moved it to sit directly above the Prairie Avenue 1904 architectural programme.
# Owner, 2026-09-30: build the human library and browser rendering path before loop optimization; Mark Beaubien is the first end-to-end historical example.
T-1786 — Define the portable Chicago human contract: Blender masters, browser GLB first, Unreal export later
T-1787 — Build the portable human export pipeline: skinned GLB, textures, LODs and validation from Blender to Chicago 4D
T-1788 — Give Chicago 4D a reusable browser human actor: skeletal animation, morphs, LODs and interaction hooks
T-1789 — Build the first modular 1835 human library in Blender on the shared portable rig
T-1790 — Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
T-1791 — Build Mark Beaubien as Chicago 4D's first historical portable human, from Blender master to interactive browser actor
T-1792 — Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly

# --- GLESSNER HOUSE 1904 — EXTERIOR AND COURTYARD PHOTOGRAPHIC FINISH (MANUAL ONLY)
# Owner, 2026-10-09 UTC: file all reviewed work below the people and comment the group out; take tickets manually one at a time.
# 31 held tickets: 26 audit packages (four split into two bounded passes) plus one missing-reference retrieval pass.
# Every row is commented and every ticket is blocked-owner. Do not auto-unblock, claim, or activate this group.
# Programme/evidence/release instructions: evidence/glessner-exterior-audit-2026-10-08/README.md
# BLOCKED-OWNER T-2201 — Glessner: close the south courtyard boundary and resolve its junctions [GA-03]
T-2203 — Correct Glessner roof tile scale and coverage on every roof plane
# BLOCKED-OWNER T-2204 — Remove Glessner roof banding and stabilize tile detail in motion [GA-05B]
# BLOCKED-OWNER T-2205 — Glessner: refine ridge caps, cresting, finials, eaves and flashing [GA-06]
# BLOCKED-OWNER T-2206 — Glessner: validate roof, dormer and courtyard-bay proportions before further reshaping [GA-07]
# BLOCKED-OWNER T-2207 — Glessner: finish stable cupola and north loft fittings [GA-08]
# BLOCKED-OWNER T-2208 — Refine Glessner street masonry courses, relief and opening returns [GA-09A]
# BLOCKED-OWNER T-2209 — Calibrate Glessner granite texture, roughness and shadow readability [GA-09B]
# BLOCKED-OWNER T-2210 — Glessner: calibrate courtyard brick and limestone as distinct materials [GA-10]
# BLOCKED-OWNER T-2211 — Finish Glessner street and stable window profiles and stone supports [GA-11A]
# BLOCKED-OWNER T-2212 — Finish Glessner courtyard, bow, turret and dormer window profiles [GA-11B]
# BLOCKED-OWNER T-2213 — Glessner: give dark glazing believable exterior-visible depth and variation [GA-12]
# BLOCKED-OWNER T-2214 — Correct the mirrored Glessner 1886 inscription and monogram [GA-13A]
# BLOCKED-OWNER T-2215 — Finish Glessner entry tympanum, ornamental band and varied capitals [GA-13B]
# BLOCKED-OWNER T-2216 — Glessner: complete the main entry oak door and iron grille [GA-14]
# BLOCKED-OWNER T-2217 — Glessner: finish both porte-cochere leaves, hardware and passage [GA-15]
# BLOCKED-OWNER T-2218 — Glessner: reconstruct the curved courtyard hall steps and cheek wall [GA-16]
# BLOCKED-OWNER T-2219 — Glessner: audit basement grilles, light wells and service openings [GA-17]
# BLOCKED-OWNER T-2220 — Glessner: refine copper roof panels, seams and weathering [GA-18]
# BLOCKED-OWNER T-2221 — Glessner: complete gutters, rainwater heads, downpipes and attachments [GA-19]
# BLOCKED-OWNER T-2222 — Glessner: resolve chimney phase and finish stack/cap detail [GA-20]
# BLOCKED-OWNER T-2223 — Glessner: date and finish courtyard service stairs, rails and rear gate [GA-21]
# BLOCKED-OWNER T-2224 — Glessner: finish courtyard paths, edging, lawn and drainage [GA-22]
# BLOCKED-OWNER T-2225 — Glessner: add restrained, dated courtyard vines and exterior planting [GA-23]
# BLOCKED-OWNER T-2226 — Glessner: balance lighting, contact shadows and restrained surface aging [GA-24]
# BLOCKED-OWNER T-2227 — Glessner: validate full/light browser quality and controlled performance [GA-25]
# BLOCKED-OWNER T-2228 — Glessner: run final photographic comparison and evidence sign-off [GA-26]
