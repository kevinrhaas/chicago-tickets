---
id: T-2109
title: 1904's Glessner glass: its transmission pass is half of every frame at both viewports — put a cheaper glass to the owner with before/after captures and ship the one he picks, at least at balanced and light
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2099
opened: 2026-10-04
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

1904's Glessner glass: its transmission pass is half of every frame at both viewports — put a cheaper glass to the owner with before/after captures and ship the one he picks, at least at balanced and light.

Piece 2 of 4 of **T-2099 — Lag in every view, not only when walking: read still-frame GPU and CPU time at every stand, the aerial and overview, arrival and jaunt views and the 1812 and 1904 scenes, attribute it by layer and pass, fix the largest causes, and hold a frame-time ceiling per tier**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2099 was split (2026-10-04T19:55:00.196Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1.9h ago, run 10/4/2026, 1:01:29 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236) — held by the run that split it
- PR #426 on steward/t2099-still-frame-time — T-2099: a still frame's time read everywhere, and whose milliseconds they are — held by the run that split it
- branch `steward/t2099-still-frame-time` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37222558236) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Decision needed

**Question:** 1904's Glessner glass costs half of every frame. Two cheaper panes are on the dev preview: /4d/dev/?year=1904&glass=clear and &glass=dark (side by side: docs/measurements/t-2109-glass/desktop-transmission-clear-dark.jpg). Either one halves the 1904 landing frame (desktop 9.1 s to 4.4 s, phone 6.0 s to 2.9 s on the test machine). Which should ship by default, and at which Scene detail settings?

- (a) clear at balanced and light; full keeps today's glass (looks almost the same as today)
- (b) clear at every setting
- (c) dark at balanced and light (every pane a darker plate)
- (d) keep today's glass everywhere

**Recommendation:** (a) clear at balanced and light; full keeps today's glass (looks almost the same as today) — Clear halves the frame and changes the least in the capture. Keeping transmission at full leaves the inspection model's best glass where the frame budget is spent on purpose. Shipped in #431 behind ?glass=, default unchanged until you choose.

**Asked:** 2026-10-04 by https://github.com/kevinrhaas/polecat-platform/actions/runs/37231030032. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

## Finding — #431 (2026-10-04)

Both candidates shipped behind `?glass=clear|dark` in #431 (`renderers/web/js/glass.js`), with the default unchanged. The reading and the capture are in `docs/measurements/T-2109-glessner-glass.md`: either pane halves the 1904 landing frame at balanced and light on both viewports. **What is left once the owner answers:** change `DEFAULT_GLASS` (or make it per tier) to his pick, and update `tools/check_glass_modes.mjs` to match. The claim was released when the question was asked, so the run that ships his answer can take it.
