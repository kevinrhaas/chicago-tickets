---
id: T-2228
title: Glessner: run final photographic comparison and evidence sign-off
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/15/2026, 5:37:22 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-15T22:37:22.951Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2227; settle reopens it in T-2227's queue line when that PR merges.

**Audit item:** GA-26 • **Priority:** P1 • **Basis:** Completion gate

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Passing a technical gate is not evidence that the house matches photographs. Exact 1904 color and hidden fabric cannot be proven from the available black-and-white record.

Deliver fixed-camera reference/render pairs and a discrepancy register for silhouette, openings, materials, ornament, ground, vegetation and lighting. Review all elevations and declare remaining uncertainties.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. All high-priority visible discrepancies resolved or explicitly accepted with a reason.
2. No unreviewed courtyard/rear face; include sunlit, shaded, near and distant views.
3. Label attested versus inferred details and present a photo-quality result without claiming unsupported historical perfection.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #104: [Glessner House stable/coach-house end on 18th Street, c. 1887 (Cornell A. D. White collection; as reproduced by the museum)](https://glessnerhouse.blogspot.com/2022/12/the-original-odd-quaint-queer-dutch.html) — `a18-gh-cornell-glessner-rear-c1887`; c. 1887; visually inspected. Rights: unknown — link only.
- Audit #106: [Female servants' entrance at Glessner House (photograph by George Glessner)](https://glessnerhouse.blogspot.com/2015/01/george-glessner-photographer.html) — `a18-gh-glessner-female-servants-entrance`; c. 1888–1890s; visually inspected. Rights: pending — permission requested.
- Audit #107: [Porte cochere doors (photograph by George Glessner, about 1888)](https://www.glessnerhouse.org/porte-cochere-doors) — `a18-gho-porte-cochere-doors-c1888`; about 1888; visually inspected. Rights: pending — permission requested.
- Audit #115: [Front elevation](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060904p) — `a18-glessner-habs-photo-02`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #118: [Interior court](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060907p) — `a18-glessner-habs-photo-05`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #144: [2. First floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=2) — `a18-glessner-habs-sheet-2`; 1963; visually inspected. Rights: no known restrictions.
- Audit #146: [4. Section A-A - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=4) — `a18-glessner-habs-sheet-4`; 1963; visually inspected. Rights: no known restrictions.
- Audit #156: [6. Front (east) elevation - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=6) — `a18-glessner-habs-sheet-6`; 1965; visually inspected. Rights: no known restrictions.
- Audit #161: [Glessner House: west roof and hayloft dormer (Richard Nickel, 1966–67)](https://glessnerhouse.blogspot.com/2022/04/richard-nickel-and-glessner-house.html) — `a18-gh-nickel-west-roof-dormer`; 1966–1967; visually inspected. Rights: copyright — link only.

**Current audit views:** prairie, northeast, north, northwest, west, courtyard, court-east, court-west, roof, entry, porte. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2227](../T-2000-2249/T-2227-glessner-validate-full-light-browser-quality-and-controlled.md)

House-only sign-off; whole-street photography additionally depends on existing T-1882/T-1883/T-1935/T-2159 context work. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## T-2199 retrieval finding — 2026-10-09 UTC

T-2199 closes the bounded retrieval pass with 10/17 recovered records and seven explicit unavailable images (#015/#025/#128–131/#140). Cornell/report duplicates do not multiply corroboration. The report and shot brief expose remaining uncertainty; final photographic acceptance cannot claim those gaps have been resolved.

[Retrieval report and photographic brief](https://github.com/kevinrhaas/chicago/blob/dev/chicago/prairie_1904_v1/docs/glessner-reference-recovery.html). This is evidence handoff only; the owner scheduling hold remains in force.

## T-2200 measurement handoff — 2026-10-09 UTC

T-2200 establishes eight core views with 80 picks plus a seven-pick limited courtyard-west reference. No whole-west calibration or pre-1904 courtyard image is available. All core views retain 1% target exceptions, and isolated-page QA is not whole-scene performance or photographic sign-off. Final acceptance must revisit missing coverage, association/camera bounds and both projected-width/observed-span residuals using frozen cameras. See `docs/RESEARCH/glessner-camera-baseline/README.md`. This handoff does not release this ticket.

The frozen-asset checker is registered as manual in `data/research/check_gate_baseline.json`, owned by this final sign-off ticket. It verifies archived caf1c4e3/T-2235 bytes; later model edits use the frozen-camera candidate command. Public instrument data is `data/comparisons/glessner/`. This ownership note does not release the manual scheduling hold.

## T-2206 proportions handoff — 2026-10-10 UTC

[PR #604](https://github.com/kevinrhaas/chicago/pull/604) provides current-model measurements through the unchanged T-2200 cameras and a 15-row dimension/confidence/disposition table. [Audit dossier](https://github.com/kevinrhaas/chicago/blob/dev/chicago/4d/docs/RESEARCH/glessner-proportions-2206/README.md). This is not photographic acceptance: HABS sheets 4/6 disagree on main-roof rise by roughly 3 ft; the section also suggests a stair cone/finial rise roughly 2–3 ft below the model, but its vertical scale and line choices are not independently controlled. North-inclined chimney/finial and courtyard residuals remain unresolved. The existing geometry is retained provisionally; no camera refit or source-pick edit masks the differences.

Retain the corrected west ridge, dormer hoods, dining hip, upper glazing and continuous eave. The northeast copper fold remains T-2220; the independent component-topology follow-up is T-2267. This evidence handoff does not release T-2228 or any other owner-held ticket.

## Image gate (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

- glessner_house

## T-2223 final-comparison handoff — 2026-10-15

All five unchanged-camera canonical renders were reviewed again in [PR #803](https://github.com/kevinrhaas/chicago/pull/803) and remain `differs`. The inclined north view clearly retains an extended horizontal roof ridge where the photograph shows a pointed tower cone; investigate the connector's apex extrusion while preserving the corrected flat north wall and partial curved return. Pillowed masonry relief, window correspondence, the rainwater receiver's absolute height and the two HABS section alignments remain open.

Include the courtyard doors in the final opening register. The modern licensed service-stair photograph shows a glazed/grilled upper landing door where the model currently uses plain timber; verify its chronology before copying 2024 details. Separately, a modeled west-wing courtyard door at x=10.8204 m, y=13.5941–14.3561 m and sill z=1.7678 m has no external access in the service views. Reconcile this with the HABS plan and the specifically dated 1955 rear-stable stair; do not assume all western doors or stairs have the same date. No opening was changed by T-2223.

**Additional plan reading:** re-viewing HABS sheet 2 identifies a second narrow `DN` flight along the courtyard face of the west service wing, beside the north-court service flight. It is distinct from the wooden stair behind the service wing that the drawing dates c.1955. Correlate its top with the elevated west-courtyard door and establish its date before final modeling; the 1955 note does not by itself justify omitting this separate flight. Coordinate its foot with T-2224's western pedestrian route. PR #803 refines the existing north-court flight and rear gate only.


## Correction to the west-courtyard access hypothesis — 2026-10-15

The actual native HABS sheet 2 detail has now been re-read: the narrow west-side flight's `DN` arrow points **toward the north/door**, opposite the existing raised north-court flight. Its tread run lies at the southern end of a long narrow landing or areaway. The earlier handoff's suggestion of another stair rising to the modeled high west door is therefore **not established**; do not build it from that suggestion.

The licensed modern courtyard photograph `wlemay_glessner_courtyard_2024_159537058` was also inspected directly at full display. It shows the west-wing door low beside a railed recess, while the north-wing door stands on the raised landing. This supports investigating the modeled west door's 1.7678 m sill and its assumed main-house floor datum. It does not independently establish a precise 1904 sill height or permission to copy every modern feature. Reconcile the plan, sections, opening register and dated alterations before changing geometry; keep the c.1955 rear-stable wooden stair distinct from this court access. HABS sheet 1 is the title/site plan, not a basement plan.

Source detail: the native `chicago/prairie_1904_v1/research/public/glessner-habs-sheet-2.tif`, crop origin (5900,3300), size 1200x1100 from the 9624x7584 plate. No new geometry or final image verdict is claimed by this correction. T-2228 remains dependent on T-2227.

**Unblocked 2026-10-15:** T-2227 merged (PR #834); this took its place in the queue. The block read: T-2227 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)

## Final implementation started — 2026-10-15

T-2227 merged as PR #834 after the full local gate, all 18 exact-head desktop/mobile smoke groups, and a successful retry of the automatic bake precheck. Its deployed dev runtime and unchanged Glessner Full/Light assets are byte-verified. T-2228 is claimed on the resulting dev commit.

The remaining photographed roof discrepancy requires geometry changes and a fresh bake. First candidate: retain the flat north facade, wrapped staggered masonry and flared eaves, but replace the extruded upper apex with a complete pointed cone united with a lower pitched connector. Its initial 39.2-ft north-grade ridge is a bounded reconstruction from the existing inclined-camera reading, not a survey measurement or an independently confirmed height from two photos. Preserve before/after camera poses and retain `differs` until actual visual review. Light remains capped at 200,000 triangles.


## 2026-10-15 — active roof/courtyard correction pass

T-2227 is merged as PR834 and deployed. T-2228 remains claimed; photographic
signoff is not being closed. The expanded HABS4 courtyard section exposed host
roof tiles crossing all three dormer windows and an eave crossing an upper wall
opening. Candidate geometry now reconciles the section eave while retaining the
approved north facade datum, cuts exact dormer/host intersections, and corrects
section dormer/finial proportions. The pointed north cone/lower connector, raised
bow hood, broad basement grille and terrace cap return are included. Native
controls, plan/section disagreements and bounded reconstruction are recorded in
`docs/RESEARCH/glessner-final-comparison-T-2228/`.

Targeted spatial tests pass; Light source candidate193796 triangles is below the
unchanged200000 ceiling. Full/master and derivatives are currently baking; visual
and integration gates are still pending. The original five comparisons remain
`differs`; the expanded section is an additional view, not a replaced baseline.
The west courtyard door/descending areaway, remaining elevation correspondence
and final photographic acceptance remain under this ticket. No main promotion,
new budget, source-rights clearance or final match verdict is claimed.


## 2026-10-15 — baked candidate and direct visual review

The correction candidate is baked and packaged. Full/Web/Light contain
1,372,996 / 1,372,996 / 193,796 triangles, with zero coincident faces and
unchanged ceilings. The derived-data sequence reached a fixed point, and the
post-publish K01 contract passes. The actual master SHA256 is
`ab8a25d604bd31da5ace816f08d2189faa8d7e71c673adfc41b94bb6f58ba9b4`.

All ten current master side-by-sides were directly reviewed. The original five
cameras retain their bytes; four additional views import unchanged T-2200 poses,
and the wide court section uses the same independent HABS4 controls. Every match
record remains `differs`. The roof no longer crosses dormer glazing or the upper
court-wall opening; the pointed north cone and lower connector are visible.
Dormer roof width, the coping/post join, plan/section tower disagreement, west
court access and street opening/camera correspondence remain open.

Published desktop/mobile review and the full integration gate are in progress.
The upcoming correction PR must not close T-2228 or imply photographic signoff.


## 2026-10-15 — preflight findings and revised candidate

The initial candidate passed all twelve published Full/Light courtyard stands and
loaded all124 credited mobile image tiles. The full895-step preflight then found
four failures: rainwater leaders crossing openings after the tower/garden-light
changes, stale opening schedules, and malformed/uncompiled liberty fields causing
two provenance gates to fail. No commit, PR or merge was made on that red gate.

The two east-court leaders are now explicitly reconstructed within clear wall
strips atS61.61 andS42.4ft, retaining their connected gutters and stock. Existing
Full/Light drainage checks pass. The liberties now carry parsed Decision/Covers/
Recorded fields, and the generated opening schedule describes the garden grille.
A revised bake also narrows dormer side projections to144mm, bounded by the native
HABS4 body/roof widths; its85mm apron run retains a gentle flare. The1500 host
samples, clear glazing and independent section-width checks pass. The revised
Light source estimate is193683 triangles under the unchanged200000 ceiling.

Fresh bake, exact-asset photographic/browser review, full preflight and dev
integration remain required. Earlier candidate screenshots and gate receipts do
not accept these revised asset bytes. T-2228 remains claimed and all photographic
verdicts remain differs; terrace/post geometry, west access and elevation
correspondence remain open.


## Owner priority — overhead roof alignment (2026-10-15)

The owner supplied a modern aerial view, an arrow-marked copy, and two model
overhead views. First straighten the north-range ridge through the west-wing
junction; the current west cross-gable crest at S18.4 differs from the north
ridge at S14.6, producing the visible diagonal join. Check the west peak's
position so the ridge axes meet at a right angle, then match the remaining roof
features, including the northeast copper corner coverage. Add a reproducible
overhead comparison. The modern aerial is surviving-form evidence, not a dated
1904 color or material survey; UI labels and trees are not roof controls.

The pending correction batch has not been committed or merged. Its full gate
was interrupted before a verdict for this priority; its ongoing browser run
will be retained as pre-correction evidence. No green or photographic match is
claimed for the upcoming roof change. Existing HABS views and north service
door/window clearances remain regression requirements. This finding extends
T-2228 and precedes the terrace/areaway corrections.

Owner follow-up, 2026-10-15: explicitly compare the west-elevation windows
under the shifted cross-gable. The owner expects the corrected roof peak to
center the windows more naturally. Verify opening-to-peak alignment and roof
clearance in the actual baked west view and historical obliques; preserve
existing opening coordinates unless source comparison supports a change.


### Ridge and west-window review, 2026-10-15

The rebuilt master `6f1cbdee8e64edacea8a6dc0ad4bb461ab43eaf6c108628e56fd81f95dd5220e`
was directly reviewed at the frozen aerial camera: the S14.6 crest now aligns
through the west crossing. Full west elevation renders show the peak/cupola
move while all eight wall openings remain unchanged and clear of both slopes.
Upper-pair midpoint S16.25 is closer to the peak (2.15 to1.65ft); the lower
pair midpoint S17.60 does not improve (0.80 to3.00ft). No arbitrary window
shift is made to force symmetry. HABS01 and the Nickel west-dormer view were
re-read; they do not independently expose a complete square-on west elevation.

The next owner-directed correction restores the aerial's omitted chamfered
copper strip, seated exactly on the existing north courtyard roof plane.
The reconstructed W55/S22 to W50/S19 boundary and east junction are recorded
in L-glessner-copper-return-2228. Tile removal matches the copper coverage,
with the radial hood subtracted; the former folded/raised rectangle does not
return. 2000 independent rays verify no gap/overlap, and Full/Light sheet stock
stays seated. Fresh bake and visual review remain pending. T-2228 stays open;
no photographic acceptance or dev merge is asserted by these source checks.


### Owner clarification — confirm window positions from northwest photographs

On2026-10-15 the owner explicitly requested historical northwest views to
confirm the west-window locations. HABS01 and Cornell's ca.1887 stable image
were directly compared, including a fixed west-plane diagnostic. The official
Cornell catalog ss:3874294 (accession15/5/3090.00156) was recovered and its
explicit public-domain statement checked; its scan and audit104 are the same
exposure. All eight west-window centers were withheld from fitting.

The southern upper slit is too far south: move its center S21.8 to S19.8,
retaining width/heights. The other seven centers agree within approximately1ft
and remain. Camera/eave uncertainty and the earlier HABS plan disagreement are
recorded in L-glessner-west-slit-2228. The copper-only bake was interrupted to
include this owner-requested correction in the next complete asset; it did not
produce a completed asset or a gate verdict. The earlier ridge-only before
master remains available. New bake and actual-asset after comparison follow.


### Completed correction review, 2026-10-16

The combined straight ridge, planar northeast copper return and west-slit
correction is baked and committed as b0286e99. The reviewed master is
`6b2cff4d0a7f41c0e5618d3df6790784126d1e7ea579312bf46a9ddd9af6391a`;
Full/Web contain 1,364,944 triangles and Light 193,697, with zero coincident
faces. All eleven canonical historical comparisons and the owner overhead
were directly reviewed. All remain `differs`; this is not final signoff.

Fresh published-app checks pass six desktop Full and six mobile Light stands,
without page/asset errors or budget breaches. All 124 credited mobile Images
tiles load. Complete pre-integration preflight passes all 895 checks. Current
dev is being integrated and its combined tree still requires its own full
gate and exact-commit desktop/mobile smoke matrix before merge. No dev merge
or deployment is claimed yet. Evidence is in the app's
`docs/RESEARCH/glessner-final-comparison-T-2228/`.

Next roof finding: Cornell and HABS01 show an exposed ventilated cupola body
which the current cap-only silhouette lacks. Its modeled louvre band sits
below the stable ridge. Reconcile body/pyramid proportions against both
photographs while retaining the corrected straight crossing; a single-camera
height estimate is not a survey. The terrace terminal/coping join, west-court
access levels, other opening/ornament and material/lighting differences also
remain open. Keep T-2228 claimed/active after this correction PR merges; do
not close the image gate on technical validation alone.
