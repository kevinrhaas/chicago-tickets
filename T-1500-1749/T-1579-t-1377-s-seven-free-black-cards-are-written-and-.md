---
id: T-1579
title: T-1377's seven free Black cards are written and never reach the town: compile_scene reads one sub-stage report of the underdocumented stage and the People view has never held them
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
decision: null
decision_answer: null
---

T-1377's seven free Black cards are written and never reach the town: compile_scene reads one sub-stage report of the underdocumented stage and the People view has never held them.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Found while wiring T-1504's `church_register` sub-stage into the scene, 2026-09-25.

**What is wrong.** `tools/compile_scene.py` builds the People view's `underdocumented`
rows out of ONE report file. Until T-1504 that file was
`data/reconstruction/1835_native_and_metis.json` and nothing else, so T-1377's seven
`hh_fb_*` cards — written, gated, `review_required`, standing in
`data/residents/underdocumented/` since they were minted — have never reached
`data/sidecars/1835/people.json` at all. Measured: 94 cards in that directory, 87 of
them `hh_um_` and 7 of them `hh_fb_`; 87 rows in people.json carrying an `hh_um_`
household and **0** carrying an `hh_fb_` one.

**Why it went unseen.** The block's own tally has always been able to count more
cohorts than the block could feed it — `underdocumented_by_sub_stage` groups the rows by
`sub_stage`, which only ever reads back the one sub-stage the single path supplied. A
counter that can only ever print one key never looks wrong.

**Why it is not a passenger on T-1504.** Seven people arriving in the People view moves
every resident tally that reads it, and a change to who the town holds owes its own gate
and its own changelog line. T-1504 turned the single path into a LIST and put its own
report in it; this ticket adds the second line and re-gates what that moves.

**And it bears on the owner's own ruling.** AGENTS.md, 2026-09-17: *"it is also very
important that we keep and capture and identify the black owned businesses and residents
and family households."* The cards exist. The town does not show them.

**Acceptance:**

1. `data/reconstruction/1835_free_black.json`'s minted rows reach the People view through
   the same list T-1504 built, and the seven cards are rows a visitor can open.
2. What the arrival MOVES is measured before and after — every resident count, ratio and
   segment that reads people.json — and the ones that move are named with their old and
   new figures rather than left to be discovered.
3. `underdocumented_by_sub_stage` prints three keys and their sum is the row count.
4. A gate refuses the next cohort that is written and not listed: a card in
   `data/residents/underdocumented/` whose id prefix no report in the list accounts for
   is a card the town cannot see, and that must go red rather than go quiet.
