---
id: T-2461
title: pr-automerge read 'every check green' on a lap head whose content build (bake + smoke) never started: #768 merged 21ef749 on gate + report alone
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: run 10/13/2026, 8:25:07 AM CT
blocked_on: null
needs_bake: false
closed_at: null
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
