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

The folded-in T-1345 half of T-1341, verbatim from the parent:

1. `audit_step_isolation.mjs` classifies a measured write by asking git, not by a list:
   a path `git check-ignore` claims is a BUILD PRODUCT, a tracked path is a TREE MUTATION.
2. The three hand-kept exemptions added on 2026-09-18 — `site/`,
   `chicago/4d/tickets/BOARD.md`, `chicago/4d/tickets/tickets.json` — are then redundant
   and removed, and the gate still passes for the same reason it passes today.
3. A write to a TRACKED path is never excused by this. The classification decides which
   question is asked, not whether one is.
4. The measurement records the classification (`wrote` vs `wrote_ignored`) so the cheap
   per-commit half does not shell out to git once per path.

Split out of T-1341 because it is a second demonstration: it needs a re-measure
(`measure_step_isolation.mjs --build`, a full serial instrumented gate) on top of the
audit change. NOTE for whoever takes it: since T-2074, `ticket.mjs check` no longer
writes BOARD.md or tickets.json at all, so those two exemptions now cover only `board`
(publish.sh's first step) — the WHY in the parent stands unchanged.
