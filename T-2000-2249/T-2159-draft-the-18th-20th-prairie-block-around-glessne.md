---
id: T-2159
title: Draft the 18th-20th Prairie block around Glessner: a serviceable kit-built house on every frontage, and the draft builder the other blocks reuse
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Draft the 18th-20th Prairie block around Glessner: a serviceable kit-built house on every frontage, and the draft builder the other blocks reuse.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 151 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-08 (project thread): after the architectural analysis and the shared components, up to five tickets draft the whole Prairie Avenue district as a serviceable first pass, ahead of every per-building ticket, which then refine that draft. Owner-requested and capped at five.

## The district draft pass (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This is one of **five** draft tickets, T-2159 to T-2163, the whole of that pass. They come after the [architectural study](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md), the three sheet reconciliations (T-1840 to T-1842) and the sixteen shared components (T-1843 to T-1858), and before every per-building ticket, each of which now **refines** this draft rather than building from an empty lot. Do not file per-building tickets from here; the per-building tickets already exist.

**This ticket: the 18th-20th block (Sanborn sheet 28) and the draft builder.** It goes first because the 1904 landing faces Glessner at Eighteenth, and the study's first comparison ensemble (1801 Kimball, 1808 Keith/Field, 1811 Coleman/Ames, 1812 Wheeler) stands on this block.

### What a serviceable draft is

A draft house is complete and believable from the street, both sidewalks, the alley and the air, and it is built only from what the study already knows plus the shared component kit:

- **Footprint** from the reconciled Sanborn polygon (main body, attached wings, porches, bays), never the viewer's parcel rectangle.
- **Height**: storeys, basement and raised principal floor from the reconciled map notation, inside the starting ranges of [RECONSTRUCTION-RULES.md](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md).
- **Walls** from the register's construction family (brick, stone-front, frame, Italianate, Second Empire, Romanesque, Gothic, Georgian) using the T-1844, T-1845 and T-1858 materials, aged with T-1856.
- **Roof** family from T-1846 and T-1847 (hip, gable, mansard, flat behind a cornice, a tower where the register names one), with T-1857 chimneys.
- **Openings and front**: window rhythm, entrance, stoop, bays and cornice from T-1848 to T-1852, with counts chosen by the family rules.
- **Landmarks** get the recognisable silhouette the [building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md) names (the tower, the mansard, the shaped gable, the twin towers, the deep round-arched entrance) but not bespoke carving.
- **Every exterior face is closed**: street, sides, rear and roof. No blank boxes, no unexplained empty frontage, and no identical repeated facades unless the study attests a pair.

A draft does **not** do bespoke carving, full-resolution photo matching, measured moulding profiles or per-house colour research. Those belong to the per-building tickets that refine it.

### Rules every draft ticket keeps

- **Glessner is untouched.** 1800 Prairie stays the canonical benchmark; the draft is judged beside it, never instead of it.
- **The study's rulings hold.** Excluded predecessors stay out (study ruling 10), a non-building frontage gets its non-building state, alias and attribution conflicts keep one provisional association, and the 1904-07-01 target is never moved.
- **Stable IDs.** Each draft structure gets the ID its per-building ticket will keep, so refinement replaces attributes in place instead of adding a second building.
- **Provenance.** Every attribute carries its tier (attested, inferred or reconstructed), a basis naming this draft pass and the register row it read, a seed for stochastic choices, and `replaceable_by` naming the per-building ticket that refines it. Each house's card says it is a draft and which ticket refines it.
- **One liberty per block, not per house.** Record this ticket's draft reconstructions as a single numbered liberty in `docs/LIBERTIES.md`. Parallel PRs keep taking the same next number, so check `dev` and every open PR for the next free L number and changelog version before merging.
- **Budgets and the phone.** Draft geometry is instanced from the kit at full, balanced and light detail. Measure 1904's JS heap, load and frame time at 390×780 and 1280×800 before and after; a phone tab killed for memory is a failed ticket. Phone-only cuts must not degrade desktop.
- **Visible progress.** A changelog entry on top (`v: null, ts: ''`), stamped before merge.

**Acceptance:**

1. **A reusable draft builder.** Data-driven and deterministic: it reads the reconciled sheet census and the study's [frontage](../evidence/T-1837-prairie-1904-architectural-study/frontage-register.csv) and [building](../evidence/T-1837-prairie-1904-architectural-study/building-register.csv) registers and emits one kit-built structure per frontage, with engine-neutral parameter data. T-2160, T-2161 and T-2162 run it on their own blocks by adding data, not by rewriting it.
2. **Every 18th-20th frontage stands as a draft**: all 23 sheet-28 rows, west and east sides, plus every detached rear polygon owned by R28W and R28E (coach houses, stables, service wings), with Glessner untouched. At the landing, 1801, 1808, 1811 and 1812 read as four distinct houses from across the street.
3. **Captured and measured**: the landing pose, both sidewalks, the alley and the air, at 1280×800 and 390×780, with 1904's load, heap and frame time before and after.
4. Every structure carries the provenance, stable ID and card the rules above require, the block's single liberty is recorded under the next free number, and the changelog entry is stamped.

**Bound:** one run plus a bake. If it cannot fit, split it into **exactly two** pieces (the draft builder with the west side, then the east side) and keep this place in the queue. Never split per building, and never add a sixth draft ticket.

**Dependencies:** [T-1841](../T-1750-1999/T-1841-reconcile-sheet-28-building-entities-for-1904.md); [T-1843](../T-1750-1999/T-1843-metric-asset-contract-and-glessner-comparison-sl.md); [T-1844](../T-1750-1999/T-1844-stone-mortar-and-dressed-masonry-materials.md); [T-1845](../T-1750-1999/T-1845-pressed-common-and-rough-brick-materials.md); [T-1846](../T-1750-1999/T-1846-period-roof-coverings-and-drainage.md); [T-1847](../T-1750-1999/T-1847-mansard-hip-gable-and-tower-roof-construction.md); [T-1848](../T-1750-1999/T-1848-windows-glazing-and-visible-interior-depth.md); [T-1849](../T-1750-1999/T-1849-entrances-stoops-porches-and-carriage-doors.md); [T-1850](../T-1750-1999/T-1850-bays-oriels-and-towers.md); [T-1851](../T-1750-1999/T-1851-carved-entrances-and-classical-or-gothic-trim.md); [T-1852](../T-1750-1999/T-1852-cornices-parapets-dormer-faces-and-cresting.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1854](../T-1750-1999/T-1854-coach-houses-stable-fittings-and-service-wings.md); [T-1855](../T-1750-1999/T-1855-conservatory-and-greenhouse-assemblies.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-1857](../T-1750-1999/T-1857-chimneys-flues-and-roof-service-details.md); [T-1858](../T-1750-1999/T-1858-frame-cladding-and-exterior-timber-construction.md)

**Refined later by** (each now depends on this ticket and refines its draft in place): [T-1882](../T-1750-1999/T-1882-build-1808-keith-field-neighbour-of-glessner-env.md); [T-1883](../T-1750-1999/T-1883-finish-1808-keith-field-neighbour-of-glessner-ar.md); [T-1884](../T-1750-1999/T-1884-build-1812-wheeler-shaped-gable-house-envelope.md); [T-1885](../T-1750-1999/T-1885-finish-1812-wheeler-shaped-gable-house-architect.md); [T-1886](../T-1750-1999/T-1886-build-1816-henderson-mansard-house.md); [T-1887](../T-1750-1999/T-1887-build-1824-marsh-altered-front-and-1828-neighbou.md); [T-1888](../T-1750-1999/T-1888-build-1834-jones-post-1886-mansard.md); [T-1889](../T-1750-1999/T-1889-build-1801-kimball-corner-mansion-envelope.md); [T-1890](../T-1750-1999/T-1890-finish-1801-kimball-corner-mansion-architecture.md); [T-1891](../T-1750-1999/T-1891-build-1811-coleman-ames-romanesque-house-envelop.md); [T-1892](../T-1750-1999/T-1892-finish-1811-coleman-ames-romanesque-house-archit.md); [T-1893](../T-1750-1999/T-1893-build-1815-sears-meeker-altered-house.md); [T-1894](../T-1750-1999/T-1894-build-1823-dent-house.md); [T-1895](../T-1750-1999/T-1895-build-1827-doane-twin-tower-mansion-envelope.md); [T-1896](../T-1750-1999/T-1896-finish-1827-doane-twin-tower-mansion-architectur.md); [T-1897](../T-1750-1999/T-1897-build-1900-elbridge-keith-corner-house.md); [T-1898](../T-1750-1999/T-1898-build-1906-edson-keith-and-attached-1908.md); [T-1899](../T-1750-1999/T-1899-build-1912-moulton-lowden-chateauesque-house-env.md); [T-1900](../T-1750-1999/T-1900-finish-1912-moulton-lowden-chateauesque-house-ar.md); [T-1901](../T-1750-1999/T-1901-build-1916-1930-identity-and-1936-allerton-estat.md); [T-1902](../T-1750-1999/T-1902-finish-1916-1930-identity-and-1936-allerton-esta.md); [T-1903](../T-1750-1999/T-1903-build-1901-ream-post-fire-house.md); [T-1904](../T-1750-1999/T-1904-build-1905-marshall-field-sr-mansion-envelope.md); [T-1905](../T-1750-1999/T-1905-finish-1905-marshall-field-sr-mansion-architectu.md); [T-1906](../T-1750-1999/T-1906-build-1919-field-jr-post-1902-enlargement-envelo.md); [T-1907](../T-1750-1999/T-1907-finish-1919-field-jr-post-1902-enlargement-archi.md); [T-1908](../T-1750-1999/T-1908-build-1923-kellogg-and-1945-armour-corwith-corne.md); [T-1935](../T-1750-1999/T-1935-build-west-1800-1900-service-buildings-and-gless.md); [T-1936](../T-1750-1999/T-1936-build-east-1800-1900-service-buildings.md)
