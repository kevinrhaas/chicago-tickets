---
id: T-2685
title: Home page destination cards play looping clips captured from each year
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
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

Home page destination cards play looping clips captured from each year.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 186 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner asked for it directly in the project thread on 2026-10-16 and asked that it be claimed now

Owner, 2026-10-16 (project thread): *"in place of the static images on the chicago 4d home page for each of the destinations ... have an actual images from the app, like a moving image of one of the best looking scenes from the target ... several in your library from each of the year destinations and rotate through them per load ... top down or of a building or sweeping up and around the river in a circle ... it should look like a seamless loop start and end at the same location, its ok if these are low res videos ... intentionally low res and can even flicker or be really pixelly at points because it should look like its an unstable connection, vary it some though, i dont want it constantly flashy"*.

**Acceptance:**
- Each of the three destination cards (1835, 1904, 1812) plays a short looping clip rendered from the app itself, picked at random per load from a library of about five clips per year.
- Every clip is a slow camera move (orbit, back-and-forth pan, top-down drift, sweep) whose first and last frames are the same pose, so the loop has no seam.
- Clips are deliberately low resolution. An "unstable connection" treatment (pixelation, flicker, signal drop) comes and goes per card at random; most of the time the picture is calm.
- Only the chosen clip per card is fetched. The current still stays as the poster and the fallback for reduced motion or a failed video.
- Works on the phone (390x780): no page errors, small total weight. The added bytes are reported in the PR.
