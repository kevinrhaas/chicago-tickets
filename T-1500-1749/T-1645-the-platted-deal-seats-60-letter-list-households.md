---
id: T-1645
title: The platted deal seats 60 letter-list households on roofs the ruling of 2026-08-30 refuses them: the deal and T-0379 disagree about 60 roofs, and one of them has to move
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-10-09
pr: 590
claimed_by: run 10/9/2026, 12:56:49 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-09T22:26:51Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37969328701
claimed_at: 2026-10-09T17:56:49.126Z
decision: null
decision_answer: null
---

The platted deal seats 60 letter-list households on roofs the ruling of 2026-08-30 refuses them: the deal and T-0379 disagree about 60 roofs, and one of them has to move.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)


## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into this ticket:** T-1678. Same defect: the platted deal ignores the T-0379 letter-list ruling. T-1678 carried the measurement (now 79 of 150 adopted roofs refused) and the acceptance; size it first and split if it is over one run.

### Folded in from T-1678 — The platted deal is blind to the letter-list ruling: it seats a household T-0379 refuses a roof onto 61 standing roofs, 11 of them on South Water, and the keeper pass must then refuse every one

The platted deal is blind to the letter-list ruling: it seats a household T-0379 refuses a roof onto 61 standing roofs, 11 of them on South Water, and the keeper pass must then refuse every one.

Found by T-1675, which asked why eleven South Water dwelling and lodging roofs stand with
no household. All eleven ARE seated by `tools/seat_platted_ground_1835.py` — the committed
`1835_platted_seats.json` names a household for each — and `tools/name_the_keepers_1835.py`
refuses all eleven for the same reason: the household is minted from the post office's
letter lists, and the owner's ruling of 2026-08-30 (T-0379) refuses that cohort a roof.
It is not one district's accident. **61 of the deal's 109 adopted seats are refused this
way**, across every district the deal reaches.

The deal never consults the ruling. `adoptable()` refuses a roof on three tests — wrong
layer, already occupied, ancillary family — and none of them is about the HOUSEHOLD. So the
deal offers each roof to the first banded row its clause order reaches, and 743 letter-list
households sit in that order with nothing marking them unseatable. T-1638 said the
disagreement was "the deal's to answer, not this pass's to route around"; this is that
ticket.

It is not a shortage. T-1675 measured the deal's own owed rows, per clause, for households
neither refusal rejects: **14** for `labourer_dwellings`, **143** for `tradesman_dwellings`
and **105** for `merchant_and_professional_dwellings` in the south division alone. Every
refused roof has a seatable household waiting behind it.

**Acceptance:** the deal does not seat a household onto a standing roof that the
letter-list ruling refuses a roof — the row is owed instead, with that reason in writing, and
the roof goes to the next row of its clause order that may have one. Then
`1835_roof_keepers.json` § `refused_letter_list` is 0 by construction rather than by
coincidence, `counts.written` rises, and `households_left` falls by what was spent. A
self-test must fire when the refusal is dropped. The blast radius is stated before it is
taken: `1835_platted_seats.json`, `1835_lot_ledger.json`, the address book's carried seats
(T-1618) and every structure record the keeper pass then writes. **Size it first** — 109
seats re-dealt across every district may be more than one run, and `split` is the answer if
it is.

**Links:** T-1675 · T-1638 · T-1613 · T-0379 · T-1200 ·
`tools/seat_platted_ground_1835.py` · `tools/name_the_keepers_1835.py`.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
