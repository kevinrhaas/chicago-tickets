---
id: T-3769
title: Remove forehead bands from generic photographic faces
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
closed: 2026-11-26
pr: 2365
claimed_by: run 11/26/2026, 1:00:15 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-26T19:43:31Z
claimed_run: null
claimed_at: 2026-11-26T19:00:17.336Z
decision: null
decision_answer: null
---

Remove forehead bands from generic photographic faces.

**Acceptance:** Reproduce the visible forehead band on generic photographic faces, remove its actual texture or hair-boundary cause, and review representative adults and children from the front and oblique at full and Light detail. Preserve identity, child proportions, eye treatment and the existing shared texture budget. Run the applicable gates, update dev, and verify the served fix.


**Delivered:** PR #2365 merged as b7938d0d758f504aeaa1d32e6f4082409955b310; deployment 45886018853 passed. Live build 79d353a9e serves all corrected atlases and passes default assignment/delivery checks in all four years. All eight gate parts, mapped smoke stages 1/4/5 at both viewports, and the portable-human renderer passed. The full proof is committed in chicago-evidence at `evidence/photo-forehead-T-3769/`, merged by evidence PR #7 (d4ae93f78eed0a69be2642faca366e63e96bdfa7). No new runtime textures or geometry.
