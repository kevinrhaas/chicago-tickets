---
id: T-1671
title: rederive.mjs --run leaves manifest steps 77-121 standing on the resident cards its second pass rewrote, and only 122-159 are now re-run
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
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
