---
id: T-2257
title: Repoint the order book's South rows off split T-2247 onto its live successor (T-2254 raises the six gated roofs): dev's gate is red on build_order_book_1835 --check since the split at 18:22Z
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/9/2026, 1:39:12 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37974395054
claimed_at: 2026-10-09T18:39:12.366Z
decision: null
decision_answer: null
---

Repoint the order book's South rows off split T-2247 onto its live successor (T-2254 raises the six gated roofs): dev's gate is red on build_order_book_1835 --check since the split at 18:22Z.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: build_order_book_1835.py --check fails on origin/dev e698c6213 because ordinary_dwellings, barns_stables and small_outbuildings/south are ordered by split T-2247; every open PR is blocked until it is swept

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
