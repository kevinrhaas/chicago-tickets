---
id: T-1773
title: The West's last freight roof: a two-storey warehouse at Lake and West Water facing the forks, built and baked
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1764
opened: 2026-09-30
closed: null
pr: 217
claimed_by: run 10/1/2026, 3:05:07 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36833749447
claimed_at: 2026-10-01T08:05:07.534Z
decision: null
decision_answer: null
---

The West's last freight roof: a two-storey warehouse at Lake and West Water facing the forks, built and baked.

Piece 1 of 2 of **T-1764 — The cabins and boarding houses of the forks, and Wolf Point's books closed: the pre-plat West roofs reconciled, the refusals resolved, the frame budget read, T-1208 handed on**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (stated before working — one demonstration, never weakened to pass)

- The order book's `structures/warehouses_freight/west` row reads 2 standing of 2: one F2
  narrow two-storey warehouse (hoist door, vertical boards) stands on plat lot 1 of
  `blk_west_lake_canal`, the Lake and West Water corner, its front on West Water and the
  South Branch at the forks, its rear toward the alley. Graded `reconstructed`
  throughout, with what bounds it written on the record and a `docs/LIBERTIES.md` entry.
- It clears the West Water corridor, traced water by 8 m or more (the memo's anonymous
  setback), every other footprint by 3 m, sits on dry modelled ground, and faces the
  street — held by a generator with `--check` and `--self-test` in `check.sh`.
- Baked with `bake.sh --only`, derived layers re-derived, `check.sh` green, the smoke
  parts `--for-diff` names green at both viewports.
- The row's owner moves from T-1764 to this ticket in `build_order_book_1835.py`.

**Why this piece, and not the cabins:** the West's remaining dwellings (24) are T-1208's
row and its boarding houses (4) are T-1209's, and both were claimed by sibling runs at
04:09Z on 2026-10-01; the one West row this split's parent owned outright was the freight
roof. The book-closing is T-1774, which cannot honestly close until those land.
