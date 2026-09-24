---
id: T-1524
title: A row carrying a printing's controlled word and a row carrying the same printing without one are two rows on the card: rule on derive_resident_roles._key
state: blocked-tech
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-23
closed: null
pr: null
claimed_by: run 9/23/2026, 11:58:23 PM CT
blocked_on: T-1515 must land first. On dev, derive_resident_roles reads only the 1839 REGISTER crosswalk (REGISTER_1839 / fergus_1839_register_crosswalk_1835.json); the 1839 DIRECTORY crosswalk is not read by directory_roles at all, so William Jones carries ONE 1839 row (role: null, no claim) and there is no pair to fold. The pair this ticket rules on comes into existence only when T-1515 puts Fergus 1839 on directory_roles()'s footing. Unblock when T-1515 merges.
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35957629711
claimed_at: 2026-09-24T04:58:23.025Z
decision: null
decision_answer: null
---

Found by T-1515 while putting the Fergus 1839 directory on the same footing as its
three siblings.

`derive_resident_roles._key` says "two rows are the SAME assertion when one source
dates one role to one bound", and it keys on the controlled word where there is one
and on `as_printed` where there is not. So one volume, one wording, one year can
produce TWO rows on a card when one of the pair has been folded onto a controlled
word and the other has not.

William Jones is the live case. Fergus 1839 prints him `justice of the peace`. The
crosswalk row carries `role: justice_of_the_peace, claim: f1839_e0814`; the
`later_occupation` pointer row carries `role: null` with the same wording, the same
volume and the same year and no claim. Both stand on his card.

WHY IT WAS NOT FIXED IN T-1515. That ticket's acceptance forbade any card LOSING a
role row, and folding the pair is exactly that. It is also the only thing keeping
T-1299's narrow clause in `crosswalk_fergus_1839.py` alive: with the pair folded, the
clause is inert for all seven people it keeps, and can go.

**Acceptance:**

- A ruling, written down, on whether a row with a printing's controlled word and a row
  with the same printing and no controlled word, from one source over one bound, are
  one assertion or two.
- If one: `_key` folds them, the survivor is the row that names its `claim`, and the
  count of rows each affected card loses is stated in the PR body.
- If two: `_key`'s docstring says why, and the card is readable with the pair on it.
- T-1299's narrow clause in `crosswalk_fergus_1839.py` is re-decided in the same
  commit, since it was kept only because this pair does not fold.
- `tools/check.sh` green.
