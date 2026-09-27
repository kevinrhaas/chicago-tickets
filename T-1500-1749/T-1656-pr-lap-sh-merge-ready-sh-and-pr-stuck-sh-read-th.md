---
id: T-1656
title: pr-lap.sh, merge-ready.sh and pr-stuck.sh read the repository from $GITHUB_REPOSITORY too, so any pass driven from a clone inside another repo's job acts on that repo
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: null
claimed_by: run 9/27/2026, 6:28:11 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36315688900
claimed_at: 2026-09-27T11:28:12.897Z
decision: null
decision_answer: null
---

pr-lap.sh, merge-ready.sh and pr-stuck.sh read the repository from $GITHUB_REPOSITORY too, so any pass driven from a clone inside another repo's job acts on that repo.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Filed by the run that fixed T-1655 for `pr-rest.sh`, which found the same shape
three files over and deliberately did not widen its own diff into them.**

| script | line | today |
|---|---|---|
| `.github/steward/pr-lap.sh` | 39 | `REPO="${GITHUB_REPOSITORY:-kevinrhaas/chicago}"` |
| `.github/steward/merge-ready.sh` | 56 | the same |
| `.github/steward/pr-stuck.sh` | 79 | the same |

The `:-kevinrhaas/chicago` default reads as a safety net and is not one: in an
Actions job the variable is always SET, so the default never fires and the value is
whatever repository owns the job. These three are less exposed than `pr-rest.sh`
was — they are run by this repository's own workflows, where the ambient name is
correct — but `pr-stuck.sh` and `merge-ready.sh` both WRITE (comments, labels), so
the silent wrong-repository write T-1655 measured is available to them the moment
anything drives them from a clone, which is exactly how T-1652's run drove
`pr-rest.sh`.

**Acceptance:** the three resolve their repository the way `pr-rest.sh` now does —
`--repo owner/name`, defaulting to the origin remote of the checkout the script is
in, never the environment — and `tools/check_gh_rest.mjs`'s `REPO_NAMED` list grows
to include them, which is what makes the tripwire cover them. Their existing tests
(`test_pr_lap_list.mjs`, `test_pr_lap_publish.mjs`, `test_pr_lap_checkout.mjs`,
`test_pr_stuck.mjs`) name the repository explicitly so that they keep testing what
they were written to test; at least one proves the refusal fires when
`$GITHUB_REPOSITORY` names a repository the checkout is not.
