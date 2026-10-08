---
id: T-2173
title: dev's gate is red since #520 (T-2172): assets/gltf/glessner_house__as_built_1887.glb differs from the packed Glessner v4 recovery archive — run tools/recover_glessner_v4.py --pack and commit the archive parts and manifest
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: 524
claimed_by: run 10/8/2026, 6:00:13 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37766823335
claimed_at: 2026-10-08T11:00:14.009Z
decision: null
decision_answer: null
---

dev's gate is red since #520 (T-2172): assets/gltf/glessner_house__as_built_1887.glb differs from the packed Glessner v4 recovery archive — run tools/recover_glessner_v4.py --pack and commit the archive parts and manifest.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 154 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> dev's gate is red; every open PR waits on this

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: check.sh fails 7 steps (Glessner v4 package, publish, dataset, derivative) on dev @ 949299f66, so no PR can go green

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
