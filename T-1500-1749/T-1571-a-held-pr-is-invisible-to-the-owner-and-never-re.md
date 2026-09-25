---
id: T-1571
title: A held PR is invisible to the owner and never resumed: split hold into the owner's park switch and a run's unfinished handoff that the next run picks up, and put every held PR on the 4D Board with its reason
state: open
epic: META
requested_by: owner
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

A held PR is invisible to the owner and never resumed: split hold into the owner's park switch and a run's unfinished handoff that the next run picks up, and put every held PR on the 4D Board with its reason.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Asked by the owner, 2026-09-25**, on finding three PRs parked on `hold` whose reasons he had not seen: *"that seems like a bad move because i am not aware of why they are held"* — and answering yes to filing this.

## What is wrong, measured 2026-09-25

`hold` was designed as **the owner's park switch** (`.github/steward/pr-stuck.sh`: "The owner's park switch"; AGENTS.md: "`hold` there means a run parked that work for the owner on purpose, so do not rebuild it, do not take the ticket and do not delete the branch"). Every automated pass therefore skips a held PR: the PR lap, the janitor, merge-ready and the stuck reporter.

But the steward prompt (`polecat-platform/.github/steward/improve.md`) tells a run to apply the same label when it merely **could not finish**: verification failed, the turn budget ran low, dev moved too fast, or dev's own gate was red. So a label that means "the owner is deciding" is mostly applied to work that needs nobody's decision, only a later run. Nothing ever lifts it, and the only place the reason is written is the PR body, which the owner does not read.

The three open PRs on 2026-09-25 at 17:35Z were all of that second kind; none needed an owner ruling:
- **#39 (T-1563)**: "this run's clock ran out" before its full gate. CI then passed all 620 steps, so the stated reason was already stale, and the PR drifted into conflict with dev while held.
- **#41 (T-1521)**: complete, held only because dev's gate was red (T-1567). "Lift the hold when T-1567 lands."
- **#42 (T-1565)**: the same. "Lift the `hold` and re-gate once `dev` is green."

Each needed a person in a session to notice, lap, re-gate and merge it.

**Acceptance:**
1. **Two labels, two meanings.** `hold` stays the owner's switch and no run applies it. A run that cannot finish applies a distinct label (e.g. `resume`) with its reason as a structured first line of a PR comment (`resume: <reason> · waits on: <ticket or "nothing">`).
2. **A later run resumes it before taking new queue work.** Resumable PRs are worked first: merge dev in, re-derive, fix what is red, gate, merge. A `resume` PR whose `waits on` ticket is still open is skipped, and the run says so. Whether the lap, merge-ready and the stuck reporter treat `resume` as live, and the tickets repo's settle workflow's reading of it, are stated.
3. **Visible on the 4D Board.** Every open PR carrying either label appears with its reason and its age: a `hold` as the owner's own, a `resume` as work the loop still owes. If a `hold` really does need the owner, it arrives as `ticket.mjs ask` on its ticket, with options, so it gets the Board's one-click answer.
4. The steward prompt (polecat-platform), AGENTS.md, `pr-stuck.sh` and `pr-lap.sh` all say the same thing, and a test fixture proves that a `resume` PR is picked up and a `hold` PR is not.
5. The PRs open at landing time are relabelled by the new rule.
