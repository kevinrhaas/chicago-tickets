---
id: T-2362
title: CI smoke leg desktop 10-14 overruns its 40-minute timeout on every run since T-2337 split part 10 into 10+11: five parts at ~8 min each, cancelled at 40m on dev (run 38138197680) and on #696 (run 38140175452); re-tile the bake workflow's desktop legs so each fits its cap, and let merge-ready see a PR go clean again
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-11
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

CI smoke leg desktop 10-14 overruns its 40-minute timeout on every run since T-2337 split part 10 into 10+11: five parts at ~8 min each, cancelled at 40m on dev (run 38138197680) and on #696 (run 38140175452); re-tile the bake workflow's desktop legs so each fits its cap, and let merge-ready see a PR go clean again.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> no PR can reach 'clean' while this leg is always cancelled, so merge-ready never merges and every run must merge by hand past a cancelled check

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
