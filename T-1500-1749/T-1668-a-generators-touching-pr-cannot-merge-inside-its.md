---
id: T-1668
title: A generators-touching PR cannot merge inside its own run: the warranted full-town bake outlasts both pr-automerge laps, so every such PR becomes a resume PR the janitor inherits green
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 9/27/2026, 7:44:24 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36319836343
claimed_at: 2026-09-27T12:44:24.323Z
decision: null
decision_answer: null
---

A generators-touching PR cannot merge inside its own run: the warranted full-town bake outlasts both pr-automerge laps, so every such PR becomes a resume PR the janitor inherits green.

Measured on T-1652 / PR #104, 2026-09-27. The PR was finished, foreground-gated
green (check.sh 666 steps none red; smoke mobile+desktop stage 3 94/0 each, zero
page errors) and mergeable. Three of its four checks completed green — `gate`
(09:31:56Z), `report`, `warranted` — and `bake` was still `in_progress` 18
minutes in. Both `pr-automerge` laps returned `pending` (exit 4), so the run
handed it on and the janitor inherited work that was never in doubt. That is the
exact outcome T-1609 was written to stop, arriving by a route T-1609 did not
close.

It is not a flake and not a misconfiguration; it is arithmetic.
`.github/workflows/chicago-4d-bake.yml`'s `warranted` job bakes when a branch's
own diff against `dev` touches `chicago/4d/generators/**`, `tools/bake.sh` or
that workflow — correctly, since a generators change is exactly what stales a
mesh. PR #104 touched `generators/build.py`, `generators/code_inputs.py` and
`generators/common/selection.py`, so its bake was warranted and right. But a
full-town bake is ~20-30 minutes and two `pr-automerge` laps are 2 x 540 s = 18
minutes, which is under the floor. So **every** PR that touches `generators/`
becomes a `resume` PR by construction, however green it is, and no amount of
laps inside a 600 s foreground ceiling changes that.

Three shapes worth pricing, not a chosen fix:

1. **Let `bake` not be a required check for the merge decision** where the PR's
   own staleness gate already passed. `check.sh` re-derives `validate.py
   --stale` over all 422 assets on the PR's tree; on #104 that was green with no
   rebake (dev's T-1654 having taken `build.py` out of the input recipe). What
   the CI bake adds over that is worth stating explicitly — and if the answer is
   "a rebake proves the generator still runs", that is a different claim from
   "the committed meshes are fresh" and should be named as such.
2. **Scope the warranted bake the way the staleness gate is scoped.** A diff that
   touches `generators/` but changes no module inside any asset's input hash
   cannot stale a mesh — and since T-1654 that set is exactly
   `code_inputs.geometry_modules()` plus `emit.py`. #104's three files are all
   outside it: two are `NO_GEOMETRY` members and one is `code_inputs.py` itself.
   The register that decides freshness could decide the bake.
3. **Accept the handoff and make it cheap.** If a 30-minute bake is simply longer
   than a run, then a generators PR's endgame is `resume` by design and the rule
   should say so, rather than each run spending 18 minutes of its budget
   discovering it. Two wasted laps per generators PR is the current price.

**Acceptance:** a green, foreground-gated PR that touches `generators/` merges
inside its own run, OR the rule in `.github/steward/improve.md` and this repo's
PIPELINE.md says plainly that it cannot and tells a run to hand it on without
spending two laps first. Either way the reason is written down, and
`test-gh-rest.sh` or the bake workflow's own self-test covers whichever of the
two was chosen.
