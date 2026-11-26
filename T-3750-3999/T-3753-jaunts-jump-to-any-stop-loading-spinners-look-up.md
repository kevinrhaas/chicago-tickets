---
id: T-3753
title: Jaunts: jump to any stop, loading spinners, look-up freeze
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-25
closed: 2026-11-26
pr: 2351
claimed_by: run 11/25/2026, 10:18:40 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-26T06:12:27Z
claimed_run: null
claimed_at: 2026-11-26T04:18:41.776Z
decision: null
decision_answer: null
---

Jaunts: jump to any stop, loading spinners, look-up freeze.

The owner, 2026-11-26 (project chat, section 1 "Jaunts – General Improvements"):

- "Stop navigation: Allow users to jump directly to a specific stop within a jaunt rather than only progressing sequentially."
- "Loading indicators: Display a spinner or loading indicator on the play and navigation buttons while a jaunt or scene is loading."
- "Camera controls: Investigate an issue where users could not look up during a jaunt, sometimes it freezes and you can't look up."

**Acceptance:**
- The jaunt panel lists the jaunt's stops; tapping one goes straight there, back or ahead. Ahead, the stops between are passed on the route the visitor is on (a stop asking for a choice is not skipped past without one). A saved outing replays to the same place.
- Start, Continue, Replay and Restart on the Jaunts list, and Next stop / Back / a picked stop on the panel, show a spinner while the jaunt or the stop's scene is loading (its people still coming, the guide on the way).
- With the mouse, looking up and down always answers after the jaunt has turned the view for you (arrivals, flights, glides): no stuck ceiling.
- Desktop 1280×800 and phone 390×780 pictures.

## Completion (PR #2351)

Jaunt panel has a Stops key: the list of stops, tap one to go there (back or ahead, on the visitor's own route). Rings on the pressed key while a stop's scene loads, on Listen while the voice buffers, and on Start/Replay/Restart. Mouse look no longer sticks after a jaunt turns the view (the look controls' hidden pitch drifted to its limit; it is now reset each frame).

Before: the panel had only Back, Jaunts, End and Next stop; no stop list, no ring.

After (1835, Women of 1835 Chicago). Phone, the list and the jump to stop 4:

<img src="//github.com/kevinrhaas/chicago-evidence/blob/4683c813ad4720e84ec4b0248730e3a021e55416/evidence/T-3753/phone-stops-list.jpg?raw=true" width=320> <img src="//github.com/kevinrhaas/chicago-evidence/blob/4683c813ad4720e84ec4b0248730e3a021e55416/evidence/T-3753/phone-jumped-to-stop-4.jpg?raw=true" width=320>

Desktop:

<img src="//github.com/kevinrhaas/chicago-evidence/blob/4683c813ad4720e84ec4b0248730e3a021e55416/evidence/T-3753/desktop-stops-list.jpg?raw=true" width=640>

<img src="//github.com/kevinrhaas/chicago-evidence/blob/4683c813ad4720e84ec4b0248730e3a021e55416/evidence/T-3753/desktop-jumped-to-stop-4.jpg?raw=true" width=640>

Loading ring on the Stops key (panel rig, phone):

<img src="//github.com/kevinrhaas/chicago-evidence/blob/4683c813ad4720e84ec4b0248730e3a021e55416/evidence/T-3753/phone-loading-ring.jpg?raw=true" width=320>
