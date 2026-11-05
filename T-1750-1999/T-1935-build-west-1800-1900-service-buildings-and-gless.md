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

**Released 2026-11-02** (claim of run 11/2/2026, 11:10:06 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41487192460): PR #1623 refines 1816's alley building (henderson_house_1816_prairie_coach_house) in place onto the K12 coach-house kit from the 1911 sheet 28: a 2½-storey brick stable 10.68 x 22.40 m (the draft's 9.25 m fit with two alley strips was wrong; the sheet draws one rectangle), party walls at both ends on the sheet's fire-wall signs, both alley window marks (6.27 and 15.72 m from the north wall, two dots each) built as sash pairs, two carriage bays, workyard to the house's rear range 11.64 m east. Draft rules skip s28-1816-rear; L-k12-1816-stable-1935. Still to do: 1824, 1834 and the 1834/1900 shed, 1900, 1906 and 1912, still the draft's. Image gate: both named pictures (Clark c.1905 north from 1936, Taylor 9974 south from 18th) show the house fronts and not the alley; no camera solved. Not split: the gate stays on this ticket.

**Released 2026-11-02** (claim of run 11/2/2026, 1:35:44 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41509211345): PR #1628 (resume: gate still running, nothing red) refines 1824's alley building (marsh_house_1824_prairie_coach_house) in place onto the K12 kit from the 1911 sheet 28: a 2-storey brick stable 10.62 x 17.60 m on the alley line, party walls at both ends on the sheet's fire-wall signs (the north one back to back with 1816's), its one alley window mark (8.34 m from the north wall) built as a sash pair, two carriage bays, workyard to the house 9.08 m east; draft rules skip s28-1824-rear; L-k12-1824-stable-1935; alley pole #02 re-laid 0.45 m clear of the eave. Still to do: 1834 and the 1834/1900 shed, 1900, 1906 and 1912. Image gate: Clark c.1905 shows the fronts, not the alley; no camera solved.

**Released 2026-11-02** (claim of run 11/2/2026, 8:35:28 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41566558611): PR #1640 (resume: gate still running, nothing red) refines 1834's alley building (jones_house_1834_prairie_coach_house) in place onto the K12 kit from the 1911 sheet 28 — the dead run 41529791662's branch, rebased onto dev, rebaked (GLB byte-identical) and gated: a 2-storey brick barn 7.52 x 16.33 m on the alley line, its 1-storey piece on the north 7.89 m of the yard wall, the one alley window mark built as a sash pair, party wall north against 1828's building; L-k12-1834-stable-1935; alley pole #03 re-laid clear. Still to do: the 1834/1900 shed, 1900, 1906 and 1912, still the draft's. Image gate: Clark c.1905 shows the fronts, not the alley; no camera solved.

**Released 2026-11-03** (claim of run 11/3/2026, 12:08:47 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41587229211): this run only lapped resume PR #1640 (the Jones 1834 barn slice); the ticket's other service buildings remain open

**Released 2026-11-03** (claim of run 11/3/2026, 11:21:18 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41678540306): PR #1667 (resume: gate still running, nothing red) refines 1900's alley building (elbridge_keith_house_1900_prairie_coach_house) in place onto the K12 kit from the 1911 sheet 28: a 2-storey brick stable (GARAGE in 1911, built as a stable) 9.15 x 15.42 m on the alley line, party walls both ends (fire-wall sign north against the 1834/1900 shed; the line shared with 1906's building south), the one alley window mark built as a sash pair, workyard walk 14.04 m to the house's rear porch; the census's '1-storey' corrected to the sheet's '2'; L-k12-1900-stable-1935. Still to do: the 1834/1900 shed, 1906 and 1912, still the draft's. Image gate: Clark c.1905 shows the fronts, not the alley; no camera solved.

**Released 2026-11-05** (claim of run 11/4/2026, 11:46:51 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41975258336): PR #1712 refines 1906's alley building (edson_keith_house_1906_prairie_coach_house) in place onto the K12 kit from the 1911 sheet 28: a 2-storey brick BARN 19.93 x 9.07 m and a 1-storey brick range 10.55 m south of it on the kit's range fitting, party wall north against 1900's stable, both alley window marks built as sash, workyard walk 9.14 m to the house's 2-storey rear piece; L-k12-1906-barn-1935; alley pole #04 re-laid clear. Still to do: the 1834/1900 shed and 1912, still the draft's. Image gate: Clark c.1905 shows the fronts, not the alley; no camera solved.
