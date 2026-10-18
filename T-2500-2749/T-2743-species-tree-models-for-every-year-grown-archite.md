---
id: T-2743
title: Species tree models for every year: grown architecture per species, species bark and true-size leaves, built once and instanced with three detail levels (1835, 1812 timber and the 1904 parkway elms)
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-17
closed: 2026-10-18
pr: 1003
claimed_by: run 10/17/2026, 2:20:55 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T10:48:07Z
claimed_run: null
claimed_at: 2026-10-17T19:20:55.979Z
decision: null
decision_answer: null
---

Species tree models for every year: grown architecture per species, species bark and true-size leaves, built once and instanced with three detail levels (1835, 1812 timber and the 1904 parkway elms).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 150 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner asked in the project thread 'Trees in 1812 and 1835' (2026-10-17) for this work; the queue is at its ceiling

**Acceptance:**
- Every tree species the zone records and plantings name is grown from its own architecture in `renderers/web/js/tree-model.js` (crown envelope, fork, scaffold angle, limb rise or sag, twig droop), with bark and leaf tiles of its own from `tools/generate_tree_atlas.py` (procedural, no third-party photograph), leaves at true size.
- Trees are built once per species variant and drawn instanced, with near, mid and far levels of one grown tree; the 1904 parkway elms use the same models.
- Measured before and after on dev's own tools: 1835 and 1812 phone and desktop memory (`tools/measure_memory.mjs`), 1835 desktop frame time (baseline taken on dev first, since dev is already red there), 1904 desktop spawn triangles. None gets worse; the saving is what T-2744 and T-2745 spend on more trees.
- The architecture rules are written up as one numbered liberty; timber census baselines rebaselined with the reason.
- Research: /mnt/project-files/trees-1812-1835/research-report.md (project thread 'Trees in 1812 and 1835').
