---
id: T-3674
title: On-site walking tour: Window mode leads a GPS walk along Prairie Avenue to Glessner House
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
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

On-site walking tour: Window mode leads a GPS walk along Prairie Avenue to Glessner House.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance:** In 1904, an "On-site tour" built on Window mode (js/controls/window.js) that a visitor standing on Prairie Avenue can follow on a phone or tablet: an ordered set of stops along the 1800 block of Prairie Avenue ending at Glessner House, each with its real-world position (lat/lon), a short cited card about what stood there in 1904, the live distance and direction to the next stop from the GPS fix, and arrival when within a radius scaled to the reported accuracy. Shows GPS accuracy honestly; a fix off the tour's ground says so and never walks there; works without motion permission (drag to align). `?window-at=lat,lon` drives it for testing; a check covers stop order, arrival and off-ground handling. No server. Works at 390x780 and 1280x800; pictures in the PR. Real on-street field testing is Kevin's.

Owner request 2026-11-19 ("work the rest of that list for anything that does not require a server"), gap-analysis item 16 (docs/CLASSROOM-FEATURES.md).
