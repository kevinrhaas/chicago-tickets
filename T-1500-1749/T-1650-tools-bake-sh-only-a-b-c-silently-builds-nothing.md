---
id: T-1650
title: tools/bake.sh --only a,b,c silently builds nothing: build.py compares the id by equality, so the comma form its own usage documents reports 0 assets built and exits 1
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: Duplicate of T-1652 (done, #104); generators/common/selection.py says so (\"filed twice — T-1650 is the same finding\")."
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

tools/bake.sh --only a,b,c silently builds nothing: build.py compares the id by equality, so the comma form its own usage documents reports 0 assets built and exits 1.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** Duplicate of T-1652 (done, #104); generators/common/selection.py says so ("filed twice — T-1650 is the same finding").
