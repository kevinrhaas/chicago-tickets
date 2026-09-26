---
id: T-1603
title: The Eagle Coffee House, Trowbridge's, is a named public house of the scene year that the structure layer does not hold: build the record or refuse it in writing
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: null
claimed_by: run 9/25/2026, 11:51:51 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36217768986
claimed_at: 2026-09-26T04:51:51.670Z
decision: null
decision_answer: null
---

The Eagle Coffee House, Trowbridge's, is a named public house of the scene year that the structure layer does not hold: build the record or refuse it in writing.

**Acceptance.** The Eagle Coffee House is ruled ONE way in writing, against a stated rule,
and the ruling is reachable from both the reading that raised it and the file the next run
would reach for when it thinks about building the house. Specifically:

1. `data/research/spend_rulings.json` no longer carries an `unresolved` rule pointing at this
   ticket. The reading `chicago_democrat_1835_06_24#c001` closes against a rule that states
   what was decided and why, and the rule that handed it here is GONE rather than left in the
   file as dead prose (it would also turn the gate red the moment this ticket closes).
2. The ruling states the STREET evidence as it actually stands, not as the hand-off found it.
   The hand-off said the preposition in the Abell advertisement "is destroyed by the
   interleave, so the street is nearly there and the seat is not". That is true of the 24 June
   printing and is not the whole corpus.
3. Whichever way it is ruled, `data/exclusions.json` says so, so the next run does not build a
   public house on an invented Dearborn frontage — and the entry carries a `reason` and a
   `sources` array that resolves, because `validate.py` requires both.
4. `tools/check.sh` is green with no step standing on a skipped reading, and the derived
   register is not hand-edited (`compile_register.py` re-derives it and the gate re-checks it).

**Not in scope, stated so the refusal cannot be read as an oversight:** no coordinate is
invented, no structure is raised, no mesh is baked, and the newspaper corpus under
`data/research/newspapers/extracted/` is not edited — a note there is a transcription record
and re-writing one re-derives the gazetteer and the register behind it, which is a second
unit's worth of work and is not needed to rule this reading.
