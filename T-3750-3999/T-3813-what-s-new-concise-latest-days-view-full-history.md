---
id: T-3813
title: What's New: concise latest-days view, full history kept, tighter entry budget
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2412
claimed_by: run 11/27/2026, 3:08:18 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T21:08:19.273Z
decision: null
decision_answer: null
---

Kevin, 2026-11-27: "That what's new has become a bit much at this point? Do you want to consolidate it some and save the old version and keep the what's new items more concise?"

The tab paints all ~3,300 releases (about 690,000 words) with every item open.

**Acceptance:**
- The What's new tab opens on the latest few release days only, grouped by day, one line per release; a release's notes open on a tap.
- The full old feed is kept, unchanged, behind a Full history control in the same tab (paged, so a phone is not handed 690,000 words at once).
- `changelog.js` keeps its path, format and every entry: Manager and the launcher read it unchanged.
- New entries are held to a tighter, concise budget (title, items, words, words per item), written into AGENTS.md; open PRs written to the old budget still pass and still fold.
- Unread flags and the dot still work; smoke checks updated; desktop and 390x780 pictures.
