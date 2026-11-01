---
id: T-1932
title: Refine north-west alley coach houses and service courts
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
claimed_by: run 11/1/2026, 11:01:54 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41328931919
claimed_at: 2026-11-01T17:01:54.677Z
decision: null
decision_answer: null
---

Package **R20W**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Enumerate each detached rear polygon behind sheet 20 west frontages 1600-1736; use its actual material/storey annotation. Includes 1620 surviving stable and 1720 large stable. Give each roof a child ID, owner property, footprint, openings, roof and service connection.

**Acceptance:**

1. One continuous alley segment with every mapped rear polygon accounted for as 1904 retained/reconstructed/excluded; no automatic 1911 auto conversion, no duplicated attached wings.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1840](../T-1750-1999/T-1840-reconcile-sheet-20-building-entities-for-1904.md); [T-1854](../T-1750-1999/T-1854-coach-houses-stable-fittings-and-service-wings.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2160](../T-2000-2249/T-2160-draft-the-16th-18th-prairie-block-with-the-draft.md)

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
  `law_house_1620_prairie_coach_house`: a16-cgy-landowner-1874-1620-law (publication plate, oblique front, May 1874)

- law_house_1620_prairie_coach_house

**Released 2026-10-31** (claim of run 10/31/2026, 7:01:57 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41198746573): PR #1525 (resume: gate still running, nothing red) refines 1620's alley building (law_house_1620_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (7.36 x 16.30 m, 2 storeys, brick, two window marks, party wall against 1616's) and Robinson 1886's brick stable X; draft rules skip s20-1620-r1. Its image-gate camera on the 1874 Land Owner engraving is solved: the engraving draws a board-and-batten building under hipped roofs where both maps draw brick, read as the frame predecessor; 5 items left open in the match record with that reasoning (closing past them needs done --anyway --why, or a picture of the brick stable). Still to do: every other rear building of the north-west alley 1600-1736, still the draft's. Not split: the gate stays on this ticket.

**Released 2026-10-31** (claim of run 10/31/2026, 11:49:13 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41221033334): PR #1535 (resume: gate still running, nothing red) refines 1616's alley building (house_1616_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (9.88 x 11.02 m, 2 storeys, brick, stable X, alley window mark, fire walls both ends; party wall north, open gable against 1620's party wall); Robinson 1886 draws the lot's rear empty, so it postdates 1886. Still to do: every other rear building of the north-west alley (1612, 1626, 1628, 1630, 1700, 1712, 1720, 1726, 1730), still the draft's; 1620's image-gate items stay open as #1525 left them. Not split: the gate stays on this ticket.

**Released 2026-11-01** (claim of run 10/31/2026, 11:56:21 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41274183966): PR #1555 (merged) refines 1612's alley building (goodman_house_1612_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (15.23 x 14.02 m, 2 storeys, brick, one stable X over both parts of a frame partition, window marks on the alley and north walls, no fire-wall sign) and Robinson 1886's 7.1 x 14.5 m crossed brick stable, which is the 1911 building's alley part; the kit gained a 'mirror' option so the party wall sits south against 1616's and the open gable north; draft rules skip s20-1612-r1. Still to do: every other rear building of the north-west alley (1626, 1628, 1630, 1700, 1712, 1720, 1726, 1730), still the draft's; 1620's image-gate items stay open as #1525 left them. Not split: the gate stays on this ticket.

**Released 2026-11-01** (claim of run 11/1/2026, 2:12:58 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41286871793): PR #1560 (resume: gate still running, nothing red) refines 1626's and 1628's alley buildings (house_1626_prairie_coach_house, house_1628_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (1626: 7.97 x 11.87 m; 1628: 7.01 x 13.94 m; one shared wall line; '2' storeys, brick, a stable X each; window marks on 1626's alley and north walls and 1628's alley wall) and Robinson 1886's matching pair of crossed brick stables on lots 16-17; 1626 in mirror image, 1628's mark read as its carriage bay; draft rules skip s20-1626-r1 and s20-1628-r1. Still to do: every other rear building of the north-west alley (1630, 1700, 1712, 1720, 1726, 1730), still the draft's; 1620's image-gate items stay open as #1525 left them. Not split: the gate stays on this ticket.

**Released 2026-11-01** (claim of run 11/1/2026, 4:04:17 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41295387638): PR #1565 (resume: gate still running, nothing red) refines 1712's alley building (house_1712_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (7.64 m deep x 11.99 m along the alley, 2 storeys, brick, stable X, one window mark at the middle of the alley wall, north wall on the lot line, no fire-wall sign) and Robinson 1886's crossed brick stable behind lot 3 (1712 in its margin); party wall north, open gable south, the kit's 40-degree roof over the shallow span; draft rules skip s20-1712-r1. 1630's is a 1-storey frame shed the two-storey brick kit does not build. Still to do: every other rear building of the north-west alley (1630, 1700, 1720, 1726, 1730), still the draft's; 1620's image-gate items stay open as #1525 left them. Not split: the gate stays on this ticket.

**Released 2026-11-01** (claim of run 11/1/2026, 6:17:47 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41305327583): PR #1570 refines 1700-1706's alley building (glessner_lee_house_1700_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (10.42 x 19.37 m, 2 storeys, brick, stable X, one window mark at the middle of the alley wall, north wall on the lot line, a dashed partition inside, not built) and Robinson 1886's crossed brick stable behind lot 2 (1702, 105 ft); party wall north, open gable south, 30-degree roof; draft rules skip s20-1700-r1; alley pole #04 steps 0.45 m west. Found, open on this ticket: the renderer beds a K12 stable at the lowest ground under its feet and counts the workyard paving's y=0 edges as feet, so on ground falling east 1700's stable sits 8.5 cm low and its apron lies under the lawn beside the yard wall (1712's clears by millimetres); a renderer/GLB-contract fix (building-feet.js), see docs/RESEARCH/k12-1700-stable-1932/README.md. Still to do: 1630, 1720, 1726, 1730, still the draft's; 1620's image-gate items stay open as #1525 left them. Not split: the gate stays on this ticket.

**Released 2026-11-01** (claim of run 11/1/2026, 8:00:02 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41313650912): PR #1573 (resume: gate still running, its only earlier red fixed) refines 1720's alley building (walker_house_1720_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet (stable 10.11 x 16.61 m, 2 storeys, brick, stable X, window mark 8.90 m from its north wall; a 1-storey brick range 4.22 m deep running on 6.93 m south along the alley to the 1720/1726 lot line, window mark at the line) and Robinson 1886's crossed brick stable and uncrossed range behind lot 4 (which divide the run about 11.2 + 13.4 m against the sheet's 16.6 + 6.9; the sheet's division built). The kit gains a 'range' fitting (two new self-tests); the other nine K12 coach houses rebake byte-identical; draft rules skip s20-1720-r1 and r2. By 1911 the range ran on past the lot line to 1726's garage; built ending on the line as the plate ends it, so 1726's draft still stands its 2-storey piece 0.56 m south. Still to do: 1630, 1726, 1730, still the draft's; 1620's image-gate items stay open as #1525 left them. Not split: the gate stays on this ticket.
