---
id: T-1752
title: dev is RED at mobile smoke parts 1-2 and has been since 2026-09-28: the frontage census has drifted a walk, a crossing and two fence runs past the exact counts the suite asserts, and no CI check looks at it
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
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

dev is RED at mobile smoke parts 1-2 and has been since 2026-09-28: the frontage census has drifted a walk, a crossing and two fence runs past the exact counts the suite asserts, and no CI check looks at it.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A standing red on the integration branch that no automated gate can see: chicago-4d-check.yml runs no smoke at all, so only a steward run that pays for mobile parts 1-2 finds it, and until 2026-09-29 the register had no reading for part 2 since 02:00 the previous day. Measured twice tonight on clean origin/dev worktrees (1b01e8b8 and 88298203) with byte-identical figures, and confirmed NOT caused by the T-1547 branch that found it. It blocks nothing today and fits no existing ticket, but every run from here that touches the frontage layer will re-derive it at 3 minutes a time.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
