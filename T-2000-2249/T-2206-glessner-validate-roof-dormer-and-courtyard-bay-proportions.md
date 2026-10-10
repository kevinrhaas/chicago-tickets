---
id: T-2206
title: Glessner: validate roof, dormer and courtyard-bay proportions before further reshaping
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: 604
claimed_by: interactive proportion audit 10/9/2026, 6:58:42 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-09T23:58:42.785Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Audit item:** GA-07 • **Priority:** P1 • **Basis:** Verify first — no established dimensional defect

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Complex dormer flares, bay roof shoulders and service-roof intersections need camera-matched checks. Recent roof corrections already shipped.

Measure roof pitches, dormer positions, hood flares, turret/bay height and copper shoulder profiles against as-built records. Change geometry only for documented residual errors.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Produce dimension/control-point table and matched comparisons.
2. Retain correct work; list any necessary corrections individually with source confidence.
3. Do not import the preliminary central gable, watercolor conservatory or fountain.

## Evidence

- Audit #104: [Glessner House stable/coach-house end on 18th Street, c. 1887 (Cornell A. D. White collection; as reproduced by the museum)](https://glessnerhouse.blogspot.com/2022/12/the-original-odd-quaint-queer-dutch.html) — `a18-gh-cornell-glessner-rear-c1887`; c. 1887; visually inspected. Rights: unknown — link only.
- Audit #118: [Interior court](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060907p) — `a18-glessner-habs-photo-05`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #136: [Glessner House courtyard looking west toward the stable wing, July 1948 (Robert C. Florian)](https://glessnerhouse.blogspot.com/2023/07/glessner-house-july-1948.html) — `a18-gh-florian-1948-court-to-stable`; July 1948; visually inspected. Rights: copyright — link only. Image is roof/dormers/stair turret (GX112.24), not courtyard toward stable.
- Audit #144: [2. First floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=2) — `a18-glessner-habs-sheet-2`; 1963; visually inspected. Rights: no known restrictions.
- Audit #145: [3. Second floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=3) — `a18-glessner-habs-sheet-3`; 1963; visually inspected. Rights: no known restrictions.
- Audit #146: [4. Section A-A - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=4) — `a18-glessner-habs-sheet-4`; 1963; visually inspected. Rights: no known restrictions.
- Audit #161: [Glessner House: west roof and hayloft dormer (Richard Nickel, 1966–67)](https://glessnerhouse.blogspot.com/2022/04/richard-nickel-and-glessner-house.html) — `a18-gh-nickel-west-roof-dormer`; 1966–1967; visually inspected. Rights: copyright — link only.

**Current audit views:** west, courtyard, roof. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2198](../T-2000-2249/T-2198-glessner-repair-source-identity-captions-and-evidence-famili.md), [T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md)

Protect T-1805/T-1830/T-1833/T-1999/T-2016/T-2157/T-2172/T-2183. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## T-2199 retrieval finding — 2026-10-09 UTC

The recovered NRHP elevated image (#166, 1972, photo/form pp.30–31) shows roof masses at limited detail; it does not resolve hidden junctions or authorize the 1904 roof shape. #046 is the same unbuilt central-gable design family, excluded. Prioritized elevated roof and courtyard east/west requests are in the new brief; T-2231 remains the current landed roof correction.

[Retrieval report and photographic brief](https://github.com/kevinrhaas/chicago/blob/dev/chicago/prairie_1904_v1/docs/glessner-reference-recovery.html). This is evidence handoff only; the owner scheduling hold remains in force.

## T-2200 measurement handoff — 2026-10-09 UTC

T-2200 provides fixed camera/source-pick/report JSON and a frozen-camera candidate command. All eight core comparisons retain errors. In particular north-inclined withheld RMS is 125.3 px, courtyard-east 53.7 px; these combine geometry, camera and correspondence uncertainty and must not be treated as direct construction dimensions. Most fitted heights touch assumed bounds. Review correspondences and silhouettes before changing T-2235 roof geometry; do not refit cameras silently to improve scores. See `docs/RESEARCH/glessner-camera-baseline/README.md` in the code repository. This is a finding only; the owner hold remains.

## Coordination — owner report, 2026-10-09 UTC

The lifted/folded copper at the inside northeast courtyard corner is now an
explicit repair in [T-2220](T-2220-glessner-refine-copper-roof-panels-seams-and-weathering.md),
with the owner's screenshot finding and a reproduced view. Use that ticket for
the local cladding-to-host attachment defect; do not duplicate it in this broader
proportions audit. Both tickets remain on their manual holds.

## Owner release — 2026-10-09 UTC

> Take 2206 next

Only this ticket is released. T-2205 merged to dev in PR #601; all other manual holds remain. Audit the current assets with frozen T-2200 cameras and retain prior corrections unless a residual error is documented.
