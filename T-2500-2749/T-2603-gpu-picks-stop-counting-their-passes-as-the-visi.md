---
id: T-2603
title: GPU picks stop counting their passes as the visitor's frame
state: done
epic: META
requested_by: steward
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-16
closed: 2026-10-16
pr: 890
claimed_by: run 10/16/2026, 12:15:04 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T18:01:19Z
claimed_run: null
claimed_at: 2026-10-16T17:15:04.570Z
decision: null
decision_answer: null
---

GPU picks stop counting their passes as the visitor's frame.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's desktop smoke part 14 fails the 1904 spawn draw budget (7,500,192 triangles against 4.6M) because T-2573's GPU pick passes stay in renderer.info; PR #851 (T-2228) cannot merge until it is fixed

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (2026-10-16)

`renderers/web/js/gpu-pick.js` (T-2573, #882) sets `renderer.info.autoReset = false`
for a pick, renders the id pass of the scene plus every batch, and restores the flag
but not the counters. A `stats()` read before the next frame therefore reports the
pick passes as the visitor's frame. Smoke part 14 picks nine times at the Glessner
front and then reads the 1904 spawn budget: desktop reads 288 calls / 7,500,192
triangles against 360 / 4,600,000, on `dev` and on PR #851 alike.

Measured on the published mirror, 1280×800, SwiftShader, at the 1904 spawn:
before the picks 3,986,918 triangles (dev 3bb708c2); after nine picks 7,005,036;
with the counters preserved across the pick, 3,982,054 before and after (PR #851 tree).

Fix: snapshot `renderer.info.render` with the other state the pick saves, and
restore it in the same `finally`. No geometry, budget or pick result changes.
