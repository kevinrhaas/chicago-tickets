---
id: T-3577
title: Window mode: stand where you are and look through a phone or iPad into the year (GPS + motion sensors)
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: 1980
claimed_by: run 11/12/2026, 9:08:58 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-13T03:08:59.683Z
decision: null
decision_answer: null
---

Window mode: stand where you are and look through a phone or iPad into the year (GPS + motion sensors).

The owner, 2026-11-13 (project thread "Add VR headset mode"): *"Would this vr stuff work on a good iPad and then we could geolocate and be on a corner and look around like it is a window"*, then *"Yes"* to building it as a Window mode on dev.

**Acceptance:**
- A Window key, offered on devices with motion sensors (phones, iPads), asks once for location and motion permission (iOS needs the tap), then sets the visitor down at their real position in the scene's year and turns the view as the device turns, compass-true.
- Outside the modelled area it says so and does not move the visitor.
- A one-tap "line up" nudge corrects compass drift; GPS accuracy is shown terse.
- Leaving Window mode hands the page's own controls back. Desktop and devices without sensors see nothing new.
- Gate green; smoke unchanged at 390x780 and 1280x800.
