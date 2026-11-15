---
id: T-3602
title: App code sweep: dead code, copied helpers and duplicate imports, with no change to what is drawn
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-14
closed: null
pr: 2059
claimed_by: run 11/14/2026, 5:17:50 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-14T23:17:51.264Z
decision: null
decision_answer: null
---

App code sweep: dead code, copied helpers and duplicate imports, with no change to what is drawn.

**Acceptance:** unused code, duplicate imports and byte-for-byte copied helpers removed from `renderers/web/js` where no gate, worker, pinned hash or open PR depends on them; the gate green; the same draw calls, triangles, textures and structures before and after on desktop (1280×800) and phone (390×780).

## Completion (2026-11-15, PR #2059, merged to dev)

Swept all 345 app modules (about 158k lines). None of the modules is dead. A lint pass found 35 unused bits; 17 are gone: unused imports and functions in flora.js, streets.js, navigation.js and year-pack.js, unused locals in gardens.js, crossings.js, terrain.js, scene-loader.js and people-view.js, and two doubled imports. yard.js now shares signage.js's phone half-size atlas instead of carrying a word-for-word copy. Left alone on purpose: tree-instances.js (three photo-match records pin its hash), frontage.js `plainTimber` (the plank checks slice it out), flora's lattice helpers (held twin to the worker kernel by check_lattice_kernel.mjs), the fauna, plants and residents card helpers (a test lays fauna.js over the published site), and files that open PRs touch.

Same scene before and after, 1835, measured in the app headless:

| | draw calls | triangles | textures | geometries | structures | JS heap |
|---|---|---|---|---|---|---|
| desktop before | 2,224 | 2,283,322 | 366 | 551 | 686 | 672.8 MB |
| desktop after | 2,224 | 2,283,322 | 366 | 551 | 686 | 672.7 MB |
| phone before | 905 | 518,281 | 406 | 269 | 686 | 289.5 MB |
| phone after | 905 | 518,281 | 406 | 269 | 686 | 288.9 MB |

The only pixels that differ are leaves moving in the wind between the two shots (0.29 % desktop, 0.01 % phone).

![1835 desktop, before (left) and after (right)](https://github.com/kevinrhaas/chicago-evidence/blob/a0c13c926bf75e397320393ddb6d002e9258a5fa/evidence/code-sweep-T-3602/1835-desktop-before-after.jpg?raw=true)

![1835 phone, before (left) and after (right)](https://github.com/kevinrhaas/chicago-evidence/blob/a0c13c926bf75e397320393ddb6d002e9258a5fa/evidence/code-sweep-T-3602/1835-phone-before-after.jpg?raw=true)
