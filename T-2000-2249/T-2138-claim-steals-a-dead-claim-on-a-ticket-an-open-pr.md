---
id: T-2138
title: claim steals a dead claim on a ticket an open PR already carries when that PR's branch names no ticket: T-2122 was rebuilt in full while #449 (claude/project-thread-*) sat open with it
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-05
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

claim steals a dead claim on a ticket an open PR already carries when that PR's branch names no ticket: T-2122 was rebuilt in full while #449 (claude/project-thread-*) sat open with it.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 170 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a repeatable claim-lock gap that cost one whole slice today: no open ticket owns the claim steal reading open PR titles, and T-1721 (the nearest) is closed by #473

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What happened (2026-10-05, slice 1/5, run 37307506107)

- T-2122's claim was 9.1 h old, so `list --workable` printed `TAKEABLE dead claim 9h`
  and `claim` stole it, as designed.
- But PR #449, opened 03:24Z by the owner's project-thread session on branch
  `claude/project-thread-gfksyy`, was OPEN with the whole fix, its title
  `T-2122: …`. `inflight` reads branch names for ticket numbers, so it printed
  nothing for T-2122; `landed` only reads MERGED PRs.
- The slice rebuilt the same change (flora.js, the three smoke guards, L375, a
  changelog entry), gated it (check.sh 782/782, smoke parts 10-11 at both
  viewports) and found #449 merged onto dev at 12:44Z only when it went to merge
  dev in. No PR opened; the ticket was closed onto #449.

**Acceptance:** `claim` (or `list --workable`) reads OPEN PRs whose title names the
ticket, as `landed` reads merged ones, and refuses or flags a dead claim whose work
is sitting in one. `inflight` lists such a PR under its ticket whatever its branch
is called.
