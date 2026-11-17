---
id: T-3643
title: Performance pass: no shader recompiles mid-walk, fewer GPU stalls at boot, nothing drawn differently
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-17
closed: null
pr: null
claimed_by: run 11/17/2026, 11:22:47 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-17T17:22:48.143Z
decision: null
decision_answer: null
---

Performance pass: no shader recompiles mid-walk, fewer GPU stalls at boot, nothing drawn differently.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
Kevin asked (2026-11-17): "Do that pass to see if you can jack up the performance", then "also 1812". Done means: no shader compiles inside a frame during an ordinary walk that boot could have done, fewer GPU stalls at boot, and nothing drawn differently on desktop or phone.

## Completion note (PR 2161)

Three fixes, all invisible in the picture:

- **Shadows (all years, desktop).** three.js r185 quietly swaps the old soft-shadow setting for plain PCF at the first shadow render. Every frame was already drawn with PCF, but everything prepared during loading had been prepared under the old setting and was thrown away. Each building, camp, door and apron then re-prepared in the middle of a frame the first time it came into view. Booting with PCF keeps the loading work.
- **Distant crowd (crowd.js).** The far townspeople re-prepared their drawing for every new dress. They now keep it, and new figures are prepared in the background.
- **Sky colour (world.js).** One trip to the graphics card instead of 36, at load and on every time-of-day change. Colours checked identical at four hours.

| reading (SwiftShader, 1280×800) | dev | after |
|---|---|---|
| 1812: shader links inside a frame, load → 60 s walk | 52 | 19 (the rest are people's shadow-depth programs, left to the 1812 frames thread) |
| 1812: live shader programs 45 s in | 112 | 80 |
| 1835: links during a 60 s walk | 12, rising per new dress | 3, all off-frame |
| 1835: JS frame p50 on the walk | ~174 ms | ~39–60 ms |
| 1835: sky sampling in the boot profile | 6198 ms | 4820 ms |

**Before (dev), 1812 desktop:**

![before 1812 desktop](https://github.com/kevinrhaas/chicago-evidence/blob/c73142a5b32c68dc1e4f8883f4d62420d4ff4a01/evidence/perf-pass-T-3643/before-1812-1280.jpg?raw=true)

**After, 1812 desktop** (same frame; only the walking soldier has moved):

![after 1812 desktop](https://github.com/kevinrhaas/chicago-evidence/blob/c73142a5b32c68dc1e4f8883f4d62420d4ff4a01/evidence/perf-pass-T-3643/after-1812-1280.jpg?raw=true)

**After, 1812 phone 390×780** (0 page errors):

![after 1812 phone](https://github.com/kevinrhaas/chicago-evidence/blob/c73142a5b32c68dc1e4f8883f4d62420d4ff4a01/evidence/perf-pass-T-3643/after-1812-390.jpg?raw=true)
