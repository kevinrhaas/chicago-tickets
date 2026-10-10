---
id: T-2273
title: The 26 tools and two card reads that take lives_at/works_at off a household record, and the 7 that read the resident index's copy, read associated_with rows instead
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: T-2261
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/9/2026, 8:49:16 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38014393336
claimed_at: 2026-10-10T01:49:16.486Z
decision: null
decision_answer: null
---

The 26 tools and two card reads that take lives_at/works_at off a household record, and the 7 that read the resident index's copy, read associated_with rows instead.

Piece 3 of 4 of **T-2261 — Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads them**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2261 was split (2026-10-10T01:43:44.993Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 14m ago, run 10/9/2026, 8:29:50 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Census (T-2271, 2026-10-10) — the readers

Off the household record (26): `adopt_street_faces.py` 573, `back_project_addresses.py` 408/680, `back_project_residences.py` 154/380, `complete_inwindow_trades.py` 371, `consolidate_town_cards.py` 226, `crosswalk_fergus_1839.py` 148, `crosswalk_fergus_1843.py` 120/312, `crosswalk_norris_1844.py` 100/285, `crosswalk_norris_1844_advertiser.py` 124/252, `export_resident_audit.py` 304/404/421, `fronting_street.py` 292, `house_the_present_1835.py` 423/924/932, `household_associations.py` (the copier itself, 128/160/346), `location_reconciliation.py` 277 (builds the reconciliation table FROM the pair — the copier's own input), `model_refamily_rule.py` 289, `profile_population_1835.py` 781-828/1277, `rebuild_resident_index.py` 171/273 (writes the index copy), `replace_invented_residents.py` 472/613/668, `report_research_signoff.py` 256/311, `spend_trade_premises.py` 518, `spend_remainder_rulings.py` 783-793, `substitute_reconstruction.py` 549, `summarize_residents.py` 334, and on the card `people.js` 879 and `residents.js` 1993-1994 (the null link's note — an absence, which has no row).

Off the index's copy (7): `build_order_book_1835.py` 1630, `compile_businesses.py` 280, `enclosure_owners.py` 61 (and `yard_rule_1835.py` through it), `report_research_closing_audit.py` 157, `residents.js` 1867/2295-2305, `smoke_renderer.mjs` 14573.

`associations.home_row` / `work_row` / `home_of` / `workplace_of` (T-2260) are the reader to move them onto. Thirty-three call sites is more than one demonstration: split by family (crosswalks and back-projections; housing and deal; index, cards and audits) before claiming.
