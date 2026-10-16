---
id: T-1883
title: Finish 1808 Keith-Field neighbour of Glessner architecture
state: split
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-1837
opened: 2026-10-01
closed: 2026-10-16
pr: null
claimed_by: run 10/16/2026, 12:02:57 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-16T05:03:06.328Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38852568409
claimed_at: 2026-10-16T05:02:58.238Z
decision: null
decision_answer: null
---

Package **C01B**, one part of the owner-requested [T-1837](../T-1750-1999/T-1837-assess-the-complete-prairie-avenue-1904-architec.md) architectural programme. See the [design study](../evidence/T-1837-prairie-1904-architectural-study/README.md), [named-building register](../evidence/T-1837-prairie-1904-architectural-study/BUILDING-REGISTER.md), [every mapped frontage](../evidence/T-1837-prairie-1904-architectural-study/FRONTAGE-REGISTER.md) and [component / Glessner acceptance contract](../evidence/T-1837-prairie-1904-architectural-study/ASSET-CATALOG.md).

[Sparse-evidence design rules](../evidence/T-1837-prairie-1904-architectural-study/RECONSTRUCTION-RULES.md) provide declared starting ranges and the complete exterior checklist.

**Scope:** Addresses/associations: 1808. Read the study register for the specific envelope, material, roof, openings, date traps and source handles. Own distinctive facade/bay/tower detailing, carved entrance, cornice, roof decoration, glazing depth, attached porch/stoop and building-local ironwork; do not move the accepted envelope.

**Property-specific brief:**

- **1808: Keith/Field Romanesque-classical stone front.** Three-storey rock-faced front; south curved bay; north entrance loggia with Ionic columns, balustraded balcony and stair; upper windows; pierced stone parapet. Common-brick side and rear ranges. Phase guard: Use the 1888 published plan and photo together; explicitly join the north wall to the Glessner court boundary and avoid duplicate surfaces or daylight gaps.

**Acceptance:**

1. Finished building, including visible side/rear treatment, passes the Glessner comparison protocol at close street, corner and aerial views; all unique features in register accounted for, liberties and licenses filed, compressed browser assets verified.
2. Preserve the 1904-07-01 target, per-attribute attested/inferred/reconstructed provenance and a replaceable working interpretation for uncertain fabric. Map-only houses receive an explicit bounded design, never an unexplained blank or a duplicate landmark. Ingest source handles actually used into the canonical source system and apply existing rights rules.
3. Supply engine-neutral parameter/source data, reproducible generator or authored-asset provenance, material/license records and compressed full/balanced/light exports as applicable. Verify the actual browser result with repeatable front, oblique, rear and roof views, including 1280×800 desktop and 390×780 mobile. Record scene load, texture/mesh and draw/frame costs; fix visible defects before closure.

**Dependencies:** [T-1882](../T-1750-1999/T-1882-build-1808-keith-field-neighbour-of-glessner-env.md); [T-1851](../T-1750-1999/T-1851-carved-entrances-and-classical-or-gothic-trim.md); [T-1852](../T-1750-1999/T-1852-cornices-parapets-dormer-faces-and-cresting.md); [T-1853](../T-1750-1999/T-1853-ironwork-gates-canopies-and-boundary-walls.md); [T-1856](../T-1750-1999/T-1856-age-surface-variation-and-ground-contact.md); [T-2159](../T-2000-2249/T-2159-draft-the-18th-20th-prairie-block-around-glessne.md)

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

## The owner's report (2026-10-13)

Owner, 2026-10-13, in the project thread, with a street photograph of the 1800 block looking south-west from Glessner's corner and a phone screenshot of the model on dev:

> One thing I want to call out on the Keith house is that it while you worked on it as a test house it does not look much like the photos i can see of it. It has an Italianette top and the round tower appears on the north not south side, maybe this is already in the tickets for this but I wanted to make sure you hit those

Side by side: [pictures-vs-model-phone.jpg](../evidence/keith-1808-T-1882/pictures-vs-model-phone.jpg) (the 1888 plate, the mid-1950s view, the owner's photograph, the model on dev; S and N marked on each). The owner's photograph is library record `a18-owner-1800-block-looking-sw` (added with this report; its file is `chicago/prairie_1904_v1/research/public/a18-owner-1800-block-looking-sw.jpg` once the library PR lands).

What stands on the lot today is T-2266's K01 kit proof, not this house: its record says so ("a SMALL PROOF, not the house ... replaced by" T-1882 and T-1883), and the K-kit chain then dressed it with generic parts. This package replaces it.

**Split between the two tickets:** T-1882 owns the shapes: the flat top and parapet height, the bow's two-storey extent with the flat third storey over it, the loggia and stair masses, the overall height, and every opening's position and size. T-1883 (this one) owns the finish on them: the lattice, pinnacles and diaper band, colonnettes, columns, balustrades and cheek walls, the stone's tone and rock face, and the front fence. Its image gate closes the house, so every item below must match before it closes.

### What the pictures show and the model does not

1. **The top.** The model has a hipped slate roof with a gabled dormer over a bracketed timber cornice, an Italianate top. Every picture shows a flat top: a deep band of rock-faced diaper (checker) work over the third-storey windows, then a pierced stone parapet (square openings, a lattice), with a stone pinnacle at each front corner. No roof slope or dormer shows from the street.
2. **The bow, and which side it is on.** All the pictures and the 1888 plan put the round bow on the **south** half of the front (beside 1812), and the entrance loggia on the **north** half (beside Glessner), so the model's bow is on the right side. Its shape is wrong: the model runs a round tower from grade to the cornice, three storeys. The real bow is two storeys (principal and second; the 1965 photograph shows the ground storey bowed too), capped by a curved moulded band; the **third storey runs flat across the whole front over it**, as one arcade of six sash windows divided by colonnettes. In the owner's photograph, taken from the north-east, the bow's curved face reads as if above the porch because of the angle, and the tall pointed gable with the round-arched window just south of the Keith house is 1812 (Wheeler, T-1884/T-1885), not this house; the mansard with dormers beyond it is 1816.
3. **The entrance.** The model has a round-arched door in the middle of the front with an open stoop. The pictures show an open loggia at the north end: paired columns at each front corner (Ionic, per the T-1837 register) on pedestals, a pierced stone balustrade between them, a carved balcony with balustrade over it, under the second-storey window, and the stair rising on the loggia's south side between scrolled stone cheek walls, with a low arch under the loggia at basement level.
4. **Height.** The real front is much taller than Glessner's eave: the parapet stands above Glessner's ridge in the c. 1888 view and in `a18-gh-glessner-front-with-keith`. The model's cornice sits near Glessner's eave and only its dormer reaches the ridge.
5. **Openings.** Principal storey: three tall windows with transoms in the bow; second storey: four windows round the bow and one window over the loggia; third storey: the continuous arcade of six; basement windows just above grade. The model has paired sashes in its tower and single windows elsewhere, three storeys alike.
6. **Stone.** Pale grey rock-faced ashlar in heavy courses, with a rusticated base (the 1965 colour photograph shows the tone). The model's front is buff/tan, more even coursed stone.
7. **Front ground.** The 1887-88 pictures show low stone posts and rails along the walk and stone carriage blocks at the curb; the 1965 photograph shows a low iron fence, later fabric. The model has a tall iron fence with gate piers and urns. Date the fence before choosing.

### Stone (owner, 2026-10-13)

Owner, in the thread: *"I think you should be able to use much of the same stone approach you did for Glessner for that, maybe it's a different color a bit, lighter greige or whatever you can find from history"*.

- **Reuse Glessner's rock-faced granite approach** (T-2416's material, `masonry_house_v4_materials.py`'s granite and its rock-face relief; the colour applied as a tint at load, as `renderers/web/js/glessner-stone.js` does for Glessner, because the glTF exporter clamps colour factors and a baked tint darkens the stone). Give the Keith house its own tint constant; do not move Glessner's.
- **What history gives for the colour.** The Glessner House Museum's account calls it "a granite front" (record `a18-gh-1808-keith-field-front`). Every monochrome picture shows it much paler than Glessner's granite: beside it in `a18-gh-glessner-front-with-keith` and in the c. 1888 street views it reads near white. The one colour picture, `a18-gh-1808-porch-1965`, reads a pale grey: on the bow, sRGB about (142, 141, 161), r/g 1.01, b/g 1.14, against a near-white wall in the same print at r/g 1.03, b/g 1.05. The wall is in shade and the print is cast blue, so the stone's true tone is a light neutral grey with at most a faint warm cast: a lighter greige than Glessner's grey-greige (Glessner's sunlit front reads r/g 1.023, b/g 0.961). Before settling the tint, look for the stone or quarry named in the 1886-88 trade notices (`a18-inland-architect-1886-09-keith-notice`, `dw-aabn-1886-keith-1808-permit`, `npo-1808-rebj-1886-08-28-keith-permit-38x80`) and record what was found and its tier.
- Measure it as Glessner's was (the `tools/qa_glessner_stone.mjs` method): the sunlit front's r/g and b/g against the pictures. In the match records for the monochrome prints, colour is `not shown`.

### Pictures the gate list above leaves out

Build toward these too (all in the Prairie library, all showing this front):
- `a18-owner-1800-block-looking-sw`: the owner's photograph, from the north-east (undated; Glessner complete, no ivy).
- `a18-gh-1800-block-looking-sw-c1888` (same photograph as `a18-gh-1800-block-sw-george-glessner`): c. 1888, from the 18th Street corner.
- `a18-gh-1812-1808-1800-mid1950s`: mid-1950s. Its record says the camera is north-east looking south-west; the picture is taken from the south-east (1812 is nearest, Glessner recedes at the right). Correct the record when the camera is solved.
- `a18-gh-nickel-1967-1812-1808-1800`: 1967, elevated, nearly square-on to the front.
- `a18-gh-1808-porch-1965`: 1965 colour, the bow, the loggia and the stair close up.
- `a18-rba-reed-1941-prairie-north-from-1820`: 1941-42, distant.

The 1941-1967 pictures are evidence of their own dates (AGENTS.md rule 11): argue any change since 1904 in the match record.

`cgn-1804-landowner-1874-double-house` (and the same engraving as `a18-gh-hitchcock-galloway-1874-sketch`) shows the 1874 Hitchcock/Galloway double house that stood here **before** the Keith house was built in 1886. It is not a picture of this building: do not build toward it or solve a camera for it.

## Owner authorization and dependency check (2026-10-16)

Owner, in the interactive ticket-status thread, after being told that the 1888
Inland Architect Keith plate's scan remained `check_required`:

> Ok to use that image, go ahead and proceed on that ticket and merge to green

This authorizes using that 1888 plate for the model and its photographic comparison,
and completing this ticket through a green merge into `dev`. Preserve the source's
credit and record this permission; it is not a claim that unrelated images have the
same permission or that their rights have been independently established.

The recorded wait on T-1882 is stale. T-1882 was split into T-2499 and T-2500;
both pieces are `done`, with code PRs #809 and #814 merged into `dev` on
2026-10-15 at 09:59:51Z and 10:58:05Z respectively. The owner's 2026-10-13
queue instruction places this finish in the predecessor's priority position.
The photographic image gate below remains the acceptance, including the floor,
stair and boundary discrepancies the envelope PRs explicitly deferred here.

## Image gate (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

Pictures:
  `keith_house_1808_prairie`: a18-gh-1808-keith-field-front (photograph, front elevation, undated (after 1886)), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-inland-architect-1888-02-glessner-plate (publication plate, oblique front, February 1888 (photograph winter 1887–88)), a18-inland-architect-1888-02-keith-plate (publication plate, front elevation, February 1888 (photograph c. 1887)), a18-rba-ia-1888-keith-1808 (publication plate, front elevation, February 1888), a18-rba-taylor-2135-glessner-ne (photograph, oblique front, c. 1889 (RBA); likely 1887–88), cgn-1804-landowner-1874-double-house (engraving, oblique front, May 1874), cgn-1808-inland-1888-keith-copy (publication plate, front elevation, February 1888 (The Inland Architect, vol. XI no. 1)), a18-gh-florian-1948-northeast-overall (photograph, oblique front, July 1948)

- keith_house_1808_prairie

## Source-cleared façade refinement (2026-10-16)

Code PR **[chicago#853](https://github.com/kevinrhaas/chicago/pull/853)** merged into `dev` with green checks. The owner-authorized
1888 plate now drives the pierced stone parapet, corner pinnacles, checkerwork,
upper colonnettes, Ionic entrance, curved stair cheeks, coursed south bow and
early low stone boundary. The contemporary September 1886 notice supports a
granite front but does not name its quarry or colour. Other source permissions
are not inferred from this approval.

The main envelope and site placement are preserved. All 16 known photographic
comparisons have camera records, rendered comparisons and **`differs`** verdicts.
This merge does **not** satisfy the owner's photographic acceptance and does
not close T-1883. Remaining differences include north-return ashlar courses,
finer balcony/pedestal and pinnacle profiles, surface and colour convergence,
and independent-camera residuals. Later ironwork/chimneys/vegetation are not
silently backdated into 1904.

Evidence: [review and measurements](https://github.com/kevinrhaas/chicago/blob/dev/chicago/4d/docs/RESEARCH/k01-1808-keith-1883/README.md).
Actual published 1904 desktop and mobile captures passed with zero loader/page
errors and unchanged scene budgets; all 28 mobile Images thumbnails loaded
with credits. Repository/preflight and CI receipts are in the PR. These checks
validate the implementation, not photographic equivalence.

The stale predecessor dependency and the 1888-plate permission blocker are
cleared. Leave this ticket **open**, retaining its owner-directed priority,
for the remaining photographic convergence.
