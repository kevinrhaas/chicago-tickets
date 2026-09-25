---
id: T-1584
title: dev is red for every PR: T-1523 settled done at 22:35Z and the 272 landholding units deferring to split parent T-1198 lost their last live leaf — repoint them at the live ticket that owns their question, or file one
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: null
claimed_by: run 9/25/2026, 5:54:32 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36198552225
claimed_at: 2026-09-25T22:54:32.593Z
decision: null
decision_answer: null
---

dev is red for every PR: T-1523 settled done at 22:35Z and the 272 landholding units deferring to split parent T-1198 lost their last live leaf — repoint them at the live ticket that owns their question, or file one.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What happened

`check.sh` on a clean `origin/dev` (and therefore on every open PR) is red on four steps:

```
CHECK FAIL — 4 of 628 steps failed:
  * research stays inside its historical ratchet and closed unit ledger
  * the closing research audit still re-derives from the ledger and the four layers
  * the research sign-off re-derives, and its GO still follows from the tree
  * …and each of its rules still fires, and hands on only to live work
```

Each FAIL reads the same: `unresolved ticket 'T-1198' is missing or not open — it was
split and every leaf of its chain has since closed (children: T-1491, T-1492, T-1493)`.

This is case 3 of T-1581, exactly as it was predicted there and in the gate's own NOTE.
Measured inside one steward run on 2026-09-25:

- **22:30Z** — `check.sh` on `steward/t1578-gate-fits-a-run` printed the NOTE and
  nothing more: *"272 unresolved unit(s) defer to T-1198, a split parent held live by
  ONE leaf (T-1523); when that closes, this gate goes red on all of them."*
- **~22:35Z** — the tickets repo's settle workflow flipped T-1523 to `done` after
  PR #49 merged (`settle: 1 ticket(s) follow their PRs`).
- **22:39Z** — the same `check.sh`, same code, went red on the four steps above.

The owner's note on T-1523 (tickets repo `0ea02dd`, 2026-09-25) asked for the repoint
**before** that PR merged. PR #49 merged without it, so the repoint is now owned by
nobody and dev carries the red.

## Acceptance

1. Every unit whose `unresolved` ticket is T-1198 names a ticket that is actually live
   and actually owns its question — chosen and stated, not swept onto whatever is open.
   Where no live ticket owns it, file the one that does and point at that.
2. `./tools/check.sh` is green on a clean `origin/dev` afterwards, and the four steps
   above are green for the reason that they are satisfied, not skipped.
3. Say in the PR how many units moved and to which ticket, and record the reasoning —
   a pointer is provenance about who owes the work, so a wrong one is a wrong claim.

This is the REPAIR. T-1581 is the mechanism that must stop it recurring; the two are
separate units and this one unblocks the lane today.
