---
id: T-3563
title: Settings card: icon tabs, mouse sensitivity, What's new and Research at the end
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
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

Kevin, 2026-11-12 (after meeting Bill Tyre, item 1): *"could you add a setting to adjust the mouse
sensitivity for the app? and probably start to organize that settings card better with tabs and
icons at the top like some of the other cards like the inspect card and make the settings consistent
and you can move whats new to one of those tabs maybe one of the last and also the research mode
should be at the end"*

**Acceptance:**
- Settings has a look-sensitivity setting that scales mouse look (pointer lock) and, on touch,
  drag-to-look; stored with the other settings, takes effect at once, default leaves look unchanged.
- The Settings card is one row of icon-over-label tabs pinned at its top, styled like Inspect's
  (T-3435): the groups are split across tabs and only the chosen tab's rows show.
- What's new is one of the last tabs (it stays openable from the unread dot and every old route);
  Research (Expert research) is the last tab.
- Every id the page, the tests and the smoke read is kept; desktop 1280x800 and phone 390x780
  show the bar on one row with no page errors.
