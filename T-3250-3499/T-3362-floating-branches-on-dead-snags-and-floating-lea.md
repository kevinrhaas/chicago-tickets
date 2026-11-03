---
id: T-3362
title: Floating branches on dead snags and floating leaf clusters on grown trees (1812, 1835)
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-03
closed: 2026-11-03
pr: 1678
claimed_by: run 11/3/2026, 3:42:28 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-03T22:39:25Z
claimed_run: null
claimed_at: 2026-11-03T21:42:36.748Z
decision: null
decision_answer: null
---

Kevin, 2026-11-03: "i see floating branches on a tree in 1835" (a dead snag on the South Water
Street bank, today 375 W Wacker Dr, NNW 28 ft up) and "there are floating leaf clusters" (1812,
the Kinzie cottonwoods at today 420 N Michigan Ave, looking ESE).

Causes, in tree-model.js:
- deadSkeleton drops or shortens a snag's scaffolds but kept the order-2 branches that grew on
  the lost part (about 4 a snag, up to 8 m in the air); it also cut each stem at its last node
  under the break, so limbs that left the stem in the last segment hung free.
- growSkeleton's shell clumps are laid on the crown envelope with no wood under them (a median
  1.8 of their own widths from the nearest twig, up to 7.6).
- Scaffolds that leave above the bole's top started on the bole's axis, up to 0.7 m off the
  leaning leader.

**Acceptance:**
- No snag or log limb starts off kept wood (0 orphans over every timber species x 40 seeds).
- No shell clump stands further than 0.6 of its radius from its nearest twig; no clump in any
  crown is isolated (no neighbour within 2.2 r and no wood in reach).
- Crown reach (p95 leaf radius) within 5% of before; no added triangles.
- Before/after at Kevin's two views, desktop.
