---
id: T-2255
title: The off-plat deal seats 69 letter-list households on roofs the ruling of 2026-08-30 (T-0379) refuses them: T-1645 made the platted deal owe that cohort, and the off-plat deal (tools/seat_off_plat_ground_1835.py) still deals from the rows it hands on without reading the ruling
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
claimed_by: run 10/9/2026, 6:05:40 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38002351036
claimed_at: 2026-10-09T23:05:40.785Z
decision: null
decision_answer: null
---

The off-plat deal seats 69 letter-list households on roofs the ruling of 2026-08-30 (T-0379) refuses them: T-1645 made the platted deal owe that cohort, and the off-plat deal (tools/seat_off_plat_ground_1835.py) still deals from the rows it hands on without reading the ruling.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found by T-1645 (2026-10-09).** T-1645 made `tools/seat_platted_ground_1835.py` read the
owner's letter-list ruling (T-0379) before it deals: a letter-list household is owed with the
ruling as its reason (`refused_by: T-0379`, 659 rows) instead of being seated. Those rows are
still HANDED ON to T-1614, because the off-plat deal's scope is the platted deal's owed list by
contract (`build_order_book_1835.py` holds the chain: off-plat `rows_in_scope` == platted
`owed`). `tools/seat_off_plat_ground_1835.py` never reads the ruling, so it seats the cohort on
off-plat roofs: 55 of its 99 adopted seats on dev before T-1645, **69 of 99** after it (measured
on the T-1645 branch: more of the cohort now reaches it).

No card shows it today — `tools/name_the_keepers_1835.py` reads only the platted seats, so no
off-plat roof names a keeper — but the address book, the housing seats and the held-head count
all read these seats as dealt roofs, so the town counts 69 letter-list households as housed.

**Acceptance:** the off-plat deal does not seat a household the letter-list ruling refuses a
roof — it owes it with the platted deal's `refused_by` reason, using the same predicate
(`name_the_keepers_1835.is_letter_list`, imported via the platted deal's `refused_a_roof()`),
and the roof goes on to the next row of its clause order; an honesty assertion and a
self-test fire when the refusal is dropped; L271 restates the count. State the blast radius
(housing seats, held-head count, the order book's family_dwelling room) before taking it.
