---
id: T-3070
title: The PR and dev gate (Chicago 4D — gate) dies with 'The runner has received a shutdown signal' (exit 143) about 6 minutes into check.sh, right after publish, on every run since about 12:15Z on 2026-10-23: dev's own run 39953163716, T-3046's 39951182314 and T-3019's 39951882275 (both attempts) all stop at the same line, so no PR can merge; find what kills the runner there (memory or disk after the ~640 MB of scene packs, or a step that grew) and bring the gate back to a verdict
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-23
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

The PR and dev gate (Chicago 4D — gate) dies with 'The runner has received a shutdown signal' (exit 143) about 6 minutes into check.sh, right after publish, on every run since about 12:15Z on 2026-10-23: dev's own run 39953163716, T-3046's 39951182314 and T-3019's 39951882275 (both attempts) all stop at the same line, so no PR can merge; find what kills the runner there (memory or disk after the ~640 MB of scene packs, or a step that grew) and bring the gate back to a verdict.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
