---
id: T-1744
title: L270 says Kinzie's twenty slots are labourers' households and the seats file says thirteen tradesmen's, six merchant and professional and one labourer's: correct the register to the ground it scopes
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: 484
claimed_by: run 10/5/2026, 11:21:20 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37339622501
claimed_at: 2026-10-05T16:21:20.860Z
decision: null
decision_answer: null
---

L270 says Kinzie's twenty slots are labourers' households and the seats file says thirteen tradesmen's, six merchant and professional and one labourer's: correct the register to the ground it scopes.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A liberties-register statement that misdescribes the committed data it scopes, and compile_liberties.py only machine-checks the scope COUNT, so no gate catches it. It is on dev now (written by T-1741) and both open T-1736 laps inherit it verbatim. Measured against data/reconstruction/1835_platted_seats.json on dev and on the T-1736 branch alike: blk_indiana_north_wolcott's eleven slots are six tradesman_dwellings and five merchant_and_professional_dwellings; blk_indiana_north_cass's nine are seven tradesman_dwellings, one merchant_and_professional_dwellings and one labourer_dwellings (hh_barre_john_s) - so the single labourer's household is on cass, not wolcott, and 'eleven labourers' households' is wrong twice over. Provenance is the product: a register entry that states the wrong clause for twenty invented seats is the kind of claim this project must not carry. XS - one paragraph of L270 plus compile_liberties.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
