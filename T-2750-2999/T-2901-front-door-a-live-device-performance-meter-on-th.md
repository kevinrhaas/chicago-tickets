---
id: T-2901
title: Front door: a live device-performance meter on the Temporal Observatory, assessed during the Wolf Point opening
state: review
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-19
closed: null
pr: 1118
claimed_by: run 10/19/2026, 9:17:44 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-20T02:17:44.409Z
decision: null
decision_answer: null
---

Front door: a live device-performance meter on the Temporal Observatory, assessed during the Wolf Point opening.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 142 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> an owner ask is filed the moment it is made (AGENTS.md); it is worked in this same session

## The ask (owner, 2026-10-20, verbatim)

> On thing that I think might be nice on the home main screen is while you are doing the wolf point opening is to run an assessment of the device you are running on and have a meter that is a fluctuating meter that hovers around your quality level like a light up meter or bar that has maybe 5 levels or whatever makes sense for how you assess and grade the device GPU, browser memory etc. so that way on the home page you can get a reading/indicator of how good the performance will be by your device like if I have a great GPU and desktop with lots of memory it's always at near peak but if i have an old mobile with poor specs you would hover in the low yellow bad range vs high green for a nice device you will run well on. Quantify it on the home page the 4D temporal observatory, fit that in on the screen

**Acceptance:**
- The Temporal Observatory (`/4d/`) assesses the device during its cold start with the SAME reading the town boots on (`js/device-profile.js`: WebGL2 renderer, cores, memory, max texture, WebGPU, the fill + vertex benchmark), never a second invented scale.
- A lit segment meter with five grades shows the result as a 0-100 score; it hovers around the score (live, from the page's measured frame pacing), red/amber low to green high, and names the grade and the detail tier the town will boot at.
- Fits on screen at 1280x800 and 390x780 with no horizontal scroll; reduced motion shows it still; the manual says this reading is real, unlike the console's fiction.
- No change to how the town chooses its tier; zero page errors in the smoke.
