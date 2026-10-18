---
id: T-2785
title: The DEV pill and the arrival card's build stamp back on a phone (dev only); the full-width preview banner stays off it
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-18
closed: null
pr: null
claimed_by: run 10/18/2026, 11:21:34 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T16:21:34.842Z
decision: null
decision_answer: null
---

The DEV pill and the arrival card's build stamp back on a phone (dev only); the full-width preview banner stays off it.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 143 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-18 in thread iPhone 1904 crash: the dev marker tag and date time stamp for dev is now gone so that should come back

Reverses part of T-2629 (NAV-305, the owner's Navigator Mk II doc), whose finding was that the dev chrome covered the HUD's top row on phones. The full-width banner was the piece that did; the 43x21 px pill at the top-right corner sits over nothing but the scene (checked at 390x780 in 1904 free roam: elementFromPoint under it is the view).

**Acceptance:** on a phone-width dev build the DEV pill always shows and the arrival card prints `build <sha> · <time>`; the banner stays hidden on phones; desktop unchanged; production draws none of it; smoke part 13's T-2629 check updated to the new expectation.
