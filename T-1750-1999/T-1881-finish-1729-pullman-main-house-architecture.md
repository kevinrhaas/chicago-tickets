---
id: T-1881
title: Finish 1729 Pullman main house architecture
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

Package **N19B**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Addresses/associations: 1729. Read the study register for the specific envelope, material, roof, openings, date traps and source handles. Own distinctive facade/bay/tower detailing, carved entrance, cornice, roof decoration, glazing depth, attached porch/stoop and building-local ironwork; do not move the accepted envelope.

**Property-specific brief:**

- **1729: Pullman Second Empire estate.** Brownstone main block, mansard/dormers/cresting, Prairie portico and terrace, 18th Street porte-cochere, 1892 east addition, rear stable and dated conservatory/palm-house complex. Phase guard: Treat estate as several connected assets; distinguish 1890 pre-addition view from c.1900 photographs and 1894 plates. Greenhouse south of 18th needs its own plot and date, not attachment to a neighbouring mansion.

**Acceptance:**

1. Finished building, including visible side/rear treatment, passes the Glessner comparison protocol at close street, corner and aerial views; all unique features in register accounted for, liberties and licenses filed, compressed browser assets verified.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1880](../T-1750-1999/T-1880-build-1729-pullman-main-house-envelope.md); [T-1851](../T-1750-1999/T-1851-carved-entrances-and-classical-or-gothic-trim.md); [T-1852](../T-1750-1999/T-1852-cornices-parapets-dormer-faces-and-cresting.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2160](../T-2000-2249/T-2160-draft-the-16th-18th-prairie-block-with-the-draft.md)

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

## Image gate (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

Pictures:
  `pullman_house_1729_prairie`: a16-aic-lowe-pullman-conservatory-c1897 (photograph, oblique front, c.1897 (view date)), a16-aic-taylor-album-pullman-p69 (photograph, oblique front, c.1880s (holder); album c.1890s), a16-aic-taylor-pullman-from-nw (photograph, oblique front, c.1890s (view date)), a16-aic-taylor-pullman-from-sw-palm-house (photograph, oblique front, c.1890–1910 (view date)), a16-albertype-1890-pullman-residence (publication plate, oblique front, 1890 (publication)), a16-cgy-1729-beman-addition (photograph, side elevation, undated (after the 1892 Beman addition)), a16-cgy-1729-dailynews-photo (photograph, oblique front, undated (Chicago Daily News negative series is 1902–1933; a 'KODAK' sign is visible on a building at far left)), a16-chm-clark-i70232-pullman-addition (photograph, side elevation, 1905–1906 (CHM-Date depicted)), a16-chm-clark-ichi-071913-pullman-1905 (photograph, oblique front, 1905 (CHM-Date depicted)), a16-ghm-blog-pullman-completed (photograph, oblique front, undated (after the 1892 Beman additions; probably 1890s)), a16-ghm-blog-pullman-terrace (photograph, side elevation, undated (after 1892)), a16-inland-1891-dexter-residence (publication plate, oblique front, 1891 (plate in The Inland Architect and News Record, vol. 17, no. 5, June 1891); addition built 1889), and 14 more in the library

- pullman_house_1729_prairie
