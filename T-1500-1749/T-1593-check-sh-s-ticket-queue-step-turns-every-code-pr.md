---
id: T-1593
title: check.sh's ticket-queue step turns every code PR red the moment an unsplit L ticket is filed: T-1585 and T-1586 did it at 23:07Z and no code change can clear it
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
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

check.sh's ticket-queue step turns every code PR red the moment an unsplit L ticket is
filed: T-1585 and T-1586 did it at 23:07Z and no code change can clear it.

## The measurement, 2026-09-25

The `gate` on kevinrhaas/chicago#51 — a PR whose whole diff is AGENTS.md, a changelog entry
and three files under `tools/` — came back red on five of 628 steps. The fifth was:

```
== ticket queue
ticket queue FAILED:
  - T-1585-…: effort L is in the queue — MORE THAN ONE RUN — must be split before it can be
    claimed. Run `node tools/ticket.mjs split T-1585 "first piece" "second piece"`
  - T-1586-…: effort L is in the queue — MORE THAN ONE RUN — must be split before it can be
    claimed. Run `node tools/ticket.mjs split T-1586 "first piece" "second piece"`
```

Both tickets were filed into the tickets repo minutes earlier. Nothing in the code repo can
make that step green, and nothing a PR author does can either: the state the step reads
lives in a different repository, so **the red belongs to every open PR at once and to none
of them in particular**. #51 was merged past it with `GH_REST_MERGE_BLIND=1` and the reason
written on the PR, which is the escape hatch working — but it is an escape hatch, and the
next run meets the same wall with less evidence in hand.

This is the same *shape* as T-1581 — shared tickets-repo state turning the code gate red
for everybody — but a different cause: T-1581 is a leaf closing under a split ancestor;
this is a ticket being *filed* at an effort the queue refuses to hold.

The queue rule itself is right and should not be weakened: an L in the queue is a ticket no
run may claim, and saying so loudly is the point. What is wrong is *where it is said*. A
filing fault is caught at the moment of filing, where one person can fix it in one command,
not hours later in the gate of an unrelated code change.

**Acceptance:** `ticket.mjs new --effort L` refuses at filing time and says to split
instead, so an unsplit L cannot enter QUEUE.md in the first place; and the gate's
`ticket queue` step distinguishes what the PR's own diff can fix from what it cannot —
either by reporting an inherited queue fault as a WARN naming the filing that caused it and
the one command that clears it, or by the tickets repo's own check catching it on push.
Prove it by filing an L against a fixture and watching the refusal, and by re-running the
step against the state that failed here. T-1585 and T-1586 were themselves split
(into T-1590, T-1591, T-1592) about half an hour later and the step went green again on its
own, so the standing red is already gone — what is left to fix is that it could happen at
all, and that the run which met it had to prove the red was not its own before it could
merge.
