---
id: T-3406
title: 1812 story jaunts: every stop opens with how long since the last one (Four hours later, Four months later)
state: open
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-05
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

1812 story jaunts: every stop opens with how long since the last one (Four hours later, Four months later).

The owner, 2026-11-06 (project thread "Add elapsed-time leads to story jaunts"): *"one thing on the jaunts for battle of fort dearborn and murder, i think for each of the stops along with the date and time, you should start them with have like 6 months later, or a few hours later, or 4 hours later, to give people a sense of what they just left and how much time has past"*.

**Acceptance:**
- Every stop after the first in `battle-of-fort-dearborn` and `killing-of-jean-lalime` opens with how much time has passed since the stop before ("Within the hour", "Four months later", "Four hours later"), shown with the stop's date and hour.
- The interval agrees with the two stops' own `date` and `hour`; a check fails when a stop's date or hour moves and its lead is not updated.
- Jaunt tone kept: plain storytelling, no hedging. Compiles, passes the refusals; phone (390x780) and desktop checked.
