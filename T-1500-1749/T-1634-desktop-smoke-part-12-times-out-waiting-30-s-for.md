---
id: T-1634
title: Desktop smoke part 12 times out waiting 30 s for the scene to be ready after the What's-new reload, when frames cost about 2 s: 2 of 3 runs on a 4-CPU session container, on a tree whose only part-12 change was a changelog stamp
state: open
epic: PIPELINE
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-26
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

Desktop smoke part 12 times out waiting 30 s for the scene to be ready after the What's-new reload, when frames cost about 2 s: 2 of 3 runs on a 4-CPU session container, on a tree whose only part-12 change was a changelog stamp.

**Seen 2026-09-26 while gating PR #82** (the Prairie library, merged as 8314fde0). Three desktop runs of `SMOKE_STAGE=12` on a 4-CPU session container, all on trees whose only part-12 input change was the changelog restamp:

| run | result | frame cost printed |
|---|---|---|
| 1, right after the mobile leg | FAIL 85 passed | 113 / 1901 / 1973 ms |
| 2, quiet machine | PASS 92/0 | n/a |
| 3, after the second restamp | FAIL 85 passed | 28 / 2019 / 2083 ms |

Both failures are the same step. "the HUD toggle drives the confidence view" passes, then the What's-new block (`tools/smoke_renderer.mjs` after line 12818) reloads the page and `page.waitForFunction(() => window.__chicago4d?.ready === true, null, { timeout: 30000 })` expires, and the throw reports as "the suite body ran to completion". No What's-new assertion is reached, so the changelog is not what failed. The steward runners pass the same part in the same hour (T-1623 recorded desktop 12 at 92/0 on dev), so the scene reload fits in 30 s on them and not reliably on this machine.

**The work:** measure the reload-to-ready time at desktop on the steward runner and on a 4-CPU container. Then make the wait honest: size the ready budget from the measured frame cost, as the harness already prints it, rather than a flat 30 s. Or, if the full reload is not what the block tests, reach the What's-new state without re-booting the scene. It must not skip or weaken any What's-new assertion.

**Acceptance:** desktop part 12 passes three consecutive runs on a 4-CPU container, with the reload wait's budget stated and derived. Every What's-new assertion is unchanged.

Low priority, filed in band 9 below the building work: the loop's own runners are not hitting it today.
