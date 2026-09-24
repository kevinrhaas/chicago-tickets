---
id: T-1543
title: Spend the Fergus annotation of Silas W Sherman's 1834 and 1836 sheriff elections onto the dated office T-1299 put on his card
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

Spend the Fergus annotation of Silas W Sherman's 1834 and 1836 sheriff elections onto the dated office T-1299 put on his card.

`data/research/spend_rulings.json` hands this unit off under
`handed_to_the_dated_role_pass`, and that rule named T-1299 until T-1299 landed as
#26. T-1299 did its own job — Sherman's card now carries a dated `sheriff` office,
`kind: office`, 1833-12-03 to 1835-07-15, `covers_scene_date: true`, and the 1835
occupation field that used to read `none_recorded` reads `sheriff` off it. What it
did NOT do is spend the book unit: that role is sourced to
`chicago_democrat_1833_1835` under claim `person_silas_w_sherman`, and nothing in
the repository cites `bk_fer2_042` at all.

The book says something the press run does not. Fergus's bracketed later annotation
in the 1843 name directory prints Sherman ELECTED sheriff of Cook County in 1834 and
again in 1836 — two election dates bracketing the scene year, where the press gives a
bound of mentions. The OCR prints the second year as `1S3G`; the claim already
normalizes it to 1836 and that reading is not reopened here.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. `bk_fer2_042` is cited by the record that carries Sherman's sheriff office, as
   corroboration and dating of an office the press already established — NOT as the
   thing that puts him in the 1835 town, which under the ladder ratified 2026-09-03
   an 1843 directory annotation cannot do on its own.
2. The 1834 and 1836 election dates are written as the book's, against the book, and
   are not flattened into the role's `from`/`to` — the press bound is the press
   bound and an election is not a term of service.
3. `handed_to_the_dated_role_pass` stops being a handoff for this unit: the ruling
   either resolves it or the rule is retired with its last unit.
4. `python3 tools/measure_research_spend.py --check` goes green without the rule
   naming an open ticket, and the closing audit and the sign-off re-derive.
