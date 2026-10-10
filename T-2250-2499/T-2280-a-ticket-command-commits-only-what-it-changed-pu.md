---
id: T-2280
title: A ticket command commits only what it changed: pushTickets' git add -A published a stray local edit, and T-1205's done (b679d90) reverted T-1171 from split to a claimed row the queue then offered for a week
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: 611
claimed_by: run 10/9/2026, 9:31:01 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38016738879
claimed_at: 2026-10-10T02:31:01.025Z
decision: null
decision_answer: null
---

A ticket command commits only what it changed: pushTickets' git add -A published a stray local edit, and T-1205's done (b679d90) reverted T-1171 from split to a claimed row the queue then offered for a week.

**What happened (measured 2026-10-10).** T-1171 was split at 07:57Z on 2026-10-03 (`08c1129`). At
09:00Z the T-1205 run, whose order-book derive refused T-1171's rows once it was split, restored the
pre-split file in ITS OWN tickets clone (`git show 08c1129~1:$f > $f`, its words: "in my local
tickets copy only; nothing was pushed"). It then ran `ticket.mjs done T-1205`. `pushTickets` stages
with `git add -A`, so the commit "T-1205: review — PR #336" (`b679d90`) carried the stray file too
and put T-1171 back to `claimed`. Nobody saw it: the message named another ticket. T-1171 then sat
in `list --workable` as a `TAKEABLE dead claim` for seven days, and a slice on 2026-10-10 spent its
first hour establishing it was spent work. (The dirty tree also made that `done`'s own pull fail,
so the command read a stale clone — "reading the local copy".)

**Acceptance:**
- A mutating `ticket.mjs` command other than `sync` that finds local edits in the tickets clone to
  files it was not asked to change REFUSES before it pulls, reads or writes anything, naming each
  file and the two remedies (`sync -m` to publish it, `git -C tickets checkout`/`stash` to set it
  aside). It never publishes a file it did not mean to, and never discards one.
- An edit to the ticket the command names (a finding added to T-NNNN, then `done T-NNNN`) still
  rides that command, as it does today.
- `sync` is unchanged: publishing hand edits is its job.
- `test_ticket_repo_mode.mjs` proves both, for real against a bare repository: a stray edit to
  another ticket refuses `done` with nothing pushed and the edit still on disk; an edit to the
  named ticket lands with its `done`.
- T-1171 restored to `split` (done in the tickets repo, 2026-10-10).
