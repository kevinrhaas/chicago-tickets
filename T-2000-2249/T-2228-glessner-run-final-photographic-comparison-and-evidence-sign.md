---
id: T-2228
title: Glessner: run final photographic comparison and evidence sign-off
state: blocked-tech
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: null
blocked_on: T-2227 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
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
