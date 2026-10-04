---
id: T-2110
title: Phone Image sharpness Medium to Low takes 25-30% off a still frame: ask the owner whether a phone should boot at Low, and read trees' and terrain's fragment cost in 1835 for a cheaper shader that draws the same picture
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2099
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/4/2026, 5:08:35 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37238704416
claimed_at: 2026-10-04T22:08:35.476Z
decision: pending
decision_answer: null
---

Phone Image sharpness Medium to Low takes 25-30% off a still frame: ask the owner whether a phone should boot at Low, and read trees' and terrain's fragment cost in 1835 for a cheaper shader that draws the same picture.

Piece 3 of 4 of **T-2099 — Lag in every view, not only when walking: read still-frame GPU and CPU time at every stand, the aerial and overview, arrival and jaunt views and the 1812 and 1904 scenes, attribute it by layer and pass, fix the largest causes, and hold a frame-time ceiling per tier**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2099 was split (2026-10-04T19:55:00.196Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1.9h ago, run 10/4/2026, 1:01:29 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236) — held by the run that split it
- PR #426 on steward/t2099-still-frame-time — T-2099: a still frame's time read everywhere, and whose milliseconds they are — held by the run that split it
- branch `steward/t2099-still-frame-time` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Decision needed

**Question:** On a phone, Image sharpness Low (pixel ratio 1) draws a frame 26-29% faster than today's default Medium (1.5) at Light detail, but softer: log courses and roofs from the air lose crispness (side by side: docs/measurements/t-2110-sharpness/phone-light-low-medium.jpg in kevinrhaas/chicago). Should a phone start at Low? A visitor can already pick it in Settings, and a stored choice is never overridden.

- (a) phone starts at Low; desktop stays at Medium
- (b) keep Medium on every device (today)
- (c) phone starts at Low only at Light detail; Medium at Balanced and Full

**Recommendation:** (a) phone starts at Low; desktop stays at Medium — Phones are where the frame budget binds (the owner's lag report was on an iPhone), and Low is the single largest lever measured: 26-29% per frame against ~3-5% for the leaf-bump fix in #435. The softness is real but small at phone viewing distance, and anyone who prefers sharpness keeps it with one setting.

**Asked:** 2026-10-04 by https://github.com/kevinrhaas/polecat-platform/actions/runs/37238704416. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

## Finding — #435 (2026-10-04)

The shader half is done in #435. Leaf cards now skip the bump, which they kept only 3.5 % of. Trees cost 12–13.5 % less, and the picture differs by at most 2 of 255 on 0.1 % of pixels. Trees' and the ground's fragment cost is read piece by piece in `docs/measurements/T-2110-fragment-cost.md`. No same-picture saving was found in the ground shader. The remaining levers there (bake the turf noises, a Lambert ground) change the picture, so they belong to the owner. **What is left once the owner answers:** make the phone's default `quality` in `hud.js` `DEFAULT_SETTINGS` follow his pick (only when the visitor has stored no choice), and re-read `measure_still_frame.mjs --gate`'s phone ceilings.
