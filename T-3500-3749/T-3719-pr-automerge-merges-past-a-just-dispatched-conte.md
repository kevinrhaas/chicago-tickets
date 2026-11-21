---
id: T-3719
title: pr-automerge merges past a just-dispatched content build: a workflow_dispatch run that has no check runs yet reads as 'nothing missing'
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-21
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

pr-automerge merges past a just-dispatched content build: a workflow_dispatch run that has no check runs yet reads as 'nothing missing'.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What happened (2026-11-21, PR #2284)

- #2284's head bed0d26 had all 8 gate parts green. The content build that is carried forward from the earlier head 1444a62 (run 44948261176) had bake-gate parts 4/16 and 11/16 red. Both failures were the source-use backlink error, which bed0d26 had already fixed (`compile_source_use.py --check` PASS locally).
- The steward dispatched `chicago-4d-bake.yml` on the branch (run 44958394116) to give the head its own run. The dispatch cancelled the stale run through the workflow's concurrency group.
- The next `pr-automerge` call merged at once: "nothing an earlier head ran is missing from bed0d26". The new run was still `queued`, and its jobs had produced no check runs on the head yet, so the carry-forward rule (T-2461) found no content-build verdict to wait on. The cancelled run's red was no longer counted either.
- What we lost: the content build never ran on the merged head. Only bed0d26's 6 one-line source-use files differed from 1444a62, whose `bake` job was green, and dev's own content build fired on the merge commit 37f6e019c. In practice the bake is still gated on dev. But the merge gate itself did not read it.

## Fix wanted

When it reads the gate, `pr-automerge` should treat a workflow run on the head SHA that is queued, pending or in progress as `pending` (exit 4), even when that run has no check runs yet. It should look at the Actions runs API (`/actions/runs?head_sha=`) as well as check-runs. A cancelled run superseded by a newer run on the same head should defer to the newer run.
