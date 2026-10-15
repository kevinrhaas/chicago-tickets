---
id: T-2224
title: Glessner: finish courtyard paths, edging, lawn and drainage
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
claimed_by: run 10/14/2026, 8:18:31 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-15T01:18:32.018Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2223; settle reopens it in T-2223's queue line when that PR merges.

**Audit item:** GA-22 • **Priority:** P1 • **Basis:** Confirmed simplification; surface chronology required

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

The court is a flat lawn and plain gray strip. Later photographs include changed surfaces; HABS records institutional paving for parking.

Reconstruct the 1904 path/drive alignment from early evidence; refine hard surface texture, lawn edging, grades and drainage. Document any inferred paving type rather than copying 1948/1960s surfaces.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. No grass in carriage routes or at building thresholds.
2. Lawn/path transitions and perimeter edging agree with the chosen dated evidence.
3. Surface choice is separately sourced from geometry; later parking pavement excluded.

## Evidence

- Audit #118: [Interior court](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060907p) — `a18-glessner-habs-photo-05`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #137: [Glessner House porte-cochère doors, July 1948 (Robert C. Florian)](https://glessnerhouse.blogspot.com/2023/07/glessner-house-july-1948.html) — `a18-gh-florian-1948-porte-cochere-doors`; July 1948; visually inspected. Rights: copyright — link only. Image is elevated courtyard toward stable (GX112.21), not porte-cochere doors.
- Audit #144: [2. First floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=2) — `a18-glessner-habs-sheet-2`; 1963; visually inspected. Rights: no known restrictions.
- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** court-east, court-west, roof. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md), [T-2201](../T-2000-2249/T-2201-glessner-close-the-south-courtyard-boundary-and-resolve-its.md), [T-2202](../T-2000-2249/T-2202-glessner-restore-prairie-frontage-curbs-thresholds-and-groun.md), [T-2218](../T-2000-2249/T-2218-glessner-reconstruct-the-curved-courtyard-hall-steps-and-che.md)

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## T-2199 retrieval finding — 2026-10-09 UTC

No pre-1904 courtyard surface/edging photograph was recovered. The ownership map (#164) is a 1972 parcel/owner diagram, not a courtyard paving survey. The arterial sketch (#165) is an unbuilt later proposal, now explicitly excluded and unknown/link-only; federal custody does not clear contributed-drawing rights.

[Retrieval report and photographic brief](https://github.com/kevinrhaas/chicago/blob/dev/chicago/prairie_1904_v1/docs/glessner-reference-recovery.html). This is evidence handoff only; the owner scheduling hold remains in force.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

## T-2223 interface handoff — 2026-10-15

[Service-access PR #803](https://github.com/kevinrhaas/chicago/pull/803) retains the courtyard drive at local datum +36.6 mm and lawn at +15.2 mm. The new rear-gate sill top is +45 mm, with the gate leaf beginning at +57 mm. The service stair retains ten treads and a +1.8288 m landing. Reconcile new paths and grades against the actual drive, sill, stair noses and terrace foot; terrain height alone misses the separate drive mesh. Keep grass clear of those access routes and do not import the 1946 parking conversion.

**Unblocked 2026-10-14:** T-2223 merged (PR #803); this took its place in the queue. The block read: T-2223 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
