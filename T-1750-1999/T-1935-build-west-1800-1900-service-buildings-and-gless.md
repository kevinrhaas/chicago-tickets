---
id: T-1935
title: Refine west 1800-1900 service buildings and Glessner boundary
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

Package **R28W**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Sheet 28 western rear barns/coach houses, with Glessner retained as existing; no duplicate Glessner stable. Resolve Allerton rear lot association first and coordinate 1808 north wall.

**Acceptance:**

1. A complete western alley frontage with every detached map polygon assigned a dated ID, joinery/openings/roof finished, shared boundaries free of overlap.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1841](../T-1750-1999/T-1841-reconcile-sheet-28-building-entities-for-1904.md); [T-1854](../T-1750-1999/T-1854-coach-houses-stable-fittings-and-service-wings.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md)

**Execution gate:** owner approved resumption on 2026-10-01 (America/Chicago): “Go”, then “Push the tickets to dev queue in one group below”. The inherited 2026-09-30 construction hold is lifted. This ticket is open in the single Prairie programme group at the bottom of QUEUE.md. Its listed dependencies and needs_bake requirement still apply; read their current state before claiming.

**Bound:** complete the stated package using shared components. If full-resolution source inspection or the rear-polygon census makes it larger than one run, split this specific child before claiming; retain the whole acceptance and parent links. Glessner roof repairs remain with T-1830/T-1833; legal-lot work remains with T-1745 and road/sidewalk materials with T-1728.

## Refines the district draft (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This package no longer builds from an empty lot. [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md), one of the five district draft tickets (T-2159 to T-2163), stands a serviceable draft of everything this package covers before this ticket can be claimed: footprint, height, walls, roof, openings, front and every closed face, built from the study and the shared components. **This ticket refines that draft in place:**

- keep the draft's structure IDs, and its footprint and placement unless this package's sources show otherwise;
- replace the draft-tier attributes with the property-specific architecture in the brief above (bespoke silhouette, carving, openings, materials, rear elevations, phase decisions), lifting each attribute's tier and basis and clearing its `replaceable_by`;
- retire, in `docs/LIBERTIES.md`, the part of the draft's block liberty this package supersedes;
- compare before and after against the draft from the same camera poses.

Rebuilding a house from scratch beside the draft, or leaving a draft copy and a refined copy both standing, is a defect. The acceptance above is unchanged: refinement is judged to the same Glessner standard.

## Image gate (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

Pictures:
  `edson_keith_house_1906_prairie_coach_house`: a18-chm-clark-c1905-prairie-west-side-north-from-1936 (photograph, street view, circa 1905), st-landowner-1874-homes-of-prairie-avenue (engraving, street view, May 1874)
  `elbridge_keith_house_1900_prairie_coach_house`: a18-chm-clark-c1905-prairie-west-side-north-from-1936 (photograph, street view, circa 1905)
  `henderson_house_1816_prairie_coach_house`: a18-rba-taylor-9974-prairie-south-from-18th (photograph, street view, undated (before 1908: a colourised version was published as a postcard postmarked 1908); mature trees suggest c. 1895–1907), st-landowner-1874-homes-of-prairie-avenue (engraving, street view, May 1874)
  `jones_house_1834_prairie_coach_house`: a18-chm-clark-c1905-prairie-west-side-north-from-1936 (photograph, street view, circa 1905)
  `marsh_house_1824_prairie_coach_house`: a18-chm-clark-c1905-prairie-west-side-north-from-1936 (photograph, street view, circa 1905)
  `moulton_lowden_house_1912_prairie_coach_house`: a18-chm-clark-c1905-prairie-west-side-north-from-1936 (photograph, street view, circa 1905), a19-nby-newchicagoalbum-1883-residences (publication plate, oblique front, 1883)
  `shed_1834_1900_prairie`: a18-chm-clark-c1905-prairie-west-side-north-from-1936 (photograph, street view, circa 1905)

- edson_keith_house_1906_prairie_coach_house
- elbridge_keith_house_1900_prairie_coach_house
- henderson_house_1816_prairie_coach_house
- jones_house_1834_prairie_coach_house
- marsh_house_1824_prairie_coach_house
- moulton_lowden_house_1912_prairie_coach_house
- shed_1834_1900_prairie
