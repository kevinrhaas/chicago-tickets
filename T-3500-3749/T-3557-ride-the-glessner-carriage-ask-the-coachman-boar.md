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
