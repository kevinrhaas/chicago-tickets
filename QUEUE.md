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
# - Below the 1835 work: Prairie Avenue 1904 (band 7), then the portable humans (8C). The Glessner photographic-finish
#   group and the Unreal holds are commented out and taken by hand only.

# --- 1. THE 1835 TOWN — the owed roofs raised, households seated and dealt, signs and cards a visitor reads, the
# ---    household-record retirement, then the research readings (owner, 2026-10-10: held tickets that can now be
# ---    worked go to the top with the core 1835 loop and research tickets)
T-2270 — The South's last owed D1 and H3 on School Section block 82: no banded South row is admitted by a clause that takes either, so T-2254 raised the block's four requested houses and left these two
T-2251 — Deposit and read the marriage leaves of St Mary's register — the book Father Rouges bound in 1880 with the baptisms already deposited — for the forename of the 1834 witness every printing sets as 'L. Franchere'

# --- 9. LOOP IMPROVEMENTS — a follow-up a run files lands at this band's foot (owner, 2026-09-27)
T-2300 — wall-relief.js's orl and frontage.js's modMap are DataTextures (flipY false) sampled beside a flipY'd normal_gl Texture, so each 1835 wall and frontage tile's AO, roughness and grain is mirrored vertically against its relief

# --- 7. SOUTH THROUGH TIME — PRAIRIE AVENUE 1904, ARCHITECTURAL ASSET PROGRAMME (T-1837)
# Umbrellas T-0475, T-0476 and T-0477 are references only; their execution is delegated to the T-1837 children below.
# Owner, 2026-10-01: “Go”; “Push the tickets to dev queue in one group below”.
# One contiguous group below all existing work. Dependencies first; individual dependency and needs_bake gates remain in each ticket.
# Owner, 2026-10-08: "a controlled set of tickets to do an initial pass of the whole district ... then the tickets later for each building can refine
# your initial serviceable good draft model layer". Order: reconciliations, components, then the DISTRICT DRAFT PASS (T-2159 the 18th-20th block and the
# draft builder, T-2160 16th-18th, T-2161 20th-22nd, T-2162 the edges, T-2163 the grounds and the whole-district phone walk), then the per-building
# REFINEMENT tickets ("Build ..." retitled "Refine ..."), each depending on its block's draft. The draft pass is capped at five; it splits only in halves.
T-2289 — K02 on the 1808 exemplar: rusticated base, coursed ashlar, corner bonds, voussoirs, coping and chipped edges built from the stone library, baked and verified at both viewports with costs
T-2291 — K03 on a named target: a facade and service-wall comparison (pressed front against common-brick return and rear) built from the brick library with bonds, corner returns, soldier and segmental heads, string course and soot/damp mask, baked and verified at both viewports with costs
T-2293 — K04 on the 1808 exemplar: slate courses with cut edges, hip and ridge caps, valley flashing, a dormer apron, gutters on brackets, outlets, downpipes and shoes ending at ground, built from the roof library, baked and verified at both viewports with costs
T-2301 — K05 roof-construction kit: hip, ordinary/stepped/ogee gable, convex and concave mansard, polygonal and conical tower roofs and gabled dormers as a data roof graph (planes, hips, ridges, valleys, fascia, soffit, verge, dormer cheeks, cross-gable return), with a generator that trims every plane at its valleys and intersections into a watertight closure, measured for planes crossing gable faces, floating cornices and doubled coplanar faces, studied in raking and diffuse light with costs
T-2302 — K05 on the 1808 exemplar: its roof rebuilt from the roof-construction kit with no plane crossing a gable face, no floating cornice and no doubled coplanar surface, dormers and chimney penetrations closed, baked and verified at both viewports (front, oblique, rear and roof views) with costs
T-2298 — K06 on the 1808 exemplar: real wall openings with jambs, reveals, sills and heads, separate sash and glass over dark enclosed backing and blinds behind the glass, built from the window kit, baked and verified at both viewports (front, oblique, rear and roof views) with costs
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

# --- 8C. PORTABLE HUMANS — Blender is canonical; browser/three.js first, Unreal is a later consumer
# Owner, 2026-10-08: "move the portable people tickets after the south through time tickets" — moved here, below the whole Prairie Avenue 1904 programme (draft pass, refinements, block checks, Glessner repair).
# Owner, 2026-10-03: had moved it to sit directly above the Prairie Avenue 1904 architectural programme.
# Owner, 2026-09-30: build the human library and browser rendering path before loop optimization; Mark Beaubien is the first end-to-end historical example.
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
