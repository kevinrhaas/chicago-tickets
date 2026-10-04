---
id: T-2065
title: The derived manifest's in-sequence lags T-1602 left: location_spend reads the reconciliation a later step rebuilds, the seating passes sit outside the manifest, and nothing gates the 84-132 answer
state: split
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-03
closed: 2026-10-04
pr: null
claimed_by: run 10/4/2026, 5:52:08 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T10:53:38.328Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37196588788
claimed_at: 2026-10-04T10:52:08.625Z
decision: null
decision_answer: null
---

The derived manifest's in-sequence lags T-1602 left: location_spend reads the reconciliation a later step rebuilds, the seating passes sit outside the manifest, and nothing gates the 84-132 answer.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 199 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1602 had T-1671 and T-1720 folded into it; PR #382 closed T-1602's own acceptance (the stale model) and not theirs, so without this line the folded work left the queue when T-1602 settled done. Net zero: T-1602's line left as this one joins.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Carried from T-1602 (2026-10-04, PR #382)

T-1602 had **T-1671** and **T-1720** folded into it. PR #382 closed T-1602's own acceptance:
- The town model now leads the second pass, with `reads_rebuilt` naming the scene's `people.json` and `town_census.json`.
- `--run` now ends with a declared `after_the_pass` tail from `compile_scene.py`, repeated until a lap moves nothing.

The folded tickets' acceptance is NOT done, and is this ticket's. Their measurements are written in full under T-1602's "Folded in from T-1671" / "Folded in from T-1720" sections; read them there.

**Acceptance:**
1. **`location_spend.py` (now step 106) reads `data/research/location_reconciliation.json.gz`, which `location_reconciliation.py --build` rebuilds at step 111.** Either the order moves (check what 107–110 feed the reconciliation before moving it), or the lag is declared. Then a merged tree with a moved seat must pass `--run` without a hand step.
2. **`seat_known_1835` → `seat_platted_ground_1835` → `seat_off_plat_ground_1835` → `build_order_book_1835` hand a row count along, and the first three are not in the manifest.** Add them in hand-off order under `_must_reproduce` (a build on clean dev moves no byte). Otherwise, say in `audit_manifest_coverage.mjs`'s NOT_DERIVABLE list why they cannot be added.
3. **The 84–132 sensitivity question**, which is T-1671's step 3: a gate holds the answer, so a step inserted between the pass and `after_the_pass.tail_from` cannot reopen it.

**What #382 measured toward (3), as evidence and not proof:** on dev, I took `people.json`, `town_census.json` and the model from before #344. The new `--run` (sequence, the 4-step pass, then the scene tail ×3) ended byte-identical to dev. So nothing between the pass and `compile_scene.py` was left moved, apart from the pass's own steps. That is one reproduction, not a per-input reading of each step.
