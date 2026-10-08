---
id: T-2147
title: Build the School Section tier's Market block south of Madison (81): ordinary dwellings dealt on the tier's own lots
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-1755
opened: 2026-10-05
closed: 2026-10-08
pr: 493
claimed_by: run 10/5/2026, 5:03:32 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-08T15:01:43Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37378847462
claimed_at: 2026-10-05T22:03:32.769Z
decision: null
decision_answer: null
---

Build the School Section tier's Market block south of Madison (81): ordinary dwellings dealt on the tier's own lots.

Piece 4 of 4 of **T-1755 — Build the South Division's remaining ordinary dwellings: the roofs the district still owes after the plat's last tier and the outer books closed, on the blocks the street carry emitted**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1755 was split (2026-10-05T18:55:43.668Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 10/5/2026, 1:53:01 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37358954436) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37358954436) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding (loop, 2026-10-08): a green DRAFT PR cannot be finished by any run

PR #493 was lapped over T-2148, T-2058, T-2022, T-2151, T-2152, T-2154 and T-2113. Its head is 428ea8166, and every check on it is green: gate, report, moving-frames, and still-frame on mobile and desktop. CHECK PASS 786/786 locally. The merge was still refused with HTTP 405 "Pull Request is still a draft".

- REST has no endpoint to mark a PR ready for review. That takes GraphQL `markPullRequestReadyForReview`.
- `gh-rest.sh` has no verb wrapping that mutation, and runs may not write GraphQL of their own.
- `pr-lap.sh`, `merge-ready.sh` and `pr-stuck.sh` all filter `draft==false`.

So a salvage-opened draft (AGENTS.md says "FINISH THAT PR") is parked where no machine can merge it.

- **Fix:** add a `pr-ready` verb to polecat-platform's `.github/steward/gh-rest.sh`, one mutation like `pr-automerge`'s. `pr-automerge` should call it when the PR it is about to merge is a draft.
- **Until then:** a person marks #493 ready, and it merges as-is.
