---
id: T-1556
title: Re-family the 523 surplus reconstructed people the re-cut held rather than clamped, as ONE unit across all 48 buckets: the unadopted heads move into the buckets the re-cut GREW instead of being un-written — the owner's ruling of 2026-09-24 on T-1530
state: split
epic: META
requested_by: owner
seen: false
effort: L
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T12:04:22.206Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Re-family the 523 surplus reconstructed people the re-cut held rather than clamped, as ONE unit across all 48 buckets: the unadopted heads move into the buckets the re-cut GREW instead of being un-written — the owner's ruling of 2026-09-24 on T-1530.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

The owner ruled this on 2026-09-24, answering T-1530 option (c): *"Re-family rather than
retire, as one unit for all 463. The book's own words are 'retired OR RE-FAMILIED'; the
surplus heads move into the buckets the re-cut GREW instead of being un-written, which
honours T-1459 and still fixes the over-supply."* T-1530 is parked `blocked-tech` on this
ticket, and every one of the other 47 buckets is this ticket's too — the point of the
ruling is that no single bucket's ticket sets the policy for all of them.

**What is measured on origin/dev today** (T-1525's re-cut of the order book; the 463 in the
question was read before that re-cut and is now 523):

- `recut_refusals` holds **48 buckets** and **523 people** drawn past what the re-cut
  would now order. 47 carry cause `the_re_cut_reached_work_already_drawn`, 1 carries
  `a_documented_reading_shrank_the_order` (`persons/male/20_29/south/family/trade`, 60
  drawn against an order of 32 — the bucket T-1530 was filed for, whose surplus is now 28
  rather than 25). All 48 sit in the `persons` family.
- Their `owning_ticket`s are T-1174 (24 buckets) and T-1347 (24). **Both are `done`**, and
  the three tickets the book's prose handed the surplus to — T-1196 (`done`), T-1197
  (`split`), T-1179 (`split`) — are closed too. Until this ticket the 523 had no live
  owner anywhere, and the T-1420 work-order gate could not see it: a refused bucket has
  `to_reconstruct` set down to `filled`, so it reads 0 left and the gate stays quiet. The
  PR that filed this ticket puts the hand-off in the book as a checked field and brings it
  under that gate.
- **There is room, and it is not unlimited.** 69 person buckets stand open with **427
  slots** of headroom between them. Re-familying a held head into an open order fills that
  order without drawing a new stranger, so each move takes one person off the remainder
  rather than out of the town.
- **How many should move is arithmetic, not taste.** 2,381 people stand in the layer and
  427 are still owed, so the book converges to 2,808 against a model point of 2,543
  (range 2,362-3,265). Moving **265** held heads into 265 of the 427 open orders lands the
  town exactly on the point. Moving all 427 would land it on 2,381 — inside the range but
  162 under the point, and it would empty every remaining order of its own draw. So the
  default is 265 moves, the remaining 258 held heads stay where they were written, and the
  book says both numbers.

**The invariant this has to reconcile, and must not quietly break.** A re-family LOWERS the
source bucket's `filled`, and T-1459's ruling of 2026-09-20 reads "a bucket's filled count
is never lowered, no already-drawn person is unwritten". The owner's answer holds that (c)
honours T-1459 because nobody is *un-written* — the person keeps his card, his id and his
grade, and only his bucket axes change. That reading is the one to build to, and it means
the book needs a re-family PATH rather than a filler path: a move must be recorded as a
move on both ends (source and destination), so `no_bucket_overfilled`, the refusal
machinery and `fills` all stay true, and no reader can mistake a move for a retirement or
for a fresh draw. Design that ledger before moving anybody.

**Acceptance**

1. A re-family ledger exists and is derived, not hand-written: every move names the person,
   the bucket he left, the bucket he entered, and the order he filled. It is re-derivable,
   so `check.sh` refuses drift in it.
2. No person is retired, no id is reused and no confidence is upgraded. `residence_grade`
   and every source citation travel with the person unchanged; what changes is the axes
   (sex is NOT one of them — a move may not re-sex anybody, and the destination bucket must
   match the person's own sex and age band).
3. 265 moves by default, and the number is stated with its reasoning: the book prints the
   held surplus, the open headroom, how many moved, and what the town converges to after.
   `converges_inside_the_model` stays green.
4. `recut_refusals` stays honest: a bucket whose surplus has moved out names both numbers
   as it does now, plus what left it. A refused bucket that has been fully re-familied stops
   being a refusal.
5. `held_surplus.owner` in the order book names a live ticket at every point — this ticket
   while it runs, its successor if it splits, and nothing when the surplus is zero. The
   T-1420 gate proves it on every `--build` and `--check`.
6. The 48 buckets are worked as ONE policy, not bucket by bucket. T-1530 unblocks when the
   `persons/male/20_29/south/family/trade` surplus is inside this ticket's ledger.
7. `docs/LIBERTIES.md` records the re-familying as what it is: a reconstruction decision
   about invented people, with the count, the rule that chose which heads moved, and the
   owner's ruling behind it.
8. The rule that chooses WHICH heads move is modelled and written down. It may not be
   "whoever failed to get a job" — the defect the owner named in rejecting option (a).
   34 of the 60 heads in T-1530's bucket alone are adopted by name elsewhere (23 hold an
   employment seat, 27 are named on business cards, 2 on lodging); an adopted head moving
   must carry those adoptions with him or not move.

**Size.** This is an **L** and `claim` will refuse it, which is correct — it is a programme,
not a run. The first run to take it should `split` it along the seams this ticket already
names: (i) the re-family ledger and the book's accounting of a move, with zero moves made;
(ii) the rule that chooses which heads move, measured against the adoption layers;
(iii) the 265 moves themselves, in bucket-family stages; (iv) LIBERTIES.md and the report.
Do not ship a self-invented "(1/4)".

