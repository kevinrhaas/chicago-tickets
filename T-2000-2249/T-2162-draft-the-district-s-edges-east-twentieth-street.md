---
id: T-2162
title: Draft the district's edges: East Twentieth Street, Calumet, Second Presbyterian and the side-street and rail-side background
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

Draft the district's edges: East Twentieth Street, Calumet, Second Presbyterian and the side-street and rail-side background.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 154 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-08 (project thread): after the architectural analysis and the shared components, up to five tickets draft the whole Prairie Avenue district as a serviceable first pass, ahead of every per-building ticket, which then refine that draft. Owner-requested and capped at five.

## The district draft pass (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This is one of **five** draft tickets, T-2159 to T-2163, the whole of that pass. They come after the [architectural study](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md), the three sheet reconciliations (T-1840 to T-1842) and the sixteen shared components (T-1843 to T-1858), and before every per-building ticket, each of which now **refines** this draft rather than building from an empty lot. Do not file per-building tickets from here; the per-building tickets already exist.

**This ticket: the district's edges**, the buildings a visitor on Prairie Avenue sees past the three blocks: the named context houses on East Twentieth Street and Calumet, Second Presbyterian's tower and roof, and the Indiana, Calumet, end-street and rail-side masses visible from Prairie's sidewalks. Run through the draft builder T-2159 made; a background mass far from any sidewalk may be drafted at light detail only.

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

1. **The four named context buildings stand as drafts**: 213, 215 and 217 East Twentieth Street as three houses, 2008 Calumet (Hanford), 2018 Calumet (Wheeler-Kohn), and Second Presbyterian's post-1900 exterior with one dated tower state.
2. **No blank background from Prairie Avenue**: a visibility census of the Indiana, Calumet, end-street and rail-side polygons seen from Prairie's camera stands, each one drafted as a bounded background mass or recorded as open ground, with T-1745 still owning legal lot numbers.
3. **Captured and measured**: views west to Indiana, east to Calumet and down each cross street, at 1280×800 and 390×780, with 1904's load, heap and frame time before and after.
4. Every structure carries the provenance, stable ID and card the rules above require, the block's single liberty is recorded under the next free number, and the changelog entry is stamped.

**Bound:** one run plus a bake. If it cannot fit, split it into **exactly two** pieces (the four named context buildings, then the background census) and keep this place in the queue. Never split per building, and never add a sixth draft ticket.

**Dependencies:** [T-1840](../T-1750-1999/T-1840-reconcile-sheet-20-building-entities-for-1904.md); [T-1841](../T-1750-1999/T-1841-reconcile-sheet-28-building-entities-for-1904.md); [T-1842](../T-1750-1999/T-1842-reconcile-sheet-35-building-entities-for-1904.md); [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md)

**Refined later by** (each now depends on this ticket and refines its draft in place): [T-1939](../T-1750-1999/T-1939-build-213-215-and-217-east-twentieth-street-cont.md); [T-1940](../T-1750-1999/T-1940-build-2008-calumet-hanford-exterior.md); [T-1941](../T-1750-1999/T-1941-build-2018-calumet-wheeler-kohn-exterior.md); [T-1942](../T-1750-1999/T-1942-build-second-presbyterian-post-1900-exterior-sky.md); [T-1946](../T-1750-1999/T-1946-close-side-street-and-rail-side-background-gaps.md)
