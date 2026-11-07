---
id: T-3455
title: Desktop content-build smoke parts 13 and 14 overrun their 40-minute job cap on dev
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-07
closed: null
pr: 1841
claimed_by: run 11/7/2026, 11:37:05 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/42396100001
claimed_at: 2026-11-07T17:37:05.916Z
decision: null
decision_answer: null
---

Desktop content-build smoke parts 13 and 14 overrun their 40-minute job cap on dev.

**What was seen (2026-11-07, resuming PR #1828):** in `chicago-4d-bake.yml`'s smoke matrix, `smoke (desktop, 13)` and `smoke (desktop, 14)` were still running when the 40-minute `timeout-minutes` cancelled them (run 42378182584, steward/t1881-rear-step-stack: started 14:20 and 14:21, cancelled 15:00 and 15:01). The other 28 legs passed in that run. Dev's own run 42363778425 had the same two legs still going at 39.5 min when the next dev push cancelled it. On the steward runner, `SMOKE_VIEWPORT=desktop SMOKE_STAGE=14 node tools/smoke_renderer.mjs --published` timed out on unmodified **origin/dev** at 520 s after 15 passes and 0 failures. On the #1828 branch it got to 38 passes and 0 failures by 595 s, stalled on the wildlife `page.evaluate` (smoke_renderer.mjs ~L18809). `smoke_budget.mjs` prices desktop 14 at 9m 55s, so it has 5 s of margin.

**Why it matters:** gh-rest `pr-automerge` (T-2461) carries the cancelled content build forward as `refused`. So every PR that fires that workflow (anything under `generators/**`) cannot merge on its gate and needs a hand-gated `GH_REST_MERGE_BLIND=1` (#1828 merged that way, with its reasoning in a PR comment).

**Acceptance:** desktop parts 13 and 14 each finish green inside the content build's 40-minute job cap on dev, and part 14 finishes inside the 600 s local foreground cap (or `smoke_budget.mjs` splits it so each piece does). Find where the time goes rather than raising the cap.
