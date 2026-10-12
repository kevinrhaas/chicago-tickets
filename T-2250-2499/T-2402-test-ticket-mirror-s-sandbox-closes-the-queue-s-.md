---
id: T-2402
title: test_ticket_mirror's sandbox closes the queue's top ticket, and an image-gated top ticket (T-2369) is refused there: check.sh is red on every PR
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-12
closed: null
pr: 723
claimed_by: run 10/12/2026, 12:14:51 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38205436187
claimed_at: 2026-10-12T05:14:51.780Z
decision: null
decision_answer: null
---

test_ticket_mirror's sandbox closes the queue's top ticket, and an image-gated top ticket (T-2369) is refused there: check.sh is red on every PR.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: CI's bake job on #720 failed exactly this one step of 863 (job 114669186011); every PR's check.sh fails it while an image-gated ticket tops the queue

## What fails, and why (found by T-2395, 2026-10-12)

CI's `bake` job on chicago#720 (job 114669186011) ran 863 check.sh steps and failed one: `closing a
ticket leaves the mirror fresh, and a stale one still fails` (`node tools/test_ticket_mirror.mjs`).
The test builds a sandbox, copies a fixed list of `tools/` files into it (line ~53), and closes the
queue's first workable ticket (line ~136: `list --workable`, `workable[0]`) with `ticket.mjs done
<victim> --pr 9999`. The victim was T-2369, whose `## Image gate` makes `done` read the image gate,
and the sandbox has no `tools/image_gate.mjs`:

    T-2369 IS NOT FINISHED: ITS BUILDING DOES NOT YET MATCH ITS PICTURES (the image gate).
      .../tools/image_gate.mjs is missing, so the image gate cannot be read

So the step's verdict depends on what tops the live queue, not on the tree under test: red on every
PR while an image-gated ticket is first, green otherwise.

**Acceptance:** `test_ticket_mirror.mjs` passes whatever the live queue's order — it closes a
victim that carries no `## Image gate` (or passes `--anyway --why` for the sandbox), so the image
gate's refusal is never what it measures; its existing assertions are unchanged; check.sh green.
