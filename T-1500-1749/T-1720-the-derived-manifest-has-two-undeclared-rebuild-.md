---
id: T-1720
title: The derived manifest has two undeclared rebuild lags a merged tree walks straight into: location_spend reads a reconciliation four steps below it, and the three seating passes hand a row count along outside the sequence entirely
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "merged into T-1602"
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The derived manifest has two undeclared rebuild lags a merged tree walks straight into: location_spend reads a reconciliation four steps below it, and the three seating passes hand a row count along outside the sequence entirely.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured

Relapping T-1714 onto a `dev` that had moved twice (#150/#152, then #143/#151),
`node tools/rederive.mjs --resolve` failed twice on ordering, not on content.

**One: `location_spend.py` is four steps above the file it reads.** It is step 101
of 160; `ROWS` is `data/research/location_reconciliation.json.gz`, which
`location_reconciliation.py --build` rebuilds at step 104. On a clean tree both
reproduce, so the lag is invisible. On a merged tree it is not: dev had seated
`business_newberry_dole` on its own new packing house (T-1709), the `.gz` still
held the pre-merge rows, and the pass refused —

    Refused: business_newberry_dole: unseated, yet it seats on
             'recon_1835_blk_south_water_clark_c2_06'

which reads as a data fault and is an ordering one. `location_spend.py --check`
on a pristine `origin/dev` passes (179 businesses, that business
`structure_committed`), which is how the lag was told apart from a real breakage.
Running `location_reconciliation.py --build` first cleared it.

**Two: the three seating passes hand a row count along, and none of them is in
the manifest.** `seat_known_1835` → `seat_platted_ground_1835` →
`seat_off_plat_ground_1835` → `build_order_book_1835`, and the order book checks
the hand-off:

    Fault: the off_plat seating pass was offered 1369 rows and the pass before it
           handed on 1371 — the two files have moved apart

Because the first three are outside the sequence, a lap that rebuilds any of them
(the gate names them itself — "run tools/seat_platted_ground_1835.py --build")
must rebuild all three IN THAT ORDER and then run the whole sequence. Rebuilding
them in the order the gate happens to report the failures in does not converge:
it took the gate from 4 red steps to 7.

## Why it belongs in the manifest rather than in a run's head

`_the_second_pass` already documents exactly this shape for the arrival stage and
says the sequence "is a measured order, not a graph — its own `_doc` says so —
and this is the edge it cannot express." These are two more edges of the same
kind. Both are cheap to state and expensive to rediscover: each one cost a
foreground `--resolve` (about 160 steps) plus a gate lap to identify.

## What would discharge it

Either a declared entry per lag — a `second_pass`-style note naming the reader
and the file below it that rebuilds — or, for the seating chain, three manifest
steps in their hand-off order so `--resolve` walks them itself. `--prove` and
`audit_manifest_coverage.mjs` are the existing gates on such an addition, and
`_must_reproduce` is the bar: run each build on a clean tree and require that git
reports nothing moved.

## Not in scope

Nothing about the seating rules, the order book's buckets, or any count. This is
the manifest's order and only that.

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into T-1602.** All three are the derived manifest re-running steps out of order or too narrowly after the second pass; one run of manifest work fixes them together (measure with rederive --prove and audit_manifest_coverage). Work it there.
