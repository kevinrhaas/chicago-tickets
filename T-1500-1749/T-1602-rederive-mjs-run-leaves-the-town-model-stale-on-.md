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
