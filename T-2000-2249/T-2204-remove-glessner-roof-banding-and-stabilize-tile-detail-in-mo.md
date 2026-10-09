---
id: T-2204
title: Remove Glessner roof banding and stabilize tile detail in motion
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: 2026-10-09
pr: 594
claimed_by: run 10/9/2026, 3:15:50 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-09T21:56:49Z
claimed_run: null
claimed_at: 2026-10-09T20:15:50.665Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Audit item:** GA-05B • **Priority:** P1 • **Basis:** Confirmed visible gap

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Broad banding dominates the street roof; overhead views show large smooth roof planes beside dense tile patterns. The material does not read consistently as fine overlapping clay tiles.

Renderer/distance pass using the completed physical tile layout from part A. Tune sampling, roughness, mip filtering and full/light transitions, without silently changing physical scale.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Compare moving near/street/overhead cameras in full and light modes; no broad banding, shimmer or abrupt smooth patches.
2. Record frame/draw/texture costs and retain the physical tile dimensions established in part A.

**Split coverage:** This is one bounded implementation pass from the original GA-05 package. Together with [T-2203](../T-2000-2249/T-2203-correct-glessner-roof-tile-scale-and-coverage-on-every-roof.md), it retains the original audit acceptance:

- Tile courses remain coherent across hips, turret cones and dormers, with no abrupt smooth-to-tiled patches.
- No distracting moire or broad striping during camera movement at street, courtyard and overhead distances.
- Source-backed scale and original-material interpretation recorded; no assumption that 1960s tar coating existed in 1904.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #104: [Glessner House stable/coach-house end on 18th Street, c. 1887 (Cornell A. D. White collection; as reproduced by the museum)](https://glessnerhouse.blogspot.com/2022/12/the-original-odd-quaint-queer-dutch.html) — `a18-gh-cornell-glessner-rear-c1887`; c. 1887; visually inspected. Rights: unknown — link only.
- Audit #136: [Glessner House courtyard looking west toward the stable wing, July 1948 (Robert C. Florian)](https://glessnerhouse.blogspot.com/2023/07/glessner-house-july-1948.html) — `a18-gh-florian-1948-court-to-stable`; July 1948; visually inspected. Rights: copyright — link only. Image is roof/dormers/stair turret (GX112.24), not courtyard toward stable.
- Audit #161: [Glessner House: west roof and hayloft dormer (Richard Nickel, 1966–67)](https://glessnerhouse.blogspot.com/2022/04/richard-nickel-and-glessner-house.html) — `a18-gh-nickel-west-roof-dormer`; 1966–1967; visually inspected. Rights: copyright — link only.
- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** prairie, northeast, roof, west. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md)

Requires its first pass [T-2203](../T-2000-2249/T-2203-correct-glessner-roof-tile-scale-and-coverage-on-every-roof.md) before shared geometry/material assumptions are changed.

New proposal. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Owner selection — 2026-10-09

The owner selected this ticket: “Take 2204 next.” Release only T-2204 in its existing manual group. T-2203 is complete in PR #583; all other manual holds remain in place.


## Implementation review — 2026-10-09

[PR #594](https://github.com/kevinrhaas/chicago/pull/594) targets **dev only**.
The renderer filters unresolved tile relief by projected course size and uses
trilinear mipmaps with anisotropy eight. Full and Light geometry retain their
original positions, normals, UVs, confidence and indices byte for byte; physical
6-inch tile width / 5-inch exposure, 244 hosts and 63,518 Full tiles are unchanged.
The required three-asset bake and recovery package are included in the PR.

[Immutable implementation and evidence dossier](https://github.com/kevinrhaas/chicago/blob/3705ce9be1cad82bdfa6a997fc746bd063c66016/chicago/4d/docs/RESEARCH/glessner-roof-filtering-2204/README.md)
contains before/after motion comparisons, 70 final browser captures, six detail
switches, the 36-pass published stage-8 regression, geometry checks, and the
804-check preflight receipt. Committed-range changelog and ticket-ID checks pass.
Both Full desktop and Light mobile complete without browser errors, failed
requests or budget overruns. Rendering timings are from software SwiftShader,
not hardware FPS; matched draw, triangle and texture counts are unchanged.

The copper fold remains held under T-2220. All other manual Glessner holds remain
in place. Live deployment verification will be recorded after the dev merge.


## Delivered to dev — 2026-10-09

PR #594 merged to dev as `1b7f7470`. Final integration validation passes **806
checks**, plus committed-range checks. Live Full desktop and Light mobile pass
with zero page errors, failed requests or budget overruns; served renderer and
Full/Light asset hashes match the reviewed implementation. Main was not promoted.

[Live verification receipts and screenshots](../evidence/glessner-roof-filtering-2204-live-2026-10-09/README.md).
The other manual holds, including T-2220, remain unchanged.
