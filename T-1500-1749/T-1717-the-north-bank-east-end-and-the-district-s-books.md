---
id: T-1717
title: The north bank east end and the district's books closed: the Lake House's neighbours, the frame budget measured, the headroom stated
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1204
opened: 2026-09-28
closed: null
pr: 161
claimed_by: run 9/28/2026, 7:43:23 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36423159485
claimed_at: 2026-09-28T12:43:23.814Z
decision: null
decision_answer: null
---

The north bank east end and the district's books closed: the Lake House's neighbours, the frame budget measured, the headroom stated.

Piece 4 of 4 of **T-1204 — Build the fort reach and the lakefront to their seats: the sutler's, the garrison's outbuildings and the Agency establishment as the dossiers allow, the lighthouse keeper's, the pier-works yard at the river mouth, the Lake House's neighbours on the north bank east end**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding, 2026-09-28 — the lodging deal draws into slots the re-family programme already holds

Raising Eve Kelsey's boarding house is what PR #161 stops on, and the fault it
uncovers is not in the roof. It is in how `tools/seat_lodgers_1835.py` reads the
order book's room.

`book_lodging_room()` reads a lodging cell's `to_reconstruct` and ignores
`filled`, and its docstring says why: `filled` is this stage's own counter, so
taking it off the room would make the second build draw against a room the first
build had shrunk. That argument covers this stage's draws **and nothing else**.
`refamilied_in` is not one of them — it is the re-family programme (T-1558)
landing a head that the book counts against the very same order, and
`build_order_book_1835.py` refuses the landing when the cell has no open order
left for it: *"a move needs an open order to fill"*.

Measured on this branch, merged with `dev` at 8d726b27:

| cell | orders | this stage draws | re-family lands | total |
|---|---|---|---|---|
| `persons/female/20_29/north/lodging/none` | 5 | 4 | 2 | 6 |
| `persons/female/30_39/north/lodging/none` | 3 | 2 | 2 | 4 |
| `persons/female/30_39/west/lodging/none`  | 4 | 2 | 3 | 5 |
| `persons/male/10_19/north/lodging/none`   | 5 | 2 | 4 | 6 |

On `dev` every one of those four cells sits **exactly** on its order (3+2, 1+2,
1+3, 1+4). The arrangement has never had a slot to spare; it held only because
the stage happened to draw exactly the number the re-family programme had left.
One more lodging roof draws one more head in each and the book refuses the whole
ledger, which is the 8-of-681 red the first run on this ticket handed on.

Two repairs were tried on the branch and both were measured and reverted, because
each moves people who are already standing — the fault T-1503 and T-1525 exist to
prevent:

* **Netting `refamilied_in` off `book_lodging_room()`.** `allocate_within`'s
  capacity decides POOL MEMBERSHIP, so a cell dropped from the split moves every
  other cell's share under largest-remainder rounding. Twelve cells re-dealt.
* **Clamping the deal after the split**, which leaves the split byte-identical.
  It fixes the four cells, but the ceiling has to be the book's LIVE order (the
  frozen basis stands above it in some cells), and that quietly absorbs a re-cut
  that T-1525 says should stop the build and ask for a deliberate re-freeze.
  Seven beds shed, two of them from houses that are already standing.

And a third effect, unrelated to the order book and not caused by either repair —
it is on the branch as it stands. Inserting one house into the deal moved **38
seats** of real layer people between reconstructed lodging houses, and shifted
the invented-name pool under every mint after it, so the Steamboat Hotel's three
boarders and two of Wolf Point's come out as different invented people than on
`dev`. `dealt_last` (T-1535) exists to stop exactly this and does not catch it:
Kelsey's house is in its last group but sorts first inside it, and the seating
pass that runs before the deal has no such ordering at all.

So finishing this ticket needs a ruling on which way the room is read, and the
repair has to carry the seating pass and the name pool with it. That is the work;
the two roofs and their research are done and stand on the branch.
