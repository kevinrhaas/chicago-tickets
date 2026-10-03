---
id: T-2015
title: Replace faceted trees and blocky flora with realistic procedural vegetation
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: null
claimed_by: run 10/3/2026, 12:02:14 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-03T05:02:15.000Z
decision: null
decision_answer: null
---

Replace faceted trees and blocky flora with realistic procedural vegetation.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 216 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner explicitly requests filing and immediately implementing the shared vegetation upgrade, with checkpoint pushes and a gated merge to dev.

## Owner brief

The two supplied screenshots show solid polygonal crowns and rectangular green understory cards. Bring trees and all shared flora toward the material, texture-scale and silhouette quality of Glessner House. Use deterministic procedural variation, preserve the evidenced species, placement and July phenology, and keep browser rendering practical. Owner authorizes parallel work, browser validation, checkpoint pushes and merging to dev.

## Acceptance

- Replace near-tree closed polygon crowns with open, detailed foliage silhouettes and visible tapered branching; retain distinct species forms and deterministic per-tree variation.
- Give wood convincing bark grain and foliage fine-scale leaf detail, readable underside lighting and coherent wind; no rectangular leaf surfaces in near shrubs/forbs.
- Apply the shared rendering improvements wherever the existing trees/flora modules are consumed; do not invent species, historical plantings or flowers outside July eligibility.
- Compare fixed desktop and mobile views plus tree and understory close-ups. Record triangles/draw calls, startup cost and material/shader errors; preserve the light detail tier as the low-end floor.
- Pass the relevant project gate and published smoke, document reconstruction liberties and limitations, push recoverable checkpoints, and merge the reviewed PR into dev.

## Recovery

Code branch: `steward/photographic-flora` in `kevinrhaas/chicago`. Attached evidence: user uploads `image(5).png` and `image(6).png` in this conversation. Implementation and render evidence will be checkpointed on the branch.
