---
id: T-1526
title: dev's gate is red on C3: T-1507 merged and its own spend ruling still hands pearsons_hiram to it, so the sign-off reads NO-GO and every PR into dev inherits the red
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: 2026-09-24
pr: 14
claimed_by: run 9/24/2026, 2:09:33 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-24T08:24:19Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35967839797
claimed_at: 2026-09-24T07:09:33.543Z
decision: null
decision_answer: null
---

dev's gate is red on C3: T-1507 merged and its own spend ruling still hands pearsons_hiram to it, so the sign-off reads NO-GO and every PR into dev inherits the red.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured 2026-09-24 on a clean `origin/dev` checkout at 6f995fc, and on GitHub: the
`Chicago 4D — gate` run for that commit is RED.** Four steps, one root cause, and every
branch cut from dev inherits all four:

    FAIL residents:…/pass_02_75_cohort.json#people/pearsons_hiram:
         unresolved ticket 'T-1507' is missing or not open
    FAIL rule the_reading_contradicts_the_trade_…_re_adjudicated:
         hands on to T-1507, which is 'done' and not live work
    FAIL docs/RESEARCH/research-closing-audit-2026-09.md is stale
    FAIL docs/RESEARCH/research-signoff-2026-09.md is stale   (rebuilds as NO-GO on C3)

## What happened

`tools/spend_trade_premises.py` carries `HANDED` — the one of its six outcomes that
DEFERS rather than answers — with `HANDED_TICKET = "T-1507"`. Its own comment says why
the ticket is named in the tool and not in the register: *"so that the register stays
derived, and the ledger's own ownership invariant is what proves it is live work rather
than a spent parent."* That invariant is exactly what has now fired. PR #7 rebuilt the
two reports for T-1507 at `review` — its third commit says so — and then the ticket went
`done` on merge, which is a state no commit in that PR could have written.

## What closes this

T-1507's work LANDED, so the unit is no longer waiting on a field: the reading it was
handed off for is carried on `data/research/residents/prose_role_readings.json`, which
#7 created for it, and from there onto `persons[].roles[]`. So this is a re-adjudication
of one rule and not a re-reading of anything.

- `HANDED` is re-ruled to the disposition its evidence now supports, with the statement
  saying what carries the reading and where — the `PROFILE` rule beside it is the shape
  ("The reading has reached a structured field; it is not waiting on one"), and whether
  the answer is that shape or an `asserted` row with a `wrote` entry naming the file and
  the field is the ruling this ticket is for. **Do not weaken C3 to make the red go away**
  — AGENTS.md's re-budget rule: say which of the two acts you are doing.
- `HANDED_TICKET` is retired or re-pointed, and the comment above it that explains the
  indirection is re-read rather than left describing a mechanism that no longer applies.
- The register, the closing audit and the sign-off are re-derived in the same commit, and
  the sign-off reads **GO** again.
- `./tools/check.sh` green — all four steps, on a tree cut from dev.

**Found by T-1506** (PR kevinrhaas/chicago#10), which gated clean on its own diff — 606 of
610 steps, the same four red on its branch as on untouched `origin/dev` — and could not
merge because of this. It is parked on `hold` until this lands.
