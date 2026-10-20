---
id: T-2924
title: dev's gate is red since #1127: publish.sh copies data/reader/*.json into the mirror and check_published.mjs has no declared transform for them (11 published files trace to no source), so 'publish.sh produces a mirror that matches its source' fails on dev and every open PR
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-20
closed: null
pr: 1133
claimed_by: run 10/20/2026, 4:36:05 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39401197922
claimed_at: 2026-10-20T09:36:05.707Z
decision: null
decision_answer: null
---

dev's gate is red since #1127: publish.sh copies data/reader/*.json into the mirror and check_published.mjs has no declared transform for them (11 published files trace to no source), so 'publish.sh produces a mirror that matches its source' fails on dev and every open PR.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: every open PR (#1126, #1128, #1129, #1130) inherits the red and none can merge

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
