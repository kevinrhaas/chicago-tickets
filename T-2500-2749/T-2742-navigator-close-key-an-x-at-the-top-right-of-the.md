---
id: T-2742
title: Navigator close key: an X at the top right of the open device that closes it like the collapse arrow, styled to match it on every appearance, with a 44 px touch target on a phone
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-17
closed: null
pr: 988
claimed_by: run 10/17/2026, 2:02:42 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T19:02:42.553Z
decision: null
decision_answer: null
---

Navigator close key: an X at the top right of the open device that closes it like the collapse arrow, styled to match it on every appearance, with a 44 px touch target on a phone.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 149 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner request 2026-10-17 in the project thread; no Navigator band ticket covers a close key, and it is worked and closed in the same session

Kevin, 2026-10-17 (project thread "Navigator close button"): *"on the upper right of the navigator i think you should have an X box button that has the same behavior as the collapse arrow ... maybe some kind of hybrid <x button ... if it does not look cool ... just make it like a more classic x that people will understand that it closes/collapses that window"*. He pointed to Claude's own expand/close pair (an arrows icon and a plain X) as the familiar pattern.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The open Navigator shows a close key at the right end of its header on desktop (panel) and phone (HALF and FULL); it is gone while the device is docked (rail or pill).
- [ ] It does what the collapse arrow does: desktop to the rail, phone to the dock, focus to the handle that reopens it. A tap on it never starts a sheet drag or reopens the device through the header's own tap.
- [ ] The X and the rail's collapse arrow are the same kind of key: same stroke, ink, hover wash, radius and focus ring, from skin tokens only, on Control Room, Precision Brass, Retro Future and Deep Space.
- [ ] Its hit area is at least 44 x 44 px on a 390 px phone; the screen code still truncates cleanly beside it.
- [ ] Labelled from the string table ("Close the Navigator"); the 390x780 mobile smoke (the release gate) passes.
