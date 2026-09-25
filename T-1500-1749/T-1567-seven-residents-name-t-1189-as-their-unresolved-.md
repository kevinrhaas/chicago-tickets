---
id: T-1567
title: Seven residents name T-1189 as their unresolved ticket and it was SPLIT five days ago, so the research-spend ledger cannot build on dev at all
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: null
claimed_by: run 9/25/2026, 12:03:40 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36164480807
claimed_at: 2026-09-25T17:03:40.795Z
decision: null
decision_answer: null
---

MEASURED 2026-09-25 on plain `origin/dev` (a49570d7), with no branch in it:

    python3 tools/measure_research_spend.py --ledger-build   -> exit 1
      FAIL: residents:data/research/residents/pass_04_75_cohort.json#people/sproat_grenville:
            unresolved ticket 'T-1189' is missing or not open
      ...and six more: st_cyr_john_mary, steele_ashbel, watkins_john (pass 04),
      myers_frederick (pass 09), barrows_mary (pass 10), lathrop_samuel_s (pass 11)

T-1189 was SPLIT on 2026-09-20 into T-1432, T-1433 and T-1434, and is `state: split,
closed: 2026-09-20`. Seven resident records still point at it. `research_spend_ledger.py`
requires an unresolved ticket to be OPEN — which is the right rule; a person waiting on a
ticket nobody can claim is waiting on nothing — so the ledger refuses to build.

**This is step 149 of 158 of the derived manifest, so it is not a local nuisance: nothing
can re-derive the derived layer on dev, and the PR lap's rebuild fails on every PR that
reaches it.** Found by T-1521's run, which had to merge dev in and could not finish its
own rebuild; the gate itself is green, because `check.sh` runs
`measure_research_spend.py --check --quiet` rather than `--ledger-build`.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Each of the seven names the piece of T-1189 that actually owns its question — T-1432
  (workplaces across household records), T-1433 (employment on reconstructed persons) or
  T-1434 — chosen per person and argued, not dealt uniformly. If a person's question
  belongs to none of the three, say which ticket it does belong to, or file one.
- `python3 tools/measure_research_spend.py --ledger-build` exits 0 on dev.
- A gate step catches the next one: `split` is not a rare event, and `--check --quiet`
  passed this by. Either the gate runs `--ledger-build`, or `ticket.mjs split` refuses to
  leave a record pointing at the ticket it just closed, or both — argue which.
