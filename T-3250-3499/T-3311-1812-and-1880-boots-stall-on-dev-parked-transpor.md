---
id: T-3311
title: /1812/ and /1880/ boots stall on dev: parked-transport.js returns before 'rows' is declared for scenes without parked vehicles, so the deferred update() hits a TDZ ReferenceError (T-3300 regression; memory (1812, desktop) red on #1605)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-02
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

/1812/ and /1880/ boots stall on dev: parked-transport.js returns before 'rows' is declared for scenes without parked vehicles, so the deferred update() hits a TDZ ReferenceError (T-3300 regression; memory (1812, desktop) red on #1605).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
