---
id: T-1872
title: Refine 1708 and 1712 townhouse fronts
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-1837
opened: 2026-10-01
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

Package **N13**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Addresses/associations: 1708, 1712. Read the study register for the specific envelope, material, roof, openings, date traps and source handles. Deliver complete exterior using the approved common components with house-specific proportion, openings, roof and material overrides. Keep individual structure IDs within grouped delivery. Detached service buildings are owned by R-series. For a true empty/duplicate/absent entity deliver the correct non-building state and explanation, not an invented house.

**Property-specific brief:**

- **1708: Thorne-associated map-led brick house.** Three-storey/basement brick townhouse with separate entry, cornice, regular sash and service rear. Phase guard: Thorne name is attested later; 1904 Blue Book lists Carpenter candidate. Preserve historic identity labels by date while reconstructing mapped envelope.
- **1712: Stone-front masonry.** Map-bound main body and attached wings; masonry corner bonds, recessed sash, lintels, foundation and high stoop; independently declared roof, gutters, chimneys and rear elevation.  Phase guard: Facade design, roof pitch, colours and unseen windows are reconstructed. Raw map notation 2B remains unexpanded until key interpretation; map plan controls plan shape, not a supposedly measured facade.

**Acceptance:**

1. One coherent small frontage ensemble in the scene, all exterior faces complete, source/date/reconstruction decisions on each property, no identical repeated facades unless an attested pair. Use Glessner QA and full/light assets. If bespoke work exceeds one run, split before claiming; never silently reduce the architectural standard.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1840](../T-1750-1999/T-1840-reconcile-sheet-20-building-entities-for-1904.md); [T-1843](../T-1750-1999/T-1843-metric-asset-contract-and-glessner-comparison-sl.md); [T-1844](../T-1750-1999/T-1844-stone-mortar-and-dressed-masonry-materials.md); [T-1845](../T-1750-1999/T-1845-pressed-common-and-rough-brick-materials.md); [T-1846](../T-1750-1999/T-1846-period-roof-coverings-and-drainage.md); [T-1847](../T-1750-1999/T-1847-mansard-hip-gable-and-tower-roof-construction.md); [T-1848](../T-1750-1999/T-1848-windows-glazing-and-visible-interior-depth.md); [T-1849](../T-1750-1999/T-1849-entrances-stoops-porches-and-carriage-doors.md); [T-1850](../T-1750-1999/T-1850-bays-oriels-and-towers.md); [T-1857](../T-1750-1999/T-1857-chimneys-flues-and-roof-service-details.md); [T-1858](../T-1750-1999/T-1858-frame-cladding-and-exterior-timber-construction.md); [T-1851](../T-1750-1999/T-1851-carved-entrances-and-classical-or-gothic-trim.md); [T-1852](../T-1750-1999/T-1852-cornices-parapets-dormer-faces-and-cresting.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2160](../T-2000-2249/T-2160-draft-the-16th-18th-prairie-block-with-the-draft.md)

**Execution gate:** owner approved resumption on 2026-10-01 (America/Chicago): “Go”, then “Push the tickets to dev queue in one group below”. The inherited 2026-09-30 construction hold is lifted. This ticket is open in the single Prairie programme group at the bottom of QUEUE.md. Its listed dependencies and needs_bake requirement still apply; read their current state before claiming.

**Bound:** complete the stated package using shared components. If full-resolution source inspection or the rear-polygon census makes it larger than one run, split this specific child before claiming; retain the whole acceptance and parent links. Glessner roof repairs remain with T-1830/T-1833; legal-lot work remains with T-1745 and road/sidewalk materials with T-1728.

## Refines the district draft (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This package no longer builds from an empty lot. [T-2160](../T-2000-2249/T-2160-draft-the-16th-18th-prairie-block-with-the-draft.md), one of the five district draft tickets (T-2159 to T-2163), stands a serviceable draft of everything this package covers before this ticket can be claimed: footprint, height, walls, roof, openings, front and every closed face, built from the study and the shared components. **This ticket refines that draft in place:**

- keep the draft's structure IDs, and its footprint and placement unless this package's sources show otherwise;
- replace the draft-tier attributes with the property-specific architecture in the brief above (bespoke silhouette, carving, openings, materials, rear elevations, phase decisions), lifting each attribute's tier and basis and clearing its `replaceable_by`;
- retire, in `docs/LIBERTIES.md`, the part of the draft's block liberty this package supersedes;
- compare before and after against the draft from the same camera poses.

Rebuilding a house from scratch beside the draft, or leaving a draft copy and a refined copy both standing, is a defect. The acceptance above is unchanged: refinement is judged to the same Glessner standard.
