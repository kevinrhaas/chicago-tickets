---
id: T-1525
title: Re-cut the reconstruction order book so the register's 120 documented residents can be minted: the south-side 20-29 trade bucket over-supplies by 25, and businesses/physician is ordered by a closed ticket
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-23
closed: 2026-09-25
pr: 12
claimed_by: run 9/24/2026, 1:08:47 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T10:46:53Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35962896257
claimed_at: 2026-09-24T06:08:47.167Z
decision: null
decision_answer: null
---

Re-cut the reconstruction order book so the register's 120 documented residents can be minted: the south-side 20-29 trade bucket over-supplies by 25, and businesses/physician is ordered by a closed ticket.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found by T-0841, 2026-09-24**, whose PR is kevinrhaas/chicago#8, on `hold` and carrying
the ladder half of the work already. That branch is the input to this ticket: rebase on it
rather than re-deriving the register reading.

## What T-0841 hit

The owner ruled that G2c reaches the parish register of 1833-1835 and its keeper. Landing
that moves `grading_proposal.json` (6,798 identities → 6,966; G2c 34 → 172), and the three
passes that SPEND the proposal then have to re-derive. They do, cleanly, and the mint is the
prize: **`mint_civic_residents.py --build` writes 120 NEW household cards** — the French,
Métis, Irish and German Catholic town the poll books never recorded, 150 of the pass's
cards carrying `church_evidence`.

`converge_resident_layer.py --run` then dies on the order book:

    build_order_book_1835.Fault: the bucket persons/male/20_29/south/family/trade
      is overfilled: 60 of 35

25 more documented tradesmen in their twenties on the south side cut that bucket's order
from 60 to 35, under the 60 already drawn against it. **The first half of this is already
fixed on #8** and is not this ticket's: the owner's ruling of 2026-09-20 (T-1459) says no
bucket's target falls below what has been drawn against it, and the book could not express
that for a PERSON bucket, because `quota_before` is computed from the residents layer as it
stands — so the moment the town reads documented people into a cell the pre-ruling quota
falls too and the test stops telling a re-cut apart from a filler. #8 extends the
`committed_order` fallback (60 = `filled`) to person and household buckets, keeping the
FAULT for a `filled` above even the order the work was drawn against.

**With that in, the book builds and hits the next one, which IS this ticket's:**

    FAIL: the book orders work from tickets nobody can claim — sweep the owner tables
    onto the live successors (T-1420): businesses/physician has 1 left and is ordered
    by T-1418, which is done

## Acceptance

- The order book builds and `--check` re-derives with the 120 minted cards in the layer.
- The `businesses/physician` bucket's 1 remaining slot is owned by a ticket a run can
  claim, by T-1420's sweep rather than by hand-editing the bucket.
- The 25-slot over-supply in `persons/male/20_29/south/family/trade` is named with both
  numbers in `what_the_re_cut_found`, and retired by the ticket that owns the bucket
  (T-1347) rather than absorbed here. **Nothing already drawn moves** — T-1459.
- `converge_resident_layer.py --run` reaches a fixed point, `node tools/rederive.mjs
  --check` agrees with it, and `./tools/check.sh` is green.
- The changelog entry on #8 already says the cards are owed to this re-cut; when they land,
  say so and name them.
