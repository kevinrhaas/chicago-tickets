---
id: T-2220
title: Glessner: refine copper roof panels, seams and weathering
state: blocked-owner
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
blocked_on: Owner-directed manual hold (2026-10-09 UTC): commented Glessner group below portable people; activate only the single ticket explicitly selected by the owner.
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

**Audit item:** GA-18 • **Priority:** P1 • **Basis:** Owner-confirmed lifted/folded copper defect plus detail simplification

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

The copper bows are recognizable but read as large uniform green surfaces with sparse seam detail.

First repair the lifted and folded copper at the inside northeast courtyard corner, then refine panel division, folded joints, edge rolls, flashing and roughness variation; document the uncertainty of 1904 patina. Preserve sound continuous roof geometry and shoulder joins, but correct the specific lifted panel documented below.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Seam layout and edge profiles agree with available photographs; no arbitrary oversized panels.
2. Patina varies plausibly with water flow without uniform green paint or unsupported black-and-white color sampling.
3. No seams lifted off surfaces, overlaps or breaks at adjacent roofs.
4. At the inside northeast courtyard corner, copper must lie flush with the intended underlying roof planes. Remove the floating lower edge, exposed dark wedge and spurious diagonal fold shown in the owner's screenshot. No unsupported tent/canopy surface or twisted quad; retain only real roof intersections and bounded sheet/seam thickness.
5. Verify the repaired corner from ground level, the supplied courtyard angle, a close oblique and overhead in Full and Light/Balanced. Add a geometric check for sheet-to-host distance and coherent planar triangulation, plus matched before/after browser captures. A colour or shading change alone cannot satisfy this defect.

## Evidence

- Audit #118: [Interior court](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060907p) — `a18-glessner-habs-photo-05`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #136: [Glessner House courtyard looking west toward the stable wing, July 1948 (Robert C. Florian)](https://glessnerhouse.blogspot.com/2023/07/glessner-house-july-1948.html) — `a18-gh-florian-1948-court-to-stable`; July 1948; visually inspected. Rights: copyright — link only. Image is roof/dormers/stair turret (GX112.24), not courtyard toward stable.
- Audit #151: [North elevation — inclined: left stereopair](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060916p) — `a18-glessner-habs-photo-14`; 1965; visually inspected. Rights: no known restrictions.
- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** courtyard, roof. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md), [T-2206](../T-2000-2249/T-2206-glessner-validate-roof-dormer-and-courtyard-bay-proportions.md)

Protect T-2157 and T-2183 copper continuity. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Owner-confirmed copper attachment defect — 2026-10-09 UTC

> You can see the copper cladding looks like it’s coming off the roof in the inside north east corner of the courtyard and it has a fold in it. It should be flat with the roof.

The owner supplied a cropped model screenshot while T-2203 was in progress.
The broad green panel over the northeast courtyard's upper windows has a lifted
lower edge and dark open wedge above the red roof, with a diagonal fold across
its face. This is explicitly added to **this existing copper ticket**, not a
new duplicate. See the [reproduced view and capture provenance](../evidence/glessner-copper-corner-2026-10-09/README.md)
and [full courtyard capture](../evidence/glessner-copper-corner-2026-10-09/reproduced-courtyard.png).

Investigate the copper corner/shoulder connector's control points, coplanarity,
triangulation and offset from its host in `masonry_house_v4_detail.py` and the
courtyard roof helper. The cause has not yet been established. Earlier T-2157 /
T-2183 continuity work is context, not a requirement to preserve this artifact.
Coordinate with T-2206's proportions audit; once this ticket is selected, the
local attachment defect may be repaired without waiting for an unrelated whole
roof proportion study. Keep the corrected clay module from T-2203 intact.

**Scheduling:** Owner asked to record the fix, not to switch the active task.
T-2220 remains `blocked-owner`, with its queue row commented in the existing
Glessner group below portable people. T-2203 remains the active implementation.
