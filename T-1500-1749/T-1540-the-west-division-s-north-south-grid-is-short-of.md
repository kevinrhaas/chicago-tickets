---
id: T-1540
title: The West Division's north-south grid is short of the plat's 458 ft module on EVERY interval, not only Clinton to Canal: say which of the two controls seats these five lines, what moves if the plat wins, and what is seated on the short spacing today
state: done
epic: GROUND
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: 2026-09-24
pr: 25
claimed_by: run 9/24/2026, 8:00:12 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-24T14:35:44Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36001914710
claimed_at: 2026-09-24T13:00:12.150Z
decision: null
decision_answer: null
---

The West Division's north-south grid is short of the plat's 458 ft module on EVERY interval, not only Clinton to Canal: say which of the two controls seats these five lines, what moves if the plat wins, and what is seated on the short spacing today.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. Every north-south line the West Division carries is DERIVED from the committed street
   file — never typed here — and each one carries the CONTROL that seated it, read off
   its own record rather than restated, so a line re-seated tomorrow arrives on its own.
2. The disagreement is measured on EVERY interval, not on one: the committed centreline
   spacing against the plat's printed street module, interval by interval and across the
   whole division, with the sheet's own figure and its confidence carried.
3. Each gap is tested against `data/datum.json`'s own coordinate residual, so an interval
   that cannot be told apart from georeferencing noise is not reported as a defect, and
   one that exceeds it is.
4. Whether the committed grid is a SCALED COPY of the plat is answered arithmetically: a
   uniform module cannot produce unequal intervals, so the spread between the intervals
   decides it and the figure that decides it is published.
5. What moves if the plat's module wins is computed for EACH candidate anchor — the line
   with a physical control and the line with the best modern survival — with every other
   line's displacement, so "move Clinton" can be priced instead of asserted.
6. What is seated on the short spacing today is COUNTED from the committed layers —
   blocks, lots, structures, seated rows — not estimated.
7. Nothing moves: no centreline is edited, no block re-emitted, no record re-seated.
8. `--check` re-derives the order byte for byte and is in `tools/check.sh`; `--self-test`
   fires and is gated beside it.
9. T-1479's refusal prose stops pointing at closed tickets. `tools/generate_plat_lots.py`
   and `tools/measure_west_grid_migration.py` name THIS ticket as the one that owns the
   street move, and the migration gate asserts it is OPEN — so the day it lands, that
   finding goes red rather than stale.

**Why it exists.** The owner's ruling on T-1479, 2026-09-21 (question 1 of 3): *"Clinton
to Canal stands at 367.9 ft against the plat's 458 ft. That 90 ft is a real defect and it
is nobody's: T-0444 and T-0445 both closed without moving it, which is how a measured
error becomes part of the town by default. A successor ticket owns it. … THE SUCCESSOR
OWNS THE WHOLE QUESTION, not just the number … A ticket that only says '458 not 367.9'
will close the same way its two predecessors did."* T-1479 is blocked on this one.
