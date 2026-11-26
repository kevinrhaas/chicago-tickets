---
id: T-3767
title: Enable the 256 generic photo faces by default in all four dev years
state: done
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-26
closed: 2026-11-26
pr: 2355
claimed_by: run 11/26/2026, 9:05:50 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-26T17:32:12Z
claimed_run: null
claimed_at: 2026-11-26T15:05:52.623Z
decision: null
decision_answer: null
group: T-3767,T-3768
---

Enable the 256 generic photo faces by default in all four dev years.

**Acceptance:** Generic photographic faces load by default on dev in 1812, 1835, 1871 and 1904, without an opt-in query flag. Existing personal historical likenesses and visitor-selected faces retain priority. Verify complete population tables and actual rendered residents; preserve stable identities across body assignments. Adult and child crowd textures share one bounded nearby page, about 12 MiB added texture memory. Publish to dev and verify the served build; a real low-power GPU timing remains an explicit outstanding measurement.

**Delivered 2026-11-26:** PR #2355 merged as cc55804d9478880ac12c656b8f69ca7b6c0c1f5f. Dev deployment 45868670040 passed; live build cc55804d9 is verified at https://dev.chicago.polecat.live/4d/dev/. Both libraries (256 adults and sixteen children), both crowd atlases and all seventeen detail pages match. The actual served module applies defaults in every supported year and preserves personal likenesses. Complete population tables, unchanged child proportions, fixed texture budget, offline reproduction, published renderer checks at phone and desktop sizes, the final eight-part gate and clothing integration are retained in `kevinrhaas/chicago-evidence/evidence/photo-faces-dev-T-3767/` at commit 15e2e5765ceb0e408bc5c8f9083002c0e42f58ad (evidence PR #6). Real low-power GPU timing remains unmeasured; source browser proof uses SwiftShader. Historical photo-person prototypes remain preserved separately on T-3762.
