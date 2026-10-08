---
id: T-2068
title: Attach the scene bundle to the scheduled content build and its manual dispatch, publish it with a discovery manifest and a latest-good pointer, and record a fresh-download receipt (a workflow change)
state: claimed
epic: PIPELINE
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1357
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/8/2026, 11:49:17 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-08T16:49:17.815Z
decision: answered
decision_answer: a
---

Attach the scene bundle to the scheduled content build and its manual dispatch, publish it with a discovery manifest and a latest-good pointer, and record a fresh-download receipt (a workflow change).

Piece 2 of 2 of **T-1357 — Publish a versioned Chicago scene bundle from every successful scheduled asset bake**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Decision needed

**Question:** T-2068 edits .github/workflows/chicago-4d-bake.yml (pack the scene bundle after a green bake, publish it, keep a latest-good pointer). AGENTS.md puts workflow files outside a run's scope ('needs an interactive, owner-visible PR'). Who makes that change?

- (a) An interactive session with you makes the workflow edit; the packer and verifier it calls (tools/scene_bundle.py, T-2067) are already on dev
- (b) A loop run may open the workflow PR and leave it for your review before merge

**Recommendation:** (a) An interactive session with you makes the workflow edit; the packer and verifier it calls (tools/scene_bundle.py, T-2067) are already on dev — It is the standing rule in AGENTS.md, and the code it needs has already landed, so the workflow change is small. Publication storage is also a cost/access question (GitHub Release assets vs expiring Actions artifacts), which is yours either way.

**Asked:** 2026-10-04 by https://github.com/kevinrhaas/polecat-platform/actions/runs/37182479150. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

**Owner answer (2026-10-04, via Manager):** (a) An interactive session with you makes the workflow edit; the packer and verifier it calls (tools/scene_bundle.py, T-2067) are already on dev
