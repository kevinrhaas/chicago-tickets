---
id: T-3501
title: Content build: cache and retry the pinned KTX-Software 4.3.2 .deb so a github.com release-asset 504 cannot fail the bake (the install step warns and goes on, then ktx2_sheets.py's single urlopen fetches again and FATALs on the first textured mesh)
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-08
closed: 2026-11-08
pr: 1874
claimed_by: run 11/8/2026, 5:56:21 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-08T13:19:57Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/42476972723
claimed_at: 2026-11-08T11:56:22.156Z
decision: null
decision_answer: null
---

Content build: cache and retry the pinned KTX-Software 4.3.2 .deb so a github.com release-asset 504 cannot fail the bake (the install step warns and goes on, then ktx2_sheets.py's single urlopen fetches again and FATALs on the first textured mesh).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #1873's content build (run 42469167608) failed three times on 2026-11-08 at 09:57, 10:06 and 10:21Z, each on HTTP 504 from the KTX-Software release asset; gate green on all 8 parts, nothing in the diff at fault

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
