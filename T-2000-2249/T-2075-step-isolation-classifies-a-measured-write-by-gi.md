---
id: T-2075
title: step_isolation classifies a measured write by git check-ignore rather than a hand-kept exempt list, and records wrote vs wrote_ignored (folded in from T-1345)
state: open
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: T-1341
opened: 2026-10-04
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

step_isolation classifies a measured write by git check-ignore rather than a hand-kept exempt list, and records wrote vs wrote_ignored (folded in from T-1345).

Piece 2 of 2 of **T-1341 — ticket.mjs --check REPAIRS the mirror it is checking, so on any branch that adds a ticket the gate's queue step mutates tickets.json while the pool reads it — the T-0856 check-that-repairs fault, one tool over**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
