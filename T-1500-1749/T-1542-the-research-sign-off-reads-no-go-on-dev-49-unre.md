---
id: T-1542
title: The research sign-off reads NO-GO on dev: 49 unresolved reading units defer to T-1514, which closed, so C3 fails and both research reports are stale — re-point the units at live work or state what would reopen them
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-24
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

The research sign-off reads NO-GO on dev: 49 unresolved reading units defer to T-1514, which closed, so C3 fails and both research reports are stale — re-point the units at live work or state what would reopen them.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Found by T-1540's gate run on 2026-09-24. `tools/report_research_signoff.py --check` and
`tools/report_research_closing_audit.py --check` are BOTH red on pristine origin/dev —
verified in a clean worktree of origin/dev with no other change in the tree — and
rebuilding them flips the verdict:

    ### GO for reconstruction   ->   ### NO-GO for reconstruction
    C3 — Every unresolved unit defers to a ticket that is still live … yes -> NO
    | T-1514 | 49 | open | yes |      ->   | T-1514 | 49 | done | **NO** |
    **0** units defer to work that is no longer live   ->   **49**

So the 49 units are not wrong and C3 is not wrong: T-1514 closed and the units it
carried were not re-pointed. The report is doing exactly what it was built to do —
"If a condition later breaks, `tools/check.sh` goes red on this report and the next run
must re-derive the signature."

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. Each of the 49 units is re-pointed at work that is live, or states the evidence that
   would reopen it — never re-pointed at a ticket chosen to make C3 green.
2. Both reports are rebuilt in the same commit, and the sign-off reads its own verdict
   from the tree rather than from a restated one.
3. If the verdict is still NO-GO after the units are honestly settled, it SHIPS as
   NO-GO with the reason — a sign-off that cannot be revoked is not a measurement.
4. Why closing T-1514 did not re-point them is stated, so the next ticket that carries
   unresolved units does not close the same way.
