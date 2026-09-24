---
id: T-0909
title: The Chappel shore drawing has no candidate left: the cheapest question is the depositor's, and it has never been asked
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-06
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: answered
decision_answer: a
---

The Chappel shore drawing has no candidate left: the cheapest question is the depositor's, and it has never been asked.

T-0716 killed the last named candidate for the Eliza Chappel shore drawing on the picture
(William Mark Young's plate is the Rumsey School of 1844, by its own inscribed caption), so
the sheet now stands with **no candidate at all** and four routes left. Three of the four
need a machine this runner is not; the fourth needs a sentence from a person.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. The depositor is asked where the scan came from, and the answer — including "don't
   remember" — is written into `docs/RESEARCH/chappel_shore_origin_search.md` § 6 as an
   answered route rather than an open one.
2. If the answer names a book, a museum or a website, the sheet is placed against it and
   `data/sources/eliza_chappel_school_shore_view.json` gains whatever the placement earns:
   `author`, `date`, `citation`, `repository`, and a re-argued `rights_status`. `verified`
   moves only if the original is located with its terms stated.
3. If it does not, the remaining routes are run from somewhere unblocked, in the order § 6
   sets: the Newberry and CPL special collections under the artist and studio NAMES; then
   the HathiTrust phrase search; then, last, the rest of Young's 1925 campaign for Koopman,
   Robinson & Neumer, which rests on nothing but the same hand having drawn old Chicago.

**Why this is blocked on the owner rather than worked.** The file arrived from the
repository owner with a social-media filename, so only he can say where he got it, and it
is the one route with a person behind it instead of a 403. Every automated route that this
runner can reach has now been run and recorded: eBay and PicClick item pages, WorthPoint,
HathiTrust, Explore Chicago Collections and `images.chicagohistory.org` all refuse it; the
Art Institute and Smithsonian APIs answer cleanly and hold no William Mark Young. Sending
another run at those walls would spend a budget on nothing.

**One thing T-0716 leaves behind that is worth more than this ticket.** The wall round the
auction listings is passable: `picclick.com/?q=` is not blocked and yields eBay's own image
id, and `i.ebayimg.com/images/g/<id>/s-l1600.jpg` then serves the full-resolution file. That
is what put Young's plate in front of a reader after T-0663 had recorded it as unreachable.
It is written up in § 3 of the research file for the next unattributed picture.

**Links:** T-0716 (the test that closed the candidate) · T-0663 (the search) · T-0649 (the
reading that closed the geometric route) · T-0617 ·
`docs/RESEARCH/chappel_shore_origin_search.md` ·
`data/sources/eliza_chappel_school_shore_view.json`.

## Decision needed

**Question:** Where did the Eliza Chappel shore drawing come from? It was deposited with a social-media filename and no artist, date or repository, and every automated lead is exhausted.

- (a) I will name the source (book, museum page or post) in this ticket
- (b) Nobody knows: keep it as text-only evidence, derive no scene assets from it
- (c) Remove the drawing from the reference corpus

**Recommendation:** (a) I will name the source (book, museum page or post) in this ticket — you deposited it, so one sentence from you settles what no catalogue sweep can; (b) is the safe fallback under rule 6

**Asked:** 2026-09-23. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.

**Owner answer (2026-09-24):** (a) — the source is
https://drloihjournal.blogspot.com/2018/01/eliza-chappell-the-first-chicago-teacher-paid-by-public-funds-in-1833.html
("Eliza Emily Chappell, the First Chicago Teacher Paid by Public Funds in 1833", *The Digital
Research Library of Illinois History Journal*, January 2018). Given in chat; the owner could not
enter a source through the board's answer buttons.

**What that page does and does not establish (checked 2026-09-24).** The page's first image is
`21617595_10203558686525015_5452300313452439832_n.jpg` — the SAME social-media filename recorded
in `data/sources/eliza_chappel_school_shore_view.json`, so this is where the deposited file was
taken from. The page itself names no artist, date, publication or holding institution for the
drawing; the journal states that it "does not use inline citations on purpose". So the
**provenance chain gains its first link** (deposit ← this 2018 journal post) and the **origin of
the drawing is still unestablished**: the post is a republication, not a source for the image.

**For the run that takes this:** record the page as the drawing's immediate source in its
source record (url, title, publisher, 2018-01), keep `describes_date` as it stands, and leave
`rights_status` at `check_required` — a republication with no credit does not clear rights, so
under AGENTS.md rule 6 the drawing may be CITED in text but no scene asset may be derived from
it. Close this ticket on that; the artist/original-publication search is not reopened unless a
lead appears.
