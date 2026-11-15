---
id: T-3557
title: Ride the Glessner carriage: ask the coachman, board, ride a short round with Mr. Glessner aboard, stop and get down, by keyboard and touch
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
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

## Added from Kevin (owner, 2026-11-14): board and drive any team

Kevin, thread "Board and drive horse teams": "One of the things with carriages and horses and wagons was we wanted to be able to board and drive the team around." So boarding is not only the Glessner ride: every driven team in every year (1812 fort wagon and shore-road haul, 1835 Western Hotel wagon, 1904 Hans's, the Pullman and the Armour broughams) can be boarded, and the visitor can take the reins and drive it, by keyboard and touch, phones included. No new ticket (Kevin's ticket restraint).

- [ ] Climb up (Interact) onto any driven team and ride its round on the seat beside the driver; look around freely; get down at any time (a moving team pulls up first) onto a clear spot beside it.
- [ ] Take the reins: walk on, pull up and steer the team; it refuses ground it cannot carry (buildings, kerbs, broken ground, people, other teams) by pulling up, never by clipping; hand the reins back and the driver takes it home to its round.
- [ ] Desktop and phone (390×780) shots in each year, with frame cost; recorded as reconstructed in LIBERTIES.

## Progress (2026-11-15): board and drive shipped to dev (PR #2060)

Kevin's 2026-11-14 ask is done on dev, merged 2026-11-15 in kevinrhaas/chicago#2060 (liberty L-board-drive-3557). Every driven team in 1812, 1835 and 1904 can be boarded. On board you can take the reins, drive (walk on, whoa, steer, back up) and hand the reins back; the driver then takes the team home to its round. You can get down at any point, by keyboard or touch, phones included. The team pulls up at walls, kerbs, rough ground, people and other teams instead of clipping through them; in 1904 it stays on the carriageways. The three boxes in Kevin's section above are met. The Glessner parts of this ticket are still open: the waiting team at the door, Mr. Glessner aboard, and the coach-house doors and drive.

1812, before (dev, only "Stop driver") and after ("Climb up onto the wagon"):

![1812 before and after](https://github.com/kevinrhaas/chicago-evidence/blob/88fbabef66e20f053a8e44a00ea04b0ff46873eb/evidence/transport/T3557-board-drive/1812-before-after.jpg?raw=true)

Driving the 1812 fort wagon:

![1812 driving](https://github.com/kevinrhaas/chicago-evidence/blob/88fbabef66e20f053a8e44a00ea04b0ff46873eb/evidence/transport/T3557-board-drive/1812-desktop-after-driving.jpg?raw=true)

1835, before and after:

![1835 before and after](https://github.com/kevinrhaas/chicago-evidence/blob/88fbabef66e20f053a8e44a00ea04b0ff46873eb/evidence/transport/T3557-board-drive/1835-before-after.jpg?raw=true)

1904, before and after (desktop above, phone below):

![1904 before and after](https://github.com/kevinrhaas/chicago-evidence/blob/88fbabef66e20f053a8e44a00ea04b0ff46873eb/evidence/transport/T3557-board-drive/1904-before-after.jpg?raw=true)

Driving Hans's brougham on a phone (390×780):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/88fbabef66e20f053a8e44a00ea04b0ff46873eb/evidence/transport/T3557-board-drive/1904-phone-after-driving.jpg?raw=true" width="300">

All 37 shots are in kevinrhaas/chicago-evidence under `evidence/transport/T3557-board-drive/`.

**Released 2026-11-14** (claim of run 11/14/2026, 1:21:32 PM CT): no reason given
