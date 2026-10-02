---
id: T-1965
title: House the town: every household's lives_at resolves to a standing structure, a vessel or a camp, the census's dwellings ratio held, the audit's unhoused count at zero
state: split
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1215
opened: 2026-10-02
closed: 2026-10-02
pr: null
claimed_by: run 10/2/2026, 8:21:34 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T13:27:11.760Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37011885513
claimed_at: 2026-10-02T13:21:34.372Z
decision: null
decision_answer: null
---

House the town: every household's lives_at resolves to a standing structure, a vessel or a camp, the census's dwellings ratio held, the audit's unhoused count at zero.

Piece 2 of 7 of **T-1215 — Converge the reconstructed town: every person housed, every business roofed, every roof occupied or its use stated, the census's dwellings ratio met, the programme reconciled, the budgets re-measured and set — the completion report a visitor can open**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## The gap, measured by T-1964 (2026-10-02, `data/render/town_completion_1835.json`)
1,917 households are unhoused (1,404 households/, 296 reconstructed_trades/, 121 readmitted/, 96 underdocumented/). **1,003 of them are present on the scene date**, listed in `housed.unhoused_present_households`; those are the ones the town owes a roof. 143 are housed (56 through `lives_at`, 87 seated by a structure's `residents[]`). 88 standing roofs name occupants in prose with no card linked (`occupied.occupants_in_prose_only`). Linking those is the cheapest housing there is. Done = `summary.households_unhoused` at zero, or each one stated. This is probably more than one run: split by division before claiming.
