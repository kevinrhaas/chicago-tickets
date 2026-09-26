---
id: T-1607
title: The anchor the paper prints for the Exchange Coffee House is 'the Exchange', and whole-set anchor matching resolves it to no building in the town
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: 66
claimed_by: run 9/26/2026, 1:17:36 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36222265041
claimed_at: 2026-09-26T06:17:36.504Z
decision: null
decision_answer: null
---

The anchor the paper prints for the Exchange Coffee House is 'the Exchange', and whole-set anchor matching resolves it to no building in the town.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Found while ruling T-1604. Russell E. Heacock's advertisement
(`chicago_democrat_1835_07_08#c012`) anchors his office on **"the Exchange"** — the
paper's own words; "the Exchange Coffee House" is a reader's expansion. The register
resolves an anchor against the committed town by WHOLE-SET equality of identity-bearing
words (T-0406, on the Tremont), so `{exchange}` is not equal to
`exchange_coffee_house`'s `{exchange, coffee, house}`, nor to either aka —
`{markle, exchange, coffee, house}`, `{illinois, exchange}` — and the anchor resolves to
no building. The 1834 Board of Trustees minutes name a venue as "the Exchange" too
(quoted in `data/structures/mansion_house.json`), so this is not a one-off printing.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
Either `"the Exchange"` is added to that record's `aka` and the register is re-derived so
the anchor resolves, with the report showing the before/after count and nothing else moved
onto or off this building; or the anchor is deliberately left unresolved with the reason
written on the record — that "the Exchange" is too thin a set to resolve safely, naming
what else in the town it could reach. Ruling either way must say what happens to the 1834
trustees' venue mentions. T-1604 did not decide it: the position ruling stands without it.
