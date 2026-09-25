---
id: T-1594
title: A step label in check.sh carries backticks inside double quotes, so every gate run prints a bash syntax error to stderr and the label loses the word it quoted
state: open
epic: META
requested_by: loop
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-09-25
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

A step label in check.sh carries backticks inside double quotes, so every gate run prints a bash syntax error to stderr and the label loses the word it quoted.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
