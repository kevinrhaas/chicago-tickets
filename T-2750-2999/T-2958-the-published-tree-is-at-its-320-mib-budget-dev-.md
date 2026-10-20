---
id: T-2958
title: The published tree is at its 320 MiB budget: dev stands about 0.02 MiB under it after T-2933's 1736 landed, so every PR that adds a byte to site/4d fails check.sh's dataset step (#1144 reads 320.034 MiB); measure where the growth since T-2596's 268.87 MiB went (Glessner's web GLB is 41.9 MiB again, data/gltf 138.9 MiB), hand bytes back or re-budget with the measurement in validate.py's SITE_BUDGET_MB note and docs/SITE-BUDGET.md
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-20
closed: null
pr: null
claimed_by: run 10/20/2026, 2:26:51 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39482826693
claimed_at: 2026-10-20T19:26:52.127Z
decision: null
decision_answer: null
group: T-2958,T-2959
---

The published tree is at its 320 MiB budget: dev stands about 0.02 MiB under it after T-2933's 1736 landed, so every PR that adds a byte to site/4d fails check.sh's dataset step (#1144 reads 320.034 MiB); measure where the growth since T-2596's 268.87 MiB went (Glessner's web GLB is 41.9 MiB again, data/gltf 138.9 MiB), hand bytes back or re-budget with the measurement in validate.py's SITE_BUDGET_MB note and docs/SITE-BUDGET.md.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate goes red on the site budget for every byte-adding PR: #1144 (T-2931) is complete and green on everything else

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
