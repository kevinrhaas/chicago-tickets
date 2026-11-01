---
id: T-3304
title: dev's gate red: house_1726_prairie_coach_house__as_standing_1904.glb stale after #1580 (T-1932) merged onto a dev whose K01 inputs had moved; rebake the one structure and land its GLB
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-01
closed: 2026-11-01
pr: null
claimed_by: run 11/1/2026, 2:45:49 PM CT
blocked_on: superseded: #1581 (T-1881) merged at 20:52Z carrying the same re-stamp (inputs_sha256 ddf15ed8…, GLB byte-identical, which this run reproduced with bake.sh --only); dev's gate went green on 7fed3a413. This run's full gate (check.sh --part 1..4/4, 1,128 steps, none red) and smoke (mobile part 3 107/0; desktop part 1 red only on T-3268's miller_house sign, as dev was at 18:03Z) confirmed the fix but have nothing left to land
needs_bake: false
closed_at: 2026-11-01T21:28:23.983Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41347446149
claimed_at: 2026-11-01T20:45:49.517Z
decision: null
decision_answer: null
---

dev's gate red: house_1726_prairie_coach_house__as_standing_1904.glb stale after #1580 (T-1932) merged onto a dev whose K01 inputs had moved; rebake the one structure and land its GLB.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on this (gate run 41345643221 on fe8015687); every open PR's gate fails on it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
