---
id: T-1606
title: The two research reports embed live ticket state from a separate repository, so a sibling run claiming a ticket turns every code branch's gate red on a diff that cannot touch it
state: open
epic: META
requested_by: loop
seen: false
effort: M
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

The two research reports embed live ticket state from a separate repository, so a sibling run claiming a ticket turns every code branch's gate red on a diff that cannot touch it.

`tools/report_research_closing_audit.py` and `tools/report_research_signoff.py` write
`docs/RESEARCH/research-closing-audit-2026-09.md` and `research-signoff-2026-09.md`, and both
tables carry a `state` column read LIVE out of kevinrhaas/chicago-tickets — a separate
repository no code branch controls and every sibling run writes to directly.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured 2026-09-26 on T-1579's PR (#61).** The branch gated green at 633 steps, merged
`origin/dev`, and went red on two steps it had not touched:

    FAIL docs/RESEARCH/research-closing-audit-2026-09.md is stale — run tools/report_research_closing_audit.py --build
    FAIL docs/RESEARCH/research-signoff-2026-09.md is stale — run tools/report_research_signoff.py --build

The whole of the staleness was one cell in each file: `| T-1600 | 10 | open | yes |` had
become `| T-1600 | 10 | claimed | yes |`, because a sibling slice claimed T-1600 while this
run was in its smoke. Nothing in the diff could cause it and nothing in the diff could
prevent it. Rebuilding both cost a lap and re-gate, and the rebuilt line will go stale again
the moment T-1600 moves — so the fix landed in a PR carrying a value that was already
expiring.

**This is T-1593's fault one step downstream.** T-1593 established the rule: a fault in the
separate list of jobs is not charged to the work under review, because nothing the work could
do would help. The same reasoning applies here and has not been applied — these two reports
COPY the list of jobs into the tree, so the copy goes stale for reasons no branch owns, and
the gate charges it to whoever is holding the branch when it happens. With N slices running
at all times the expected number of laps paid for this is not small.

**Acceptance:**

1. A ticket state moving in kevinrhaas/chicago-tickets does not, on its own, turn any code
   branch's gate red. Demonstrated the way T-1593 demonstrated its own: against the exact
   state that failed on #61.
2. Whatever the reports say about an unresolved unit's ticket is still TRUE when read — the
   answer is not to print a stale value and stop checking it. Either the state stops being
   copied into the report (the report names the ticket and the reader looks it up), or the
   column is re-derived and compared by the tickets repo's own check rather than by a code
   branch's, or the staleness of that column alone is reported rather than failed. Say which
   and why.
3. The two reports' other assertions — the ones that read the ledger and the four layers, and
   that hold the sign-off's GO to the tree — keep their present strictness. This must narrow
   what is charged to a code diff, never what is checked.
4. `tools/report_research_signoff.py --self-test` and the closing audit's self-test both still
   pass, with a case for the new behaviour among them.

Found by T-1579, whose PR paid the lap.
