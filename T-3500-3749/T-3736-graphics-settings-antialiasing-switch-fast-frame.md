---
id: T-3736
title: Graphics settings: antialiasing switch, Fast frame pacing, and a line saying what is drawn
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-23
closed: null
pr: null
claimed_by: run 11/23/2026, 8:48:56 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-23T14:48:57.102Z
decision: null
decision_answer: null
---

Graphics settings: antialiasing switch, Fast frame pacing, and a line saying what is drawn.

Kevin, 2026-11-23: "Yes add them and organize integrate them cleanly so it it elegant and simple for people to understand" (all three of the proposed Graphics changes).

**Acceptance:**
- Settings > Graphics has an Antialiasing choice: Auto (off on a weak computer, on elsewhere), On, Off. It is a context-creation flag, so a change says it applies after a reload, and Use Auto restores Auto.
- Frame pacing offers Adaptive, Fast and Fixed. Fast is the weak-computer rule (T-3728: moving frames at 0.55 of Sharpness, still at 0.67, sun shadow every second frame; captures, photos and the welcome still full). Any device can pick it; Auto picks Fast on a weak desktop and Adaptive elsewhere.
- One line under the controls says what is actually drawn (detail, sharpness in force moving and still, antialiasing), so a governor cut is never hidden.
- The Graphics pane reads simply at 1280 and at 390: grouped, short labels, Auto first.
- People, horses, carriages and wagons are untouched by every choice. Phone defaults are unchanged.
