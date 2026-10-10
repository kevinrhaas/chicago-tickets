---
id: T-2275
title: The crosswalks and back-projections (crosswalk_fergus_1839, crosswalk_fergus_1843, crosswalk_norris_1844, crosswalk_norris_1844_advertiser, back_project_addresses, back_project_residences) read a household's home and workplace from its associated_with rows instead of the singular lives_at/works_at
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2273
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/9/2026, 8:49:31 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38014393336
claimed_at: 2026-10-10T01:49:31.710Z
decision: null
decision_answer: null
---

The crosswalks and back-projections (crosswalk_fergus_1839, crosswalk_fergus_1843, crosswalk_norris_1844, crosswalk_norris_1844_advertiser, back_project_addresses, back_project_residences) read a household's home and workplace from its associated_with rows instead of the singular lives_at/works_at.

Piece 1 of 3 of **T-2273 — The 26 tools and two card reads that take lives_at/works_at off a household record, and the 7 that read the resident index's copy, read associated_with rows instead**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2273 was split (2026-10-10T01:49:23.148Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/9/2026, 8:49:16 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38014393336) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38014393336) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The six tools take a household's home and workplace only through `associations.home_of` / `workplace_of`; none reads `lives_at` or `works_at` off a household record; each tool's `--check` re-derives its committed file byte-identically on dev's records AND on the same records with `lives_at`/`works_at` stripped from all of them (the old code fails that second run); the two back-projections' self-tests build their fixtures from `associated_with` rows only. Output field names (`lives_at_1835`, `works_at_1835`, `*_real_values`) are the files' published schema and stay; T-2274 decides them with the pair.
