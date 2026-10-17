---
id: T-2736
title: The HUD target tag fades: shown after the 400 ms dwell, it fades out a few seconds later and when you look away, and wraps to show the whole name and distance instead of cutting it off with an ellipsis
state: review
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-17
closed: null
pr: 985
claimed_by: run 10/17/2026, 1:41:59 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T18:42:00.001Z
decision: null
decision_answer: null
---

The HUD target tag fades: shown after the 400 ms dwell, it fades out a few seconds later and when you look away, and wraps to show the whole name and distance instead of cutting it off with an ellipsis.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 146 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner bug report 2026-10-17 with screenshot: the target tag hangs in the view and its text is cut off

## Report

Owner, 2026-10-17, thread "Look-at label that never fades", with a dev 1904 screenshot on the Prairie Avenue
sidewalk showing `1612 PRAIRIE AVENUE — JOSEPH GOODMA…` under the reticle: *"your new messages for what you are
lookin at stay up and then there is no way for them to disappear and they hang there, it seems like if you see it
it should show and then disappear on the point, and also the interesting info gets cut off on the box, figure out
how to display the full info consistently"*.

Cause: the T-2627 target tag (`renderers/web/js/target-tag.js`, `.target-tag` in `walk.css`) hides only when the
probe's answer changes, so standing or walking with the same building in the reticle keeps it up indefinitely;
its CSS is `white-space: nowrap; text-overflow: ellipsis` inside `max-width: min(320px, 100vw - 120px)`.

**Acceptance:**
- After the 400 ms dwell the tag shows, holds a few seconds, then fades out on its own; it does not come back
  for the same building until the reticle has left it (looking away and back shows it again).
- Looking away still hides it at once, as before.
- The full name and distance always show: the tag wraps to a second line (desktop and a 390 px phone) and never
  ends in an ellipsis.
- The quick column's Inspect key stays while the building is in the reticle, so Inspect is still one tap away
  after the tag fades.
- tools/test_navigator.mjs covers the hold, fade and re-show; before/after screenshots in the project folder
  look-at-label/.
