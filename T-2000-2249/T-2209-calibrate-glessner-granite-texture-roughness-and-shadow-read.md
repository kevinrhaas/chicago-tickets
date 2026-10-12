---
id: T-2209
title: Calibrate Glessner granite texture, roughness and shadow readability
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: 2026-10-11
pr: 711
claimed_by: run 10/11/2026, 6:02:15 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-12T00:39:44Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38182481220
claimed_at: 2026-10-11T23:02:15.294Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2208; settle reopens it in T-2208's queue line when that PR merges.

**Audit item:** GA-09B • **Priority:** P1 • **Basis:** Confirmed visible gap

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Close-ups show noisy faceted stone and highly uniform joint treatment; at street distance the texture overwhelms coherent masonry. Shaded walls lose the intended rock-face relief.

Surface finish: use part A masonry to calibrate Wellesley-granite color range, normals, roughness and texture density under neutral and actual light.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Coherent joints and rock-face relief remain legible in sun and shade without triangulated sparkle.
2. No global lighting workaround conceals an incorrect normal/material response; record material provenance.

**Split coverage:** This is one bounded implementation pass from the original GA-09 package. Together with [T-2208](../T-2000-2249/T-2208-refine-glessner-street-masonry-courses-relief-and-opening-re.md), it retains the original audit acceptance:

- Long/short block distribution, course heights and opening returns align with reference zones.
- Rock-face silhouettes and joints remain legible at street distance without random triangulated sparkle.
- Review front and shaded north/west under both neutral diagnostic and actual scene lighting.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #106: [Female servants' entrance at Glessner House (photograph by George Glessner)](https://glessnerhouse.blogspot.com/2015/01/george-glessner-photographer.html) — `a18-gh-glessner-female-servants-entrance`; c. 1888–1890s; visually inspected. Rights: pending — permission requested.
- Audit #114: [Glessner, John J., Residence — Main reception hall](https://artic.contentdm.oclc.org/digital/collection/mqc/id/38063) — `a18-rba-glessner-main-hall`; undated (probably c. 1923); visually inspected. Rights: unknown — link only.
- Audit #115: [Front elevation](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060904p) — `a18-glessner-habs-photo-02`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #116: [18th Street arch](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060905p) — `a18-glessner-habs-photo-03`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #117: [Detail: gable and chimney 18th Street side](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060906p) — `a18-glessner-habs-photo-04`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** prairie, entry, north, west. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md)

Requires its first pass [T-2208](../T-2000-2249/T-2208-refine-glessner-street-masonry-courses-relief-and-opening-re.md) before shared geometry/material assumptions are changed.

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

**Unblocked 2026-10-11:** T-2208 merged (PR #707); this took its place in the queue. The block read: T-2208 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
