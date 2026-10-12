---
id: T-2413
title: Smoke part 1-2's Sauganash colour reading screenshots on a 300 ms wait, not a drawn frame: delta 0.00 on slow runners
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-12
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

`tools/smoke_renderer.mjs` (~line 6030, T-1800's colour reading) hides the frontage
group, waits a fixed **300 ms**, and takes `page.screenshot()` — it never asks the
renderer to draw. The luminance reading just above it goes through
`__chicago4d.capture()`, which renders, and it *does* see the walks. On a CI runner
where one frame costs seconds (T-2412 measured ~8 s frames on desktop part 6), both
screenshots are the same frame, so the colour delta is **exactly 0.00** — a
reading of the wait, not of the scene.

**Seen:**
- PR #696 (T-2356, 1626 Prairie — touches no 1835 frontage), head de72dbc06, CI
  `smoke (mobile, 1-2)` 2026-10-12 11:20Z: `FAIL [4:14] … the Sauganash's walks and
  posts reach the screen from Lake Street — colour cell delta mean 0.00, worst 0
  (need worst>=6, mean>=0.3); luminance alone 0.23, worst 6` — 180 passed, 1 failed.
- PR #721 (T-2400, Glessner granite — also not 1835), desktop 1-2, the same line with
  delta 0.00, once; dev passed it.

Two unrelated PRs red on one assertion, each with a delta of exactly zero, is the
signature of the screenshot not waiting for a drawn frame.

**Acceptance:**
- Each of the two screenshots is taken after a frame has actually been drawn with the
  frontage in the state being read (e.g. force a render the way `capture()` does, or
  wait on `requestAnimationFrame` until a frame has been presented), not after a fixed
  sleep.
- The bar is NOT moved: worst >= 6 and mean >= 0.3, unchanged.
- Proof that the fix reads the scene and not the clock: with the frontage left visible for
  both shots, the check still FAILS (delta 0), and with it hidden it passes, on desktop
  and mobile part 1.
