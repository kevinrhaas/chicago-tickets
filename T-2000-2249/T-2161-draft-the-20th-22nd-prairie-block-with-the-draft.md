---
id: T-2161
title: Draft the 20th-22nd Prairie block with the draft builder: every frontage and its rear service buildings
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

Draft the 20th-22nd Prairie block with the draft builder: every frontage and its rear service buildings.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 153 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-08 (project thread): after the architectural analysis and the shared components, up to five tickets draft the whole Prairie Avenue district as a serviceable first pass, ahead of every per-building ticket, which then refine that draft. Owner-requested and capped at five.

## The district draft pass (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This is one of **five** draft tickets, T-2159 to T-2163, the whole of that pass. They come after the [architectural study](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md), the three sheet reconciliations (T-1840 to T-1842) and the sixteen shared components (T-1843 to T-1858), and before every per-building ticket, each of which now **refines** this draft rather than building from an empty lot. Do not file per-building tickets from here; the per-building tickets already exist.

**This ticket: the 20th-22nd block (Sanborn sheet 35)**, run through the draft builder T-2159 made.

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

1. **Every 20th-22nd frontage stands as a draft**: all 33 sheet-35 rows, west and east sides, plus every detached rear polygon owned by R35W and R35E, built by T-2159's draft builder from data. The 2108/2110 coach house is **one** shared building, and Rees stands at its historical 2110 site.
2. **The study's south-block rulings are visible**: Robbins 2126 in one declared working phase for 1 July 1904, 2140 Tucker/Smith in one documented roof state (never both), and 2141 as a non-building frontage.
3. **Captured and measured**: both sidewalks from 20th to 22nd, the alleys and the air, at 1280×800 and 390×780, with 1904's load, heap and frame time before and after.
4. Every structure carries the provenance, stable ID and card the rules above require, the block's single liberty is recorded under the next free number, and the changelog entry is stamped.

**Bound:** one run plus a bake. If it cannot fit, split it into **exactly two** pieces (the west side, then the east side) and keep this place in the queue. Never split per building, and never add a sixth draft ticket.

**Dependencies:** [T-1842](../T-1750-1999/T-1842-reconcile-sheet-35-building-entities-for-1904.md); [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md)

**Refined later by** (each now depends on this ticket and refines its draft in place): [T-1909](../T-1750-1999/T-1909-build-2000-and-2010-detached-frame-houses.md); [T-1910](../T-1750-1999/T-1910-build-2018-and-2026-masonry-houses.md); [T-1911](../T-1750-1999/T-1911-build-2036-buckingham-corner-house.md); [T-1912](../T-1750-1999/T-1912-build-2001-2003-and-2005-attached-row.md); [T-1913](../T-1750-1999/T-1913-build-2009-mayer-meyer-french-gothic-house-envel.md); [T-1914](../T-1750-1999/T-1914-finish-2009-mayer-meyer-french-gothic-house-arch.md); [T-1915](../T-1750-1999/T-1915-build-2011-romanesque-house-beside-mayer.md); [T-1916](../T-1750-1999/T-1916-build-2013-reid-classical-house.md); [T-1917](../T-1750-1999/T-1917-build-2017-2021-high-and-2027-cobb-associated-gr.md); [T-1918](../T-1750-1999/T-1918-build-2031-2033-and-2035-limestone-row.md); [T-1919](../T-1750-1999/T-1919-build-2100-sherman-victorian-gothic-house-envelo.md); [T-1920](../T-1750-1999/T-1920-finish-2100-sherman-victorian-gothic-house-archi.md); [T-1921](../T-1750-1999/T-1921-build-2108-mark-kimball-and-2112-rothschild.md); [T-1922](../T-1750-1999/T-1922-build-2110-rees-at-its-historical-site-envelope.md); [T-1923](../T-1750-1999/T-1923-finish-2110-rees-at-its-historical-site-architec.md); [T-1924](../T-1750-1999/T-1924-build-2101-and-2109-roloson-neighbours.md); [T-1925](../T-1750-1999/T-1925-build-2115-armour-second-empire-house.md); [T-1926](../T-1750-1999/T-1926-build-2120-and-the-2126-robbins-construction-pha.md); [T-1927](../T-1750-1999/T-1927-build-2130-murdoch-rounded-bay-house.md); [T-1928](../T-1750-1999/T-1928-build-2140-tucker-smith-corner-mansion-envelope.md); [T-1929](../T-1750-1999/T-1929-finish-2140-tucker-smith-corner-mansion-architec.md); [T-1930](../T-1750-1999/T-1930-build-2123-masonry-and-2125-frame-neighbours.md); [T-1931](../T-1750-1999/T-1931-build-2127-2129-flats-and-2141-non-building-fron.md); [T-1937](../T-1750-1999/T-1937-build-south-west-service-buildings-and-shared-re.md); [T-1938](../T-1750-1999/T-1938-build-south-east-service-buildings.md)
