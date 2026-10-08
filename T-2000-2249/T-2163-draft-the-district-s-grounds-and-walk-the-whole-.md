---
id: T-2163
title: Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all three blocks, measured on a phone
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

Draft the district's grounds and walk the whole draft: walls, fences, gates, lawns, drives and street trees on all three blocks, measured on a phone.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 155 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-08 (project thread): after the architectural analysis and the shared components, up to five tickets draft the whole Prairie Avenue district as a serviceable first pass, ahead of every per-building ticket, which then refine that draft. Owner-requested and capped at five.

## The district draft pass (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This is one of **five** draft tickets, T-2159 to T-2163, the whole of that pass. They come after the [architectural study](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md), the three sheet reconciliations (T-1840 to T-1842) and the sixteen shared components (T-1843 to T-1858), and before every per-building ticket, each of which now **refines** this draft rather than building from an empty lot. Do not file per-building tickets from here; the per-building tickets already exist.

**This ticket: the district's grounds, and the proof of the whole draft.** It lays a first pass of every property's boundary and yard across all three blocks, then walks the finished draft end to end. It is the last draft ticket; when it merges, every per-building ticket below can start refining.

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

1. **Every property on all three blocks has draft grounds**: its wall, fence or railing and gate from T-1853, lawn and beds, carriage drive, basement area and coal cover where the plan shows one, and a street-tree rhythm along both sidewalks, reusing T-1728's street surfaces. No obstacle across a public path and no modern furniture.
2. **The whole draft walks**: both Prairie sidewalks from 16th to 22nd and each alley, with no unexplained blank frontage, no duplicated address building and no missing mapped service roof. Anything found missing is fixed here or added to the owning draft ticket's record, not filed as a new ticket.
3. **The whole draft fits a phone**: 1904 measured at full, balanced and light detail at 390×780 and 1280×800 for load, JS heap and frame time on that walk. The district loads and walks on a phone profile without the tab being killed, and the numbers go into this ticket for the refinement tickets to stay under.
4. Every structure carries the provenance, stable ID and card the rules above require, the block's single liberty is recorded under the next free number, and the changelog entry is stamped.

**Bound:** one run plus a bake. If it cannot fit, split it into **exactly two** pieces (the grounds, then the whole-district walk and phone measurements) and keep this place in the queue. Never split per building, and never add a sixth draft ticket.

**Dependencies:** [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md); [T-2160](../T-2000-2249/T-2160-draft-the-16th-18th-prairie-block-with-the-draft.md); [T-2161](../T-2000-2249/T-2161-draft-the-20th-22nd-prairie-block-with-the-draft.md); [T-2162](../T-2000-2249/T-2162-draft-the-district-s-edges-east-twentieth-street.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md)

**Refined later by** (each now depends on this ticket and refines its draft in place): [T-1943](../T-1750-1999/T-1943-finish-north-block-boundaries-gardens-and-fronta.md); [T-1944](../T-1750-1999/T-1944-finish-18th-20th-block-boundaries-gardens-and-fr.md); [T-1945](../T-1750-1999/T-1945-finish-20th-22nd-block-boundaries-gardens-and-fr.md)
