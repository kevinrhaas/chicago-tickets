---
id: T-3664
title: smoke part 14 dies after T-3658's 'Space activates a focused Navigator control' check: the next page.evaluate (on-foot Space) throws 'Execution context was destroyed, most likely because of a navigation' — the walk page reloads itself (same URL ?year=1835&keep-geometry=1, twice ~25 s before, then again) during the keyboard section; red on desktop and mobile on every PR since #2197 landed without a part-14 run (#2150 CI 135363867200 + local, #2207 mobile, #2210 desktop)
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-19
closed: null
pr: null
claimed_by: run 11/19/2026, 4:04:34 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/44501061259
claimed_at: 2026-11-19T10:04:35.624Z
decision: null
decision_answer: null
---

smoke part 14 dies after T-3658's 'Space activates a focused Navigator control' check: the next page.evaluate (on-foot Space) throws 'Execution context was destroyed, most likely because of a navigation' — the walk page reloads itself (same URL ?year=1835&keep-geometry=1, twice ~25 s before, then again) during the keyboard section; red on desktop and mobile on every PR since #2197 landed without a part-14 run (#2150 CI 135363867200 + local, #2207 mobile, #2210 desktop).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> every PR's content-build smoke leg 14 is red, so no resume PR on dev can merge on a green gate

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
