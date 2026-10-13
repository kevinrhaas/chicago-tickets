---
id: T-2461
title: pr-automerge read 'every check green' on a lap head whose content build (bake + smoke) never started: #768 merged 21ef749 on gate + report alone
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-13
pr: kevinrhaas/polecat-platform#198
claimed_by: run 10/13/2026, 8:25:07 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-13T13:35:09Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38403972172
claimed_at: 2026-10-13T13:25:07.182Z
decision: null
decision_answer: null
---

pr-automerge read 'every check green' on a lap head whose content build (bake + smoke) never started: #768 merged 21ef749 on gate + report alone.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was seen (2026-10-13, steward slice 5/5)

- PR #768 (T-2214) head `4d4a9944a`: `gate`, `warranted`, `report` green; `bake` green by 13:06;
  the content build's smoke legs (`smoke (desktop, 9-12)` and the rest) still queued.
- A PR lap then pushed `21ef74936` (merge of dev through #762 into lap/768). On that head the
  Actions list shows only `Chicago 4D — gate` and `stuck PR report`: **no content build run was
  ever created for it** (the 4d4a9944a content build was still queued/in progress on the branch).
- `gh-rest.sh pr-automerge` waited on the gate, then printed "every check on 21ef749 is green —
  merging 21ef749, pinned" and merged. It read two check runs as the whole gate.
- The merge happened to be safe in substance: the lap only brought in dev content already gated
  on dev, the branch's own changes had a green bake on 4d4a9944a, and the run's local smoke on the
  same resolution (desktop 1 87/0, desktop 3 106/0, mobile 3 106/0) was green. The gap is in the
  tool, not in this merge.

## The question

Should pr-automerge refuse to call a head green when a check that ran on its parent (bake, smoke)
is absent from the new head, i.e. compare against the set of check names the PR has carried, and
read "absent" as pending? Or should the content build's concurrency stop swallowing the lap
head's run? Either closes it; the first is a gh-rest.sh change in polecat-platform, the second a
workflow change in this repo.

## Done 2026-10-13 — kevinrhaas/polecat-platform#198 (merged 13:35:09Z, ce61977)

The first of the two answers: a gh-rest.sh change. When a head's own checks are clear,
`pr-automerge` now reads the PR's commits and the branch's workflow runs. A workflow that ran on an
earlier commit of the PR but has no run on the head carries its newest verdict to the head:
running → `pending` (exit 4), red → `refused` (exit 3, `resume`, naming the run and the head that
never re-ran it), green → carried. Runs on commits outside the PR are not read. Read live against
#768, it no longer calls 21ef749 green on `gate` + `report`, and c3fffe5 (no content build, one
push after 79eaf83's FAILED) would have been refused. `test-gh-rest.sh` § 7b-vi replays both; 86/86.

The workflow answer (unfiltered content-build push trigger) was not taken: it would start a full
1.3 GiB checkout on every push to every branch, and with per-ref `cancel-in-progress` each lap would
restart a ~40-minute bake on any PR that owns generator changes.

**Closed by hand, not with `done --pr`:** settle reads every `pr:` as a kevinrhaas/chicago PR
(T-1617, folded into T-1612). chicago #198 is an unrelated PR that was closed without merging, so `done --pr 198`
would have had settle REOPEN this ticket. Not yet followed up: chicago's own `.github/steward/pr-lap.sh`
also reads only `commits/<sha>/check-runs`, and if it merges, it has the same gap.

