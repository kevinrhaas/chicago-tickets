---
id: T-1655
title: .github/steward/pr-rest.sh reads the repo from $GITHUB_REPOSITORY, so a steward run driving it from a chicago checkout comments on and labels a PR in polecat-platform instead
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-09-27
pr: 106
claimed_by: run 9/26/2026, 11:40:09 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-27T05:19:52Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36294756723
claimed_at: 2026-09-27T04:40:10.402Z
decision: null
decision_answer: null
---

.github/steward/pr-rest.sh reads the repo from $GITHUB_REPOSITORY, so a steward run driving it from a chicago checkout comments on and labels a PR in polecat-platform instead.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured 2026-09-27, by the run that hit it (T-1652, PR #104).**

`.github/steward/pr-rest.sh` line 38: `repo="${GITHUB_REPOSITORY:?…}"`. There is no
`--repo` and no argument for it. A steward improve run executes inside a
**polecat-platform** Actions job and clones this repo into the workspace, so
`$GITHUB_REPOSITORY` is `kevinrhaas/polecat-platform` for every call made from
`chicago-repo/` — while `.github/steward/improve.md` tells a run to use *"that
repo's own `.github/steward/pr-rest.sh resume <N>`"* for a chicago PR. The two
instructions cannot both be followed.

What it actually did:

* `pr-rest.sh create` **failed loudly** — 422, `base` and `head` invalid, because
  `dev` and `steward/t1652-bake-only-list` do not exist in polecat-platform. Its
  recovery notice printed a `polecat-platform/compare/…` URL, which is the tell.
* `pr-rest.sh resume 104` **succeeded silently against the wrong repository**: it
  commented the resume reason on, and applied the `resume` label to,
  **kevinrhaas/polecat-platform#104** — an unrelated PR ("fix: mobile drawer has no
  way to close except tapping the backdrop"). Both were reverted by hand
  (comment 5852649999 deleted, label removed, verified back to 0 labels / 0
  comments) and re-applied to kevinrhaas/chicago#104 with the platform's own
  `gh-rest.sh pr-resume kevinrhaas/chicago 104 …`, which takes the repo as its
  first argument and is why it cannot make this mistake.

The silent case is the whole ticket. A number collision across two repos is not
rare — both had a #104 open on the same day — so the failure mode is *labelling a
stranger's PR*, which is the one thing T-1577 was written to stop happening
without the owner knowing why.

**Acceptance:** every verb in `.github/steward/pr-rest.sh` names the repository it
acts on, or refuses to act. Concretely: take `--repo owner/name`, default it to the
**git remote of the checkout it is run from** (not the ambient environment), and
refuse with a one-line error when the resolved repo does not contain the head
branch or the PR. A self-test proves the refusal fires when `$GITHUB_REPOSITORY`
names a repo the checkout is not. `tools/check_gh_rest.mjs` is the existing gate
over these surfaces and is where the assertion belongs.
