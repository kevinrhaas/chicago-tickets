---
id: T-2274
title: Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads or writes them
state: open
epic: META
requested_by: loop
seen: false
effort: S
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

Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads or writes them.

Piece 4 of 4 of **T-2261 — Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads them**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2261 was split (2026-10-10T01:43:44.993Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 14m ago, run 10/9/2026, 8:29:50 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Found by T-2276 (2026-10-10, PR #610) — prose and pointers the readers leave behind

- About 22 authored business records (`data/businesses/authored/biz_*`) carry a `basis` sentence written by `tools/complete_inwindow_trades.py` that quotes "`works_at: <structure>`". The tool now reads the work row, but the sentence still names the singular field. Rewording it rewrites business cards a visitor reads, so it is left for this retirement.
- The `…#works_at` / `…#lives_at` provenance pointers that the copier (`household_associations.py`) writes into household rows, `household_associations.json` and `data/sidecars/1835/*` go dangling the moment the singular fields are removed. Repoint them in the same change.

## Finding (T-2277, PR #613, 2026-10-10) — what the pair still carries that no row can

1. **The note on a NULL link.** 1,425 households carry a null `lives_at` with a note and 1,408 a null `works_at` with a note: the reason no address resolves. Every card shows it (`residents.js` `absenceRow`, `people.js` 879's "no known address" reason), and so does `report_research_signoff.py`'s "a printed reason no premises resolves" linkage. An absence has no `associated_with` row, so T-2277 left these three reads on the singular block on purpose. Before the pair retires, give the absence prose a home (an absence block, or an unresolved row kind) or rule that it goes.
2. **The attribute-tier census.** `summarize_residents.s_tiers` walks every `{value, confidence}` block through `migrate_attribute_tiers.walk_blocks`, so it counts the pair as attributes. With the 67 non-null values stripped, attested 741→701 and inferred 3720→3686. Decide whether the census counts the rows instead.
3. **The copier and its input** (`household_associations.py`, `location_reconciliation.py`) build the rows FROM the pair. They retire with the writers (T-2272, blocked for that reason).
