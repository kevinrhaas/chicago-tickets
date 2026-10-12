---
id: T-2412
title: Desktop smoke part 6 clicks the first-entry guide on 8 s frames and spends 74-90 s of a 90 s timeout, on dev's own mirror too
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

Desktop smoke part 6 clicks the first-entry guide on 8 s frames and spends 74-90 s of a 90 s timeout, on dev's own mirror too.

## Evidence (found lapping PR #721, 2026-10-12)

- CI `smoke (desktop, 6-7)` on #721 failed twice identically at `page.click('#control-help-gotit')`
  (tools/smoke_renderer.mjs, part 6): `Timeout 90000ms exceeded` after "click action done -
  waiting for scheduled navigations to finish", with "one animation frame costs 18 / 8282 /
  8246 ms here (0.46-1.10 s is this scene's cost on a quiet machine)".
- The legs that PASSED on the same dev base are not far off. That one click took 74 s on #722
  (2:02 to 3:16), 48 s on #696 and 47 s on #720. The boot to `ready` ranged 0:30 to 0:56
  across those runners.
- A/B on the steward runner (4 cpu, quiet, published mirrors of dev 98503e557 and #721 head
  20809799b, desktop 1280x800, `--enable-unsafe-swiftshader`, alternating runs):
  dev boots to ready in 55-61 s, the gate click takes 34.5 s, and after entry the 1835 scene
  draws 3 frames in 20 s at about 8.0 s each. The branch measured the same (61 s, 34 s,
  8.0 s). So **8 s frames at desktop are dev's normal cost on this class of machine**.
  The smoke's "0.46-1.10 s on a quiet machine" note is stale, and every click in part 6 is
  priced at roughly ten frames against a 90 s ceiling.

**Acceptance:** desktop part 6 cannot time out on a frame budget dev itself spends. Either
(a) the first-entry clicks stop waiting on rendered frames (e.g. `noWaitAfter`, or dispatch +
read the DOM state, as line ~1481 already does), with the guide's dismiss-and-remember check
still asserted; or (b) the smoke's frame-cost note and timeout are re-measured on CI. Proven by
three consecutive green CI `smoke (desktop, 6-7)` legs, and a desktop part 6 run on a steward
runner that logs how many seconds the click took.
