---
id: T-1568
title: Twelve resident cohort units still name T-1189 unresolved, and its last live leaf closed with #40: the dev gate is red for every run
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: null
claimed_by: null
blocked_on: Duplicate of T-1567 (claimed 2026-09-25 17:03Z), which names the same fault — the twelve resident cohort units still pointing at the split T-1189 after #40 closed its last live leaf. Withdrawn so two runs do not repair dev's gate in parallel.
needs_bake: false
closed_at: 2026-09-25T17:38:35.662Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

`./tools/check.sh` on `dev` is RED, and it is red for every run that gates on it.
Four steps, one cause:

    * research stays inside its historical ratchet and closed unit ledger
    * the closing research audit still re-derives from the ledger and the four layers
    * the research sign-off re-derives, and its GO still follows from the tree
    * ...and each of its rules still fires, and hands on only to live work

    FAIL: residents:data/research/residents/pass_02_75_cohort.json#people/hamilton_richard_j:
          unresolved ticket 'T-1189' is missing or not open

Twelve of them, across pass_02, pass_03, pass_04 (five), pass_09, pass_10 and
pass_11 of the 75-person cohorts: hamilton_richard_j, hogan_john_s_c,
snow_george_w, fullerton_alexander, meeker_joseph, sproat_grenville,
st_cyr_john_mary, steele_ashbel, watkins_john, myers_frederick, barrows_mary,
lathrop_samuel_s.

WHAT CHANGED, AND IT WAS NOT THE DATA. T-1189 has been `split` since 2026-09-20.
Its chain was lifted by one live leaf the whole time: T-1189 -> T-1434 -> T-1448.
T-1448 merged as #40 at 16:13Z on 2026-09-25 and settled to `done`, so the chain
now reads spent, and the ledger's own rule — a live leaf lifts every split above
it — stops holding these twelve up. Nothing in the tree moved; a ticket closed.

MEASURED. The four steps fail identically on a pristine `git worktree` of
`origin/dev` with no branch work in it, and GitHub's `chicago-4d-check` on `dev`
went `success` (a5078492, 15:39Z) -> `failure` (a49570d7, 16:13Z) across exactly
that merge. It is not a branch's fault and no branch can gate green until it is
fixed: PR #42 (T-1565) is parked on `hold` for this and nothing else.

This is the rule T-1530 had just established from the other side — an unsettled
step of a programme must name a ticket a run can claim — arriving as a red
instead of as a refusal, because the naming lives in twelve data records rather
than in the queue.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Each of the twelve unresolved clauses names a ticket that is actually open, or
  states its evidence clause instead, by whatever the ledger's rule allows. The
  reading itself is not touched and no confidence moves.
- Which live ticket inherits T-1189's staffing-join question is stated in writing,
  not implied by an edit.
- `python3 tools/measure_research_spend.py --check` is green, and the two derived
  reports (`report_research_closing_audit.py --build`,
  `report_research_signoff.py`) are rebuilt in the same commit so all four steps
  go green together.
- `./tools/check.sh` green on the branch.

**Note on ordering:** filed under T-1566 because that is where the staffing mint's
own follow-on sits. It blocks every other run's gate, so the owner may well want
it higher; the queue is his to order.
