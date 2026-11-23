---
id: T-3734
title: Jaunt flights rise over the buildings and chimneys in their way, in every year, instead of passing through them
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-23
closed: null
pr: 2320
claimed_by: run 11/23/2026, 6:42:29 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-23T12:42:29.988Z
decision: null
decision_answer: null
---

Jaunt flights rise over the buildings and chimneys in their way, in every year, instead of passing through them.

Owner, 2026-11-23 (project thread "Keep jaunt flights clear of buildings"): *"when you fly on the jaunts in 1904 and probably others you will often clip fly though a building or chimney, when you fly if you run into a thing you should fly over or around"*.

Cause: both kinds of jaunt flight know only the ground. The timed glide (`travel.glide`, the flight to stop 1 and the closing look) flies a fixed arc, 0 m for a hop under 30 m and 18 m for a short one, whatever stands under it; the steered Fly ride between stops (`steerFlight`) climbs while moving forward, cruises at 20 m on a short leg, and comes down an 18° slope across the houses in front of the stand. The walker's fly mode keeps only 1.2 m off the terrain.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- Every flight a jaunt or Go to makes (the glide and the steered Fly ride) keeps the eye clear of the drawn buildings it passes, chimneys and towers included, and of the context city's stand-ins, in every year: 3 m above the tallest point of anything within 5 m of the eye's ground track, except over the stand it takes off from or lands on.
- It rises before it reaches a building, not when it is over it, and comes down onto the stand rather than through the house in front of it.
- A test flies real legs of 1904, 1871 and 1835 jaunts past their buildings and fails on any frame inside a building's clearance; it fails on the code before this change.
- Before and after pictures from inside the flight, desktop and phone, in the PR and the close note.
- No cost a weak PC can see: the clearance is looked up per flight, never a per-frame scan of the town.

## Completion (PR #2320)

Both jaunt flights now clear what stands in their way: the timed glide (flight to stop 1, the closing look) lifts onto a clearance profile worked out once as it sets off, and the steered Fly ride looks ahead and climbs before it reaches a roof, then comes down onto the stand. The index (`renderers/web/js/flight-clearance.js`) holds every drawn structure's whole box over its footprint and the context city's stand-ins, 1904 and 1871.

Measured in the published app, the same jaunts flown by air before and after: Glessner Household 166 frames inside a building before (deepest 10.5 m), 0 after; Pullman's Other Son 120 → 0; Who Started the Fire? (1871) 79 → 0; Fort Dearborn Errand (1835) 51 → 0; Across Wolf Point (1835) 15 → 0.

Before and after, the Glessner Household's second leg, the same moment of the flight (desktop, then phone):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/c899cdc81052c1535b5c84e2669612e16b2c10e8/evidence/T-3734/glessner-desktop-before-after.jpg?raw=true" width="900">

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/c899cdc81052c1535b5c84e2669612e16b2c10e8/evidence/T-3734/glessner-phone-before-after.jpg?raw=true" width="640">

1871, coming down onto the O'Leary lot:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/c899cdc81052c1535b5c84e2669612e16b2c10e8/evidence/T-3734/oleary-1871-desktop-before-after.jpg?raw=true" width="900">

Left as it is: trees are not in the index, and the flight goes over rather than around.
