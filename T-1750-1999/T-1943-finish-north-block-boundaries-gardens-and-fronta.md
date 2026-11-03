---
id: T-1943
title: Finish north-block boundaries, gardens and frontage fittings
state: withdrawn
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-1837
opened: 2026-10-01
closed: 2026-11-02
pr: null
claimed_by: null
blocked_on: Closed as delivered on the owner's answer (a), 2026-11-02 via Manager: every 16th-18th house has its own boundary and walk (T-3204 pieces T-3214/3221/3222/3229/3230), front yards (T-3203/3223), lamps (T-3199), hydrants and poles (T-3201/3202), curb and carriage walks (T-2474), corner ramps (T-3200), parkway elms (T-2473); carriage blocks and hitching posts stay picture-only (2026-10-27 ruling).
needs_bake: true
closed_at: 2026-11-03T04:32:01.424Z
claimed_run: null
claimed_at: null
decision: answered
decision_answer: a
---

Package **E20**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** North block, 16th-18th Streets only. Apply per-property wall/fence/gate variants, lawns/beds, carriage drives, basement areas, coal covers, hitching/mounting blocks, lamps only where dated or reconstructed, mature street-tree rhythm and young replacements. Reuse existing T-1728 surfaces.

**Acceptance:**

1. One north-block traversal with readable individual property boundaries and entrances, no obstacles across public paths; documented tree/fixture assumptions and no modern furniture.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1840](../T-1750-1999/T-1840-reconcile-sheet-20-building-entities-for-1904.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2163](../T-2000-2249/T-2163-draft-the-district-s-grounds-and-walk-the-whole-.md)

**Execution gate:** owner approved resumption on 2026-10-01 (America/Chicago): “Go”, then “Push the tickets to dev queue in one group below”. The inherited 2026-09-30 construction hold is lifted. This ticket is open in the single Prairie programme group at the bottom of QUEUE.md. Its listed dependencies and needs_bake requirement still apply; read their current state before claiming.

**Bound:** complete the stated package using shared components. If full-resolution source inspection or the rear-polygon census makes it larger than one run, split this specific child before claiming; retain the whole acceptance and parent links. Glessner roof repairs remain with T-1830/T-1833; legal-lot work remains with T-1745 and road/sidewalk materials with T-1728.

## Refines the district draft (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This package no longer builds from an empty lot. [T-2163](../T-2000-2249/T-2163-draft-the-district-s-grounds-and-walk-the-whole-.md), one of the five district draft tickets (T-2159 to T-2163), stands a serviceable draft of everything this package covers before this ticket can be claimed: footprint, height, walls, roof, openings, front and every closed face, built from the study and the shared components. **This ticket refines that draft in place:**

- keep the draft's structure IDs, and its footprint and placement unless this package's sources show otherwise;
- replace the draft-tier attributes with the property-specific architecture in the brief above (bespoke silhouette, carving, openings, materials, rear elevations, phase decisions), lifting each attribute's tier and basis and clearing its `replaceable_by`;
- retire, in `docs/LIBERTIES.md`, the part of the draft's block liberty this package supersedes;
- compare before and after against the draft from the same camera poses.

Rebuilding a house from scratch beside the draft, or leaving a draft copy and a refined copy both standing, is a defect. The acceptance above is unchanged: refinement is judged to the same Glessner standard.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

No picture of this building was found by address in the Prairie library on 2026-10-11. Before building, search the library (every record, street views and neighbours' plates included) and `data/sources/`. If one turns up, add an `## Image gate` section here naming the structure id as a bullet.

## Decision needed

**Question:** T-1943's north-block grounds look already built by later, finer tickets. Close it (and leave T-1944/T-1945 for the same check), or keep it for what is left?

- (a) Close T-1943 as delivered: every 16th-18th house now has its own boundary and walk (T-3204 pieces T-3214/3221/3222/3229/3230; the 1700 block per house), front yards (T-3203/3223), lamps (T-3199), hydrants and poles (T-3201/3202), curb and carriage walks (T-2474), corner ramps (T-3200), parkway elms (T-2473). Carriage blocks and hitching posts stay picture-only per your 2026-10-27 ruling.
- (b) Keep T-1943 for the remainder only: a north-block walk at phone and desktop sizes with its costs recorded, plus coal-hole covers, basement areaways and side carriage drives wherever a picture or the Sanborn sheet shows one (nothing placed by rule).

**Recommendation:** (a) Close T-1943 as delivered: every 16th-18th house now has its own boundary and walk (T-3204 pieces T-3214/3221/3222/3229/3230; the 1700 block per house), front yards (T-3203/3223), lamps (T-3199), hydrants and poles (T-3201/3202), curb and carriage walks (T-2474), corner ramps (T-3200), parkway elms (T-2473). Carriage blocks and hitching posts stay picture-only per your 2026-10-27 ruling. — Run on 2026-11-02 (slice 5/5) claimed T-1943 and found nothing left to build that is not already standing or that your 2026-10-27 carriage-block ruling did not take out. Walking the 1600 block at 1280x800, the only fronts without a fence are the east side's, which are open on purpose (1621/1623 drawings and the 1625 photograph, T-3221). The ticket also still depends on T-2163, which is blocked-tech on T-2983, although every piece of T-2983 (T-3008/3009/3011/3018/3019) is done, so that block is stale. Recommending (a) so the queue stops sending runs to a package the per-house tickets already built.

**Asked:** 2026-11-01 by https://github.com/kevinrhaas/polecat-platform/actions/runs/41379397907. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

**Released 2026-11-01** (claim of run 11/1/2026, 8:58:37 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41379397907): nothing left to build that later tickets have not built; the owner is asked whether to close it (decision pending)

**Owner answer (2026-11-02, via Manager):** (a) Close T-1943 as delivered: every 16th-18th house now has its own boundary and walk (T-3204 pieces T-3214/3221/3222/3229/3230; the 1700 block per house), front yards (T-3203/3223), lamps (T-3199), hydrants and poles (T-3201/3202), curb and carriage walks (T-2474), corner ramps (T-3200), parkway elms (T-2473). Carriage blocks and hitching posts stay picture-only per your 2026-10-27 ruling.
