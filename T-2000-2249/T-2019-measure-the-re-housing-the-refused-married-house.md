---
id: T-2019
title: Measure the re-housing the refused married houses can take from the town's own women: T-1174's woman-headed houses matched to them by the wife cell's division, the spacing rule and the child cap, written into the modelled-families ledger and report
state: claimed
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1171
opened: 2026-10-03
closed: null
pr: null
claimed_by: run 10/3/2026, 2:57:08 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37107550471
claimed_at: 2026-10-03T07:57:08.227Z
decision: null
decision_answer: null
---

Measure the re-housing the refused married houses can take from the town's own women: T-1174's woman-headed houses matched to them by the wife cell's division, the spacing rule and the child cap, written into the modelled-families ledger and report.

Piece 1 of 3 of **T-1171 — Give the remaining attested and inferred heads reconstructed families from the household model: wives, children, servants and apprentices drawn by the head's age, trade and household type, seeded, named from the pools, every member marked reconstructed**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Acceptance (this piece):**

- `reconstruct_modelled_families.py` writes, into `1835_modelled_families.json`, every house the
  book refused a wife (its wife cell, the head's band, the size drawn) and the re-housing those
  houses can take from T-1174's woman-headed houses: matched by the wife cell's division, the
  spacing rule, the child cap and the kin limit of 8, with the pairs, what is left on each side,
  and the female-headed share before and after.
- `--report` prints it; `--check` re-derives it byte for byte; a self-test fires each rule.
- The stage's `what_closes_it` stops saying a move closes the sex ratio, and its counts are
  derived rather than typed.
- Nobody moves and no card changes — that is T-2020.
- `./tools/check.sh` green.
