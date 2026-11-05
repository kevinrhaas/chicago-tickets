---
id: T-3391
title: Navigator Map close-up drawn crisp: footprints, streets and ground drawn at the window's own scale instead of a blown-up whole-field picture
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: 1728
claimed_by: interactive 11/5/2026, 1:51:29 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-05T19:51:30.525Z
decision: null
decision_answer: null
---

Navigator Map close-up drawn crisp: footprints, streets and ground drawn at the window's own scale instead of a blown-up whole-field picture.

Owner, 2026-11-05 (screenshot of SCR 05 at its close-up zoom): "at that zoom level its very lo-fi and it could be much cleaner".

Cause: the Map app's close-up (1.25 px/m, `map-view.js` NEAR_K) blits a window out of navigation.js's whole-field background, which is painted once at 0.25 px/m (SUPER / M_PER_PX). Each house is blown up about five times (ten device pixels per background pixel on a 2x screen), so footprints and streets smear into soft blobs.

**Acceptance:**
- Above the background's own detail, `drawView` draws the window afresh: ground sampled from the heightfield at its own 2.5 m cells, period streets and every footprint stroked as paths, culled to the window. The round HUD inset and any view at or below the background's scale keep the blit.
- Footprints read with hard edges at 1.25 px/m on desktop and 390x780; checked by screenshot in all four appearances.
- No new whole-field buffer: the only new canvas is window-sized and made on the first close-up. 1904 phone memory not raised.
- Map smoke (close-up and whole field inked, tap a building to preview, Go) still passes.
