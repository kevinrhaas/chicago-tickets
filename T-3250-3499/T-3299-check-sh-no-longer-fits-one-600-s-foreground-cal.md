---
id: T-3299
title: check.sh no longer fits one 600 s foreground call on a 4-core steward runner: 1118 steps ran past 600 s on 2026-11-01 (one red step, so the verdict came only after the cap), and a re-run on the same tree was cut off by timeout at 585 s just after its publish step; find the new heavy tail with CHECK_TIMINGS and cut it, or re-argue the budget in check.sh's header
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-01
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

check.sh no longer fits one 600 s foreground call on a 4-core steward runner: 1118 steps ran past 600 s on 2026-11-01 (one red step, so the verdict came only after the cap), and a re-run on the same tree was cut off by timeout at 585 s just after its publish step; find the new heavy tail with CHECK_TIMINGS and cut it, or re-argue the budget in check.sh's header.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
