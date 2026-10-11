---
id: T-1934
title: Refine Pullman stable, additions and conservatory estate
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

Package **RP**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Use 1894 conservatory and palm-house/stable plates and map evidence to separate residence east addition, stable, conservatory and garden complex across 18th. Coordinate with R28E so greenhouse polygons have exactly one owner. The residential 1892 east addition stays with N19A; this ticket owns detached service and glasshouse geometry.

**Acceptance:**

1. One estate service ensemble with dated site relation and custom glasshouse silhouette, both exterior glazing and opaque service walls, no duplicated greenhouse or borrowed neighbouring yard. Split before claim if two geographically separate demonstrations are needed.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1840](../T-1750-1999/T-1840-reconcile-sheet-20-building-entities-for-1904.md); [T-1841](../T-1750-1999/T-1841-reconcile-sheet-28-building-entities-for-1904.md); [T-1880](../T-1750-1999/T-1880-build-1729-pullman-main-house-envelope.md); [T-1854](../T-1750-1999/T-1854-coach-houses-stable-fittings-and-service-wings.md); [T-1855](../T-1750-1999/T-1855-conservatory-and-greenhouse-assemblies.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2160](../T-2000-2249/T-2160-draft-the-16th-18th-prairie-block-with-the-draft.md)

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

## What the district draft left here (T-2335, 2026-10-11)

The district draft's 16th-18th east side (T-2335, piece 2 of T-2160) stands the Pullman house (`pullman_house_1729_prairie`) with its traced wing, keeping the K13 conservatory record's footprint (`pullman_house_1729_prairie_conservatory`, T-2306) out of its fill, and its two-storey building at the wing's east end. It does **not** stand the estate's ground across 18th Street: the two glasshouse ranges and the two-storey lodge the sheet-28 census allocates to this package (`s28-pullman-service-garden`: `s28-pullman-greenhouse-north`, `s28-pullman-greenhouse-east`, `s28-pullman-garden-lodge`). The sheet-28 trace never drew them, so the draft builder had no polygon to read, and the draft archetype has no glass roof. This ticket therefore builds them from empty ground, not from a draft: trace them off sheet 28, then build the ranges from the K13 kit (its `span` form) and the lodge as this package's service building. Recorded in `L-draft-prairie-16-18-east-2335`.

## Image gate (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

Pictures:
  `pullman_house_1729_prairie_conservatory`: a16-aic-lowe-pullman-conservatory-c1897 (photograph, oblique front, c.1897 (view date)), a16-aic-taylor-album-pullman-p69 (photograph, oblique front, c.1880s (holder); album c.1890s), a16-aic-taylor-pullman-from-nw (photograph, oblique front, c.1890s (view date)), a16-aic-taylor-pullman-from-sw-palm-house (photograph, oblique front, c.1890–1910 (view date)), a16-aic-taylor-pullman-west-front-palm-house (photograph, street view, c.1890–1910 (holder view date); content dates it 1892–May 1894), a16-andreas-1884-chicagos-historic-tree (publication plate, street view, 1884 (publication)), a16-cgy-1729-beman-addition (photograph, side elevation, undated (after the 1892 Beman addition)), a16-chm-clark-i70232-pullman-addition (photograph, side elevation, 1905–1906 (CHM-Date depicted)), a16-chm-ichi-19208-monument-pullman-wall (photograph, street view, circa 1900), a16-ghm-blog-massacre-tree-george-glessner-c1888 (photograph, street view, about 1888), a16-ghm-blog-massacre-tree-pullman-coachhouse (engraving, street view, 1880s (per blog)), a16-ghm-blog-pullman-completed (photograph, oblique front, undated (after the 1892 Beman additions; probably 1890s)), and 13 more in the library

- pullman_house_1729_prairie_conservatory
