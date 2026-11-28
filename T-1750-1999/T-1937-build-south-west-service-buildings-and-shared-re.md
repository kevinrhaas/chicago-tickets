---
id: T-1937
title: Refine south-west service buildings and shared Rees coach house
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-1837
opened: 2026-10-01
closed: null
pr: null
claimed_by: run 11/28/2026, 1:13:55 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/46118916196
claimed_at: 2026-11-28T07:13:55.875Z
decision: null
decision_answer: null
---

Package **R35W**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Sheet 35 west rear polygons; 2108/2110 coach house as ONE divided building with period basement ramp, two occupancies and shared roof; Robbins retained rear wing only after phase decision.

**Acceptance:**

1. Continuous south-west alley ensemble with service IDs, shared-wall correctness and dated functions; no duplicate Rees/Kimball roof or modern auto frontage.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1842](../T-1750-1999/T-1842-reconcile-sheet-35-building-entities-for-1904.md); [T-1854](../T-1750-1999/T-1854-coach-houses-stable-fittings-and-service-wings.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2161](../T-2000-2249/T-2161-draft-the-20th-22nd-prairie-block-with-the-draft.md)

**Execution gate:** owner approved resumption on 2026-10-01 (America/Chicago): “Go”, then “Push the tickets to dev queue in one group below”. The inherited 2026-09-30 construction hold is lifted. This ticket is open in the single Prairie programme group at the bottom of QUEUE.md. Its listed dependencies and needs_bake requirement still apply; read their current state before claiming.

**Bound:** complete the stated package using shared components. If full-resolution source inspection or the rear-polygon census makes it larger than one run, split this specific child before claiming; retain the whole acceptance and parent links. Glessner roof repairs remain with T-1830/T-1833; legal-lot work remains with T-1745 and road/sidewalk materials with T-1728.

## Refines the district draft (owner, 2026-10-08)

Owner, 2026-10-08: *"once you do your architectural analysis and build all the components, you should go through and do maybe up to 5 tickets and draft the whole district, I don't want you to keep propagating all those tickets out so it winds up with a ticket for each building like you already have, but should be a controlled set of tickets to do an initial pass of the whole district based on what you know, and then the tickets later for each building can refine your initial serviceable good draft model layer"*.

This package no longer builds from an empty lot. [T-2161](../T-2000-2249/T-2161-draft-the-20th-22nd-prairie-block-with-the-draft.md), one of the five district draft tickets (T-2159 to T-2163), stands a serviceable draft of everything this package covers before this ticket can be claimed: footprint, height, walls, roof, openings, front and every closed face, built from the study and the shared components. **This ticket refines that draft in place:**

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
  `buckingham_house_2036_prairie_coach_house`: a20-chicagology-2036-street-engraving-1880 (engraving, street view, 1880 (Chicagology caption)), a20-glessner-2100-block-west-side-1890s (photograph, street view, 1890s (blog caption: "early 1890s"))
  `mark_kimball_house_2108_prairie_coach_house`: a20-chicagology-2110-rees-street-c1895 (photograph, street view, about 1895 (Chicagology caption)), a20-glessner-2100-block-west-side-1890s (photograph, street view, 1890s (blog caption: "early 1890s")), a20-glessner-rees-coach-house-2014 (photograph, rear, 2014), a20-rees-nrhp-2007-photo-coach-house (photograph, rear, December 2006 (photos); April 2007 (form))
  `rothschild_house_2112_prairie_coach_house`: a20-chicagology-2110-rees-street-c1895 (photograph, street view, about 1895 (Chicagology caption)), a20-glessner-2100-block-west-side-1890s (photograph, street view, 1890s (blog caption: "early 1890s"))
  `sherman_house_2100_prairie_coach_house`: a20-chicagology-2110-rees-street-c1895 (photograph, street view, about 1895 (Chicagology caption)), a20-glessner-2100-block-west-side-1890s (photograph, street view, 1890s (blog caption: "early 1890s"))

- buckingham_house_2036_prairie_coach_house
- mark_kimball_house_2108_prairie_coach_house
- rothschild_house_2112_prairie_coach_house
- sherman_house_2100_prairie_coach_house

**Released 2026-11-26** (claim of run 11/26/2026, 10:15:33 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45936701416): PR #2383 refines 2108's and 2110's shared alley building (mark_kimball_house_2108_prairie_coach_house) in place onto K12 as ONE building divided on the lot line, 15.48 x 10.67 m, flat-roofed behind parapets 7.01 m up, from the 1911 sheet and the Glessner House post of 1 Oct 2014 (now a source: glessner_blog_2014_10_rees_coach_house_relocated); K12 gains roof_form 'flat'. Ramp attested but not built (no place, no ground cut). Still to do: the image gate on 2108's coach house (solve the 2014 photograph's camera; settle which of its faces is the alley's and lay its segmental-headed openings there), and 2036, 2100, 2112, 2120, 2126, 2130 and 2140's alley buildings, still the draft's. Not split: the gate stays on this ticket.

**Released 2026-11-27** (claim of run 11/27/2026, 12:37:31 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/46047869310): PR #2405 (resume: CI gate queued) refines 2100's alley building (sherman_house_2100_prairie_coach_house) in place onto K12: one 22.50 x 10.74 m rectangle off sheet 35, wagon house north / stable south, under the kit's hip_deck (deck 2.04 m in). Declared difference: the sheet draws no hip at the south end (the deck runs to the wall); the kit hips all four sides (L-k12-2100-wagon-house-1937). Image gate: neither named picture shows 2100's or 2112's alley building (both are street-front views), so no camera can be solved from them. Still to do: 2108's 2014-photograph camera and alley openings; 2036, 2112, 2120, 2126, 2130 and 2140's alley buildings (2112: plain 2-storey rectangle 14.7 x 8.6 m lettered AUTO, no roof marks).
