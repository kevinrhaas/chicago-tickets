---
id: T-2732
title: Read frame pacing: a dev-only Settings action that drives walk, turn and flight at light through the page's own loop, Fixed then Adaptive, and shows each move's frame-time sd and p95 with a Copy button, for the owner's phone
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2722
opened: 2026-10-17
closed: null
pr: 990
claimed_by: run 10/17/2026, 1:22:10 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39057123887
claimed_at: 2026-10-17T18:22:10.621Z
decision: null
decision_answer: null
---

Read frame pacing: a dev-only Settings action that drives walk, turn and flight at light through the page's own loop, Fixed then Adaptive, and shows each move's frame-time sd and p95 with a Copy button, for the owner's phone.

Piece 1 of 2 of **T-2722 — Frame governor's moving reading on a GPU: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read on hardware whose frame costs tens of milliseconds (a GPU runner or the owner's phone)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2722 was split (2026-10-17T18:21:54.818Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/17/2026, 1:19:48 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39057123887) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39057123887) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. Settings → Performance carries a **Read frame pacing** button on the dev preview (`/4d/dev/`, recognised by its banner) and anywhere with `?pacing=read`; on production without the parameter it is not there.
2. Pressing it enters the town if the welcome is up, closes the panel, sets Scene detail to light and drives walk, turn and flight through the page's own animation loop — the moves, poses and interval arithmetic of `measure_walk_frames.mjs --live` (only canvas draws counted, offscreen picks excluded) — Fixed then Adaptive, a few seconds each, then puts back the visitor's detail, pacing, place and flight.
3. It shows, per move, Fixed and Adaptive frame-time sd and p95 (with draws, mean, median, max) and FELL / DID NOT FALL, with the device it was read on (screen, ratio, user agent), and a Copy button that puts that text on the clipboard to send back.
4. A node test pins the arithmetic and the visibility rule; a Playwright run at 390x780 on the runner presses the button and reads a complete result with zero page errors and the settings restored (the numbers there are SwiftShader's noise and are not the reading — T-2733 is).
