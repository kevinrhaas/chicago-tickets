---
id: T-2722
title: Frame governor's moving reading on a GPU: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read on hardware whose frame costs tens of milliseconds (a GPU runner or the owner's phone)
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2592
opened: 2026-10-17
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: pending
decision_answer: null
---

Frame governor's moving reading on a GPU: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read on hardware whose frame costs tens of milliseconds (a GPU runner or the owner's phone).

Piece 2 of 2 of **T-2592 — Frame governor's moving reading: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read where a frame costs inside the governor's range (the steward runner's SwiftShader draws one in 2.3 to 3.6 s)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2592 was split (2026-10-17T17:13:44.235Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 15m ago, run 10/17/2026, 11:58:48 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39051404538) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39051404538) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Decision needed

**Question:** The governor's moving reading needs hardware that draws a frame in tens of milliseconds; the steward runner draws the town in 0.8-2.3 s on both software rasterisers (T-2721). Where should it be read?

- (a) On your own phone: a run first builds a dev-only 'Read frame pacing' action that drives walk, turn and flight Adaptive then Fixed in the page and shows sd and p95 to copy back (no cost)
- (b) On a GPU-backed GitHub runner for this one workflow (paid per minute; you would need to enable a larger GPU runner on the account)
- (c) Leave the reading until a GPU is available some other way; the governor stays as shipped

**Recommendation:** (a) On your own phone: a run first builds a dev-only 'Read frame pacing' action that drives walk, turn and flight Adaptive then Fixed in the page and shows sd and p95 to copy back (no cost) — it costs nothing and reads the device the 'walking is laggy' report came from, at its own refresh rate

**Asked:** 2026-10-17 by https://github.com/kevinrhaas/polecat-platform/actions/runs/39051404538. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.
