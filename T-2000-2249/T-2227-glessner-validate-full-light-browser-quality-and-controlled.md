---
id: T-2227
title: Glessner: validate full/light browser quality and controlled performance
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
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Audit item:** GA-25 • **Priority:** P1 • **Basis:** Completion gate

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

This audit checked 1600×1000 full desktop stills only. Captures booted without page errors or failed requests and reported within-budget draw/triangle counts; paused animation means FPS=0 is not a performance measurement.

Reuse the metric/browser contract for full and light assets, motion, desktop and mobile. Test distance transitions, texture filtering, clipping, picking and actual frame timing after visual work.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Repeat front/oblique/rear/roof views at 1280×800 desktop and 390×780 mobile, plus close details.
2. Measure moving-frame performance on a declared device; keep agreed draw/triangle/texture/load budgets and owner dark-glass default.
3. No missing detail at LOD transitions, flicker, errors, failed assets or UI-dependent rendering changes.

## Evidence

- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** prairie, northwest, courtyard, roof, entry, porte. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2201](../T-2000-2249/T-2201-glessner-close-the-south-courtyard-boundary-and-resolve-its.md) through [T-2226](../T-2000-2249/T-2226-glessner-balance-lighting-contact-shadows-and-restrained-sur.md) as applicable

Reuse T-1843 acceptance framework; do not create parallel test infrastructure. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.
