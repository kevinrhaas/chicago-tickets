---
id: T-3383
title: Wall ivy sways into the wall: Pullman's (and 1912's) Boston ivy vanishes into the brick in the wind
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: null
claimed_by: run 11/5/2026, 12:38:32 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-05T18:38:33.454Z
decision: null
decision_answer: null
---

Wall ivy sways into the wall: Pullman's (and 1912's) Boston ivy vanishes into the brick in the wind.

The owner, 2026-11-05, with a screenshot of the ivy on 1729 Prairie's front in 1904: *"on pullman these vines when they blow they disappear into the building"*.

Cause: the grown plants' wind sway (`patchTreeWind`, tree-surface.js) moves every vertex ±x/±z in the plant's own frame. A wall vine's (`vine_wall`, buildWallVineTemplate) +x is out of the wall and its leaves sit only 0.02-0.16 m off it, while the sway at the top of a 6 m patch reaches about 0.19 m, so half of every gust carries the mat into the masonry.

**Acceptance:**
- A wall vine's leaves never move to the wall side of their rest place: its sway lifts them off the wall and along it, never into it (shader, colour and shadow passes alike).
- Every other grown plant (parkway elms, yard shrubs, trees, 1835 timber) sways exactly as before.
- Every wall vine in the app shares the fix: Pullman's seven patches and 1912 Prairie's two (the only `vine_wall` users; Glessner's vines are baked, still geometry).
- Gate green; phone 390x780 checked.
