---
id: T-2286
title: The North and West family_dwelling orders still owe 10 households (North 1, West 9) once all 23 waiting families are spent: no held head, waiting family or household beyond the index is left in either division to fill them
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2279
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/10/2026, 12:29:40 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38027458922
claimed_at: 2026-10-10T05:29:40.412Z
decision: null
decision_answer: null
---

The North and West family_dwelling orders still owe 10 households (North 1, West 9) once all 23 waiting families are spent: no held head, waiting family or household beyond the index is left in either division to fill them.

Piece 2 of 2 of **T-2279 — The North and West family_dwelling orders owe 12 households again (North 2, West 10): T-2255 took the off-plat roofs from letter-list households, so the held heads under North and West dwellings fall 8 and 15 short of the order, the families waiting on a roof discharge 6 and 5, and T-2256, which owned the rows, is done**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2279 was split (2026-10-10T04:39:34.278Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/9/2026, 11:35:15 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38024434610) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38024434610) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Measured by T-2285 (2026-10-10).** Once the waiting families' share past the South's
shortfall goes on to the North and West, all 23 families waiting on a roof discharge a cell
and the book reads North 1, West 9 still owed (`waiting_families_ruling`). Nothing left fills
them on a rule the book already states: every North and West held head under a standing
dwelling is counted (`1835_held_head_dwellings.json`, `not_counted` 0); the 42 other rows
waiting on a roof are 39 single persons (a bed, never a household of its own) and 3 families
the book already counts as a house; no waiting row is a letter-list household; the person
side cannot take a minted family (the North and West family person buckets are full, and
the town stands 2,864 against a model of 2,549). Ten standing D roofs hold boarders and no
household (North 8, West 2), which is short of the West's 9 even if a boarders' roof were
ruled a household.

**Acceptance:** the North and West `family_dwelling` rows read 0 left on a rule the book
states, never by re-admitting a letter-list household or by counting a bed as a house — or
the rows are discharged on a ruling stated beside the T-2256 one, with the owner asked where
the ruling is his (what the project IS); `FAMILY_HOUSEHOLD_OWNER_BY_DIVISION` moves on or is
retired in the same PR.
