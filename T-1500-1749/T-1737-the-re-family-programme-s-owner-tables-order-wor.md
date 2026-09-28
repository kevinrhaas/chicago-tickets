---
id: T-1737
title: The re-family programme's owner tables order work from tickets nobody can claim, and its report's held count disagrees with the book's
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

The re-family programme's owner tables order work from tickets nobody can claim, and its report's held count disagrees with the book's.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> found by T-1717's re-deal: refamily_moves_1835.py --build faults with 'the book orders work from tickets nobody can claim' (the_programme ordered by T-1597, done; who_makes_the_moves by T-1559, split with no live piece), and report_refamily_programme.py --build then reports 384 people held where the book settles 395. The fault is latent on dev and any re-deal of the lodging layer surfaces it, so it blocks every future lodging roof

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
