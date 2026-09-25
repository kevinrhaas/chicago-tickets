---
id: T-1555
title: employment_coverage_1835.py writes but measured as a non-writer, so rederive never runs it
state: review
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: 38
claimed_by: run 9/25/2026, 9:42:25 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36149056077
claimed_at: 2026-09-25T14:42:25.135Z
decision: null
decision_answer: null
---

employment_coverage_1835.py writes but measured as a non-writer, so rederive never runs it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was found (T-1525, 2026-09-25)

`tools/step_isolation.json` records `tools/employment_coverage_1835.py` as
`{"wrote": []}`, so `tools/audit_manifest_coverage.mjs` does not require it in
`tools/derived_manifest.json`, so `rederive.mjs --run` never runs it — it is not
one of the 157 steps. But it DOES write
`data/residents/employment_coverage.json`, and check.sh asserts that file
re-derives. Any change to the resident layer leaves it stale with no automated
remedy.

THE MEASUREMENT IS THE BUG, NOT THE TOOL. The write-set was taken by running the
build on a clean tree, where the output was already current — so `--build` was a
no-op and the tool looked like a non-writer. A tool that rewrites only when its
inputs have moved is invisible to that measurement. Any other gated writer with
the same shape is in the same hole, and the audit should be asked for the list.

Hand-fixed twice in one session on this branch, which is the cost the manifest's
own preamble was written to stop: "if you add a writer it should be in that
manifest, right?"

Before listing it, `_must_reproduce` applies: run the build on a clean tree and
confirm it changes no committed byte.
