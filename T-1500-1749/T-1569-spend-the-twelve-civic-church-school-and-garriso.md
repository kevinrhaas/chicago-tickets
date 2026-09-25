---
id: T-1569
title: Spend the twelve civic, church, school and garrison post enrichments T-1301 routed to T-1188 and then T-1189: the county offices, trusteeships, ministries, schools kept and the fort clerkship written onto the held cards by the fields that now exist
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

T-1301 read the completed resident passes one finding at a time and handed each to the OPEN
ticket whose acceptance owned the kind of fact it named. Twelve of them name a CIVIC, CHURCH,
SCHOOL or GARRISON POST — a county office, a town trusteeship, a coronership, a ministry, a
church membership, a school kept, an assistant's post, an officer's clerkship — on a card this
town already holds, and no exact source-bearing structured field on that card carries it.

They were routed to T-1188, which raised those establishments; T-1188 split into T-1410 and
T-1411, T-1411 into T-1421 and T-1422, and all four closed, so on 2026-09-20 the pointer moved
to T-1189 — the ticket that put real persons into them. **T-1189's chain is now spent too**:
T-1432 and T-1433 are done, T-1434 split to T-1448 (done, #40, 2026-09-25) and T-1449, whose
own pieces T-1461 and T-1462 are done. A unit cannot defer to finished work, so the twelve
were stranded and `check.sh` on dev went red on them (T-1567, T-1568). T-1569 is where they
land, and it is a SPEND and not a routing: the staffing join built the fields these findings
want — `persons[].employment` (T-1461) and the businesses' `staff[]` (T-1432, T-1462) — so
what is left is the walk the three closed children never did, the resident layer's own
enrichments against the establishments they raised.

This is the same shape as T-1315 (the three dated birth and age enrichments) and T-1335 (the
kin), and it sits beside them on purpose.

THE TWELVE, with what T-1301 read and the source it rests on:

| person | the post | source_id |
|---|---|---|
| hamilton_richard_j | county clerk and recorder from 1831, later probate judge, treasurer, school commissioner | goodman_history_cook_county_hamilton |
| hogan_john_s_c | Chicago corporate trustee named in the 1835 incorporation act | pal_chicago_incorporation_1835 |
| snow_george_w | elected assessor and surveyor, December 1833 | chm_george_snow_assessor |
| fullerton_alexander | the 1835 town-clerk chronology | goodman_history_cook_county_early |
| meeker_joseph | First Presbyterian membership 1833-09-08, Sunday-school librarian 1835-03-16 | first_presbyterian_chicago_1833_1913 |
| sproat_grenville | an English and Classical School opened in the fall of 1833 | goodman_history_cook_county_early |
| st_cyr_john_mary | 1833 appointment to Chicago, the first Mass, the first church | catholic_chicago_st_cyr_1833 |
| steele_ashbel | county coroner in the 1835 period | goodman_history_cook_county_early |
| watkins_john | a school taught in Chicago in 1835 | goodman_history_cook_county_early |
| myers_frederick | quartermaster's clerkship at Fort Dearborn, 1831-33 | resident_research_myers_glen_ellyn |
| barrows_mary | an assistant's post in Miss Chappel's school | early_illinois_barrows_school |
| lathrop_samuel_s | First Baptist membership from October 1833 | rr_baptist_chicago_lathrop |

Six of the twelve are posts held BEFORE the scene date or spanning it, and three name offices
the source dates to 1835 itself; the window rule decides each one and some will end refused
rather than written. A refusal is a spend.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Each of the twelve is either WRITTEN onto its held card — as `persons[].employment` at the
  establishment the register carries, or as the field the fact actually is (a membership is
  not an employment) — or REFUSED in writing, by rule and evidence, with the units named by
  `person_id`. No confidence is upgraded to make one writable and no citation is invented.
- Where the post's establishment is in the business register, the card's employment and that
  business's `staff[]` agree; where it is not, the unit says so rather than raising a house.
- The rulings file re-derives: `python3 tools/spend_remainder_rulings.py --check` green, and
  `python3 tools/measure_research_spend.py --check` green with these twelve no longer
  `unresolved`.
- `./tools/check.sh` green on the branch.
