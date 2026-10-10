---
id: T-2272
title: The 17 tools that mint or rewrite household records write associated_with rows instead of the singular lives_at/works_at
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: T-2261
opened: 2026-10-09
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

The 17 tools that mint or rewrite household records write associated_with rows instead of the singular lives_at/works_at.

Piece 2 of 4 of **T-2261 — Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads them**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2261 was split (2026-10-10T01:43:44.993Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 14m ago, run 10/9/2026, 8:29:50 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Census (T-2271, 2026-10-10) — the writers

Read off `git grep -n -E "lives_at|works_at"` over tools/, with comments and labels set aside. Each of these writes the pair into a household record (null blocks included; a null block retires with the pair and needs no row):

`generate_inferred_households.py` (243-244, 1421-1425, also `documented_updates`), `mint_civic_residents.py` (1056-1060; own gate 1691), `mint_documented_residents.py` (671-677), `mint_letter_list_residents.py` (1285-1289; gate 2055), `mint_placed_residents.py` (510-516), `readmit_borderline_roster.py` (436-438), `reconstruct_church_register.py` (397-403), `reconstruct_free_black.py` (696-700), `reconstruct_garrison_1835.py` (723-739 — the fort roof, and the `basis`/`replaceable_by` T-2271 carried onto the row), `reconstruct_institutional_households.py` (457-481), `reconstruct_trade_households.py` (982-989, 1052), `reconstruct_transients_1835.py` (666-676), `reconstruct_underdocumented.py` (315-321), `reconstruct_women_children.py` (462-470, 646), `seat_lodgers_1835.py` (1575-1596, writes `basis.note` and `replaceable_by.match`), `synthesize_resident_research.py` (936-937), `migrate_attribute_tiers.py` (133-134).

Most write null blocks only, so the work is mostly deleting a key and its gate lines; the five that write a VALUE (garrison, institutional, trade households, women/children, lodgers) have to write the row the copier (`household_associations.py`) writes today, and the copier then has nothing left to copy. If that is more than one demonstration, split the value-writers from the null-writers.
