---
id: T-3262
title: Reduce phone renderer memory without scene changes
state: review
epic: RENDERING
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-30
closed: null
pr: 1486
claimed_by: Codex phone renderer memory support 2026-10-30 10/30/2026, 7:07:11 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-30T12:07:12.875Z
decision: null
decision_answer: null
---

## Why

The owner reported mobile browser memory crashes on 2026-10-16: “I see often that in a browser on mobile we get memory crashes and it's getting jittery … keep it simple and lightweight the way we have it now” (T-2546). This is one bounded renderer allocation fix supporting T-2373, T-2377, T-2381 and T-2384. It is a performance follow-up, not new picture or geometry work.

The implementation has already been checked as part of PR1456 at native commit3746b23b: compact railway normals, omit only uniform ground confidence attributes while preserving their value, and clear dead initial spatial update ranges. Its 398.9841709/400 MiB phone result is historical evidence, not a measurement of the new standalone branch. A separate renderer-only PR can land without repeatedly conflicting with generated scene data as dev advances.

## Scope

Use the exact reviewed extraction in PR1456-standalone-phone-memory-extraction-20261030:

- renderers/web/js/railway.js
- renderers/web/js/spatial-batch.js
- tools/check_confidence_lane.mjs
- tools/test_rail_geometry_lifecycle.mjs

Add one ticket-named changelog entry and the required concise STATUS/ROADMAP notes. Do not change models, materials, asset registries, Libs, source indexes, reference views, the four building records, memory limits or measurement assertions. Preserve the original image tickets and their existing group/PR assignments.

## Acceptance

1. The fresh branch starts from actual current dev and contains only the reviewed renderer/test changes plus its own changelog/status notes; all scene/model/registry/Lib/source-index bytes remain unchanged.
2. Compact-normal, confidence and lifecycle tests pass. Mixed confidence retains its attributes; uniform values, picking, materials, grade modes and visible geometry remain equivalent within the existing precision contract.
3. Native publish/check_published and a fresh complete1904 mobile measurement on the actual standalone head pass the unchanged 400 MiB gate, with its normal source/config guards and no page/network errors. Do not relabel the earlier3746 reading as this result or repeat the meter for a greener number.
4. Run the normal source/preflight gates, the diff-selected published desktop/mobile smoke and required exact-head CI. Merge through a normal PR to dev after required checks pass. No assertion, source gate, performance threshold or workflow bypass.
5. This PR closes only this support ticket. The four original picture tickets remain responsible for their picture/source/app acceptance and normal merge/settlement.
