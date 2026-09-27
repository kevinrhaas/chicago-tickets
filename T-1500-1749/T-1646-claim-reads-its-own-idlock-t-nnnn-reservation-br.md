---
id: T-1646
title: claim reads its own idlock/t-NNNN reservation branch as a rival run, so every freshly minted or split ticket refuses its first claim and teaches the next run to reach for --force
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-09-27
pr: null
claimed_by: null
blocked_on: duplicate of T-1666, fixed by PR #108 — the rival scan now skips refs/heads/idlock/*. Filed the day after T-1601 by another run that hit the same refusal.
needs_bake: false
closed_at: 2026-09-27T06:50:03.587Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

claim reads its own idlock/t-NNNN reservation branch as a rival run, so every freshly minted or split ticket refuses its first claim and teaches the next run to reach for --force.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
