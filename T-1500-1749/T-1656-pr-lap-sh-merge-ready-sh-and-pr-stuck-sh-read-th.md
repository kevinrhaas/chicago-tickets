---
id: T-1656
title: pr-lap.sh, merge-ready.sh and pr-stuck.sh read the repository from $GITHUB_REPOSITORY too, so any pass driven from a clone inside another repo's job acts on that repo
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
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

pr-lap.sh, merge-ready.sh and pr-stuck.sh read the repository from $GITHUB_REPOSITORY too, so any pass driven from a clone inside another repo's job acts on that repo.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
