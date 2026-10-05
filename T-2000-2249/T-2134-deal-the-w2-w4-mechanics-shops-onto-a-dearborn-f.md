---
id: T-2134
title: Deal the W2-W4 mechanics' shops onto a Dearborn face with the cross-street term: State is a light street and refuses a workshop, and every Dearborn corner lot of the blocks whose best face Dearborn is will be built or reserved once T-2130 lands, so first decide whether a corner lot's side street may carry a second principal roof, then deal, seat and bake
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-1684
opened: 2026-10-05
closed: null
pr: 481
claimed_by: run 10/5/2026, 8:31:38 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37316967785
claimed_at: 2026-10-05T13:31:38.371Z
decision: null
decision_answer: null
---

Deal the W2-W4 mechanics' shops onto a Dearborn face with the cross-street term: State is a light street and refuses a workshop, and every Dearborn corner lot of the blocks whose best face Dearborn is will be built or reserved once T-2130 lands, so first decide whether a corner lot's side street may carry a second principal roof, then deal, seat and bake.

Piece 2 of 2 of **T-1684 — The W2-W4 mechanics' shops have no State or Dearborn face to take: no platted-block slot in the whole recipe is dealt onto a cross-street face, and every Lake-Randolph block reads at_capacity**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1684 was split (2026-10-05T09:51:18.949Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 10/5/2026, 4:48:42 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37291989694) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37291989694) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Found while building T-2133 (#469), 2026-10-05.** The term is on dev: a slot whose `fronts` names its corner lot's side street stands off that side line (`generate_block_infill.py` `slot_frame` / `cross_street_frame`, demonstrated by `--self-test`). What this piece still has to settle:

- **Where.** `check_non_dwelling_slot` is unchanged, so State (`light`) refuses a workshop outright. A workshop on Dearborn (`ordinary`) is admitted only where no face of the block outranks it: `blk_washington_dearborn` and `blk_washington_clark` (Dearborn against `light`/unclassed faces), and `blk_randolph_dearborn` / `blk_randolph_clark` (a tie with Randolph). It is refused wherever Lake or South Water bounds the block. The schedule apportions `blk_washington_dearborn` **2 trade roofs**.
- **Density.** Once T-2130 (#466) lands, the Washington-Dearborn corner of `blk_washington_dearborn` carries a D7 and its Madison-Dearborn corner (lot 1) is the block's reserved open lot. The Clark block's Dearborn corners carry boarding houses. So a shop on Dearborn needs a corner lot's side street to carry a **second** principal roof behind the long-face house, which `check_block`'s "two principal roofs on one lot" refuses today. Decide that (with its arithmetic against `ROW_UNITS_PER_LOT` and the lot-ceiling sizing), or release the reserved corner with a written reason.
- **Downstream readers of `fronts`.** No committed record has ever fronted a cross street, so check the street-face tables (`adopt_street_faces`), the seating chain and `lot_addresses` against the first one dealt.
