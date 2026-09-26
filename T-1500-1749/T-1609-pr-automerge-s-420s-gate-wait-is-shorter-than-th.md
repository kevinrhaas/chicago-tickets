---
id: T-1609
title: pr-automerge's 420s gate wait is shorter than this repo's own CI gate, so a finished green unit ends as a resume PR and the janitor pays a lap for it
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: 179
claimed_by: run 9/26/2026, 12:45:06 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36221512163
claimed_at: 2026-09-26T05:45:06.749Z
decision: null
decision_answer: null
---

pr-automerge's 420s gate wait is shorter than this repo's own CI gate, so a finished green unit ends as a resume PR and the janitor pays a lap for it.

**Acceptance.** Either the wait is long enough that a green unit merges inside its own run,
or the refusal stops being the normal outcome for a PASSING gate. Measured, not asserted:
the next two steward units on this repo merge in-run, or the file that decides it says in
writing why 420 s is the right number and what the run should do instead.

**THE MEASUREMENT, 2026-09-26.** Two consecutive units, both fully gated green in the
foreground, both ended as `resume` PRs on the same line:

* **PR #60** (T-0419) — opened 04:13Z. `pr-automerge` refused at 04:20Z: *"check gate
  (in_progress) had not finished within 420s"*. The janitor lapped it twice (`lap/60`) and
  merged it as `f6f91ed3` at about 05:20Z — **an hour after the work was finished and green.**
* **PR #63** (T-1603) — opened 05:31Z. Refused at 05:38Z, same line, same reason.

**WHY IT IS NOT A RED GATE.** `in_progress` is not `failure`. The refusal is correct as
written — T-1572 built it precisely so nothing merges onto a gate nobody read, after #43
landed on a red `dev` one second after opening — and nothing here proposes merging blind.
The problem is the NUMBER: `GH_REST_GATE_WAIT_SECONDS` defaults to 420 s, and this repo's
`chicago-4d-check.yml` runs the same 635-step gate that takes several minutes locally plus
a `pip install` and a publish before it. So the wait expires on a gate that was always
going to pass, and the refusal is a timeout dressed as a verdict.

**WHAT IT COSTS, per unit.** One janitor lap (fetch, merge base, re-derive, re-gate,
merge) for work that was already green; up to two hours of latency between a finished unit
and dev moving; and a `resume` PR whose stated reason is stale the moment CI finishes —
exactly the drift T-1577 measured on the three held PRs ("one's stated reason was already
stale — CI had since passed all 620 steps").

**Three remedies, and the one this ticket does NOT ask for.** (a) Raise the default wait on
this repo to something past the gate's own measured duration — cheapest, and the run pays
the minutes it was going to pay anyway. (b) Have `pr-automerge` distinguish *pending* from
*red*: on a red check refuse as now; on a still-pending one, arm-or-poll rather than
refuse, since a pending gate is not a verdict. (c) Leave it and accept the janitor lap as
the design. **NOT asked for:** `GH_REST_MERGE_BLIND=1` as routine practice. That is the
switch T-1572 exists to keep off the normal path, and a run that sets it every time has
re-created #43.

**Where it lives.** `gh-rest.sh` is in **kevinrhaas/polecat-platform**
(`.github/steward/gh-rest.sh`), not in this repo — so this ticket is a finding filed where
the loop files findings, and the fix is a platform change. It sits under T-1577 because it
is the same contract: what a run does when it cannot finish.

**Found by:** the T-1603 run, which hit it on its own merge after watching it happen to
PR #60 earlier in the same hour.
