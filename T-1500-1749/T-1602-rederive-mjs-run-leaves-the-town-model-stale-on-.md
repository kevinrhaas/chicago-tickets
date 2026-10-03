---
id: T-1602
title: rederive.mjs --run leaves the town model stale on any branch that adds residents: model_town_1835.py reads the sidecar compile_scene rebuilds after it, and the second pass does not carry it, so a clean full rebuild still fails check.sh
state: open
epic: META
requested_by: owner
seen: false
effort: S
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

rederive.mjs --run leaves the town model stale on any branch that adds residents: model_town_1835.py reads the sidecar compile_scene rebuilds after it, and the second pass does not carry it, so a clean full rebuild still fails check.sh.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured twice on 2026-09-25**, landing #50 (T-1504, which adds residents from St Mary's register) onto a moving dev. Each time `node tools/rederive.mjs --run` completed cleanly (158 steps, then the second pass of 3). Then `./tools/check.sh` failed exactly one step:

```
FAIL: the 1835 town model is stale — run --build
FAIL: the 1835 town model report is stale — run --build
  * the 1835 town model re-derives, and every figure is bounded and says what it rests on
```

One `python3 tools/model_town_1835.py --build` fixed it, and nothing downstream moved (the order book, the population profile and `compile_scene --all --check` all re-check green). Each occurrence cost a full extra gate cycle. The PR lap runs the same `rederive.mjs --run`, so it will leave the same stale model on any resident-adding PR it laps.

**Why.** `model_town_1835.py` reads `data/sidecars` and `data/town_census.json` (its declared reads in `1835_resident_layer_rebuild_order.json`). `compile_scene.py --all`, which rewrites `data/sidecars/1835/people.json`, runs later in the manifest's order on such a branch. `second_pass` in `tools/derived_manifest.json` re-runs only `attribute_fill_arrival`, `migrate_attribute_tiers` and `profile_population_1835`, so nothing rebuilds the model after its input moves.

**Acceptance.** After `rederive.mjs --run` on a branch that adds residents, `check.sh` is green with no hand step. Either the town model (and its report) is carried in the second pass with its `reads_rebuilt` named, or the order is corrected so the model is built after the sidecar. State which, and why the other is wrong. `rederive.mjs --check`'s `_the_second_pass` shape check accepts it. A fixture or a measured branch shows the stale model no longer survives a `--run`.


## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into this ticket:** T-1671, T-1720. All three are the derived manifest re-running steps out of order or too narrowly after the second pass; one run of manifest work fixes them together (measure with rederive --prove and audit_manifest_coverage).

### Folded in from T-1671 — rederive.mjs --run leaves manifest steps 77-121 standing on the resident cards its second pass rewrote, and only 122-159 are now re-run

rederive.mjs --run leaves manifest steps 77-121 standing on the resident cards its second pass rewrote, and only 122-159 are now re-run.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

The manifest's second pass (`_the_second_pass`, T-1363) re-runs three steps AFTER the
159-step sequence: `reconstruct_residents_1835.py --stage attribute_fill_arrival --build`,
`migrate_attribute_tiers.py --build` and `profile_population_1835.py --build`. Those three
sit at manifest indices **76, 102 and 105**. So everything the manifest places below index
76 — steps 77 through 159 — may be standing on resident cards, tiers and a population
profile the pass has since moved.

T-1661 closed the half of that hole the PR lap had already discovered by hand: the lap
re-runs `compile_scene.py` late, and now re-runs it with `rederive.mjs --tail`, which
carries steps **122-159**. Steps **77-121** are still re-run by nobody.

**What is NOT known, and is the whole ticket:** whether any of 77-121 is actually
sensitive to what the second pass writes. `check.sh` asks `--check` of most of them, and
laps have been going green on those steps, which is evidence they settle — but it is
evidence, not a reason. The manifest's own doc claims only that "model, profile, tiers and
residents all --check green afterwards", which is the cycle, not its downstream.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. For each of steps 77-121, say whether it reads anything the second pass writes —
   measured, from the step's own inputs, not asserted.
2. Either the sensitive set is empty and the manifest says so where a reader will find it,
   or `--run` carries a tail over them the way `--tail` now carries 122-159, with the cost
   measured.
3. A gate holds whichever answer it is, so the next step inserted at 90 cannot reopen it.

Found by T-1661, which measured the 122-159 half and is where the reasoning stops.

## MEASURED, 2026-09-28 (loop): one of 77-121 IS sensitive, and it is step 99

This ticket's open question — "whether any of 77-121 is actually sensitive to what the
second pass writes" — has one confirmed instance, found the way the ticket predicted:
by a merge, not by a lap going green.

`rederive.mjs --run` on a merge of `dev` (carrying T-1712 and T-1709) into the T-1714
branch **died at step 99**:

```
[99/160] python3 tools/location_spend.py --build
FAILED: Refused: business_newberry_dole: unseated, yet it seats on
        'recon_1835_blk_south_water_clark_c2_06'
```

The cause is an ordering lag INSIDE the sequence rather than one the second pass
introduced, which widens this ticket rather than answering it:

- `location_spend.py` (step **99**) reads `data/research/location_reconciliation.json.gz`
  for `row["business_limit"]` and `row["resolved_structure"]`.
- `location_reconciliation.py --build` (step **104**) is what REBUILDS that file, and the
  manifest declares it under `resolves`.

So step 99 prices its assertion against the committed reconciliation, and on a tree where
that file is stale the two disagree: T-1709 moved `business_newberry_dole` from a
`street_only` seat on a reconstructed roof to a `structure` seat on its own new packing
house, and until step 104 runs, step 99 still reads the old pair and refuses it as
"unseated, yet it seats on …".

**Running `python3 tools/location_reconciliation.py --build` by hand first, then
`rederive.mjs --tail tools/location_spend.py`, cleared it** — after which the same run
took `./tools/check.sh` to 679/679 green. `adopt_street_faces.py` (step 109) is NOT the
fix and was ruled out by measurement: rebuilding it leaves `business_newberry_dole` absent
from both `adoptions` and `refusals`, because the business is not a street-face case at
all once the reconciliation is current.

**Why this matters beyond one business:** nothing in the gate catches it. `check.sh`
asks `--check` of both tools and both pass once the sequence has been walked by hand, so
the hole is invisible except to an operator running `--run` on a merge — which is exactly
the situation `--resolve` exists for. A merge lap that cannot get past step 99 has no
message telling it to run step 104 first.

### Folded in from T-1720 — The derived manifest has two undeclared rebuild lags a merged tree walks straight into: location_spend reads a reconciliation four steps below it, and the three seating passes hand a row count along outside the sequence entirely

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
