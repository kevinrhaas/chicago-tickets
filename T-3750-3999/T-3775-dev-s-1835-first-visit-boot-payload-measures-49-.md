---
id: T-3775
title: dev's 1835 first-visit boot payload measures 49.767 MB, over SITE-BUDGET § 4's 49.6 MB: every PR's smoke (desktop, 1-2) is red on it — the photo-face libraries' two review.json (0.166 MB) now load at boot (dev 71566d43b, after T-3767/T-3768)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
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

dev's 1835 first-visit boot payload measures 49.767 MB, over SITE-BUDGET § 4's 49.6 MB: every PR's smoke (desktop, 1-2) is red on it — the photo-face libraries' two review.json (0.166 MB) now load at boot (dev 71566d43b, after T-3767/T-3768).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content-build smoke (desktop, 1-2) is red on measure_boot_payload --check for every PR, #2369 included

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
