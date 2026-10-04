---
id: T-2113
title: The arrival and welcome screens redraw an unchanged town on every frame: draw it once under the menu and again only when something under it changes
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-04
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

The arrival and welcome screens redraw an unchanged town on every frame: draw it once under the menu and again only when something under it changes.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 190 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Found by T-2111 reading the arrival screen: the owner-reported lag (T-2099) includes every second a visitor spends on the welcome, where a phone redraws an identical picture at full cost

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What T-2111 read (2026-10-04, dev @ 29fa96f2, published mirror)

`node tools/measure_still_frame.mjs --arrival 15` leaves the loop running for the window with
the welcome up and nothing touched, counts `renderer.info.render.frame`, and compares the
`capture()` signature of the first and last frame. Desktop 1280x800: 3 frames in 23.5 s;
phone 390x780 (CPU 4x): 6 frames in 19.5 s — **every one the same picture**. On SwiftShader a
frame is seconds, so that is a few frames; on a phone GPU it is every display refresh, each one
the cost of the landing view (T-2099's table: the landing is a whole town frame, 740 k
triangles at `light`). `main.js` `tick()` holds the walk while `gateOpen` (`frameDt` is 0) but
still calls `renderer.render` every frame, under a translucent gate whose `backdrop-filter`
blur the compositor redraws on top (walk.css `.gate`).

## The work

Draw the frame under the gate when it can have changed — the first frame, a resize, a detail
or sharpness change, a capture asked for, layers still streaming in — and not otherwise; the
welcome's own animation and the year counter are DOM and unaffected. Prove it with the same
reading (frames drawn under an idle welcome falls to about zero, the picture unchanged) and the
arrival smoke green at both viewports. Nothing a visitor sees changes except a cooler phone and
a menu that scrolls without stutter.
