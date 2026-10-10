---
id: T-2256
title: The South's family_dwelling order has 2 households no held head fills: once T-1645 stopped dealing roofs to letter-list households, count_held_head_dwellings_1835.py finds 165 heads under South dwellings against room for 167, and T-2193, which owned the order, is done
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: 600
claimed_by: run 10/9/2026, 5:59:59 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38001642938
claimed_at: 2026-10-09T22:59:59.390Z
decision: null
decision_answer: null
---

The South's family_dwelling order has 2 households no held head fills: once T-1645 stopped dealing roofs to letter-list households, count_held_head_dwellings_1835.py finds 165 heads under South dwellings against room for 167, and T-2193, which owned the order, is done.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found by T-1645 (2026-10-09).** With the letter-list households owed rather than dealt a
roof, `tools/count_held_head_dwellings_1835.py` finds 213 heads on the `dealt` rung (263
before) and 149 on `family` (188), and the South's walk runs out at 165 against room for 167
in the book's `households/family_dwelling/south` order. The North and West are full. T-2193,
which counted the held heads and owned the order, is done, so `FAMILY_HOUSEHOLD_OWNER` in
`tools/build_order_book_1835.py` now names this ticket (T-1420: a bucket names a run that
can still claim it).

**Acceptance:** the two are filled by a rule the book already states (a held head the housing
seats put under a standing South dwelling, a household beyond the index, or the order
discharged on a ruling), never by re-admitting a letter-list household; the bucket reads 0
left and the owner moves on or is retired in the same PR.
