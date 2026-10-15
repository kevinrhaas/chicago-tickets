---
id: T-2223
title: Glessner: date and finish courtyard service stairs, rails and rear gate
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: 2026-10-14
pr: 803
claimed_by: run 10/14/2026, 5:55:49 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-15T01:16:22Z
claimed_run: null
claimed_at: 2026-10-14T22:55:49.943Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2222; settle reopens it in T-2222's queue line when that PR merges.

**Audit item:** GA-21 • **Priority:** P2 • **Basis:** Verify first, then refine

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

A service landing and rail already exist. Later records contain altered stairs and doors; the HABS plan labels a 1955 wooden stair behind the stable, which is not automatically the courtyard service stair.

Separate each stair/landing/gate in a dated component register, preserve documented early fabric and refine iron profiles, posts, hinges, thresholds and masonry piers.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. No later stair is silently inserted into 1904 and no original stair is removed because another was added in 1955.
2. Rails attach to landings and posts with plausible joints; gates connect to the enclosure.
3. Hidden or uncertain details remain replaceable and labeled.

## Evidence

- Audit #137: [Glessner House porte-cochère doors, July 1948 (Robert C. Florian)](https://glessnerhouse.blogspot.com/2023/07/glessner-house-july-1948.html) — `a18-gh-florian-1948-porte-cochere-doors`; July 1948; visually inspected. Rights: copyright — link only. Image is elevated courtyard toward stable (GX112.21), not porte-cochere doors.
- Audit #144: [2. First floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=2) — `a18-glessner-habs-sheet-2`; 1963; visually inspected. Rights: no known restrictions.
- Audit #146: [4. Section A-A - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=4) — `a18-glessner-habs-sheet-4`; 1963; visually inspected. Rights: no known restrictions.
- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** court-west, southwest. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md), [T-2201](../T-2000-2249/T-2201-glessner-close-the-south-courtyard-boundary-and-resolve-its.md)

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## T-2199 retrieval finding — 2026-10-09 UTC

Barford courtyard and side-door records remain unavailable; collection c.1945– is not a photograph-specific date, and the former 1972 upper bound was unsupported. No new evidence dates the service stairs/rails/gate to 1904. H02/H04 identify needed views and current-fabric measurements.

[Retrieval report and photographic brief](https://github.com/kevinrhaas/chicago/blob/dev/chicago/prairie_1904_v1/docs/glessner-reference-recovery.html). This is evidence handoff only; the owner scheduling hold remains in force.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

**Unblocked 2026-10-14:** T-2222 merged (PR #802); this took its place in the queue. The block read: T-2222 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)

## T-2223 execution and material handoff — 2026-10-15

The north-courtyard service stair retains its plan, ten treads and landing elevation. Ten seated posts, six continuous closed rail bars, stepped brick cheek, closed tread noses and capped piers replace the detached or incomplete joints. The separate HABS 1955 stable stair remains excluded. The paired boarded rear gate now has masonry-connected hinges, exposed pins, an open latch keeper and a stone sill 8.4 mm above the modeled drive. Exact 1904 stock, hardware and finish remain reconstructed.

The credited w_lemay service-stair reference is published through image-store PR #4. Canonical Full/web is 1,315,351 triangles; Light is 199,475 against the unchanged 200,000 limit. Asset and geometry checks pass. Ten fixed-camera published-app views pass unchanged budgets with no page errors or failed requests; every screenshot and all five historical pairs were visually reviewed. Mobile loads 124 credited image tiles and the reconstruction note.

The five whole-house historical comparisons remain differs for T-2228. The new Light stair supports preserve contacts but their clay-grain surfaces lack visible mortar courses; T-2226 must add a dedicated flat-brick joint pattern without double-gridding individually modeled bricks. T-2226 also retains member-specific wood grain on gate braces/ledges and shaded material readability. T-2227 retains the earlier scene-budget failures. These component checks are not whole-house photographic sign-off or hardware FPS results.

Implementation and validation: [PR #803](https://github.com/kevinrhaas/chicago/pull/803), head `71b78905affc892535c26edddb0a9cc31a353744`. Local preflight passes all 885 checks (356 self-tests); exact-head CI and all 18 published smoke groups are required before merge.
