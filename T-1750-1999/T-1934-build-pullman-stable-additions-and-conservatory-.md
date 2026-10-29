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
- pullman_house_1729_prairie_ranges

## Reopened (owner, 2026-10-28)

Owner, 2026-10-28: *"in looking at 1729 prairie, the pullman estate it seems like tickets are closed and the gate is exited, but it is still way off from a photographic match, the stepped front, the south face, the entire greenhouses and the stable are all way off, not to mention the greenhouse area south of 18th, am i wrong? did you consider it done? because its not and you need to reenter the photographic match on that one if not"*.

This ticket closed without passing its image gate: `ticket.mjs split` closed it without asking the gate, and the pieces it minted carried no `## Image gate` section, so none of their `done`s asked it either (fixed by T-3235: a split parent's gate is now asked by its last piece). On 2026-10-28 its match records read:

- `pullman_house_1729_prairie_conservatory`: inland_1894_plate differs, taylor_16554_from_south matches, taylor_16555_west_front differs
- `pullman_house_1729_prairie_ranges`: no reference view solved

The owner names the conservatory and the stable. The stable and its one-storey ranges (`pullman_house_1729_prairie_ranges`) are still a `prairie_draft` record and have no reference view of their own, so the image gate above now names them as well as the palm house. Against the 1894 Inland plate and Taylor's 16555, the palm house renders as a faceted drum behind solid parapets on a blank wall, where the pictures show a colonnaded glass drum, its entablature, balustrade and ribbed dome, rusticated walls with pilasters, balustraded terraces with urns, and a stable with a moulded belt course, an open belvedere and crested deck.

Owner, 2026-10-28, the same thread: *"the surrounding wall/fence around the property also should be included in the match, as well as the flora"*. So each view also judges the lot's boundary (the coping walls, piers, posts and balustrades on Prairie Avenue, 18th Street and Calumet Avenue, and the garden wall round the glasshouse ground) and its planting (the ivy on the walls, the shrubs and beds, the yard and parkway trees as far as the picture shows them in its season), and a difference in either is `open` by the same bar.

It is reopened in place, not refiled. Read every picture itself, solve a camera for each one not yet solved, and work every view to `matches` under the T-3153 bar: an element missing or the wrong shape, a wrong count, a wrong material or colour, or a gap over about 0.3 m is `open`, never `within tolerance`. If it must be split again, its gate stays on it and the last piece closes it.

**Released 2026-10-28** (claim of run 10/28/2026, 10:52:41 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40719330148): PR #1425 works the palm house and its range to the Inland plate and Taylor's 16555 (open colonnade, open balustrades, rustication and pilasters, urns, broader ribbed dome); still open in the match records: the stable (belt course, open belvedere, crested deck, roof mass, corner bay's shape), the 18th Street boundary and the terrace's two-flight approach, and the planting. Not split: the split escape (T-3235) is not on dev yet, so the gate stays on this ticket.

**Released 2026-10-29** (claim of run 10/29/2026, 12:24:06 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40822599544): PR #1432 works the stable (pullman_house_1729_prairie_ranges) to its pictures through its own three reference views (T-3193's cameras re-anchored): open belvedere balustrade, open iron cresting with corner spires, moulded stone belt course with the upper sash on it, low cap on the corner bay, stone-toned mouldings. Still open in the match records: the 18th Street boundary (piers, coping, posts, lamps) and the planting in every view, the terrace's two-flight approach (conservatory), and the north block's lower roof that the plate alone places 1.5 m north. Not split: the gate stays on this ticket.

**Released 2026-10-29** (claim of run 10/29/2026, 2:54:31 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40837979830): PR #1435 (resume: gate still running, nothing red) builds the 18th Street wall before the palm house and stable (five piers, the 0.9 m coping wall, the two flights' openings, the curved low wall between them, the carriage-way opening, on to the stable's east wall) off the 1894 Inland plate's camera, and draws the planting in every estate view (camera flora). Still open in the match records: the lamps and urn on the piers and the lamp post by the court, the trees' places, the terrace's two-flight approach, the north block's lower roof, and Taylor 16555's camera depth (its eye 9.9 m from the lot line where the print puts the wall about 20 m off; its near gate piers stand on 18th Street's south side), which wants re-solving with the wall's piers in its fit. Not split: the gate stays on this ticket.

**Released 2026-10-29** (claim of run 10/29/2026, 12:02:11 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40912493836): PR #1450 (resume: gate still running, nothing red) builds the fifth 18th Street pier's urn off the 1894 Inland plate (read at full size as one squat lidded urn, 0.4 by 0.5 m, not a globe lamp with an urn behind it; the kit's turned urn stretched to it) and fixes that item in both plate records. Still open in the match records: the lamp post by the court (only Taylor 16554 shows it, rights unresolved, so nothing can be built from it), the trees' places, the terrace's two-flight approach, the north block's lower roof, and Taylor 16555's camera depth. Not split: the gate stays on this ticket.

**Released 2026-10-29** (claim of run 10/29/2026, 2:11:57 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40935892185): PR #1454 (merged) re-solves Taylor's 16555 camera with the 18th Street wall in its fit (eye about 21 m south of the lot line, focal 976 px; all readings 8.7 px rms, was 44.5) and re-judges both 16555 records through it. Newly open where the print and the 1894 plate disagree: the court's way east of the drum (piers 4.8 m apart around a way about 4 m wide in the print; 0.95 m opening built), the stable's eave 25 px high, the wing about 1 m longer in the print, and a street tree 4.1 m before the eye. Still open: the terrace's two-flight approach, the lamp post, the trees' places, the north block's lower roof. Not split: the gate stays on this ticket.

**Released 2026-10-29** (claim of run 10/29/2026, 3:14:05 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40946226768): PR #1458 (resume: gate still running, nothing red) places 18th Street's parkway trees before the estate off the 1894 Inland plate and Taylor's 16555 (data/street_trees/pictured_1904.json: six trees in place of four, the tree before Taylor's eye and the plate's foreground trunk withdrawn) after re-solving 16555's camera with the street's ground in its fit (eye 11.7 m further south in the garden across 18th Street, focal 1192 px, 6.9 px rms); through it the stable's eave (now about 12 px, 0.4 m, the plate disagreeing) and the wing's length (within 4 px) go within tolerance. Still open in the match records: the clipped shrubs and potted palms, the terrace's two-flight approach, the court's way (re-read: the print's piers at x 500-520, 580-600, 775-800 against the build's one at 535-570), the north block's lower roof, the lamp post. Not split: the gate stays on this ticket.
