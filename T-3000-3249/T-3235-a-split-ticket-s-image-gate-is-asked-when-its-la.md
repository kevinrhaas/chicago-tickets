---
id: T-3235
title: A split ticket's image gate is asked when its last piece closes, and Pullman's match records reopened where missing elements were passed as within tolerance
state: done
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-28
closed: 2026-10-28
pr: 1421
claimed_by: run 10/28/2026, 10:47:22 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-28T17:44:42Z
claimed_run: null
claimed_at: 2026-10-28T15:47:23.987Z
decision: null
decision_answer: null
---

A split ticket's image gate is asked when its last piece closes, and Pullman's match records reopened where missing elements were passed as within tolerance.

## Owner's report (2026-10-28, thread "Rework Pullman estate photo match")

Owner, 2026-10-28: *"in looking at 1729 prairie, the pullman estate it seems like tickets are closed and the gate is exited, but it is still way off from a photographic match, the stepped front, the south face, the entire greenhouses and the stable are all way off, not to mention the greenhouse area south of 18th, am i wrong? did you consider it done? because its not and you need to reenter the photographic match on that one if not"*.

What happened:
- `ticket.mjs split` closes the parent (`split`) without asking the image gate, and the pieces it mints carry no `## Image gate` section, so `done` never asked it again. T-1881 (house) split into T-3157..T-3161 and T-1934 (stable and conservatory) into T-3164/T-3165 -> T-3177/T-3178/T-3179 -> T-3192/T-3193; every piece closed while `pullman_house_1729_prairie`'s three match records still read `differs`.
- The stable, palm-house and glasshouse records were set `matches` by marking missing or mis-shaped elements (columns, balustrades, rustication, cresting, arched lights, a faceted dome, gaps of 0.6-1.5 m) `within tolerance`, which T-3153 reserves for gaps a street visitor would not notice.
- The same split escape closed eight other houses whose records read `differs` or have no camera; the owner chose to reopen them below Pullman (decision card, 2026-10-28).

**Acceptance:** `done` on the last live piece of a split ancestor that carries an `## Image gate` section runs that ancestor's gate and refuses while its buildings do not match (a piece in `review` counts as closed; nested splits are walked); `split` writes into each piece that the gate stays on the parent; a fixture test proves it (fails on the old tool) and runs in check.sh; AGENTS.md rule 11 and data/reference_views/README.md say so; the Pullman match records' misfiled `within tolerance` differences are set `open` and their verdicts `differs`, with the owner's report written into the house's, the palm house's and the 18th Street glasshouses' records.
