---
id: T-2160
title: Draft the 16th-18th Prairie block with the draft builder: every frontage and its rear service buildings
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

Draft the 16th-18th Prairie block with the draft builder: every frontage and its rear service buildings.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 152 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-08 (project thread): after the architectural analysis and the shared components, up to five tickets draft the whole Prairie Avenue district as a serviceable first pass, ahead of every per-building ticket, which then refine that draft. Owner-requested and capped at five.

## The district draft pass (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This is one of **five** draft tickets, T-2159 to T-2163, the whole of that pass. They come after the [architectural study](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md), the three sheet reconciliations (T-1840 to T-1842) and the sixteen shared components (T-1843 to T-1858), and before every per-building ticket, each of which now **refines** this draft rather than building from an empty lot. Do not file per-building tickets from here; the per-building tickets already exist.

**This ticket: the 16th-18th block (Sanborn sheet 20)**, run through the draft builder T-2159 made.

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

1. **Every 16th-18th frontage stands as a draft**: all 35 sheet-20 rows, west and east sides, plus every detached rear polygon owned by R20W, R20E and the Pullman estate package (stables, coach houses, the conservatory as a kit glasshouse), built by T-2159's draft builder from data.
2. **The study's north-block rulings are visible**: the 1609-1611 pair and 1620 at their 1904 forms, two Glessner-family townhouses at 1700/1706 and no third house at 1702, one Dexter house at 1719/1721, and Forsyth 1635 left as an unresolved non-building state rather than a house on its neighbour.
3. **Captured and measured**: both sidewalks from 16th to 18th, the alleys and the air, at 1280×800 and 390×780, with 1904's load, heap and frame time before and after.
4. Every structure carries the provenance, stable ID and card the rules above require, the block's single liberty is recorded under the next free number, and the changelog entry is stamped.

**Bound:** one run plus a bake. If it cannot fit, split it into **exactly two** pieces (the west side, then the east side) and keep this place in the queue. Never split per building, and never add a sixth draft ticket.

**Dependencies:** [T-1840](../T-1750-1999/T-1840-reconcile-sheet-20-building-entities-for-1904.md); [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md)

**Refined later by** (each now depends on this ticket and refines its draft in place): [T-1859](../T-1750-1999/T-1859-build-1600-1604-and-1608-north-west-frontage.md); [T-1860](../T-1750-1999/T-1860-build-1612-goodman-and-1616-neighbour.md); [T-1861](../T-1750-1999/T-1861-build-1620-law-house-restored-for-1904.md); [T-1862](../T-1750-1999/T-1862-build-1626-1628-and-small-frame-1630.md); [T-1863](../T-1750-1999/T-1863-build-1634-and-1636-stone-front-pair.md); [T-1864](../T-1750-1999/T-1864-build-1638-shortall-gregory-gothic-house-envelop.md); [T-1865](../T-1750-1999/T-1865-finish-1638-shortall-gregory-gothic-house-archit.md); [T-1866](../T-1750-1999/T-1866-build-1601-house-and-1603-station-side-envelope.md); [T-1867](../T-1750-1999/T-1867-build-1609-1611-lost-pair-and-1607-association.md); [T-1868](../T-1750-1999/T-1868-build-1613-1615-and-1619-east-row.md); [T-1869](../T-1750-1999/T-1869-build-1621-1623-and-1625-east-row.md); [T-1870](../T-1750-1999/T-1870-build-1635-unresolved-site-and-1637-spalding-rem.md); [T-1871](../T-1750-1999/T-1871-build-1700-1706-glessner-family-townhouses.md); [T-1872](../T-1750-1999/T-1872-build-1708-and-1712-townhouse-fronts.md); [T-1873](../T-1750-1999/T-1873-build-1720-walker-frame-villa.md); [T-1874](../T-1750-1999/T-1874-build-1726-1730-and-1736-replacement-altered-hou.md); [T-1875](../T-1750-1999/T-1875-build-1701-hibbard-house-and-rear-veranda-envelo.md); [T-1876](../T-1750-1999/T-1876-finish-1701-hibbard-house-and-rear-veranda-archi.md); [T-1877](../T-1750-1999/T-1877-build-1709-palmer-kellogg-successor.md); [T-1878](../T-1750-1999/T-1878-build-1719-1721-dexter-address-and-altered-house.md); [T-1879](../T-1750-1999/T-1879-finish-1719-1721-dexter-address-and-altered-hous.md); [T-1880](../T-1750-1999/T-1880-build-1729-pullman-main-house-envelope.md); [T-1881](../T-1750-1999/T-1881-finish-1729-pullman-main-house-architecture.md); [T-1932](../T-1750-1999/T-1932-build-north-west-alley-coach-houses-and-service-.md); [T-1933](../T-1750-1999/T-1933-build-north-east-rear-service-buildings.md); [T-1934](../T-1750-1999/T-1934-build-pullman-stable-additions-and-conservatory-.md)
