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

## Implementation checkpoint — 2026-10-03

The owner explicitly authorized measured budget raises during implementation. T-2014 / chicago PR #328 owns distant shrub visibility and forward-walk continuity. T-2015 preserves its geometry interface and will test the composed rendering without replacing that work.

Implemented in the work branch: open species-family leaf sprays, deterministic leaf and bark atlases, curved/tapered branches and near understory, matching tree wind/cutout/confidence shadows, and readable outward-facing trunk surfaces. The first integrated browser pass exposed a vertex-attribute limit in ground flora; the shader data is now packed into existing attribute slots and is being revalidated. Isolated tree review passes 180 RNG/finite/light-cost cases with zero shader errors. Full scene budget measurements, final before/after views and required gates remain in progress. Do not treat this as accepted photographic quality or a merged delivery yet.

### Saved code checkpoint

[Chicago e9c02d7](https://github.com/kevinrhaas/chicago/commit/e9c02d727d7e6acaaa447ae66b302deb49f2b5a7) saves the implementation, reproducible review tools, before-scene images and bark/tree closeups on `steward/photographic-flora`. The source gate passes all 750 steps. The packed foliage shader passes all four actual-scene desktop views with zero page/console errors. Final budgets, mobile smoke and T-2014 composed walk remain under verification; the ticket stays claimed.
