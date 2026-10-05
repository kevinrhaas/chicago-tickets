---
id: T-2117
title: check.sh no longer fits a steward run's 600 s on four cores: 763 of 774 steps done at 595 s, 2,288 CPU-seconds, slowest steps derive_resident_roles --check 168 s and placement_policy_1835 --self-test 162 s
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: 476
claimed_by: run 10/5/2026, 7:23:54 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37308752130
claimed_at: 2026-10-05T12:23:54.515Z
decision: null
decision_answer: null
---

check.sh no longer fits a steward run's 600 s on four cores: 763 of 774 steps done at 595 s, 2,288 CPU-seconds, slowest steps derive_resident_roles --check 168 s and placement_policy_1835 --self-test 162 s.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 185 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> AGENTS.md rule 9 says the gate must keep fitting the 600 s foreground ceiling; measured 2026-10-05 on a 4-core steward runner it does not (three runs, rc 124 each, CHECK_TIMINGS taken), so every steward run now gets no local verdict and leans on CI's gate. No open ticket owns the gate budget (T-1578, which bought the last helping, is closed).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
