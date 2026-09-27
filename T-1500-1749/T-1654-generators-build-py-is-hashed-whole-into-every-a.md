---
id: T-1654
title: generators/build.py is hashed WHOLE into every asset's inputs, so changing its argparse or its docstring stales all 422 assets and demands a full-town rebake
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-09-27
pr: 112
claimed_by: run 9/27/2026, 2:50:14 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-27T09:06:50Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36302744474
claimed_at: 2026-09-27T07:50:14.122Z
decision: null
decision_answer: null
---

generators/build.py is hashed WHOLE into every asset's inputs, so changing its argparse or its docstring stales all 422 assets and demands a full-town rebake.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured on 2026-09-27**, on `steward/t1652-bake-only-list` (PR for T-1652):

* `generators/mesh_inputs.py::_code_shas` hashes `[build.py, archetypes/<arch>.py]
  + code_inputs.geometry_modules()`. `build.py` goes in WHOLE — all ~420 lines,
  including its module docstring, its `argparse` block and its result summary.
* T-1652 is a fix to `--only`'s argument handling. It changes nothing between
  `to_params()` and `export_glb()`. It staled **422 of 422** assets.
* Proven not to be real staleness, two ways. (1) On `origin/dev` the recorded and
  recomputed hashes for `beaubien_barn__converted_1817` are the same
  (`a9a8703a9c80…`); with only the T-1652 build.py in place it recomputes
  `08ead3786dbf…`, and the only moved term is `build.py` itself
  (`23b6ee4ec1da…` → `15f137ce5f17…`). (2) Rebaked `beaubien_barn`,
  `brickyard_north_side` and `blacksmith_shop_state_st` with the new build.py at
  default flags: all three GLBs are **byte-identical** to the committed ones
  (66,332 / 90,372 / 31,168 bytes, `cmp` clean).
* So `tools/validate.py --stale` is red on a PR whose meshes are provably the
  meshes already committed, and the only route the gate offers is a full-town
  rebake: ~20 min of Blender, ~18 min of `web_derivatives.sh`, and 422 GLBs whose
  bytes all move because Cycles is not bit-reproducible — a diff in which the
  reader cannot tell a real content change from a re-roll.

**This is T-0164's finding, one directory up.** That ticket stopped
`generators/common/` being globbed into the recipe, because "a hash that cries
stale for reasons that cannot change the geometry gets disbelieved, and a
disbelieved gate is worse than no gate" — measured there at 349 of 349 assets for
one comment line. A whole module is no more a statement about geometry than a
directory listing is. `tools/measure_generator_half.py` already says the cost out
loud ("a new archetype edits build.py's registry and costs the town"), so the
figure is known and unaddressed rather than unknown.

**Acceptance:** a change to build.py that cannot move a vertex does not stale a
committed mesh, and one that can still does. Whatever the route, it is a change
to what an input hash MEANS, so it bumps `mesh_inputs.SCHEME` and re-stamps
through `tools/restamp_inputs.py --reason …` (whose guard is exactly a scheme
bump, and which therefore permits this and not a blessing of real staleness),
with a byte-identity measurement over a sample recorded in the PR. Candidate
routes, to be chosen in the ticket rather than assumed here:

1. Split build.py's geometry pipeline out of its CLI and hash only the former —
   the direct analogue of what T-0164 did to `common/`.
2. Keep one file and hash a declared REGION of it (the archetype registry and the
   export path), with a gate that refuses geometry code outside the region — cheap
   to write, easy to get subtly wrong.

**It blocks T-1652**, whose fix is complete, gated and proven on that branch and
which cannot go green until a build.py edit stops costing a full-town rebake. Do
not land T-1652 by rebaking the town: that pays the exact cost this ticket exists
to remove.
