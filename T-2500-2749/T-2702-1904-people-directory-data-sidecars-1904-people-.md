---
id: T-2702
title: 1904 people directory: data/sidecars/1904/people.json compiled by the 1835 generator from 1904 household records, starting with the attested Glessner household, and the Glessner summary record's residents filled
state: done
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: 2026-10-16
pr: 930
claimed_by: run 10/16/2026, 7:44:27 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T02:32:53Z
claimed_run: null
claimed_at: 2026-10-17T00:44:27.946Z
decision: null
decision_answer: null
---

1904 people directory: data/sidecars/1904/people.json compiled by the 1835 generator from 1904 household records, starting with the attested Glessner household, and the Glessner summary record's residents filled.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 179 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner ruling 2026-10-17, given in the coordinating session: file it in band 3, as its own ticket. It is a separate parcel from T-2637 (1904 household records, a compile path, the T-1740 People-section rule), and T-2638's Inspect front page needs it for Who lives here.

Filed from T-2637's finding (PR #922). **Owner ruling, 2026-10-17, given in the coordinating session: "File it in band 3"**, as its own ticket, between the Glessner pilot (T-2637) and the Inspect front page (T-2638) that will show its Who lives here.

## Depends on

- T-2637 (PR #922): the Glessner summary record whose `residents` this fills.

## What to build

- `data/sidecars/1904/people.json`, compiled by the same generator as 1835 (`tools/compile_scene.py` `compile_people`), from 1904 household records kept apart from the 1835 town's `data/residents/`. Today the directory is compiled only for a scene that lists the `residents` layer, and only from the 1835 manifest. T-1739 made that rule because 1904 once carried 3,308 people of 1835.
- Start with the attested Glessner household at 1800 S. Prairie Avenue: John J. and Frances M. Glessner in 1904, per the HABS data pages and the museum's family page. The grown children had married and moved out by 1904. Staff or others go in only where a source names them; nothing is invented.
- Fill `residents` in `data/summaries/glessner_house.json`, and gate it with `compile_summaries.py`.
- **T-1740's smoke rule** ("the 1904 drawer offers no People section"): read why it exists and decide one of two things, saying which in the PR. Either the rule is updated, with its reason, because 1904 now has an honest directory; or the directory is built and the drawer's People section stays off until the Navigator's People app.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] `data/sidecars/1904/people.json` is written by `compile_scene.py`, and its `--check` holds it like every sidecar. 1835's `people.json` is byte-identical.
- [ ] Every 1904 person is graded, every attested one cites a source that resolves, and no one is placed in the house without a source. The children and staff are absent unless a source puts them there.
- [ ] The Glessner summary record names its residents from the 1904 directory and passes `compile_summaries.py --check`.
- [ ] The T-1740 rule is either updated with its reason, or kept true with the directory built. The smoke stays truthful, and the PR says which.
- [ ] `./tools/check.sh` passes, and the smoke parts the diff touches pass, or are named for a runner.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
