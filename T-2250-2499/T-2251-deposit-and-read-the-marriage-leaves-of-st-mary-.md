---
id: T-2251
title: Deposit and read the marriage leaves of St Mary's register — the book Father Rouges bound in 1880 with the baptisms already deposited — for the forename of the 1834 witness every printing sets as 'L. Franchere'
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: pending
decision_answer: null
---
Deposit and read the marriage leaves of St Mary's register for the forename of the 1834 witness every printing sets as 'L. Franchere'.

**Why (T-1554, 2026-10-09).** T-1554 read every printing of St Cyr's first Chicago marriage (N. Murphy and Mrs M. Frauner, 1834, after 5 June) that this project can reach, and all of them set the witness as an initial: the Genealogy Trails page (`data/research/church/text/st_cyr_marriages_1834_1839.txt` line 7), and the *Illinois Catholic Historical Review* vol. 4 itself, July 1921, "The First Chicago Marriage Records", in two independent archive.org scans (`illinoiscatholic04illi_0`, `illinoiscatholic04unse`) — 'L. Franchere'. The Review's own baptism table (vol. 3 no. 4, April 1921, pp. 406-408, archive.org `illinoiscatholic03unse_2`) skips 1833 entry 5, where the deposited scan reads 'Louis Franchère', so no one title sets both. So the `franchere` cluster (franchere_l / franchre_louis) stays U1 in `data/residents/card_merge_rulings.json`, now referred here.

**The page exists.** The Review (vol. 3 p. 405) quotes the fly leaf: *"This record of baptisms and marriages solemnized from the year 1833-39 … was collected and bound by me in the year 1880. Jos. P. Rouges, Rector."* The marriages are in the SAME book whose title page and pages 1-19 are deposited at `chicago/reference/catholic-baptisms-1833-1835/` (FamilySearch S3HT-DHG9-*). Its marriage leaves are not deposited. FamilySearch is login-walled, so a person with an account has to deposit the leaf; the rights posture is the baptisms' (`check_required`, read-only, nothing published).

**Also found, not yet a source here:** the 1833 petition of Chicago's Catholics to Bishop Rosati, as printed in the Review vol. 3 (January 1921, "First Catholics in and about Chicago", p. 231; archive.org `illinoiscatholic00illi_1`), lists 'Francherez, Louis 1' among heads of family. It names a Louis, not an L., so it does not decide the pair. Carding it is a separate question.

**Acceptance:** the marriage leaf carrying the 1834 Murphy–Frauner entry is deposited and read; the witness's forename as written is recorded with its image locator; the `franchere` cluster is ruled on that reading (merge under C2 if the register writes Louis, distinct if it writes another forename, and stays U1 with the reason if the register itself writes only the initial).

## Decision needed

**Question:** The marriage leaf this ticket needs is on FamilySearch behind a login (the same book as the deposited baptisms, S3HT-DHG9-*). No run can fetch it. Will you, or someone with an account, deposit the leaf carrying the 1834 Murphy–Frauner entry?

- (a) Yes: the owner deposits the leaf under chicago/reference/catholic-baptisms-1833-1835/, and a run then reads it and rules on the franchere cluster
- (b) No: withdraw the ticket; the franchere cluster stays U1 with T-1554's reason (every printing sets only 'L.')

**Recommendation:** (a) Yes: the owner deposits the leaf under chicago/reference/catholic-baptisms-1833-1835/, and a run then reads it and rules on the franchere cluster — It is the one reading that can decide the cluster, and depositing it is a person's action: the login wall is the only blocker, and runs keep stepping over it at the top of the queue

**Asked:** 2026-10-10 by https://github.com/kevinrhaas/polecat-platform/actions/runs/38054512154. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.
