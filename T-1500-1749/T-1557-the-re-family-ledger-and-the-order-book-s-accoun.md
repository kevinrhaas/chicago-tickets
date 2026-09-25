---
id: T-1557
title: The re-family ledger and the order book's accounting of a move, with zero moves made
state: done
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1556
opened: 2026-09-25
closed: 2026-09-25
pr: 32
claimed_by: run 9/25/2026, 7:04:28 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T12:46:18Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36132515332
claimed_at: 2026-09-25T12:04:28.318Z
decision: null
decision_answer: null
---

The re-family ledger and the order book's accounting of a move, with zero moves made.

Piece 1 of 4 of **T-1556 — Re-family the 523 surplus reconstructed people the re-cut held rather than clamped, as ONE unit across all 48 buckets: the unadopted heads move into the buckets the re-cut GREW instead of being un-written — the owner's ruling of 2026-09-24 on T-1530**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The book has two words for a person — DRAWN, or not drawn — and the owner's ruling of
2026-09-24 needs a third. A re-family is neither a retirement (T-1459 forbids un-writing
anybody) nor a fresh draw (no stranger enters the town). Without a word for it, a move
would be indistinguishable from a deletion in every count the book keeps. This piece
builds that word and moves nobody: T-1558 models WHICH heads move, T-1559 spends them.

1. A move is recorded ON BOTH ENDS and `filled` is the arithmetic of the three numbers:
   the source keeps `drawn_here` (never lowered — nobody is un-written) and names
   `refamilied_out`; the destination names `refamilied_in`.
2. The ledger is DERIVED, carried off the committed book exactly as `fills` are, so
   `--check` re-derives it and `check.sh` refuses drift. A hand-written row cannot survive.
3. Every row names the person, the bucket he left, the bucket he entered, the order he
   filled, THE RULE that chose him, and the adoptions travelling with him — the last two
   because T-1556 § 8 makes both a condition of moving at all.
4. What a move may not do is a FAULT, not a convention: no re-sexing, no re-aging, no
   person moved twice, no bucket moving out more than was ever drawn in it, no landing in
   a bucket with no open order (the check the overfill gate cannot make on its own).
5. `recut_refusals` names what has left each bucket (`refamilied_out`, `surplus_still_held`)
   so the surplus can be read shrinking, and a bucket re-familied down to the re-cut's
   order stops being a refusal at all.
6. The book and its report state the shape of the programme from their own arithmetic:
   held surplus, open headroom, moves made, and what the town would still be owed at each
   end of the range. No number typed beside the table.
7. ZERO MOVES ARE MADE. A book with an empty ledger is bucket-for-bucket the book that
   stood before this ticket, and the self-test asserts it.

