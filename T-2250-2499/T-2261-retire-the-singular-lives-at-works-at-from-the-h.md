---
id: T-2261
title: Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads them
state: split
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-1274
opened: 2026-10-09
closed: 2026-10-09
pr: null
claimed_by: run 10/9/2026, 8:29:50 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-10T01:43:52.035Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38013053524
claimed_at: 2026-10-10T01:29:51.027Z
decision: null
decision_answer: null
---

Retire the singular lives_at/works_at from the household records, schema and validate.py once nothing reads them.

Piece 4 of 4 of **T-1274 — Move the renderers and tools off the singular lives_at/works_at once the plural rows carry every claim, and retire the pair**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding (T-2260, PR #598)

`tools/seat_known_1835.py` still reads `lives_at.basis.note` and `lives_at.replaceable_by.match`, for the address book's PROSE only. Its roofs, tiers and works seats come from the rows. A row's note is that basis with the copier's sentences appended, and a row has no `replaceable_by`. With the pair stripped, 34 `basis` and 11 `replaceable_by` strings change, and the garrison's 11 households lose "a plan of the post that assigns its quarters". Before the pair retires, give those words a home on the row (an optional `replaceable_by` key?) or rule that they go.
