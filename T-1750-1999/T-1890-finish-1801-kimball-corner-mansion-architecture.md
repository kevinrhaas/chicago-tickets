---
id: T-1890
title: Finish 1801 Kimball corner mansion architecture
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
claimed_by: run 10/27/2026, 8:46:54 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/40514290501
claimed_at: 2026-10-27T13:46:55.299Z
decision: null
decision_answer: null
---

Package **C06B**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Addresses/associations: 1801. Read the study register for the specific envelope, material, roof, openings, date traps and source handles. Own distinctive facade/bay/tower detailing, carved entrance, cornice, roof decoration, glazing depth, attached porch/stoop and building-local ironwork; do not move the accepted envelope.

**Property-specific brief:**

- **1801: Kimball Chateauesque.** Bedford-stone envelope, tall hip/slate roofs, corner tower and conical cap, elaborate gabled dormers, finials/cresting, arched loggia and broad curved entry stair, long 18th Street flank. Phase guard: Period Taylor view is preferable for phase; HABS later drawings/photos only for surviving fabric. Side elevations and rear cannot be a mirrored front.

**Acceptance:**

1. Finished building, including visible side/rear treatment, passes the Glessner comparison protocol at close street, corner and aerial views; all unique features in register accounted for, liberties and licenses filed, compressed browser assets verified.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1889](../T-1750-1999/T-1889-build-1801-kimball-corner-mansion-envelope.md); [T-1851](../T-1750-1999/T-1851-carved-entrances-and-classical-or-gothic-trim.md); [T-1852](../T-1750-1999/T-1852-cornices-parapets-dormer-faces-and-cresting.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md)

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
  `kimball_house_1801_prairie`: a18-cgy-1801-kimball-early (photograph, oblique front, undated (1890s)), a18-chicago-and-its-makers-1929-kimball (publication plate, oblique front, 1929 (photograph 1890s)), a18-rba-taylor-1801-kimball-c1895 (photograph, oblique front, c. 1895), dw-rb-inland-kimball-1801-entrance-plate (publication plate, detail, Inland Architect vol. XX no. 6 (Jan. 1893), photogravure edition), dw-rb-architects-club-house-kimball-1801 (publication plate, oblique front, n.d. (c. 1925–26; page [11] of an Architects Club/Sketch Club publication mentioning the Dec. 8, 1925 Dickey competition)), a18-cgy-1801-kimball-1945 (photograph, oblique front, 1945), a18-cgy-1801-kimball-doorway-1961 (newspaper item, detail, June 29, 1961), a18-gh-kimball-exterior-2013 (photograph, oblique front, 2013), a18-gh-kimball-porch-north-2013 (photograph, detail, 2013), a18-gho-simmerling-kimball-1994 (lithograph, oblique front, 1994), a18-kimball-habs-photo-01 (photograph, oblique front, June 1965), a18-kimball-habs-photo-02 (photograph, oblique front, June 1965), and 1 more in the library

- kimball_house_1801_prairie

## Found by T-3000 (2026-10-22): the mansard's curb and deck against the Taylor photograph

Laying the cresting, the corner hood and the finials on the build's curb (T-3000) showed the curb
itself off the print. At the front's north-west corner the print's curb stands about 35-50 px lower
than the build's (the corner hip's top at about x 950, y 320 on the 1600 px print against the
build's x 978, y 247), and the print's corner hip runs about 25-30 px west of the build's all the
way down from the cornice. The front's deck ends at the print's x 1092, under its south finial,
where the build's runs on to x 1187. Re-read the lower faces' rise and pitch and the deck's extent
against the print (the queue was at its ceiling, so this is a finding here, not a ticket of its
own); the cresting, hood and finials `mansard.deck` lays follow the curb when it moves. The match
record's open difference names it.

**Found by T-3001 (2026-10-24).** Two more pieces of the 18th Street flank, read through T-3074's
camera (the queue was at its ceiling, so they are findings here, not tickets of their own; the
match record's open differences name both):

- *The gabled section's openings.* The print's principal storey has three round-arched lights
  across the section (x 360-440), the second an oriel on corbels with a carved panel over it
  (about 5.4-8.1 m), and the third an open loggia (head about 11.4 m) behind a balustrade that
  runs straight across it, under the gable; a pier at about u 0-0.9 (x 422-445) rises to the
  cornice. T-3001 lays one mullioned and transomed pair a storey on `p_gable` and K08's floor
  balcony, which bows.
- *The flank section's top.* Over the corbel table (about 9.5 m) the print's section carries a
  third storey of paired lights under a cornice, a gabled wall dormer with a finial (x 520-600)
  and the tall round-topped stack (x 467-530); the build carries `p_flank`'s wall to 13.9 m under
  K08's low hip.

**Released 2026-10-26** (claim of run 10/26/2026, 2:44:10 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40387345044): PR #1353 rebuilt the 18th Street tower on a corbelled stage and sized the tower's and turret's finials to the Taylor print (Taylor 'tower's form', 'east turret's shaft and finial' and HABS 2 'round tower' now fixed). The image gate still has 22 open differences across the three match records (gabled section's oriel and openings, flank section's top, mansard curb and deck, dormer hoods and faces, east range side door, dormer and stack, main flank stack position, south-east pinnacle and recessed range, rear range, south bay top, south cornice, the corner-balcony light, the loggia lights' frames, the tower finial's turned shape), more than one run holds; split is refused on a photo-gated house, so the rest goes back to the queue.

**Released 2026-10-27** (claim of run 10/27/2026, 6:27:04 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40495380150): PR #1372 rebuilt the 18th Street flank section on its corbel table under the coped fan gable and moved the flank stack (HABS 2 'flank section's top' and 'main block's flank stack', Taylor 'flank section's top' now fixed). The image gate still has open differences across the three match records (the section's rounded west corner, gabled section's oriel and openings, mansard curb and deck, dormer hoods and faces, east range side door, dormer and stack, south-east pinnacle and recessed range, rear range, south bay top, south cornice, corner-balcony light, loggia lights' frames, tower finial's turned shape), more than one run holds; a sign-off is never split, so the rest goes back to the queue.
