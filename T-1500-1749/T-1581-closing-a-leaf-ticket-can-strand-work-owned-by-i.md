---
id: T-1581
title: Closing a leaf ticket can strand work owned by its split ancestors and turn dev red for every PR: ticket.mjs done and the gate must catch it before the PR merges, not after
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: 55
claimed_by: run 9/25/2026, 6:44:41 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36201998560
claimed_at: 2026-09-25T23:44:41.798Z
decision: null
decision_answer: null
---

Closing a leaf ticket can strand work owned by its split ancestors and turn dev red for every PR: ticket.mjs done and the gate must catch it before the PR merges, not after.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Asked by the owner, 2026-09-25**, after dev went red three times in one afternoon when tickets closed, with no code wrong.

## What happened, three times in one day

1. **#40 (T-1448) merged at 16:13Z.** T-1448 was the last live leaf of `T-1189 → T-1434 → T-1448`. When it settled `done`, twelve resident cohort units whose `unresolved` ticket is T-1189 deferred to finished work. The research ledger's ownership rule fired and four gate steps went red on dev and on every PR. It was fixed by #44 (T-1567/T-1568), about 2.5 hours later.
2. **#43 (T-1560) merged at 17:50Z.** The order book's re-family programme names T-1556 (split). T-1560 was its last *direct* piece, so `every_work_order_names_a_live_ticket` called the programme ended, although T-1564 was open under the split T-1559. That gate went red on dev. It was fixed in #44 (T-1575: the walk now descends through split pieces).
3. **Imminent: #49 (T-1523).** 272 landholding units defer to T-1198, held live by T-1523 alone. It is written onto T-1523 so the closing PR repoints them, but only because a person read a NOTE.

**The shape is always the same.** A work pointer names a *split ancestor*. The last live descendant closes somewhere else. The pointer goes dead on dev, found afterwards by whichever run gates next, and every open PR inherits the red until someone repairs it.

## Why the existing guards miss it

- **T-1548's scanner in `ticket.mjs done`** refuses to close a ticket that a committed file still names as live work. It matches the closing ticket's **own id** only. All three pointers above named an *ancestor* of the ticket being closed.
- **`done --pr` sets `review`, and the tickets repo's settle workflow sets `done` when the PR merges.** So the state that breaks dev arrives *after* the PR's gate has already passed. The PR's gate reads the ticket as `review`, which is live.
- **#44 added a NOTE** naming any pointer one closure away from this ("held live by ONE leaf"). A NOTE is read by a person or not at all.

## Acceptance

1. **Closing refuses, naming what it would strand.** When `ticket.mjs done` (and `done --pr`) closes a ticket, it computes every ancestor that would be left with **no live descendant at any depth**. It then scans for units, rules and work orders that defer to any of them, using the same readers the ledger and order-book gates use rather than a grep. If any exist, it refuses and names each one (file, rule or bucket, count, ancestor). The repo's `--anyway --why` escape applies.
2. **The gate asks the same question for PRs in review.** A `check.sh` step reads the tickets this branch closes (its `review` tickets, or a declared list). It evaluates the research ledger's and order book's ownership gates **as if those tickets were `done`**, so the PR that would strand units goes red on its own diff, before merge, and not dev afterwards.
3. **One walk, not three.** The "live through its pieces at any depth" rule (T-1575's `live_pieces_of`) and the ledger's `split_live` reading (T-1237/T-1421) are one shared definition. The order book, the research ledger and `ticket.mjs` all use it.
4. **Proved on today's cases.** Self-tests on fixtures reproduce all three shapes (a leaf closing under a split grandparent, a direct piece closing while a grandchild lives, a single-leaf chain). Each is caught, and a split with a live descendant two levels down is NOT refused.
5. **Measured on dev at landing.** List every pointer that is currently one closure away (today: the 272 on T-1198 via T-1523, unless #49 has already repointed them) and say what each is waiting on.
