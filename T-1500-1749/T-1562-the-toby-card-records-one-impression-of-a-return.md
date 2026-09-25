---
id: T-1562
title: The Toby card records one impression of a return the T-1528 merge showed was printed three times: decide whether letter_list_returns and the presence leg follow the merged record's own first and last printings, or stay on the impression this pass reached
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: 37
claimed_by: run 9/25/2026, 8:50:41 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T15:06:14Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36143304814
claimed_at: 2026-09-25T13:50:41.841Z
decision: null
decision_answer: null
---

The Toby card records one impression of a return the T-1528 merge showed was printed three times: decide whether letter_list_returns and the presence leg follow the merged record's own first and last printings, or stay on the impression this pass reached.

**Acceptance:** (stated 2026-09-25, before working)

**The decision, and it is NEITHER of the two the title offers.** The three printings
the T-1528 merge gathered — 1834-07-02, 1834-07-09, 1834-07-16 — are three impressions
of ONE return, the office's list of what was still uncalled-for at Chicago on 1 July
1834. `letter_list_returns` is one date PER RETURN and not per printing
(`return_dates()` in tools/mint_letter_list_residents.py: "A return is dated by the
first of its printings that carries a readable issue date"), so the card takes ONE
date, and it is `1834-07-02`.

- NOT the merged record's first AND last printings. Two dates in that list assert two
  returns, which is false here and is read as such: the mint's own note branches on
  `len(groups) > 1` to say "HELD THERE MORE THAN ONCE … which is the strongest thing a
  letter list can say about residence", and `RANKED_FIRST_RETURNS` ranks a name held in
  two returns ahead of one held in a single return. A reprint run must never buy that.
- NOT the 1834-07-09 impression this pass reached. It is neither the first printing nor
  the last; it is the issue one extraction crop happened to catch, which is the exact
  defect T-0425 exists to prevent and which cost `hh_conger_thomas` nine weeks.

Done means:

1. `hh_toby_samuel.json` carries `letter_list_returns: ["1834-07-02"]` — the value the
   mint's own `return_dates()` derives from the merged gazetteer record, DEMONSTRATED
   from the tool rather than asserted in prose.
2. The presence leg is re-derived by `tools/derive_presence_evidence_leg.py --write`,
   `--check` re-derives it clean, and it reads `1834-07-02` (364 days short of the
   scene date) with its note naming the field it came from.
3. `arrival.value` stays `1834-07-01`: the bound belongs to the return, the earliest
   printing moved, and `bound_for('1834-07-02')` still returns it. The mint's T-0425
   arrival gate passes on the new earliest return.
4. Every date sentence on the card that named 1834-07-09 as THE reading now names the
   return and its three printings, in the generator's own words — the arrival note, the
   person note, the presence note.
5. `./tools/check.sh` green, the `--for-diff` smoke legs green, a changelog entry.

Out of scope, and deliberately: the card's DISPLAY NAME. That is T-1561, claimed by
another run; this ticket touches no `name` field.
