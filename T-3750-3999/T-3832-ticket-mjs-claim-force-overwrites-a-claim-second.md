---
id: T-3832
title: ticket.mjs claim --force overwrites a claim seconds old: two slices took T-1938 33 s apart (2026-11-28) and built 2021's stable twice (#2426, #2428); --force should clear stale litter branches, never a live claim under 3 h
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-28
closed: null
pr: 2435
claimed_by: run 11/28/2026, 4:12:12 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/46129608998
claimed_at: 2026-11-28T10:12:13.043Z
decision: null
decision_answer: null
---

ticket.mjs claim --force overwrites a claim seconds old: two slices took T-1938 33 s apart (2026-11-28) and built 2021's stable twice (#2426, #2428); --force should clear stale litter branches, never a live claim under 3 h.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

`claim T-NNNN --force` on a ticket whose claim is younger than the run window is REFUSED with the live-claim message (asked before the branch scan, so it is the first thing a run reads), and the claim on the tickets repo is untouched; `--force` still passes a rival branch, an open PR, a busy house and a pending decision. Taking a live claim is a separate `--steal`, which must carry `--why "…"`; the steal is printed and its reason rides the claim's commit. The same split holds for the embedded-mode lock branch. Demonstrated in `test_ticket_repo_mode.mjs` § 5d (T-1938's shape: a live claim carrying a pending question, `--force` refused, `--steal` without a reason refused, `--steal --why` taken and recorded) and `test_ticket_claim_lock.mjs` § 4; both fail on the old code (6 and 2 checks).
