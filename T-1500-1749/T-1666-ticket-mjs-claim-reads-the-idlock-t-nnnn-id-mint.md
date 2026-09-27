---
id: T-1666
title: ticket.mjs claim reads the idlock/t-NNNN ID-mint branch as a rival work branch, so every freshly-minted ticket says 'already being worked' and trains runs to --force
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 9/27/2026, 1:11:08 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36299236519
claimed_at: 2026-09-27T06:11:08.282Z
decision: null
decision_answer: null
---

ticket.mjs claim reads the idlock/t-NNNN ID-mint branch as a rival work branch, so every freshly-minted ticket says 'already being worked' and trains runs to --force.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured

2026-09-27, taking T-1657 as slice 1. `claim` refused it:

    T-1657 looks like it is already being worked:
      idlock/t-1657

`idlock/t-1657` is not a work branch. It is the ID-MINT LEASE `ticket.mjs` itself
pushes when it mints a number (see the comment at `ticket.mjs:1285` and
`idLockBranch()` at :1294) — one orphan commit, `claim T-1657 — mint nonce:
mujcd1k638zszwh5wz8x`, with no merge base against `dev` and no PR. Every ticket in
the queue has one, so `claim` reports EVERY unclaimed ticket as taken, and
`inflight` lists the mint locks for T-1650, T-1651, T-1652 and T-1653 as "branches
on unfinished tickets" beside the two that are real work branches.

## Why it matters more than the noise

The check is the residual-race catcher: two slices reaching for one ticket must not
both win, and `--force` is the documented escape for a stale claim or your own
branch. When the check cries wolf on every ticket, `--force` becomes the normal way
to claim, and the one case it exists for — a live sibling genuinely on the ticket —
stops being distinguishable from the mint lease that is always there.

## Acceptance

The branch scan that `claim` and `inflight` read EXCLUDES `refs/heads/idlock/*`,
which is this tool's own bookkeeping namespace and never a work branch. `claim` on a
freshly minted ticket succeeds with no `--force`; `claim` on a ticket a rival
`steward/*` or `idlock`-free branch carries still refuses. Both proved by a self-test
in `test_ticket_claim_split.mjs`, which already enumerates `refs/heads/idlock/` and
so already has the fixture.

Found while closing T-1657 (PR #107); nothing there depended on it.
