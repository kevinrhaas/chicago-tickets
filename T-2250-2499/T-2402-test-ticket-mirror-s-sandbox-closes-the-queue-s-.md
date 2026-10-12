---
id: T-2402
title: test_ticket_mirror's sandbox closes the queue's top ticket, and an image-gated top ticket (T-2369) is refused there: check.sh is red on every PR
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-12
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

test_ticket_mirror's sandbox closes the queue's top ticket, and an image-gated top ticket (T-2369) is refused there: check.sh is red on every PR.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: CI's bake job on #720 failed exactly this one step of 863 (job 114669186011); every PR's check.sh fails it while an image-gated ticket tops the queue

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
