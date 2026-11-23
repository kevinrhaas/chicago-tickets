---
id: T-3732
title: dev's 1835 first-visit boot payload measures 49.657 MB, over SITE-BUDGET § 4r's 49.6 MB: every PR's smoke (desktop, 1-2) is red on it (dev ef2ef1ecc, after #2311)
state: review
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-23
closed: null
pr: 2315
claimed_by: run 11/23/2026, 4:37:45 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/45156611402
claimed_at: 2026-11-23T10:37:46.095Z
decision: null
decision_answer: null
---

dev's 1835 first-visit boot payload measures 49.657 MB, over SITE-BUDGET § 4r's 49.6 MB: every PR's smoke (desktop, 1-2) is red on it (dev ef2ef1ecc, after #2311).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's smoke (desktop, 1-2) refuses every PR on BOOT PAYLOAD OVER BUDGET; measured identical on dev and on PR #2300's head

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
