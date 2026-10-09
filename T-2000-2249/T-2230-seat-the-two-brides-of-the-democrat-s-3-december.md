---
id: T-2230
title: Seat the two brides of the Democrat's 3 December 1833 MARRIED column: Charlotte Wesencraft as Mark Noble jun.'s wife and Mary Noble as George Bickerdyke's (where T-2020 folded Bridget Ryan in), reading the column's Mr. and Miss onto the two cards drawn the wrong sex ('Jun Marknoble' drawn female; Charlotte drawn male, heading a modelled wife and sons)
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: T-2192
opened: 2026-10-08
closed: null
pr: null
claimed_by: run 10/8/2026, 8:12:10 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37868324385
claimed_at: 2026-10-09T01:12:10.113Z
decision: null
decision_answer: null
---

Seat the two brides of the Democrat's 3 December 1833 MARRIED column: Charlotte Wesencraft as Mark Noble jun.'s wife and Mary Noble as George Bickerdyke's (where T-2020 folded Bridget Ryan in), reading the column's Mr. and Miss onto the two cards drawn the wrong sex ('Jun Marknoble' drawn female; Charlotte drawn male, heading a modelled wife and sons).

Piece 2 of 2 of **T-2192 — Read the Democrat's MARRIED column of 3 December 1833 onto the Noble, Wesencraft and Bickerdyke cards: Mark Noble jun. (hh_marknoble_jun), second son of Mark Nobles Esq. (hh_noble_mark), married Charlotte, only daughter of Charles Wesencraft; Mary (hh_noble_mary), second daughter of Mark Noble Esq., married George Bickerdyke — write the parent ties and rule where the two brides live in 1835**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2192 was split (2026-10-09T00:12:14.094Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 10/8/2026, 7:09:36 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37862982534) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37862982534) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## What the splitting run found (T-2229's run, 2026-10-09)

- The parent ties are T-2229's, and Charlotte's tie to her father was already landed by T-1134 (`kin_rulings.json` `hh_wesencraft_charles__daughter__charlotte`). This piece is the marriages only.
- **The precedent is T-2190** (#547): `PRINTED_WIVES` in `tools/reconstruct_modelled_families.py` folds a printed bride's card into her husband's drawn house, in the cell the drawn wife filled. Neither house here fits it as-is. `hh_marknoble_jun` has no modelled family at all, because its head is drawn female under a mis-parsed name ('Jun Marknoble'). `hh_bickerdyke_george`'s wife is no draw: she is T-2020's fold of `hh_rc_ryan_bridget`, with her two children.
- **The sex readings come first.** The column prints 'Mr. MARK NOBLE, jun.' and 'Miss CHARLOTTE'. T-2190's rule 1 in `spend_person_sex_age.py` reads a title directly before the name as read; it did not fire on either card (#547's PR body names both as follow-ups). Each flip withdraws or adds a modelled family: Charlotte's card heads a drawn wife 'Martha' and two drawn sons.
- Effort raised to M: two folds, two sex readings and a re-derive of the whole derived layer. #547 did one fold and ran out of clock.
