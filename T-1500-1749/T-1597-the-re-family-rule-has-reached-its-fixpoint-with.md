---
id: T-1597
title: The re-family rule has reached its fixpoint with 395 of the 523 held people still held in 44 refused buckets: the order book's programme step needs a live owner for them, and the owner's ruling of 2026-09-24 that they are re-familied and never retired needs somewhere to land
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: answered
decision_answer: a
---

The re-family rule has reached its fixpoint with 395 of the 523 held people still held in
44 refused buckets: the order book's programme step needs a live owner for them, and the
owner's ruling of 2026-09-24 that they are re-familied and never retired needs somewhere
to land.

## How this was found, 2026-09-25

T-1581's new gate step — *closing this branch's tickets strands nobody above them* — fired
on T-1564's own pull request, which is exactly what it was built to do. T-1564 is the last
live descendant of T-1559, and T-1559 of T-1556, so closing it kills both. The order book
carries a forward-looking work order that names T-1556:

```
"the_programme": {"ticket": "T-1556", "settled": still == 0},
```

`settled` is arithmetic and not opinion — the programme finishes when nobody is held — and
395 people are still held, so the order is live and was about to name a ticket nobody can
claim. T-1564's PR repointed it here rather than leaving the red for `dev`.

## What is and is not already answered

**Answered, and not reopened by this ticket.** The moves the rule allows are all made:
`who_makes_the_moves` reads `settled: true`, 129 of 129 spent across three rounds, the
third changing nothing. T-1563 spent the 19 trade households and T-1564 the 54 women and
children. None of that is in question.

**Not answered.** The owner ruled on 2026-09-24 (T-1530, carried in T-1556) that the
surplus is *re-familied, never retired*, and as ONE unit for all 523. The rule built to
carry that ruling can move 129 of them. The remaining 395 sit in 44 buckets the rule
REFUSES — refused for reasons the rule states and which are not defects: a house moves
whole or not at all, and a move may not change a person's sex or age band. So the ruling
as written cannot be carried out in full by the rule that was written to carry it, and
nothing in the tree currently says what the other 395 are.

This is not a missing number. It is the same question T-1530 asked, asked again of the
residue, and the answer is the owner's: see the `## Decision needed` section.

## What may not be done

* No person may be deleted or un-written to make the arithmetic close — that is the exact
  thing the ruling of 2026-09-24 refused.
* No confidence may be upgraded, and no refusal reworded to look like a move.
* The rule's refusals may not be quietly widened to catch more of the 395 without the
  owner saying so: the reasons a bucket is refused are stated in
  `data/reconstruction/1835_refamily_rule.json` and each is a rule, not a gap.

**Acceptance:** the order book's `the_programme` work order names a ticket a run can
claim for as long as it is unsettled, and the 395 still-held people have a written owner
that says what becomes of them — either a rule change the owner approves, or a recorded
decision that they remain held, with `settled` re-derived from whatever that decision
makes true rather than from `still == 0` alone. Whichever it is, `docs/LIBERTIES.md` and
the re-familying report carry the count and the reason. Prove it by re-deriving the order
book and by running `python3 tools/ticket_liveness.py --closing` against this ticket.

## Decision needed

**Question:** Your ruling of 2026-09-24 was that the 523 surplus reconstructed people are re-familied and never retired, as ONE unit. The rule built to carry it has reached its fixpoint: 129 moved, 395 still held in 44 buckets the rule refuses (a house moves whole or not at all; a move may not change a person's sex or age band). The ruling cannot be carried out in full by that rule. What are the other 395?

- (a) They remain held, recorded as held, and the programme is settled at its fixpoint rather than at zero — the refusals stand as written and the book says so.
- (b) Widen the rule so more of the 395 can move — you name which refusal gives way (whole-house, sex, or age band), and the cost in what the town then claims.
- (c) Something else — the 395 are neither held nor moved but handled some third way you name.

**Recommendation:** (a) They remain held, recorded as held, and the programme is settled at its fixpoint rather than at zero — the refusals stand as written and the book says so. — Every one of the 44 refusals is a rule you approved, not a gap: option (a) changes no person and no confidence, and it makes the book state the true finish line instead of one it can never reach. (b) buys a smaller residue by loosening a constraint that exists to stop a mother being counted on one side of the river and her daughter on the other, which is the worse record.

**Asked:** 2026-09-25 by https://github.com/kevinrhaas/polecat-platform/actions/runs/36205104435. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

**Owner answer (2026-09-25, in session):** (a) They remain held, recorded as held, and the programme is settled at its fixpoint rather than at zero — the refusals stand as written and the book says so.
