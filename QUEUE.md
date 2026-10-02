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
# STANDING RULE (owner, 2026-09-27): LOOP FOLLOW-UPS GO TO THE FOOT OF BAND 9, NOT BESIDE THE BUILD. A ticket a run files
# while working — tooling, lap, bake and rederive faults, deal and seating refinements, measurement gaps — is filed
# `--after` the LAST band-9 row. Two exceptions only, stated in the ticket's first line: (a) dev's gate is red, or
# (b) the build ticket being worked, or the next 5C/5D row, cannot be finished without it — then it goes directly above
# that row. Add a finding to the ticket being worked before filing anything. Owner: "move loop follow-ups to band 9".
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
T-1950 — The plan's last H3 on blk_washington_clark raised on lot 0, the Washington-and-Clark corner, with its stable and privy, keeper and lodgers seated — the lot's slot request re-seated and any household it displaces owed in writing
T-1951 — The South's remaining H3 boarding houses the book orders — the plan's two on blk_washington_dearborn and two on blk_washington_market, whose every free lot but the kept-open one carries a dwelling slot request — each with its stable and privy, keepers and lodgers seated, the displaced requests re-seated or owed in writing, and the cell's orders the plan holds no H3 for stated
# --- 5D. STRUCTURES — finish: fabric by household, plank walks, yards, signs, camps
# Owner, 2026-09-30: photographic quality; T-1769 prepares the Glessner v4 methods and textures before T-1210–T-1213 can close.
T-1771 — Shape South Water and the working riverfront as worn earth, low docks and connected ramps up to muddy streets
# Owner, 2026-09-30: full dirt streets, working river ramps, grey sand-to-prairie transitions and worn owner-varied plank colours; consume T-1769, coordinate T-1211.
T-1839 — The fabric's cladding, trim and chimney fabric by household, dealt under the same rule, siding stock reconciled with T-0112's neighbour separation
T-1818 — The fabric to the photographic benchmark: T-0002's board-tone jitter, phase-age weathering and board-width irregularity in materials.py under the rule, the full bake, lake_market and south_water critic frames, before/after captures at 390x780 and 1280x800 against Glessner v4 with a written critique and town-wide frame costs, no two neighbouring reconstructed buildings sharing a finish
T-1823 — The walk by business carried to the new business fronts town-wide as the frame budget allows — the cross streets and the West Division — with corner crossings at the principal streets and the cost measured
T-1815 — The street edge to the photographic benchmark: planks, stoops, posts and blocks at period scale with joinery, contact and shadow, before/after captures at 390x780 and 1280x800 against Glessner v4, a written critique, town-wide frame costs measured
T-1212 — Yards for every household: lot-line and dooryard fences, gardens, woodpiles, wells, privies and stables assigned by household type, wagons and barrels and trade goods at the shops by trade — the enclosure, yard and outbuilding layers extended to the reconstructed town
T-1836 — Signboards to the photographic benchmark: painted lettering on wood, grain, edge wear, bracket and strap timber, a store board, bracket sign and tavern device reviewed at 390x780 and 1280x800 against Glessner v4 with before/after captures, a written critique and town-wide frame costs
T-1804 — The conjectural camp grounds and the Native and Métis camps: the land-sale crowd south of the fort, the immigrants' wagons at the west approach, and the trading families from T-1177's evidence (review_required + touches_removal), with the screenshot from the fort's south-west corner
T-0772 — Twelve dooryard gardens went with the retired households: should a garden follow the house or the household?
# --- 5E. STRUCTURES — converge: every person housed, every business roofed, the town complete
T-1215 — Converge the reconstructed town: every person housed, every business roofed, every roof occupied or its use stated, the census's dwellings ratio met, the programme reconciled, the budgets re-measured and set — the completion report a visitor can open
# Arrival/jaunts: read docs/ARRIVAL-JAUNTS-EXECUTION.md; honor ticket dependencies.
# Finish each subsection; unavoidable successors stay beside their dependency, not at the tail.
# --- 6A. ARRIVAL AND SOURCES — measured loading, time rollback, source library, free start
# --- 6B. JAUNTS ENGINE — content contract, navigation, travel, choices, history and menu
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
# --- 2026-09-28 (owner): in render order — ground and the 1904 landing (T-1250..T-1252), structure versions by URL (T-1727), streets then their materials (T-0474, T-1728), the Glessner House and its compared versions (T-1729, T-1730), then the rest of the district.
# RESUMED — owner, 2026-10-01: Go; enqueue the complete T-1837 implementation programme as one group below the existing queue. Legacy umbrellas remain references; work the 110 child tickets at the bottom.
# UMBRELLA T-0475 — Build the 1904 Prairie Avenue landmark mansion core — execution delegated to T-1837 children below
# UMBRELLA T-0476 — Fill the 1904 Prairie Avenue corridor with documented residences and outbuildings — execution delegated to T-1837 children below
# UMBRELLA T-0477 — Build the 1904 Prairie Avenue streetscape, vegetation and urban furniture — execution delegated to T-1837 children below
# Architectural decomposition: T-1837; T-1840..T-1949 are open in one dependency-ordered group at the bottom. See evidence/T-1837-prairie-1904-architectural-study/README.md.
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
# BLOCKED-TECH T-1205 (opened 2026-09-16, TOWN) — Build the North Division's Kinzie band to its seats: the Kinzie properties' neighbours, the North Water ban…
#     waits: the north ground. All 61 remaining north roofs sit in one district_balance row, north_division_beyond_modelled_ground, state gated: terrain, hydrology, flora and map coverage stop short of local N +760 m, 27 of the district's 32 platted block rows are unsubdivided and district headroom is 0. Unblock when the ground is carried and the balance opens.
# BLOCKED-TECH T-1566 (opened 2026-09-25, META) — The staffing mint's payment never prices the DIVISION axis: a north lodging slot pays for a hand in a south…
#     waits: T-1209 — the lodging roofs the beds are in are not raised, so the_owner_s_ruling.mintable_today is 0 and the division axis prices a payment nobody can spend. The ticket's own text says it rides along with T-1209 rather than opening a PR of its own; three runs have claimed it to re-read that same note.
#
# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-09-30: build the human library and browser rendering path before loop optimization; Mark Beaubien is the first end-to-end historical example.
T-1786 — Define the portable Chicago human contract: Blender masters, browser GLB first, Unreal export later
T-1787 — Build the portable human export pipeline: skinned GLB, textures, LODs and validation from Blender to Chicago 4D
T-1788 — Give Chicago 4D a reusable browser human actor: skeletal animation, morphs, LODs and interaction hooks
T-1789 — Build the first modular 1835 human library in Blender on the shared portable rig
T-1790 — Build the portable human animation library: idle, walk, talk, gesture and work clips on the shared Chicago rig
T-1791 — Build Mark Beaubien as Chicago 4D's first historical portable human, from Blender master to interactive browser actor
T-1792 — Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly
# --- 9. LOOP IMPROVEMENTS — scene budgets, gates, build cost, and rendering
T-1617 — settle reads every ticket's pr: as a kevinrhaas/chicago PR, so a ticket whose PR is in polecat-platform never settles, and will be settled by an unrelated chicago PR once the numbers meet
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
T-1634 — Desktop smoke part 12 times out waiting 30 s for the scene to be ready after the What's-new reload, when frames cost about 2 s: 2 of 3 runs on a 4-CPU session container, on a tree whose only part-12 change was a changelog stamp
T-1671 — rederive.mjs --run leaves manifest steps 77-121 standing on the resident cards its second pass rewrote, and only 122-159 are now re-run
T-1669 — The street-face business deal and the platted household deal take from one pool of roofs and neither can see the other's picks: 40 seats owed, and a re-order of either moves the count with nobody deciding it
T-1670 — A counter trade and a works trade want different roofs and the register holds no reading that tells them apart, so a cabinet manufactory can still be seated in a store-residence
T-1650 — tools/bake.sh --only a,b,c silently builds nothing: build.py compares the id by equality, so the comma form its own usage documents reports 0 assets built and exits 1
T-1653 — bake.sh --only <one-id> still runs web_derivatives.sh over all 422 assets, so a one-roof re-bake costs ~18 minutes of a run's foreground budget
T-1632 — adopt_street_faces.derive() shadows named_dwellings() with a list of businesses, so every street's roofs_home_named reads 0 and roofs_home_inferred absorbs the named homes
T-1678 — The platted deal is blind to the letter-list ruling: it seats a household T-0379 refuses a roof onto 61 standing roofs, 11 of them on South Water, and the keeper pass must then refuse every one
T-1679 — Haddock's Tavern may stand one lot east of its seat: five printings of G. Spring's notice put it one lot west of plat lot 7 of block 16, and mansion_house's own position declares a lot's width of slack
T-1684 — The W2-W4 mechanics' shops have no State or Dearborn face to take: no platted-block slot in the whole recipe is dealt onto a cross-street face, and every Lake-Randolph block reads at_capacity
T-1694 — The south division's last store has no ground: the stores_mixed_use cell reads 41 of 42 with one owed, every Lake-Randolph block reads at_capacity, and T-1201's four children have all closed
T-1689 — Seven household cards are still NAMED a name from the post office's letter lists while their person's letter_list_only flag has been correctly cleared: the minting pass revises the name when it clears the flag, or says why the name stands
T-1690 — Place the First Baptist meeting house on South Water Street near Franklin: the small frame building that was a Baptist meeting house on Sunday, Sproat's boys' school on weekdays and the first Episcopal services' room on 19 October 1834
T-1691 — The Lake district's 44 empty dwelling, business and civic roofs: extend the roof-keeper layer past south_water and write a household onto every Lake-Randolph roof the platted deal seated one on, or say on the roof what refuses it
T-1697 — The roof-keeper layer selects by ID PREFIX and a roof's block is a matter of POSITION: recon_1835_west_018, _019 and _021 stand on blk_randolph_clinton and were invisible to T-1685's pass by construction, which will recur in every district where a block's ground and a roof's id disagree
T-1692 — One yard building for every four houses is a claim about the TOWN's A-family targets and not about any block: price the 158 stables, barns, privies, woodsheds and utility roofs against the dwellings they are meant to serve, and say whether the target is short or the districts are unevenly dealt
T-1693 — dev's frontage census is one refusal out: the walk layer refuses 109 street walls where the smoke expects 108, measured on a pristine dev
T-1695 — T-1202's acceptance asks D4-D7 dwellings to fall in SIZE southward and the programme has no size-by-latitude term: the authored policy grades density, the D4-D7 mean footprint rises 53.0 to 55.2 to 59.0 m2 going south, and the clause should be corrected rather than chased
T-1696 — Carry the plat's seven north-south columns from local N -400 to Madison: the terrain no longer blocks them (T-0219 reached N -3800, and all 24 boundary points of the Washington-Madison tier are on modelled ground), but thompson_lots.json holds no blk_washington_ block, so the last tier has no committed geometry and no roof can stand there
T-1698 — Desktop part 1 is red on dev on four fence, pen and dooryard visibility checks, and the smoke record still says PASS
T-1701 — T-1698's four fence reds are five, and the fifth is at mobile: the frontage layer's walks and posts fail with its own problem list reading [none]
T-1699 — Make data/wharves and data/frontage target surfaces for the research-spend ledger: the wharfing ordinance's eighty feet and the South Water Street footway have a layer and cannot reach it
T-1700 — The county called something the Court House at Chicago in December 1834 and the town holds only the brick one erected that fall: find where the May 1835 term sat, or refuse it in writing
T-1702 — The town's southern land approach is missing from the street layer: the located State road from Vincennes over Hubbard's Trail reaches the modelled ground and no corridor carries it
T-1705 — Two tools still hand work to T-1202, which closed with T-1688 and is now a spent split parent: build_order_book_1835.py routes (south, institutional_public) to it and name_the_keepers_1835.py names it as a live parent — each needs a live owner or the reference retired
T-1706 — The walk backend never attaches on a mobile viewport: dev is red on five of part 4's checks — walk intent moves the camera 0.00 m with 'backend none', touch activates nothing, the thumbstick writes forward 0, and a right-half drag turns 180 degrees
T-1711 — A steward run cancelled at the 150-minute cap does not tell the scheduler its slot is free, so the lane sits empty until a cron tick that arrives 20-40 minutes apart
T-1720 — The derived manifest has two undeclared rebuild lags a merged tree walks straight into: location_spend reads a reconciliation four steps below it, and the three seating passes hand a row count along outside the sequence entirely
T-1721 — Two slices relapped PR #154 at the same time: a resume PR is not counted as a row a live sibling holds, so under slices > 1 more than one run takes it
T-1723 — Newberry & Dole's warehouse: Bonnell puts it on the north bank east end eight weeks after the scene date, so the south-bank reading now rests on an untraceable dossier tag against a contemporaneous witness
T-1724 — A yellow finish for the one house a source paints: Bonnell's small yellow house builds in unpainted clapboard because no archetype in this project has a yellow, and white was refused as a substitute
T-1725 — The Pruyne-Kimberly partnership household split, and the two Kelsey identities merged: Bonnell puts one partner's residence on the north bank and spells Kelsey both ways in one sentence
T-1726 — The platted-corridor gate sees 33 of the 79 streets this town draws: decide whether the corridor layer should reach the other 46, and adjudicate what turning it on would find
T-1737 — The re-family programme's owner tables order work from tickets nobody can claim, and its report's held count disagrees with the book's
T-1740 — In the 1904 scene the drawer's text panels are still the 1835 town's (What is not here, Residents, Businesses, Wildlife, Plants, Population, order book, jaunts, source index): gate them by the scene's layers list as T-1739 gated the drawn layers
T-1744 — L270 says Kinzie's twenty slots are labourers' households and the seats file says thirteen tradesmen's, six merchant and professional and one labourer's: correct the register to the ground it scopes
T-1745 — The 1904 grid's remaining lots: Robinson 1886 legal lot numbers on 16th-18th Prairie, and the Indiana and Calumet frontage lots
T-1746 — The seating pass asks twenty roofs of Kinzie's Addition's two subdivided blocks and the north-division memo will not carry twenty: rule which of the two moves, or carry the surplus off the addition
T-1749 — The frontage smoke's fence census has drifted on dev: 28 fence runs where the clause holds 31, and the two checks that read it are red on dev and on every branch
T-1755 — Build the South Division's remaining ordinary dwellings: the roofs the district still owes after the plat's last tier and the outer books closed, on the blocks the street carry emitted
T-1758 — Build the Market block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_market
T-1759 — Build the South Division's remaining ordinary dwellings on the plat's last tier: the Dearborn, Market and Clark blocks the platted deal still holds slots against, the rest of the tier's open ground left honestly open
T-1829 — The West Division's remainder handed on from T-1208: the 16 ordinary dwellings the programme still orders, blk_west_lake_canal's three dealt frame cottages first, built and baked with their households seated
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
T-1644 — The river walk's east end no longer walks far enough west: T-1630's recut south bank leaves the walker at E 811.5 where the check wants past E 802
T-1645 — The platted deal seats 60 letter-list households on roofs the ruling of 2026-08-30 refuses them: the deal and T-0379 disagree about 60 roofs, and one of them has to move
T-1673 — The four warehouses the South Water and Lake street line still owes: the platted-ground half of the south freight cell, raised on the party lines at the crosswalk's required F-family variants
T-1743 — The Beaubien homestead reads as three identical log houses by the fort, and two of them stand on the fort road

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
T-1955 — dev's mobile smoke part 2 is red since T-1812 graded the streets: the plank decks sit 0.120 m below grade, and all 25 aims at the inn frontage return nothing
