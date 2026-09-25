---
id: T-1523
title: Carry the policy-only rung's division back onto the household card and data/residents/index.json through the carry slot the mint stages use, so no rung-5 household reads unplaced and the People view's division filter fills
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1513
opened: 2026-09-21
closed: 2026-09-25
pr: 49
claimed_by: run 9/25/2026, 2:49:53 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T22:26:32Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36181111897
claimed_at: 2026-09-25T19:49:53.428Z
decision: null
decision_answer: null
---

Carry the policy-only rung's division back onto the household card and data/residents/index.json through the carry slot the mint stages use, so no rung-5 household reads unplaced and the People view's division filter fills.

Piece 2 of 2 of **T-1513 — Seat the policy-only rung: the 1,186 households no source places anywhere, banded by the policy's class rule and dealt a division from the town model — seeded, order-book-counted, and every card's division re-derived so the People view's division filter fills**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## ⚠️ BEFORE THIS MERGES: landing it turns dev red unless one rule is repointed in the same PR (owner, 2026-09-25)

Measured on `origin/dev` at `4fead554`, `python3 tools/measure_research_spend.py --check`:

```
NOTE: 272 unresolved unit(s) defer to T-1198, a split parent held live by ONE leaf
(T-1523); when that closes, this gate goes red on all of them
```

The deferral is ONE rule: `data/research/residents/spend_rulings.json` →
`rules.the_enrichment_names_a_landholding_no_field_carries` (`disposition: unresolved`,
`ticket: T-1198`). These are 272 sourced LAND facts (a purchase, an original-town lot, a
holding) that no card field carries yet. T-1198 is `split`, and every other piece is
done or withdrawn (T-1491, T-1493, T-1522 done; T-1492 split; T-1516, T-1517 withdrawn).
So the moment this ticket settles to `done`, the ledger's ownership rule fires on all
272. dev goes red for every PR, exactly as T-1448 closing did to T-1189's units at
16:13Z today (#40 → T-1567/T-1568 → #44).

**What the PR that closes this ticket must also carry:** repoint that rule at the OPEN
ticket whose acceptance owns seating a landholding onto a card, or file one with
`ticket.mjs new --after` and point at it. It must not point at a closed ticket to clear
the red, and it must not change the units' disposition. Then show
`measure_research_spend.py --check`, `spend_remainder_rulings.py --check`, the closing
audit and the sign-off all green on the branch with T-1523 read as `done` (for example
by gating after `ticket.mjs done` in a scratch tickets clone). The same
applies to whichever run resumes PR #49.
