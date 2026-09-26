---
id: T-1596
title: The PR lap's ticket-id collision step crashes where tickets/ is absent, so a green PR that merges dev cleanly is left alone as a 'TICKET ID COLLISION': resolve_id_collisions answers 'not applicable' where the tickets live in their own repository
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: null
claimed_by: run 9/25/2026, 7:59:32 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-26T00:59:32.871Z
decision: null
decision_answer: null
---

The PR lap's ticket-id collision step crashes where tickets/ is absent, so a green PR that merges dev cleanly is left alone as a 'TICKET ID COLLISION': resolve_id_collisions answers 'not applicable' where the tickets live in their own repository.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Asked by the owner, 2026-09-25**, answering "make the fix yourself".

**Measured.** At 00:29Z the PR lap run 36205023683 reported, on PR #45 (gate green, merges dev cleanly):

```
TICKET ID COLLISION it would not resolve — left alone:
    code: 'ENOENT', syscall: 'scandir',
    path: '/home/runner/work/chicago/chicago/chicago/4d/tickets'
```

`pr-lap.sh` runs `tools/resolve_id_collisions.mjs --base origin/dev` after every clean merge. That tool's `ticketsOnDisk()` reads `chicago/4d/tickets/` without asking whether it exists. Since 2026-09-23 the tickets are kevinrhaas/chicago-tickets, gitignored here and not cloned by the lap, so the read throws. The lap then counts the PR as left alone, with a message about a collision that does not exist. In a clone that does hold `tickets/`, it holds it as its own repository in chunk folders the flat reader never listed, so "no collision" was true only by accident.

**Acceptance.** Where `tickets/` is absent or is a repository of its own, the tool exits 0 in every mode (repair, `--check`), and it says why the question does not apply: ids are allocated on the tickets repository's `main` by `ticket.mjs`, which renumbers a collision as it pushes. Its self-test proves both shapes. The in-tree layout's existing cases still pass unchanged.
