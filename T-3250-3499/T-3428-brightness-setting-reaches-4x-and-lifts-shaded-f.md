---
id: T-3428
title: Brightness setting reaches 4x and lifts shaded facades without blowing out the sky
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-06
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

Brightness setting reaches 4x and lifts shaded facades without blowing out the sky.

Owner (Kevin, 2026-11-06), with a screenshot of the Architects jaunt stop 2 at the Glessner
front under the parkway elms: "jack up the settings brightness control and let me make the
scenes much brighter ... increase the brightness several steps like 3x or 4x maybe".

The K24 aid tops out at one stop (2x) and multiplies the tone-mapping exposure only, so a
facade in shade barely moves while the sunlit roofs and sky reach the ACES shoulder first.

**Acceptance:**
- Settings › Display › Brightness runs from the calibrated 1x up to 4x (two stops), in steps.
- At the top a facade in shade reads about 4x brighter; the sky and sunlit surfaces rise far
  less, so the sky does not wash white.
- 0 is still bit-identical to the calibrated frame; a stored value from the old 0..1 stop
  slider keeps meaning what it meant.
- Checked on phone (390x780) and desktop with before/after shots at the Glessner front.
