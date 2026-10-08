---
id: T-2189
title: Five people the town's own burial entries and death notices bury before 1 July 1835 are ruled present on the scene date: W. Brannen (St Cyr burial 2, 1834-07), John Hogan (burial 3, 1834-10), William Bourque (burial 4, 1835-06), Charles Rollins (Democrat 1834-09-17, died aged 2, heading a modelled household of six) and Sarah Hoit (Democrat 1834-09-24) — rule them not present and withdraw what was modelled around them
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: run 10/8/2026, 3:22:07 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37838503447
claimed_at: 2026-10-08T20:22:07.590Z
decision: null
decision_answer: null
---

Five people the town's own burial entries and death notices bury before 1 July 1835 are ruled present on the scene date: W. Brannen (St Cyr burial 2, 1834-07), John Hogan (burial 3, 1834-10), William Bourque (burial 4, 1835-06), Charles Rollins (Democrat 1834-09-17, died aged 2, heading a modelled household of six) and Sarah Hoit (Democrat 1834-09-24) — rule them not present and withdraw what was modelled around them.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 147 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1335's family pass found it: each card claims the burial or death notice as its own evidence, and 1835_presence_rulings.json still rules all five present at the reconstructed tier; a death is the one departure no later source can undo, and no open ticket owns presence by death

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Two more, found while T-1335 ruled the burials (2026-10-08)

The readmission stage (`data/reconstruction/1835_readmissions.json` `minted[]`) mints two
more cards off St Cyr's burial entries and prices their presence off the BURIAL'S OWN DATE
as `dated_evidence`: `hh_one_of_daughters_of_m_colewell` (burial 1, 1834-06) and
`hh_william_bourque_burke` (burial 4, 1835-06). A burial is a departure, not a sighting;
the persistence model cannot read it as evidence of presence. Same fix, and the class is
worth a gate: no card whose dated evidence is its own burial or death notice is present.
