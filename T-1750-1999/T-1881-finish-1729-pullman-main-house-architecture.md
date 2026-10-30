---
id: T-1881
title: Finish 1729 Pullman main house architecture
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
claimed_by: run 10/29/2026, 8:11:28 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/40983527311
claimed_at: 2026-10-30T01:11:28.567Z
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

## Reopened (owner, 2026-10-28)

Owner, 2026-10-28: *"in looking at 1729 prairie, the pullman estate it seems like tickets are closed and the gate is exited, but it is still way off from a photographic match, the stepped front, the south face, the entire greenhouses and the stable are all way off, not to mention the greenhouse area south of 18th, am i wrong? did you consider it done? because its not and you need to reenter the photographic match on that one if not"*.

This ticket closed without passing its image gate: `ticket.mjs split` closed it without asking the gate, and the pieces it minted carried no `## Image gate` section, so none of their `done`s asked it either (fixed by T-3235: a split parent's gate is now asked by its last piece). On 2026-10-28 its match records read:

- `pullman_house_1729_prairie`: albertype_1890 differs, detroit_det_4a08065 differs, taylor_1445_album differs

The owner names the stepped front and the south face. The house is built as one K01 block whose Prairie front and 18th Street flank are flat faces under one continuous mansard; the Detroit print (LC-D4-12551), the 1890 Albertype plate and Taylor's no. 1445 show the fronts breaking forward and back in pavilions, each under its own mansard section. 26 pictures are listed above and 3 have cameras. The CHM 1905 views, Detroit det 4a08066, the Daily News negative and the Beman-addition side views are still to be solved, or recorded as unusable with the reason.

Owner, 2026-10-28, the same thread: *"the surrounding wall/fence around the property also should be included in the match, as well as the flora"*. So each view also judges the lot's boundary (the coping walls, piers, posts and balustrades on Prairie Avenue, 18th Street and Calumet Avenue, and the garden wall round the glasshouse ground) and its planting (the ivy on the walls, the shrubs and beds, the yard and parkway trees as far as the picture shows them in its season), and a difference in either is `open` by the same bar.

It is reopened in place, not refiled. Read every picture itself, solve a camera for each one not yet solved, and work every view to `matches` under the T-3153 bar: an element missing or the wrong shape, a wrong count, a wrong material or colour, or a gap over about 0.3 m is `open`, never `within tolerance`. If it must be split again, its gate stays on it and the last piece closes it.


## Owner's report, 2026-10-29: fix these first

The owner, after walking it on the phone (dev, 1904): "the front is very janky and the entry is not straight and still the front facade and entry need a lot of work and the south face is still incredibly messed, there is a big box in there that is still off ... the whole area needs more work to get to photographic reproduction." He chose (2026-10-29) that steward runs keep this ticket. Take these before any further detail (hoods, cresting, courses):

1. **The grey box on the 18th Street face.** Seen from the lawn inside the 18th Street wall looking east, a low flat-topped block with one sash window stands in front of the porte-cochère's arches. It is the 18th Street pavilion's (`bays` p_18th) ground storey east of the porte-cochère: geometry at u 10.4-19.5, v 20.2-20.8, y 0-2.6 in material `bay_stone`, reading grey against the red-toned walls, with a sash at u 10.5-12.3. Taylor's no. 1445 shows the flank there as one stone wall, full height, under the pavilion's own cornice: no low block and no second stone. Make the pavilion one full-height mass in the walls' own stone, or take it off where the photograph shows none.
2. **The entry is not straight.** Through the Prairie front: the stair is not on the door's axis (the door stands right of the stair's centre), its cheeks run into the portico's columns, and a plain solid stone block stands beside it. The front walk bends between the gate piers and the stair. In the Detroit print the stair rises straight between the portico's two northern columns to a door centred between them, from a straight walk. Put the door, the stoop, the walk and the gate on one axis.
3. **The walls read as red brick.** Up close the brownstone renders with brick-like courses and a red tone. Every picture shows dressed ashlar, light in the prints. Check the K02 stone's course size and tone against the pictures.
4. **The front facade overall** (the forward block, the portico and balcony, the pavilion piers) reads as stacked pieces, not one front. Judge it against the Detroit print and Taylor's no. 1445 as a whole, not item by item.
**Released 2026-10-29** (claim of run 10/28/2026, 11:07:12 PM CT): no reason given

**Released 2026-10-29** (claim of run 10/29/2026, 7:18:56 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40871419322): PR #1437 (belt course, eared dormer hoods, brownstone dormer faces) merged to dev; the image gate stays open on the forward-block and 18th Street pavilion dormers (needs a K08 bay-kit change) and the broken pediment, so the owner's ticket stays open

**Released 2026-10-29** (claim of run 10/29/2026, 8:39:42 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40883140451): PR #1444 (dormers on the forward block's and the 18th Street pavilion's own mansards, via a new K08 mansard_dormers kit path) is up on resume while its gate finishes; the image gate stays open on the broken pediment, the oculus pier and the flank's east section, the 18th Street wall's balustrade and posts, the trees and ivy, and the unsolved CHM 1905 views

**Released 2026-10-29** (claim of run 10/29/2026, 4:02:02 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40953655189): PR #1459 (owner's 2026-10-29 items 1-2: the ranges draft's grey porte-cochere box r3 taken off 18th Street; door, stair, inner columns and gate on one axis v 5.25 with stone balustrades) is up on resume while its CI gate finishes; items 3 (the K02 stone's tone and brick-like courses) and 4 (the front judged as a whole) and the image gate's open differences remain, so the owner's ticket stays open
