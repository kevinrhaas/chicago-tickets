---
id: T-2185
title: The St Mary's mothers and godmothers drawn male (28): read them female, and withdraw the modelled wives and children the modelled-families stage gave the ones heading a house, through the women-and-children re-family fixpoint
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2177
opened: 2026-10-08
closed: 2026-10-09
pr: 563
claimed_by: run 10/9/2026, 2:05:15 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-09T08:56:37Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37896778263
claimed_at: 2026-10-09T07:05:15.187Z
decision: null
decision_answer: null
---

The St Mary's mothers and godmothers drawn male (28): read them female, and withdraw the modelled wives and children the modelled-families stage gave the ones heading a house, through the women-and-children re-family fixpoint.

Piece 2 of 2 of **T-2177 — The St Mary's baptismal register states the sex of 42 people whose cards carry a drawn sex that contradicts it: 22 children (fils/fille, son/daughter) and 20 mothers drawn male. Read the entry's role and term onto the card and retire the draws**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2177 was split (2026-10-08T17:55:13.123Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 16m ago, run 10/8/2026, 12:39:16 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37817443904) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37817443904) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## What the first attempt found (2026-10-08, slice 5/5, while landing T-2184)

T-2184 put `tools/spend_person_sex_age.py`'s register rule in place (`ROLE_SEX`,
`register_sex`, `child_term`) and READS ONLY `father`/`godfather` and the children's term.
This piece is adding `"mother": "female", "godmother": "female"` to `ROLE_SEX` (and their
`ROLE_WORDS`), and then making everything downstream converge. Measured with them in:

- **28 women drawn male**: 20 mothers (4 also godmothers) and 8 godmothers. One godmother
  was already read female from her forename; she leaves the draw's rate measurement
  (`reconstruct_sex_age.measure` skips register-read sexes), which moves the civic roll
  from 94.71% to 95.17% and the pooled rate from 93.10% to 93.24%. That re-words the
  rate in **224 unrelated drawn cards' notes** and flips one draw (`calhoun_alvin`, F→M).
  Consider counting a register-read person whose forename also settles her, so the rate
  does not move.
- **`reconstruct_modelled_families.py --build` withdraws the invented families of 13
  women** it had married off as men (e.g. `hh_beaubien_monique` had a modelled WIFE;
  `hh_chandler_catherine` a wife and five children) and re-deals folded wives among four
  male heads (`hh_abbott_titus_h`, `hh_adams_hiram_a`, `hh_ballard_thomas`,
  `hh_nicole_l`). That is the visible point of this piece.
- **The freed slots land on T-1174's cells** (female 20-29 north/south/west, under-10s;
  about 30 people), and T-1174 is done, so `build_order_book_1835`'s
  `every_work_order_names_a_live_ticket` refuses. Re-owning that rule to `FAMILY_OWNER`
  is WRONG: `reconstruct_women_children.py` selects its buckets by `owning_ticket ==
  "T-1174"` and then derives 0 of its 124 houses.
- **The designed answer is for the women-and-children stage to re-draw the room**, but
  it is a fixpoint: the book refuses until the room is filled, the stage reads its room
  from the book on disk, and the re-family rule (`model_refamily_rule.py`) is derived
  from the cards the stage last wrote. Rebuilding the book once with the liveness gate
  skipped, then the stage, then the rule, then the stage again, failed on
  `hh_rc_dufresne_therese` and then on `hh_rc_barnes_nancy` ("a house moves whole or not
  at all") and overfilled `persons/female/20_29/north/family/none` (30 of 16). Budget a
  whole run for that loop, and expect to need the order the programme front door
  (`reconstruct_residents_1835.py --stage …`) uses rather than ad hoc rebuilds.
