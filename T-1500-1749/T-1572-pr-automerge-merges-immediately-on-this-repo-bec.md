---
id: T-1572
title: pr-automerge MERGES IMMEDIATELY on this repo, because auto-merge is disabled on kevinrhaas/chicago — a steward slice cannot arm-and-walk-away and lands its PR on whatever state dev is in
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: 47
claimed_by: run 9/25/2026, 1:53:47 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T19:39:15Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36175706148
claimed_at: 2026-09-25T18:53:48.236Z
decision: null
decision_answer: null
---

pr-automerge MERGES IMMEDIATELY on this repo, because auto-merge is disabled on kevinrhaas/chicago — a steward slice cannot arm-and-walk-away and lands its PR on whatever state dev is in.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## MEASURED 2026-09-25 on PR #43

`bash "$GHREST" pr-automerge kevinrhaas/chicago 43 squash "…"` printed:

    gh-rest: pr-automerge: could not arm ({"errors":[{"type":"UNPROCESSABLE",
      "message":"Auto merge is not allowed for this repository"}]}) — merging directly instead
    7107fcaac32ca7271f9cde7e3a76da2a1d212f9e

and the PR was merged into `dev` in that same call, about one second after it was opened.

WHY THAT MATTERS HERE AND NOT ELSEWHERE. The steward prompt's argument for
`pr-automerge` is that it "ARMS GitHub's auto-merge and returns, so the PR lands the
moment its required checks go green" and is "never worse than `pr-merge`". Both halves
rest on auto-merge being ENABLED on the repository. It is not enabled on
kevinrhaas/chicago, so the documented fallback — merge directly — is the ONLY path this
call ever takes here, and every slice that reaches for it is merging with no gate
consulted at all. On 2026-09-25 that put #43 onto a `dev` whose four research steps were
already red (T-1567/T-1568), which #43 neither caused nor touched, but which a green gate
would have caught and an armed auto-merge would have waited for.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Either auto-merge is enabled on kevinrhaas/chicago (a repository setting, and if that
  is the owner's call then `ask` him rather than assuming), or `pr-automerge`'s fallback
  on THIS repo does not merge blind: it reads the PR's own check runs and refuses to
  merge a red or pending one, saying which check it refused on.
- Whichever way it goes, the behaviour is stated where a slice will read it before it
  calls the tool — `chicago/4d/docs/PIPELINE.md` — because the prompt's sentence about
  arming is false here and a run has no way to find that out except by merging.
- A run that cannot merge safely still finishes: the refusal leaves the PR open and
  labelled `hold` with the check it refused on, which is the outcome the steward rules
  already ask for.

**Note.** The `$GHREST` script itself lives in kevinrhaas/polecat-platform
(`.github/steward/gh-rest.sh`), so the fix for the second option is a PR there, not here.
This ticket is filed in chicago because chicago is where the consequence lands.
