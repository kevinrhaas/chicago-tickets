---
id: T-1617
title: settle reads every ticket's pr: as a kevinrhaas/chicago PR, so a ticket whose PR is in polecat-platform never settles, and will be settled by an unrelated chicago PR once the numbers meet
state: open
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-26
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

settle reads every ticket's pr: as a kevinrhaas/chicago PR, so a ticket whose PR is in polecat-platform never settles, and will be settled by an unrelated chicago PR once the numbers meet.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found 2026-09-26 at 04:16 CT**, when the owner asked why T-1577 and T-1609 stood at the top of the queue: both sat in `review` with `pr: 177` and `pr: 179`. Those are **kevinrhaas/polecat-platform** pull requests (the fleet steward prompt and pr-automerge live there), merged 2026-09-25 19:26Z and 2026-09-26 05:54Z. Both were settled by hand in the owner's session.

**Why it happened.** `ticket.mjs settle` reads `repos/kevinrhaas/chicago/pulls/<pr>` for every `review` ticket, and `prUrl()` knows only chicago and the pre-move kevinrhaas/custom. A `pr:` is a bare number with no repository. chicago has no PR #177 yet, so the lookup fails and the ticket is left in review for ever. **The fuse:** chicago's own numbering is at about #60. When it reaches #177 and #179, settle will read those unrelated PRs and mark these tickets done, or reopen them, on someone else's merge.

**Acceptance.** `pr:` can name a repository (for example `kevinrhaas/polecat-platform#177`), and `done --pr` accepts that form. `settle`, `prUrl()`, the board and `tickets.json` all read it, and a bare number still means kevinrhaas/chicago. A self-test proves that a cross-repo PR settles from its own repository and that a bare number never reads another repository's PR. T-1577's and T-1609's `pr:` are rewritten to the qualified form in the same change, and any other ticket whose PR is not chicago's is found and listed.
