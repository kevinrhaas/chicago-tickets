---
id: T-2243
title: Repoint the order book's three T-2239 rows (South ordinary_dwellings, barns_stables, small_outbuildings) onto T-2242, the live piece that owns the five dwellings: T-2239 was split and build_order_book_1835 --check refuses the book
state: claimed
epic: META
requested_by: loop
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/9/2026, 5:08:16 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37914561384
claimed_at: 2026-10-09T10:08:16.271Z
decision: null
decision_answer: null
---

Repoint the order book's three T-2239 rows (South ordinary_dwellings, barns_stables, small_outbuildings) onto T-2242, the live piece that owns the five dwellings: T-2239 was split and build_order_book_1835 --check refuses the book.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 142 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> dev's own gate is red on this one step and every open PR inherits it; an XS repoint, merged in the run that files it

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: build_order_book_1835.py --check fails 'structures/ordinary_dwellings/south has 5 left and is ordered by T-2239, which is split', so every open PR (#564's resume note names it) inherits the red

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
