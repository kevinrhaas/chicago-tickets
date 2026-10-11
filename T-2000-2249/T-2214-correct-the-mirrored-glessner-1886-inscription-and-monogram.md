---
id: T-2214
title: Correct the mirrored Glessner 1886 inscription and monogram
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
blocked_on: T-2213 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2213; settle reopens it in T-2213's queue line when that PR merges.

**Audit item:** GA-13A • **Priority:** P1 • **Basis:** Confirmed visible defects

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

The close north-gable view confirms the 1886 inscription is mirrored from outside. The front tympanum and ornamental band exist, but relief, edge wear and varied capitals need close-range fidelity.

Bounded visible correction to north-gable inscription orientation, placement and relief; check monogram handedness against HABS photo #117.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. 1886 reads correctly from outside in a repeatable close-up and street view.
2. Monogram, date surround and relief agree with source; no unrelated front carving changes.

**Split coverage:** This is one bounded implementation pass from the original GA-13 package. Together with [T-2215](../T-2000-2249/T-2215-finish-glessner-entry-tympanum-ornamental-band-and-varied-ca.md), it retains the original audit acceptance:

- Ornament remains recognizable in matched close-ups, with correct silhouette and varied capital patterns.
- Inscription reads correctly from outside; record the check.
- No added ornament based solely on rejected/preliminary drawings.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #115: [Front elevation](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060904p) — `a18-glessner-habs-photo-02`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #117: [Detail: gable and chimney 18th Street side](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060906p) — `a18-glessner-habs-photo-04`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #135: [Glessner, John J., Residence — removal of the Graphic Arts Technical Foundation sign (Richard Nickel)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/71832) — `a18-rba-nickel-glessner-sign-removal`; 1950s–1960s; visually inspected. Rights: copyright — link only.
- Audit #156: [6. Front (east) elevation - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=6) — `a18-glessner-habs-sheet-6`; 1965; visually inspected. Rights: no known restrictions.

**Current audit views:** entry, prairie, north, detail:north-gable. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2198](../T-2000-2249/T-2198-glessner-repair-source-identity-captions-and-evidence-famili.md), [T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md), [T-2208](../T-2000-2249/T-2208-refine-glessner-street-masonry-courses-relief-and-opening-re.md), [T-2209](../T-2000-2249/T-2209-calibrate-glessner-granite-texture-roughness-and-shadow-read.md)

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library
