---
id: T-1601
title: The claim check reads a MINT lock as work in flight, so every freshly filed ticket looks already taken and the only way past is --force
state: open
epic: META
requested_by: loop
seen: false
effort: M
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

The claim check reads a MINT lock as work in flight, so every freshly filed ticket looks already taken and the only way past is --force.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The measurement, 2026-09-26 (found while claiming T-1594)

`node tools/ticket.mjs claim T-1594` refused, on a ticket nobody held:

```
T-1594 looks like it is already being worked:
  idlock/t-1594
Check whether that branch has an open PR before starting.
```

`idlock/t-1594` is not a work branch. It is the MINT lock T-1287 introduced: `reserveIdNum`
pushes a parentless empty commit to `refs/heads/idlock/t-NNNN` with `--force-with-lease=<ref>:`
so that two runs minting in the same second cannot take the same id. Its commit message even
says which it is — `claim T-1594 — mint nonce: …`, written by `claimCommit(id, 'mint', null)`.
Work claims use a different namespace, `claim/t-nnnn` (`claimBranch`), and there was no
`claim/t-1594`: `git ls-remote origin 'refs/heads/claim/*'` was EMPTY across the whole
repository at the time.

So the pre-claim in-flight check is matching the mint lock. Every ticket filed since T-1287
landed has one of these branches for life, which means:

* **every newly filed ticket reads as already taken**, i.e. exactly the tickets at the top of
  the queue that a run is told to take first;
* the only way past is `claim --force`, whose entire purpose is to STEAL a claim it believes
  another run holds — so the habit this trains is to force past a live claim without looking.
  That is the one thing the lock exists to prevent, and it is being taught by the false
  positive.

`ticket.mjs inflight` reports the same branches (it listed `idlock/t-1582`, `idlock/t-1583`,
`idlock/t-1587`…`idlock/t-1592` as "15 branch(es) on unfinished tickets" while none of those
tickets was claimed and none had a PR), so the same fault reads out of the tool a run is
pointed at when it wants to know whether to force past a claim. Two runs were live at that
moment and their real branches were `steward/t1545-…` and `steward/t1564-…`.

**Acceptance:** the branch scan behind `claim` and `inflight` excludes the `idlock/` namespace
(or, better, reads only the namespaces that mean work — `claim/` and branches carrying a ticket
id that have commits of their own), so a freshly filed unclaimed ticket claims cleanly with no
`--force`; `inflight` names no mint lock; and a self-test puts a mint lock and a real work
branch in front of the scan and requires it to report only the second. Check that the same scan
is not read anywhere else (BOARD, `check`) with the same result.
