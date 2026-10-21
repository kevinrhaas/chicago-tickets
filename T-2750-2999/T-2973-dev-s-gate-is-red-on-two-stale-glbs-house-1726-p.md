---
id: T-2973
title: dev's gate is red on two stale GLBs: house_1726_prairie__as_mapped_1904.glb and house_1730_prairie__as_mapped_1904.glb no longer match their inputs (T-2934 #1154 moved them onto K01, then T-2931 changed the K01 recipe and re-emitted every K01 asset but these two, which were not yet on its base); re-bake both on the merged recipe (tools/bake.sh --only house_1726_prairie, house_1730_prairie) so validate.py's stale check passes
state: claimed
epic: SOUTH_TIME
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-20
closed: null
pr: null
claimed_by: run 10/20/2026, 8:42:22 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39528387434
claimed_at: 2026-10-21T01:42:23.831Z
decision: null
decision_answer: null
---

dev's gate is red on two stale GLBs: house_1726_prairie__as_mapped_1904.glb and house_1730_prairie__as_mapped_1904.glb no longer match their inputs (T-2934 #1154 moved them onto K01, then T-2931 changed the K01 recipe and re-emitted every K01 asset but these two, which were not yet on its base); re-bake both on the merged recipe (tools/bake.sh --only house_1726_prairie, house_1730_prairie) so validate.py's stale check passes.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate (dataset: stale) fails every PR until these two are re-baked; this runner has no Blender

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
