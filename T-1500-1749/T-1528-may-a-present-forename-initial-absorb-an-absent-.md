---
id: T-1528
title: May a present forename initial absorb an ABSENT one at the same entry of the same list — the two the unread-initial ruling held over
state: open
epic: PAPERS
requested_by: loop
seen: false
effort: XS
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

May a present forename initial absorb an ABSENT one at the same entry of the same list — the two the unread-initial ruling held over.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

The owner ruled on T-0392, 2026-09-21: a merge MAY be declared where one side's forename
initial is `[?]` — unread — and the other's is read, at the same entry of the same list, with
no competing letter, and it must carry its own undo. Seventeen refusals became merges under it.

**TWO DID NOT, and they are the same shape as each other.** An ABSENT initial is not an unread
one: nothing on the page says a letter stood there, so there is no position to agree about.

- `Samuel E. Toby` / `Samuel. Toby`, three printings of the 1 July 1834 letter list. The second
  sets NO middle initial where the first reads E.
- `J. W. Smith` / `[?]. Smith`, the same list. 'J. W. Smith' reads two initials; '[?]. Smith'
  sets ONE slot and cannot read it, so the second slot is absent rather than unread. This one
  had been filed under `unread_initial` and is reclassified `absent_initial` by T-0392's
  execution. Its alignment is also the weakest of the eighteen: '[?]. Smith' is read `[?]` by
  BOTH the 1834-07-09 and 1834-07-16 printings, at entry 205 of each, and the only reading of
  'J. W. Smith' is the 1834-07-02 segmentation's entry 146 — a segmentation holding 228
  entities against the others' 324 and 321, so the ordinal aligns with nothing.

Both refuse today and both are carried as duplicate persons. The ticket's own two cases from
the 1 April 1834 return — `[uncertain: — Duncklo]` and `[uncertain: — Denny]`, whose FORENAME is
missing entirely and which the 1834-04-16 printing sets as Hezekiah and William — are the same
question a third way, and T-0392 recorded them and did not answer them either.

**THE QUESTION IS THE OWNER'S** for the reason T-0392's was: it changes what a declared
identity is. T-0392's own reasoning does not carry over by itself. Its ground was that *the two
readings are of one line* and the unread side supplies no competing letter; here one side
supplies no SLOT, and the merge would have to assert that a printing which set 'Samuel. Toby'
had an E it did not print. That may be the right reading of a compositor dropping a letter, and
it is not the same sentence.

- **No**: two accepted duplicates on the July list, plus two on the April one, documented in
  `data/research/newspapers/README.md` as a known cost, and this ticket is withdrawn with the
  ruling recorded on it.
- **Yes, bounded the same way**: same list, same entry, the absent side supplying no competing
  letter, with the same `unread_initial`-style undo record saying the agreement is positional.

**Acceptance:** the owner rules; the ruling is written into `identity.json`'s note and into
`data/research/newspapers/README.md`, not only into a PR body; and whichever branch it takes is
carried out. Filed by T-0392's execution, which is where the eighteenth case was found.
