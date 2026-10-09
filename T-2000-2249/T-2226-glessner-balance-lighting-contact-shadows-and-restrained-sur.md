---
id: T-2226
title: Glessner: balance lighting, contact shadows and restrained surface aging
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
