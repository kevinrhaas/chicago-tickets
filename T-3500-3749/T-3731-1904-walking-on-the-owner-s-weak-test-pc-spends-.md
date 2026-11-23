---
id: T-3731
title: 1904 walking on the owner's weak test PC spends about 44 ms a frame preparing structure draw lists one instance at a time
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-22
closed: 2026-11-22
pr: 2310
claimed_by: run 11/22/2026, 8:22:37 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-23T05:03:03Z
claimed_run: null
claimed_at: 2026-11-23T02:22:38.694Z
decision: null
decision_answer: null
---

1904 walking on the owner's weak test PC spends about 44 ms a frame preparing structure draw lists one instance at a time.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Measured with `?device=weak` at 1920x1080 (Balanced, the tier the owner's i5-10400 / UHD 630 boots), walking south down Prairie from 1600: 129,844 BatchedMesh instances in 837 batches, 89,524 of them structure pieces and cells in 712 batches. The structures' draw-list hooks cost about 22 ms in the colour pass and 22 ms in the sun's pass of a 73 ms frame: three's per-instance cull and sort (matrix read, packed-sphere decode, transform, six planes, every instance, every pass), shadow-casters.js's own loop over every piece, and batch-coalesce.js remaking its scratch arrays as lists grow.
- Done when a structure batch's bounds are read once and culled a block at a time, the structures' hook time on the same walk is at most half of what it was, and the draw lists are identical: the same frame drawn by the old path and the new gives the same multi-draw entries in the same order for every batch in every pass. People, horses and carriages are untouched. The frame-governor resolution cap is another PR's.
