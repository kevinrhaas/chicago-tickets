---
id: T-1575
title: The order book's re-family owner table names T-1556, which is split with no live piece: build_order_book_1835.py --build refuses on dev, so no branch can re-derive the book
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

The order book's re-family owner table names T-1556, which is split with no live piece: build_order_book_1835.py --build refuses on dev, so no branch can re-derive the book.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Measured working T-1545, 2026-09-25, on a clean `origin/dev` worktree with a fresh
tickets clone — so this is dev's red and not a branch's:

```
$ python3 tools/build_order_book_1835.py --check      # on origin/dev
FAIL: the book orders work from tickets nobody can claim — sweep the owner tables onto
the live successors (T-1420): the re-family programme's the_programme is ordered by
T-1556, which is split and has no live piece left — the programme ended with people
still held
$ python3 tools/build_order_book_1835.py --build      # on origin/dev
FAIL: (the same)
```

**What happened.** T-1560 — `the_programme`'s live piece — was closed `done` at
2026-09-25T17:50:47Z. Its parent T-1556 is `split` and has no other live piece, so the
order book's own T-1420 invariant ("every work order names a ticket a run can still
claim") goes red, and it goes red in `--build` as well as `--check`.

**Why that is worse than one red step.** `--build` refusing means the book cannot be
re-derived AT ALL. Any branch that changes something the book counts — a roof, a
household, a person — makes it stale and then cannot restate it, so that branch carries
either a stale book or no update. T-1545 hit exactly this: two West Division roofs
arrived, the book's `roofs to go` should fall by two, and the file was left at dev's
bytes because nothing could rewrite it. It is the same shape as T-1568 (T-1189's last
leaf closing red-ed the research ledger for every run) and wants the same remedy.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. `the_programme` names a ticket a run can claim, or the programme is settled and the
   book says the people are no longer held — whichever the evidence supports. Do not
   point it at a closed ticket to clear the red.
2. `build_order_book_1835.py --build` writes on dev, and `--check` is green.
3. The two roofs T-1545 landed are counted: the book's roofs-to-go falls by two on the
   first successful rebuild after this. State the before and after.
4. The general fault is named: a `split` parent whose pieces all close leaves a work
   order with no claimable owner, and the invariant fires only when somebody tries to
   build. Say whether closing the LAST piece of a split should be what refuses, and
   where that check would live.
