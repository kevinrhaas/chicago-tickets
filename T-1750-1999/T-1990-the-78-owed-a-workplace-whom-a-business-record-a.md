---
id: T-1990
title: The 78 owed a workplace whom a business record already names as proprietor, partner or staff: the employment join reads the register's own rows and places each at that house
state: open
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1982
opened: 2026-10-02
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

The 78 owed a workplace whom a business record already names as proprietor, partner or staff: the employment join reads the register's own rows and places each at that house.

Piece 1 of 3 of **T-1982 — The 308 working-age persons owed a workplace: each works_at resolved or the reason none is owed stated, the audit's owed count at zero**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (stated before working)

`tools/employment_coverage_1835.py` reads the business register's own people rows (`proprietors[]`, `partners[]`, `staff[]` with a `person_id`, on records present at the scene date and rows whose dates do not exclude 1 July 1835), across `data/businesses/*.json` AND `data/businesses/authored/*.json`, and a person with no house from the card or the seating whom such a row names is placed at that house: proprietors and partners on their own account, staff at a named house, each with the record's own tier in `decided_by`. Measured 2026-10-02: 78 of T-1982's 308 (72 `keeps_their_own_house`, 6 `trade_attested_no_house_named` — the Indian agent and his interpreter, the land-office register, the county clerk, the Presbyterian minister, the priest of St Mary's). `python3 tools/audit_town_completion_1835.py` then reports `working_age_persons_owed_a_workplace` at 230 (308 - 78) with no dangling id; every one of the 78 opens with a house named under "Were they at work?"; check.sh green. No business record and no card is written.
