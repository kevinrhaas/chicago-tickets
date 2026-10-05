---
id: T-1721
title: Two slices relapped PR #154 at the same time: a resume PR is not counted as a row a live sibling holds, so under slices > 1 more than one run takes it
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-28
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

Two slices relapped PR #154 at the same time: a resume PR is not counted as a row a live sibling holds, so under slices > 1 more than one run takes it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Measured 2026-09-28: slices 1 and 4 of a 4-slice chicago lane each spent most of a run
relapping **the same** PR (#154, T-1707) over `dev`, and reached the same eight conflict
resolutions, the same derivation fixpoint and the same four restated numbers independently.
Slice 4 found out only when its `git push` was rejected, after its gate and all four smoke
legs had already run. One of the two runs was wasted, and the waste was not a race the
claim mechanism could catch.

**Why the claim did not catch it.** `ticket.mjs claim` guards a ticket about to be WORKED.
T-1707 was already `review` with an open PR, so neither run claimed anything, and
`inflight` showed both of them the same true thing: *"PR #154 is OPEN and labelled resume."*

**Why both runs took it anyway, correctly.** The steward prompt holds two rules that point
different ways when `slices > 1`:

* *"RESUMABLE WORK COMES BEFORE NEW QUEUE WORK. Before you pick, look for an open `resume`
  PR on your focus app. If there is one, THAT is your unit."* — unconditional, no slice
  index in it.
* *"TAKE THE k-TH TOPMOST WORKABLE ITEM"* — which spreads N slices over N rows.

The first overrides the second, and it is the same for every slice, so N slices take one PR.
It is worse than the cold-fill case the k-th rule was written for: there, N runs build N
copies of new work and N-1 are thrown away; here they push to a single shared branch, so the
loser discovers the collision only at push time.

**What a fix has to decide**, and both halves matter:

1. **Which slice owns a `resume` PR.** The cheap answer is slice 1, with the other N-1
   falling to the k-th row as normal — but then a lane whose slice-1 slot is busy leaves a
   resumable PR for the janitor. A claim-shaped answer is better: a resume PR is a row a
   live sibling can hold, so it occupies a place in the workable list and the usual "never
   take one somebody is on" rule does the work with no new concept.
2. **How a slice detects the hold without a push.** `inflight` already reads remote branches
   and the PR list; it could say *"a branch carrying this PR was pushed N minutes ago — a
   live run is relapping it"* from the PR head commit's own committer date. Slice 4 could
   have known at 12:03 instead of 12:44.

This ticket is about the chicago-side tools (`inflight`, and whatever the tickets repo can
assert); the prompt rules themselves live in `kevinrhaas/polecat-platform`
(`.github/steward/improve.md`) and changing them is a platform unit, not this repo's — name
that in the PR rather than reaching for it here.

## Seen again, 2026-10-05 (PR #442, T-2115)

It happened again. Slice 5/5 (a refill) took `resume` PR #442 at 02:31Z. At 02:33:46Z
another run had already pushed its own lap (`cacb545`, "restamp the changelog after lapping
dev"). Both laps merged the same `dev` (`eb0a5117`) and differed only in the changelog's
stamp instant. The PR merged from `cacb545` at 02:47:40Z. Slice 5's push of `32c1d20f` landed
on the branch after the PR had moved past it, so a whole check.sh run and a mobile part-13
smoke went into duplicate work. `inflight` printed `PR #442 OPEN · resume` and had no way to
show that another run was lapping it right then. What would have caught it: a marker for
"a run is lapping this PR now", like a claim, that `inflight` reads.
