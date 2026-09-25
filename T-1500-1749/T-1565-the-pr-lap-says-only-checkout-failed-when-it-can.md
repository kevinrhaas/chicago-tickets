---
id: T-1565
title: The PR lap says only `checkout failed` when it cannot check out a branch, and #1629 was left alone on no evidence at all
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: 42
claimed_by: run 9/25/2026, 11:00:48 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T19:54:46Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36157433279
claimed_at: 2026-09-25T16:00:48.969Z
decision: null
decision_answer: null
---

The lap's checkout guard says four words and nothing else:

    git checkout -B "lap/$N" "origin/$BR" -q 2>/dev/null || { say "  checkout failed"; ... }

Both `git fetch` and `git checkout` are silenced to `/dev/null`, so when #1629
failed here on 2026-09-21 (lap run 35624254338) the run summary carried no reason
at all — not which of the two failed, not git's own message, not the ref it could
not resolve. T-1521 measured it as a SECOND fault in the same lap run and
deliberately did not fold it in: T-1521 fixed the rebuild's missing publish, which
is a different cause with a different fix.

The lap is otherwise good at this — every other refusal in it names the step and
tails the log, which is how T-1521 was found in the first place. These two guards
are the exception.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- The fetch and the checkout are reported separately, each with git's own stderr in
  the run summary, the way the rebuild and regeneration failures already are.
- A PR whose branch has been deleted under the lap — the likeliest cause — reads as
  that, and not as an unexplained `checkout failed`.
- Held to it by `tools/test_pr_lap_publish.mjs`'s harness or one like it: the real
  script, a real bare remote, a branch that is not there.
