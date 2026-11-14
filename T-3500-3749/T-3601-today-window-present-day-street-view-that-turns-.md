---
id: T-3601
title: Today window: present-day Street View that turns with you
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-14
closed: 2026-11-14
pr: 2056
claimed_by: run 11/14/2026, 3:40:09 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-14T23:53:28Z
claimed_run: null
claimed_at: 2026-11-14T21:40:10.989Z
decision: null
decision_answer: null
---

Today window: present-day Street View that turns with you.

Owner, 2026-11-14: "Is there a way to do this corner today and show the view from the street view side of Google Maps or Apple and show what that view is today in a window? Would be cool if you could have a small expandable today window that would sync along with the main window, you could hide or show that window".

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- A small Today window under the THEN/TODAY readout shows Google Street View at the walker's spot, aimed where they look, and follows as they walk and turn (all years).
- It expands and shrinks, and hides/shows from the TODAY tag, its own close key and Settings › Show; the choice is remembered.
- Nothing from Google loads until the window is first shown; hidden, it costs nothing per frame. Panorama lookups are throttled by distance and time, point-of-view sets by time.
- Without a key it is a card with the heading and Google Maps' keyless Street View link; with the owner's key (today-view-config.js, restricted to the site's hosts) it is the live panorama.
- Local metres to lat/lng agree with pyproj (EPSG:26916) to a centimetre; grid bearings become true headings.
- Apple Look Around rejected: MapKit JS takes no heading, so it cannot turn with the walker.

## Completion (PR #2056, merged to dev 2026-11-14)

The Today window shipped. Tap TODAY under the compass for Google Street View today at your spot, turning and following as you walk; expand, open in Google Maps, hide; Settings › Show › Today window. Nothing from Google loads until it is opened. Until the owner's Maps JavaScript API key goes into `renderers/web/js/today-view-config.js`, visitors get a card with the heading and Google Maps' keyless Street View link.

**Before** (1904, Prairie & 18th, desktop and phone):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/desktop-before.jpg?raw=true" width="640"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/mobile-before.jpg?raw=true" width="200">

**After, live** (Google's keyless development mode, hence washed out and watermarked; NNE 028°, then turned to E 090° and the panorama followed):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/desktop-live.jpg?raw=true" width="420"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/desktop-live-turned.jpg?raw=true" width="420">

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/mobile-live.jpg?raw=true" width="200"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/mobile-live-turned.jpg?raw=true" width="200">

**After, until the key is added** (the card):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/desktop-link.jpg?raw=true" width="420"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9aced37a150f763ef084b1c99621ae66f721970f/evidence/today-window-T-3601/mobile-link.jpg?raw=true" width="200">
