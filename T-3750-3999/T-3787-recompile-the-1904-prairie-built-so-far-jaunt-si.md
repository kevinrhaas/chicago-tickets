---
id: T-3787
title: Recompile the 1904 prairie-built-so-far jaunt sidecar: dev's gate part 5/8 red since #2379 (stale jaunts)
state: open
epic: META
requested_by: steward
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
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

Recompile the 1904 prairie-built-so-far jaunt sidecar: dev's gate part 5/8 red since #2379 (stale jaunts).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red: compile_jaunts --check fails on data/sidecars/1904/jaunts/prairie-built-so-far.json since 6e252e9955 (#2379 changed data/jaunts/prairie-built-so-far.json without recompiling); fix is python3 tools/compile_jaunts.py, one file

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
