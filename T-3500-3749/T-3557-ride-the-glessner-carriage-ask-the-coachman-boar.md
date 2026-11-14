---
id: T-3557
title: Ride the Glessner carriage: ask the coachman, board, ride a short round with Mr. Glessner aboard, stop and get down, by keyboard and touch
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: null
claimed_by: run 11/14/2026, 1:21:32 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-14T19:21:33.496Z
decision: null
decision_answer: null
---

Ride the Glessner carriage: ask the coachman, board, ride a short round with Mr. Glessner aboard, stop and get down, by keyboard and touch.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This is the carriage ride he asked for on 2026-11-09: "the existing nice carriage in front of Glessner House" is the first vehicle a visitor can ride. It replaces **T-2797** (board, ride and leave a carriage or wagon), which is withdrawn into it. T-2795 (running gear and hitches) and T-2801 (draft harnesses) are closed as done; any hitch work the moving ride still needs is part of this ticket.

## Already done on dev — reuse it, don't rebuild it

- The waiting Glessner team (#1908), individual horse coats (#1911), the coachman beside the team (#1917), visible pavement support (#1921), the draft hitch and tack (`draft-hitch.js`).
- Driven loops with turning wheels (`transport-loop.js`), Hans's brougham, the step-back-and-let-it-pass interaction (T-3475, #1846), Stop driver and Continue journey.
- ROOT's carriage-door work under T-2797 (door sweeps, optical door and glass views, evidence in chicago-evidence `evidence/transport/T2797/`); nothing of it is on dev yet, so pick it up from there.

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] Approach the coachman and ask for a ride (Interact); the door opens, the step is usable, the visitor boards and sits at the right eye height.
- [ ] The team pulls out, walks a short round of the block and comes back, wheels turning and the hitch moving with the horses. Mr. Glessner may ride as an identified passenger from his own record; the coachman stays the coachman.
- [ ] Stop and get down at any point, by keyboard and by touch; leaving a moving carriage stops it first. Reduced motion respected; no camera clipping; reload or a year switch never strands the camera.
- [ ] Desktop and phone (390×780) clip or shots of the whole round trip in the real scene, with frame cost. Route and activity recorded as reconstructed.

## Added from T-3564 (owner, 2026-11-12): the coach house doors open and the carriage goes in

Kevin, of his photographs of the 18th Street coach-house doors: "the main coach house door can open and a horse and carriage can enter according to normal standards of how that would work ... i imagine there would be like a driveway to the coach house as well". T-3564 builds the still parts: the two diagonal-boarded leaves with the man door (glessner_house.json `v4_detail.north_stable_fabric.carriage_leaves`, doorway W 134.9-147.0) and the carriage drive from the doors over the curb to the roadway (`data/street_section/1904.json` `carriage_drives`, `prairie_1800.carriage_drive`). What is left belongs here, with the ride: the two leaves swing (inward or outward as the hinges read on the photographs; renderers/web/js/house-doors.js already swings door leaves), the man door opens for people, and the Glessner carriage can drive in off 18th Street over that drive and out again. No new ticket (Kevin's ticket restraint).
