---
id: T-2248
title: Repoint the order book's three South rows (ordinary_dwellings, barns_stables, small_outbuildings) off T-2242, withdrawn on the owner's answer (a), onto T-2247, the live ticket that owns the gated balance's five dwellings: build_order_book_1835 --check refuses the book
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
claimed_by: run 10/9/2026, 10:00:21 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37948040963
claimed_at: 2026-10-09T15:00:21.661Z
decision: null
decision_answer: null
---

Repoint the order book's three South rows (ordinary_dwellings, barns_stables, small_outbuildings) off T-2242, withdrawn on the owner's answer (a), onto T-2247, the live ticket that owns the gated balance's five dwellings: build_order_book_1835 --check refuses the book.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it since 14:28Z: 'structures/ordinary_dwellings/south has 5 left and is ordered by T-2242, which is withdrawn', so every open PR inherits the red (#569's CI gate on 2e655632f)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- `tools/build_order_book_1835.py`'s three rows `("south","ordinary_dwellings")`, `("south","barns_stables")`, `("south","small_outbuildings")` name T-2247, with the comment block extended (T-2242 withdrawn 2026-10-09 on owner decision (a): the five stay owed in the gated balance until the S9 street work, which T-2247 owns).
- The order book is re-derived and `build_order_book_1835.py --check` passes; `./tools/check.sh` is green on dev's tree.
- Nothing in the scene changes (exemption 3: a gate blocking every open PR, among them #569).
