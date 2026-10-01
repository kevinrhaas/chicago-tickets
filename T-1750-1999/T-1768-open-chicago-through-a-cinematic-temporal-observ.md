---
id: T-1768
title: Open Chicago through a cinematic temporal observatory with three eras and shared interface skins
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: 207
claimed_by: interactive temporal menu
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-01T03:07:33.236Z
decision: null
decision_answer: null
---

Open Chicago through a cinematic temporal observatory with three eras and shared interface skins.

**Acceptance:** /4d/ opens a cinematic, responsive temporal menu with 1835, 1904 and 1812; animated acquisition and departure; secondary sci-fi, steampunk and space-age skins persisted into renderer windows; 1835 opens /4d/1835/ and the other years use their own doors. Identify unavailable 1812 honestly. Preserve explicit query deep links, dev-relative paths, keyboard access and reduced motion. Verify desktop/mobile published pages and the project gate.


Implementation checkpoint: kevinrhaas/chicago#207, branch `steward/t1768-temporal-arrival-menu`, commit `b067036ba59bd4ad4866cf4ae53a50392bcedf00`. Published portal checks pass desktop/mobile; mobile scene part 1 passes 80/0. Full CI gate and desktop scene readiness verification remain before merge.


Completed 2026-10-01: PR #207 merged into dev as `c2dccdcd6fc8c3d6e1d2ba17e2e62e8d3f5b840b`. Final CI passed on `66ac7d6` (run 36811965569); published renderer part 1 passed 80/0 on desktop and mobile; final menu browser checks passed both sizes, all skins, navigation, and zero page errors. Preview refresh started in run 36812892609. Production awaits the owner's normal promotion dispatch. The settle workflow follows the merged PR for ticket closure.
