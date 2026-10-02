---
id: T-1971
title: House the present: the 1,003 households present on the scene date seated by a housing deal (rule, ledger, sidecar overlay), every seat on a standing dwelling, the census's people per dwelling held
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1965
opened: 2026-10-02
closed: 2026-10-02
pr: 277
claimed_by: run 10/2/2026, 8:27:16 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T14:30:04Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37011885513
claimed_at: 2026-10-02T13:27:16.336Z
decision: null
decision_answer: null
---

House the present: the 1,003 households present on the scene date seated by a housing deal (rule, ledger, sidecar overlay), every seat on a standing dwelling, the census's people per dwelling held.

Piece 1 of 2 of **T-1965 — House the town: every household's lives_at resolves to a standing structure, a vessel or a camp, the census's dwellings ratio held, the audit's unhoused count at zero**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. `tools/house_the_present_1835.py --build|--check|--self-test` writes
   `data/reconstruction/1835_housing_seats.json`: one seat per household present on
   1835-07-01 that no card `lives_at` and no other overlay houses; every seat on a standing
   reconstruction dwelling (never a documented building, never a roof whose record already
   names other occupants), in the household's own division where it has one; no household
   seated twice. In `check.sh` and the derived manifest.
2. `compile_scene.py` carries every seat onto the building card (`residents[]`), so T-1964's
   audit reads **0 present households unhoused** (from 1,003) with **0 dangling ids**.
3. The town is no more crowded than the census: people under a roof / standing dwellings
   ≤ 8.204 (3,265 in 398, November 1835), with the most crowded roof printed beside it.
4. LIBERTIES entry for the deal; changelog entry.
