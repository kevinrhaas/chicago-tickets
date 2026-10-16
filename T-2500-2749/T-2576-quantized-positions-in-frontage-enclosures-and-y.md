---
id: T-2576
title: Quantized positions in frontage, enclosures and yard: Int16x4 relative to each chunk with the offset and scale in its matrix, every probe and spatialBatch reader made to apply it, so the four layers reach T-2549's 40 %
state: claimed
epic: RENDERING
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 4:10:06 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38966866392
claimed_at: 2026-10-16T21:10:06.180Z
decision: null
decision_answer: null
---

Quantized positions in frontage, enclosures and yard: Int16x4 relative to each chunk with the offset and scale in its matrix, every probe and spatialBatch reader made to apply it, so the four layers reach T-2549's 40 %.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What T-2569 left (2026-10-16, PR #867)

- T-2569 compacted normals (Int8x4), linear tones (Uint16x4) and the yard atlas uv (Uint16x2) with no shader change: frontage 52 -> 40 B a vertex, enclosures 28 -> 20, yard 56 -> 40 (207.4 -> 154.7 MB across every vertex the three build on `/1835/`, -25 %). The `/1835/` phone fell 795.7 -> 745.5 MB resident.
- Position is now the largest stream in all three (12 of 20-40 B). Int16x4 normalized relative to the chunk (8 B, a stride multiple of 4) takes about another 19 MB off the three.
- What reads positions as world metres and would have to apply the matrix: the smoke's probes on these layers (`smoke_renderer.mjs`, e.g. the yard's pile, outbuilding and shed bounds), `spatial-batch.js` (cell keys from `position.getX`), `createFarWalkTops` in `frontage.js`, `view-occlusion.js` `backingTriangles` (it already takes a matrix), and `far-merge.js` (already applies the relative matrix). `filterPlankGaps` offsets vertices by `aChiPlankGap` in local metres, so a scale in the matrix would scale the gap: keep the scale uniform and divide the gap by it, or keep the gap in world units.
- `_confidence` (0 / 0.5 / 1) stays float32: no 8-bit normalized value holds 0.5, and the shader bands on it.

**Acceptance:** positions in the three layers at 8 B or less; frontage + enclosures + yard GPU geometry on the `/1835/` phone down at least 40 % from dev before T-2569 (207.4 MB by stride); pixel parity at the T-2569 anchors at both viewports; the smoke's probes and every pick unchanged.
