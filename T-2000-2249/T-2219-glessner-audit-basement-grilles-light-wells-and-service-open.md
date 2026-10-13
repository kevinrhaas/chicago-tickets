---
id: T-2219
title: Glessner: audit basement grilles, light wells and service openings
state: open
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
blocked_on: null
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

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2218; settle reopens it in T-2218's queue line when that PR merges.

**Audit item:** GA-17 • **Priority:** P2 • **Basis:** Verification and detail completion

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Front stone grids already exist. Courtyard dark barred openings appear deep/tall in current views and need source-based proportion checks.

Inventory lattice/grille dimensions, setbacks, wells, basement vents, doors and drainage edges. Distinguish window, vent and passage openings; refine only demonstrated differences.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Every basement opening is cross-referenced to elevation/plan and assigned a type.
2. No missing well bottoms, see-through voids or inconsistent grille thickness.
3. Any courtyard opening resize follows matched evidence, not a visual guess.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #106: [Female servants' entrance at Glessner House (photograph by George Glessner)](https://glessnerhouse.blogspot.com/2015/01/george-glessner-photographer.html) — `a18-gh-glessner-female-servants-entrance`; c. 1888–1890s; visually inspected. Rights: pending — permission requested.
- Audit #118: [Interior court](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060907p) — `a18-glessner-habs-photo-05`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #144: [2. First floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=2) — `a18-glessner-habs-sheet-2`; 1963; visually inspected. Rights: no known restrictions.
- Audit #148: ["Granite block old home of late J. J. Glessner at 1800 Prairie av." (Chicago Tribune, January 31, 1965)](https://chicagology.com/chicagostreets/prairieavenue/1800prairie/) — `a18-cgy-1800-glessner-tribune-1965`; January 31, 1965; visually inspected. Rights: copyright — link only.
- Audit #156: [6. Front (east) elevation - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=6) — `a18-glessner-habs-sheet-6`; 1965; visually inspected. Rights: no known restrictions.

**Current audit views:** entry, north, courtyard, court-west. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md), [T-2208](../T-2000-2249/T-2208-refine-glessner-street-masonry-courses-relief-and-opening-re.md), [T-2209](../T-2000-2249/T-2209-calibrate-glessner-granite-texture-roughness-and-shadow-read.md), [T-2210](../T-2000-2249/T-2210-glessner-calibrate-courtyard-brick-and-limestone-as-distinct.md)

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

## Owner-reported north service-opening / west-gable junction, 2026-10-13

The owner supplied a pink-circled model screenshot and the corresponding crop of HABS photograph 1, and asked that this be recorded after T-2470 lands:

> we have half a door and half a window and the gable roof from the west wing does not intersect correctly with the north wing

This is the north service doorway immediately east of the west/stable gable on 18th Street, not the east-wing round tower corrected by T-2470. The model's projecting west-gable masonry covers approximately half the doorway and the upper window. A dark triangular roof fragment appears at the junction. The photograph shows the full service door, its step, the full upper window, and a continuous roof/gable junction beside the downpipe.

Extend this service-openings ticket to correct the shared junction that clips those two apertures. First reconcile the wall planes, aperture extents and intersecting roof pitches with HABS 01 and sheets 2–4; do not simply shift the openings to hide an overlap or copy later stable alterations into 1904. Preserve the accepted T-2470 north-east gable/tower correction and the measured stable footprint.

Additional acceptance:

1. The complete service doorway and upper window remain visible from the matched HABS 01 camera and a close street view. Reveal depth, lintels, sill and threshold follow the photograph within explicitly stated reconstruction bounds.
2. The west/stable gable meets the north range roof cleanly, with no roof triangle, gap or overlapping wall covering an opening. Preserve the downpipe's relationship to the junction and inspect both sides and an overhead view.
3. Rebuild Full and Light, compare before/after in the actual desktop and phone renderer, and run the applicable roof/aperture checks and required repository/browser gates. Record any new dimensions as inferred or reconstructed with their evidence.

Reference: HABS IL-1015 photograph 1, Cervin Robinson, 23 July 1963, https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060903p (`habs_glessner_photo_01_nw_1963`, no known restrictions). The owner's two comparison images were reviewed directly in the project conversation. This finding is recorded for later work; this update does not claim or rerank T-2219.

**Owner continuation, 2026-10-13:** "Keep going", immediately after the T-2470 merge and recorded T-2219 service-door/window/roof finding. T-2219 is selected next; the serialized order is T-2219 → T-2217 → T-2218 → T-2220. This supersedes the earlier scheduling dependency only.
