---
id: T-3654
title: Build the 1871 citywide context baseline with varied buildings, streets and bridges
state: review
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: 2198
claimed_by: continuing the same 1871 integration 11/18/2026, 11:06:18 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-18T17:06:19.857Z
decision: null
decision_answer: null
---

Build the 1871 citywide context baseline with varied buildings, streets and bridges.

## Owner request

2026-11-18: “Go ahead and lay the foundations to start working through 1871 and then built it out entirely perfectly photographic cinematic quality.” Scope clarified: “build the entire city as a context city to start with general buildings with basic textures that look ok but all the buildings in the city have variation and are correct in form and style for the business or residential area of the city, built the entire city map with a baseline city.” Also: “And of course the streets and walks etc, bridges other structure.”

## Acceptance

A visitor can enter an explicit pre-fire 1871 scene and see a citywide baseline across the documented/reconstructed municipal extent, with varied period commercial, residential and industrial building forms, streets, walks, river/lake edges, bridges and supporting infrastructure. Ordinary building placement and unmeasured fabric are visibly identified as reconstructed context; no later-year terrain, named houses or people silently leak into the scene. Context geometry is generated reproducibly as glTF plus JSON from a sourced plan, with district variation and detail levels that support street-level and citywide cameras. Source/date/rights limitations are exposed on the scene or context card. Cinematic camera views show the actual rendered city. Validate both desktop and mobile, full project checks, published mirror, and rendering/performance checks appropriate to the change.

This acceptance is the explicitly requested citywide context baseline, not a claim that every historical parcel or facade has been identified, or that the finished photographic-quality city is complete. The baseline is the foundation into which researched named structures and higher-detail materials can be substituted.

## Scope

1871 scene/epoch selection, context generation, plan/source records, portable building and infrastructure assets, city exploration/cinematic views, and a link from the pre-fire research viewer if needed. Preserve existing 1812, 1835 and 1904 behavior. No production dispatch.


## Validation and recovery checkpoint — 2026-11-18

Implementation and research are pushed on `steward/t3654-1871-city-baseline`, current checkpoint `8d59e79cd657f58f483533246973e0e1c00ebf51`, draft PR #2198 into dev. `docs/measurements/t-3654-validation-checkpoint.json` records resumable status and run IDs. Production promotion is not part of this task.

Durable evidence: [chicago-evidence:evidence/t3654-1871-city-2026-11-18/](https://github.com/kevinrhaas/chicago-evidence/tree/0e0afc408bbeda75cbe7c687a2bc09342e46d538/evidence/t3654-1871-city-2026-11-18), commit `0e0afc408bbeda75cbe7c687a2bc09342e46d538`. The archive contains 85 files with a verified SHA256 manifest: final city mobile/desktop runs, focused 1812 probe, shared-entry proofs, sky diagnostics, coordinate audit and partial-gate receipts.

The final 1871 runtime (`ae259f9a5d`, unchanged by the metadata checkpoint) passes both viewports/all three tiers, all 22 bridges in both directions, 597 quay approaches, streets/walks, collision and source/liberty checks with zero app/page/resource errors. The focused 1812 entry/walking/canvas probe also passes both widths. Source part 4/16 passes 89 steps on `8d59e79cd6`, clearing the two repaired validator failures; preflight part 2/16 and PR-only checks also passed. These are partial source receipts, not a full source or full legacy gate. Complete CI remains required before merge.

The modern-intersection cross-check requested by the owner is recorded in `t-3654-today-registration-audit.json`: nine City-centreline/OSM targets agree within 2.023 m RMS; fourteen inherited targets match exactly. Older-year Today lookup shifts are not copied into 1871, and the historical-map residuals remain separately declared.
