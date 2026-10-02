---
id: T-1996
title: The 38 on their own account at a census class whose printed count is already held (32 at a store, 3 attorneys, 2 forwarders, a watchmaker): each told from the order book's own bucket that no house is owed
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1992
opened: 2026-10-02
closed: 2026-10-02
pr: 304
claimed_by: run 10/2/2026, 2:40:52 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T21:41:54Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37054254990
claimed_at: 2026-10-02T19:40:52.953Z
decision: null
decision_answer: null
---

The 38 on their own account at a census class whose printed count is already held (32 at a store, 3 attorneys, 2 forwarders, a watchmaker): each told from the order book's own bucket that no house is owed.

Piece 1 of 3 of **T-1992 — The 134 on their own account whose house of trade the register does not hold: each house raised by the business band, or the reason none is owed stated**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (stated before working)

`tools/employment_coverage_1835.py` reads the order book's business buckets (`data/reconstruction/1835_reconstruction_order_book.json`, family `businesses`) and, for a person still reading `keeps_their_own_house` with no house, whose trade's premises ruling names a `census_class` the book has a bucket for, and whose bucket is FULL (`to_reconstruct - filled <= 0`: the register plus the business band already hold the printed count, or the scene-date bracket of it), answers `the_printed_count_is_held` — status `at_a_trade_with_no_house_to_join`, a STATED reason (the audit's WORK_STATED), with the bucket's own figures (census count, target, known, filled) in `decided_by`. ONLY a person graded `reconstructed`: a documented person is never told a count is held, because a count a reconstructed house fills is exactly the count a documented house would retire it from. Measured 2026-10-02: 37 people — 8 grocers, 8 hardware merchants, 7 merchants, 7 dry-goods merchants, a liquor dealer and a sutler (store: printed 44, held 65), 3 attorneys (lawyer: bracket target 15, 14 known + 1 filled), 2 forwarders (storage_and_forwarding: printed 4, held 7). The 38th of the title, E. H. Mulford (attested watchmaker), stays owed and is handed to T-1998. The physician bucket (target 10, 8 known, 0 filled) is NOT full and its head stays owed (T-1998). `verify` refuses a held-count answer on a documented person or against a bucket that is short; the self-test fires both. `python3 tools/audit_town_completion_1835.py` then reports owed a workplace 37 lower than the dev it is built on, check.sh green; each of the 37 cards' "Were they at work?" prints the count that holds it. No business record and no card is written.
