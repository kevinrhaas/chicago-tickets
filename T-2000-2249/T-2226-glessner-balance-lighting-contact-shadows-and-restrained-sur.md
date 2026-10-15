---
id: T-2226
title: Glessner: balance lighting, contact shadows and restrained surface aging
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: 813
claimed_by: run 10/15/2026, 1:03:31 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-15T06:03:31.866Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2225; settle reopens it in T-2225's queue line when that PR merges.

**Audit item:** GA-24 • **Priority:** P1 • **Basis:** Confirmed rendering gap; calibration required

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Bright front texture and very dark blue-shaded north/west surfaces make materials read inconsistently. The house/ground interface lacks convincing variation.

Compare neutral material diagnostics with actual July scene light; tune ambient contribution, exposure, normals, contact shadows and roughness. Add evidence-based soot/runoff/dirt in joints and sheltered zones, with the 17-year building age in mind.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Stone relief stays readable in shade without flattening sunny facades or crushing blacks.
2. Contact shadows anchor the building, steps and enclosure without halos or detached dark bands.
3. No baked double shadows, random grunge or deterioration copied from the neglected mid-century house.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #115: [Front elevation](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060904p) — `a18-glessner-habs-photo-02`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #118: [Interior court](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060907p) — `a18-glessner-habs-photo-05`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** prairie, north, west, courtyard. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2203](../T-2000-2249/T-2203-correct-glessner-roof-tile-scale-and-coverage-on-every-roof.md), [T-2204](../T-2000-2249/T-2204-remove-glessner-roof-banding-and-stabilize-tile-detail-in-mo.md), [T-2208](../T-2000-2249/T-2208-refine-glessner-street-masonry-courses-relief-and-opening-re.md), [T-2209](../T-2000-2249/T-2209-calibrate-glessner-granite-texture-roughness-and-shadow-read.md), [T-2210](../T-2000-2249/T-2210-glessner-calibrate-courtyard-brick-and-limestone-as-distinct.md), [T-2213](../T-2000-2249/T-2213-glessner-give-dark-glazing-believable-exterior-visible-depth.md), [T-2220](../T-2000-2249/T-2220-glessner-refine-copper-roof-panels-seams-and-weathering.md), [T-2224](../T-2000-2249/T-2224-glessner-finish-courtyard-paths-edging-lawn-and-drainage.md)

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

## T-2223 material findings — 2026-10-15

The final Full/Light browser screenshots in [PR #803](https://github.com/kevinrhaas/chicago/pull/803) expose two material follow-ups. Light's simplified stair cheek and piers retain the geometry contacts but read as smooth clay because the existing brick normal map contains clay grain, not mortar courses. Supply a dedicated flat-brick joint pattern for these faces without double-gridding individually modeled bricks or repainting the shared K01 palette. Gate ledges and diagonal braces also need grain aligned to the member. Preserve the owner's granite tint and dark glass, the same physical contacts and the unchanged 200,000-triangle Light limit. Both are explicitly recorded as pending material work, not photographic parity.

**Unblocked 2026-10-15:** T-2225 merged (PR #805); this took its place in the queue. The block read: T-2225 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
