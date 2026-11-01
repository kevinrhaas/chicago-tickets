---
id: T-3299
title: check.sh no longer fits one 600 s foreground call on a 4-core steward runner: 1118 steps ran past 600 s on 2026-11-01 (one red step, so the verdict came only after the cap), and a re-run on the same tree was cut off by timeout at 585 s just after its publish step; find the new heavy tail with CHECK_TIMINGS and cut it, or re-argue the budget in check.sh's header
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-01
closed: 2026-11-01
pr: 1587
claimed_by: run 11/1/2026, 1:01:59 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-01T21:46:48Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41338975666
claimed_at: 2026-11-01T19:02:00.668Z
decision: null
decision_answer: null
---

check.sh no longer fits one 600 s foreground call on a 4-core steward runner: 1118 steps ran past 600 s on 2026-11-01 (one red step, so the verdict came only after the cap), and a re-run on the same tree was cut off by timeout at 585 s just after its publish step; find the new heavy tail with CHECK_TIMINGS and cut it, or re-argue the budget in check.sh's header.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
