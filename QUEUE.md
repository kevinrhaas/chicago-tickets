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
T-2123 — Fort Dearborn's roofs sit on their walls and its timber reads weathered: the artillery house's shed roof gets its gable walls, gable ends are timber not shingle, the pickets are split and irregular with a ribband and a grained face, in 1812 and 1835
T-2124 — A period US flag flies on Fort Dearborn's staff: 15 stars and 15 stripes in 1812, 24 stars in 1835, with a gentle wind flutter that costs no lag

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
# --- 8. UNREAL DELIVERY — repeatable native builds, web parity, then streaming
# Programme: T-1356; docs/unreal/README.md. Owner-ranked here on 2026-09-18.
# Remote-workable preparation (still subject to the city-first ordering above):
T-2068 — Attach the scene bundle to the scheduled content build and its manual dispatch, publish it with a discovery manifest and a latest-good pointer, and record a fresh-download receipt (a workflow change)
#   ? T-2068 DECISION: T-2068 edits .github/workflows/chicago-4d-bake.yml (pack the scene bundle after a green bake, publish it, keep a latest-good pointer). AGENTS.md puts workflow files outside a run's scope ('needs an interactive, owner-visible PR'). Who makes that change? — (a) An interactive session with you makes the workflow edit; the packer and verifier it calls (tools/scene_bundle.py, T-2067) are already on dev  (b) A loop run may open the workflow PR and leave it for your review before merge — recommended: (a)
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
#
# --- 9. LOOP IMPROVEMENTS — scene budgets, gates, build cost, and rendering
T-2069 — Scope chicago-4d-pr-stuck.yml's concurrency group per ref, so one branch's push stops cancelling another PR's report check and leaving it unstable (a workflow change; T-1520's reading)
T-1118 — A bake whose ref merged mid-run still spends the whole bake before the PR is withheld
T-2134 — Deal the W2-W4 mechanics' shops onto a Dearborn face with the cross-street term: State is a light street and refuses a workshop, and every Dearborn corner lot of the blocks whose best face Dearborn is will be built or reserved once T-2130 lands, so first decide whether a corner lot's side street may carry a second principal roof, then deal, seat and bake
T-2136 — Name or refuse the keepers on the 24 roofs the platted deal seats outside the keepers pass's three districts — 18 on the Washington tier's blocks, the rest West and North: run name_the_keepers_1835.py over them, adding each district with the ticket that carries it
T-1711 — A steward run cancelled at the 150-minute cap does not tell the scheduler its slot is free, so the lane sits empty until a cron tick that arrives 20-40 minutes apart
T-1723 — Newberry & Dole's warehouse: Bonnell puts it on the north bank east end eight weeks after the scene date, so the south-bank reading now rests on an untraceable dossier tag against a contemporaneous witness
T-2137 — Newberry & Dole's store house stands at the Dearborn end of South Water Street by its neighbours' advertisements, and the committed warehouse stands four blocks west at Franklin: rule which building the paper means, then move or keep it
T-1725 — The Pruyne-Kimberly partnership household split, and the two Kelsey identities merged: Bonnell puts one partner's residence on the north bank and spells Kelsey both ways in one sentence
T-1726 — The platted-corridor gate sees 33 of the 79 streets this town draws: decide whether the corridor layer should reach the other 46, and adjudicate what turning it on would find
T-1744 — L270 says Kinzie's twenty slots are labourers' households and the seats file says thirteen tradesmen's, six merchant and professional and one labourer's: correct the register to the ground it scopes
T-2117 — check.sh no longer fits a steward run's 600 s on four cores: 763 of 774 steps done at 595 s, 2,288 CPU-seconds, slowest steps derive_resident_roles --check 168 s and placement_policy_1835 --self-test 162 s
T-1746 — The seating pass asks twenty roofs of Kinzie's Addition's two subdivided blocks and the north-division memo will not carry twenty: rule which of the two moves, or carry the surplus off the addition
T-1755 — Build the South Division's remaining ordinary dwellings: the roofs the district still owes after the plat's last tier and the outer books closed, on the blocks the street carry emitted
T-2132 — The West Division's remainder after T-1829: 12 ordinary dwellings and one freight roof the programme still orders, with every lot-ruled West block at capacity and 19 unruled blocks gated on a lot line
T-1957 — The South's five boarding houses still owed after T-1951: the schedule's re-apportioned H3 on blk_washington_market, the gated one on blk_south_water_market, and the three the plan holds no roof for
T-1977 — The Native and Métis trading-family camps T-1214 asked for: wait for a source that counts or places them, or build one declared camp
#   ? T-1977 DECISION: T-1214 asked for Native and Métis trading-family camps 'sized from T-1177's evidence', but T-1177 refused a count (1835_native_and_metis.json § the_counted_but_unnamed: no 1835 roll, annuity schedule or estimate in the corpus). T-1804 shipped the land-sale and wagon camps (L355) and built no Native or Métis camp. Which way? — (a) Wait for a source that counts or places the families; build nothing until one is found  (b) Build one small camp at Wolf Point or the Agency as a declared reconstruction (review_required + touches_removal, no figures), bounded by a stated figure rather than a count — recommended: (a)
T-1983 — The programme reconciled: the order book's stable and outbuilding roofs built or re-budgeted, dwellings against the census's 398, residents/transients/garrison on the census screen
T-2018 — Rule whether Jefferson Street's 1835 line stops at Kinzie: its committed reach north to Hubbard crosses Wabansia block 59, which Wright's 1834 survey draws whole
T-2022 — Seat the North Division's one owed F3 warehouse on the North Water bank: a bank-landing clause or a regrade of North Water argued on its own evidence, since no committed clause builds a warehouse on a light street
T-2023 — Seat the lodging remainder as lodging roofs rise: 7 West adults the book orders with no free bed, and 44 boarding-house and inn households waiting on roofs. T-1538's frozen top-up deals new roofs to them automatically
T-2043 — Reconcile the family rows the order book still orders after T-2021's ruling: 464 family and store households and 208 adult men in family houses, against the 1,293 head records awaiting a household and a town at its 3,265 ceiling
T-2058 — Take liberties.json off the boot path: a first visit downloads 13.122 MB against the 13 MB budget
T-2059 — The mobile flora heartbeat went from 140 to 340-390 ms with T-2015's leaf-scale trees, past the 250 ms check
T-2060 — Re-measure boot-weights.js: the terrain phase grew 0.7 to 3.7 s and the boot moved 25-70 % since its reading
T-2062 — Place the first fort's factor's house, gardens and outbuildings in the 1812 scene: the 1808 draught draws them without any regular rule (sheet_only) or not at all (not_located), so find a scaled source or rule how they may stand
T-2066 — Raise the 1812 shore bank south of Twelfth to Moses & Kirkland's 10-20 ft, with low broken sand-hills and swales the sand prairie can stand in
T-2093 — dev's smoke part 2 is red at both viewports since #396: the frontage layer lays 33 fence runs and the check still asserts 32 — T-1679 changed town_street_edge.json and not the count; read the 33rd run and restate the count or refuse the run
T-2100 — Re-pose town_backyard and town_south_water_store: both stand a metre from a wall, so their captures cannot show the yard or shop front T-2085..T-2087 are judged by
T-2113 — The arrival and welcome screens redraw an unchanged town on every frame: draw it once under the menu and again only when something under it changes
T-2138 — claim steals a dead claim on a ticket an open PR already carries when that PR's branch names no ticket: T-2122 was rebuilt in full while #449 (claude/project-thread-*) sat open with it
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
T-1645 — The platted deal seats 60 letter-list households on roofs the ruling of 2026-08-30 refuses them: the deal and T-0379 disagree about 60 roofs, and one of them has to move
T-1673 — The four warehouses the South Water and Lake street line still owes: the platted-ground half of the south freight cell, raised on the party lines at the crosswalk's required F-family variants

# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-10-03: moved to sit directly above the Prairie Avenue 1904 architectural programme.
# Owner, 2026-09-30: build the human library and browser rendering path before loop optimization; Mark Beaubien is the first end-to-end historical example.
T-1786 — Define the portable Chicago human contract: Blender masters, browser GLB first, Unreal export later
T-1787 — Build the portable human export pipeline: skinned GLB, textures, LODs and validation from Blender to Chicago 4D
T-1788 — Give Chicago 4D a reusable browser human actor: skeletal animation, morphs, LODs and interaction hooks
T-1789 — Build the first modular 1835 human library in Blender on the shared portable rig
T-1790 — Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
T-1791 — Build Mark Beaubien as Chicago 4D's first historical portable human, from Blender master to interactive browser actor
T-1792 — Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly

# --- PRAIRIE AVENUE 1904 — ARCHITECTURAL ASSET PROGRAMME (T-1837; 110 tickets)
# Owner, 2026-10-01: “Go”; “Push the tickets to dev queue in one group below”.
# One contiguous group below all existing work. Dependencies first; individual dependency and needs_bake gates remain in each ticket.
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
T-1859 — Build 1600, 1604 and 1608 north-west frontage
T-1860 — Build 1612 Goodman and 1616 neighbour
T-1861 — Build 1620 Law house restored for 1904
T-1862 — Build 1626, 1628 and small frame 1630
T-1863 — Build 1634 and 1636 stone-front pair
T-1864 — Build 1638 Shortall-Gregory Gothic house envelope
T-1865 — Finish 1638 Shortall-Gregory Gothic house architecture
T-1866 — Build 1601 house and 1603 station-side envelope
T-1867 — Build 1609-1611 lost pair and 1607 association
T-1868 — Build 1613, 1615 and 1619 east row
T-1869 — Build 1621, 1623 and 1625 east row
T-1870 — Build 1635 unresolved site and 1637 Spalding remodel
T-1871 — Build 1700-1706 Glessner family townhouses
T-1872 — Build 1708 and 1712 townhouse fronts
T-1873 — Build 1720 Walker frame villa
T-1874 — Build 1726, 1730 and 1736 replacement/altered houses
T-1875 — Build 1701 Hibbard house and rear veranda envelope
T-1876 — Finish 1701 Hibbard house and rear veranda architecture
T-1877 — Build 1709 Palmer Kellogg successor
T-1878 — Build 1719-1721 Dexter address and altered house envelope
T-1879 — Finish 1719-1721 Dexter address and altered house architecture
T-1880 — Build 1729 Pullman main house envelope
T-1881 — Finish 1729 Pullman main house architecture
T-1882 — Build 1808 Keith-Field neighbour of Glessner envelope
T-1883 — Finish 1808 Keith-Field neighbour of Glessner architecture
T-1884 — Build 1812 Wheeler shaped-gable house envelope
T-1885 — Finish 1812 Wheeler shaped-gable house architecture
T-1886 — Build 1816 Henderson mansard house
T-1887 — Build 1824 Marsh altered front and 1828 neighbour
T-1888 — Build 1834 Jones post-1886 mansard
T-1889 — Build 1801 Kimball corner mansion envelope
T-1890 — Finish 1801 Kimball corner mansion architecture
T-1891 — Build 1811 Coleman-Ames Romanesque house envelope
T-1892 — Finish 1811 Coleman-Ames Romanesque house architecture
T-1893 — Build 1815 Sears-Meeker altered house
T-1894 — Build 1823 Dent house
T-1895 — Build 1827 Doane twin-tower mansion envelope
T-1896 — Finish 1827 Doane twin-tower mansion architecture
T-1897 — Build 1900 Elbridge Keith corner house
T-1898 — Build 1906 Edson Keith and attached 1908
T-1899 — Build 1912 Moulton-Lowden Chateauesque house envelope
T-1900 — Finish 1912 Moulton-Lowden Chateauesque house architecture
T-1901 — Build 1916-1930 identity and 1936 Allerton estate envelope
T-1902 — Finish 1916-1930 identity and 1936 Allerton estate architecture
T-1903 — Build 1901 Ream post-fire house
T-1904 — Build 1905 Marshall Field Sr. mansion envelope
T-1905 — Finish 1905 Marshall Field Sr. mansion architecture
T-1906 — Build 1919 Field Jr. post-1902 enlargement envelope
T-1907 — Finish 1919 Field Jr. post-1902 enlargement architecture
T-1908 — Build 1923 Kellogg and 1945 Armour-Corwith corner
T-1909 — Build 2000 and 2010 detached frame houses
T-1910 — Build 2018 and 2026 masonry houses
T-1911 — Build 2036 Buckingham corner house
T-1912 — Build 2001, 2003 and 2005 attached row
T-1913 — Build 2009 Mayer-Meyer French Gothic house envelope
T-1914 — Finish 2009 Mayer-Meyer French Gothic house architecture
T-1915 — Build 2011 Romanesque house beside Mayer
T-1916 — Build 2013 Reid classical house
T-1917 — Build 2017, 2021 High and 2027 Cobb-associated group
T-1918 — Build 2031, 2033 and 2035 limestone row
T-1919 — Build 2100 Sherman Victorian Gothic house envelope
T-1920 — Finish 2100 Sherman Victorian Gothic house architecture
T-1921 — Build 2108 Mark Kimball and 2112 Rothschild
T-1922 — Build 2110 Rees at its historical site envelope
T-1923 — Finish 2110 Rees at its historical site architecture
T-1924 — Build 2101 and 2109 Roloson neighbours
T-1925 — Build 2115 Armour Second Empire house
T-1926 — Build 2120 and the 2126 Robbins construction phase
T-1927 — Build 2130 Murdoch rounded-bay house
T-1928 — Build 2140 Tucker-Smith corner mansion envelope
T-1929 — Finish 2140 Tucker-Smith corner mansion architecture
T-1930 — Build 2123 masonry and 2125 frame neighbours
T-1931 — Build 2127-2129 flats and 2141 non-building frontage
T-1932 — Build north-west alley coach houses and service courts
T-1933 — Build north-east rear service buildings
T-1934 — Build Pullman stable, additions and conservatory estate
T-1935 — Build west 1800-1900 service buildings and Glessner boundary
T-1936 — Build east 1800-1900 service buildings
T-1937 — Build south-west service buildings and shared Rees coach house
T-1938 — Build south-east service buildings
T-1939 — Build 213, 215 and 217 East Twentieth Street context
T-1940 — Build 2008 Calumet Hanford exterior
T-1941 — Build 2018 Calumet Wheeler-Kohn exterior
T-1942 — Build Second Presbyterian post-1900 exterior skyline
T-1943 — Finish north-block boundaries, gardens and frontage fittings
T-1944 — Finish 18th-20th block boundaries, gardens and frontage fittings
T-1945 — Finish 20th-22nd block boundaries, gardens and frontage fittings
T-1946 — Close side-street and rail-side background gaps
T-1947 — Verify the completed 16th-18th Prairie streetscape
T-1948 — Verify the completed 18th-20th Prairie streetscape
T-1949 — Verify the completed 20th-22nd Prairie streetscape
T-2125 — Zone edges blend and wander: the town, the prairies and the fort's apron meet in a ragged margin about 100 m wide, and a lone cabin's clearing is no longer a disc
T-2135 — The smoke's plant panel still asserts ten communities and 155 species, and dev has served eleven and 166 since #460 (T-2101's vacant-lot prairie): part 13 is red on dev at mobile, three checks
