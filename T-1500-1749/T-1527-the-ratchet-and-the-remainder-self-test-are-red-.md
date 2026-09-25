---
id: T-1527
title: The ratchet and the remainder self-test are red on dev: pass_02_75_cohort and a remainder rule both hand on to T-1507, which has settled to done
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: 2026-09-25
pr: null
claimed_by: null
blocked_on: Both reds were cleared on dev by T-1526 (#14, merged 2026-09-24): pass_02_75_cohort no longer names T-1507 and spend_trade_premises retired HANDED_TICKET. Withdrawn during the owner's re-rank of 2026-09-25.
needs_bake: false
closed_at: 2026-09-25T14:30:16.957Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Found by T-1515 (PR #9) while gating a merge of `dev`. **Both reds are on `dev` itself**,
proved by running the two commands in a clean `origin/dev` worktree — they are not the
merging branch's.

```
== research stays inside its historical ratchet and closed unit ledger
   FAIL: residents:data/research/residents/pass_02_75_cohort.json#people/pearsons_hiram:
         unresolved ticket 'T-1507' is missing or not open

== …and each of its rules still fires, and hands on only to live work
   FAIL rule the_reading_contradicts_the_trade_the_card_carries_and_the_field_is_
        re_adjudicated: hands on to T-1507, which is 'done' and not live work
```

The closing research audit and the research sign-off go red behind them, so `check.sh`
reports **4 of 610** steps failed on a tree whose only other change is green.

WHAT HAPPENED. T-1507 landed work that hands on to T-1507 — an unresolved unit and a
remainder rule both naming their own ticket as the live work that will finish them. The
settle workflow then flipped T-1507 to `done` when its PR merged, and both gates are
right to refuse: a hand-off to a closed ticket is a hand-off to nobody. This is a shape
any ticket can walk into, so the fix is worth more than the two edits.

**Acceptance:**

- `pass_02_75_cohort.json#people/pearsons_hiram` and the
  `the_reading_contradicts_the_trade_the_card_carries_and_the_field_is_re_adjudicated`
  rule hand on to live work, or state their evidence clause instead.
- `./tools/check.sh` green on `dev` — all 610.
- A gate or a `done` guard that refuses a hand-off naming the ticket doing the handing,
  since that is the one ticket guaranteed to close before the hand-off is honoured.
