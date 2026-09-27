---
id: T-1654
title: generators/build.py is hashed WHOLE into every asset's inputs, so changing its argparse or its docstring stales all 422 assets and demands a full-town rebake
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

generators/build.py is hashed WHOLE into every asset's inputs, so changing its argparse or its docstring stales all 422 assets and demands a full-town rebake.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
