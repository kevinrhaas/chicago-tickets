---
id: T-1612
title: A dead claim parks a queue row for days: list --workable prints 'claimed' without saying the claim is three hours stale, and the picking rule says skip anything claimed
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-10-03
pr: 361
claimed_by: run 10/3/2026, 1:31:52 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-03T19:51:56Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37144343848
claimed_at: 2026-10-03T18:31:52.336Z
decision: null
decision_answer: null
---

A dead claim parks a queue row for days: list --workable prints 'claimed' without saying the claim is three hours stale, and the picking rule says skip anything claimed.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured on T-1444, 2026-09-26.** T-1444 was claimed on 2026-09-20 at 14:15 CT by a run
that died. The claim never came off, and for **131.8 hours** the ticket sat at the top of
band 5B reading `claimed`. Its substance had been delivered in the meantime by the tickets
either side of it (T-1490, T-1545), so the row was a finished job wearing a live claim.

`claim` already handles this correctly — it stole the dead claim without argument, saying
`stealing a dead claim (taken 131.8h ago)`. The fault is upstream of `claim`, in what a run
SEES before it gets there:

* `node tools/ticket.mjs list --workable` prints the state word `claimed` and nothing else.
  Nothing on that line says the claim is 131.8 h old, or that the three-hour rule has
  already expired it, or that `claim` would take it.
* `QUEUE.md`'s own picking rule is *"Work top-down, skipping a blocked or already-claimed
  ticket"*, and the steward prompt's slice rule says a claimed item keeps its place. So a
  run reading that list does the correct thing with the information it has: it walks past.
* The result is a row that is invisible to every automated pass and visible only to a run
  that happens to open the ticket file and read `claimed_by` / `claimed_at` by hand. Six
  days of runs did not.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

`list --workable` distinguishes a live claim from a dead one on the line itself — a dead
claim reads as takeable (the same three-hour rule `claim` enforces, from the same place, not
a second copy of the number) — and the ordering rule the steward and the slice logic follow
counts a dead-claimed row as workable. Demonstrated on a ticket with a claim older than
three hours and one with a fresh claim, with the fresh one still protected.

Two things that are NOT this ticket. `claim`'s stealing rule is correct and is not changed.
And a claim going stale because a run died is not itself a fault to fix here — runs die;
what must not happen is the queue hiding the row afterwards.

Related: [[T-1601]] is the other direction of the same reading — a lock that is not work in
flight being read as one.


## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into this ticket:** T-1617. Both are small ticket.mjs fixes to how a ticket's live state is read (stale claims in list --workable; settle reading a non-chicago PR).

### Folded in from T-1617 — settle reads every ticket's pr: as a kevinrhaas/chicago PR, so a ticket whose PR is in polecat-platform never settles, and will be settled by an unrelated chicago PR once the numbers meet

settle reads every ticket's pr: as a kevinrhaas/chicago PR, so a ticket whose PR is in polecat-platform never settles, and will be settled by an unrelated chicago PR once the numbers meet.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found 2026-09-26 at 04:16 CT**, when the owner asked why T-1577 and T-1609 stood at the top of the queue: both sat in `review` with `pr: 177` and `pr: 179`. Those are **kevinrhaas/polecat-platform** pull requests (the fleet steward prompt and pr-automerge live there), merged 2026-09-25 19:26Z and 2026-09-26 05:54Z. Both were settled by hand in the owner's session.

**Why it happened.** `ticket.mjs settle` reads `repos/kevinrhaas/chicago/pulls/<pr>` for every `review` ticket, and `prUrl()` knows only chicago and the pre-move kevinrhaas/custom. A `pr:` is a bare number with no repository. chicago has no PR #177 yet, so the lookup fails and the ticket is left in review for ever. **The fuse:** chicago's own numbering is at about #60. When it reaches #177 and #179, settle will read those unrelated PRs and mark these tickets done, or reopen them, on someone else's merge.

**Acceptance.** `pr:` can name a repository (for example `kevinrhaas/polecat-platform#177`), and `done --pr` accepts that form. `settle`, `prUrl()`, the board and `tickets.json` all read it, and a bare number still means kevinrhaas/chicago. A self-test proves that a cross-repo PR settles from its own repository and that a bare number never reads another repository's PR. T-1577's and T-1609's `pr:` are rewritten to the qualified form in the same change, and any other ticket whose PR is not chicago's is found and listed.
