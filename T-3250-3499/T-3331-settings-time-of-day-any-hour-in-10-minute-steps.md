---
id: T-3331
title: Settings › Time of day: any hour in 10-minute steps, named times, night grade, and a setter jaunts can call
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-02
closed: 2026-11-02
pr: 1636
claimed_by: run 11/2/2026, 8:36:48 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-03T04:27:59Z
claimed_run: null
claimed_at: 2026-11-03T02:36:49.435Z
decision: null
decision_answer: null
---

Settings › Time of day: any hour in 10-minute steps, named times, night grade, and a setter jaunts can call.

The owner, 2026-11-03 (project thread "Add time-of-day setting"): *"Cans we add a setting to control time of day? Would be near if we could choose any time or any hour or roughly half hour or 10 min interval? Or it could be 4 hour segments like daybreak, morning, daytime, etc. this will also include lights in the houses and business appropriate to the era, lit street lamps etc in 1904 yoh can do this as multiple tickets and default it to daytime in settings and add features over a number of tickets, you can start with 1812 since that is less comple but you will need to deal with fire/lights/oil lamps maybe ? however they would have lit the fort, do this over multple tickets"*. Chain: T-3331 (the setting) → T-3332 (1812) → T-3333 (1835) → T-3334 (1904); each waits on the one before. T-3328 (the 1812 jaunts set each stop's hour) waits on T-3331's setter.

**What ships:**
- Settings › Show › Time of day: a slider over the whole day in 10-minute steps (local solar time, as the scene's own hour already is), plus named times — daybreak, morning, daytime, afternoon, sunset, dusk, night. Default **daytime**: the scene's own hour (1812 15:00, 1835 12:30, 1904 10:30), which is the frame that shipped before.
- The sun follows the hour on the scene's (or the Season's) date: bearing, height, colour toward the horizon, shadows. Below the horizon the sky goes through twilight to a night sky; the fill, the haze and the ground dome follow; the sward and the far timber band follow too.
- Night is graded for the dark-adapted eye so it stays walkable (a liberty: no moon or starlight is measured).
- `api.timeOfDay.set(hourOrName, { date, transient })` / `.restore()` / `.current` for jaunt stops (T-3328): a transient hour is not stored and `restore()` returns the visitor's own.

**Not here:** lamps, candles, fires, lit windows (T-3332..T-3334).

**Acceptance:** daytime is pixel-identical to today's frame; phone and desktop shots at daybreak, sunset, dusk and night in 1812; no new per-frame cost; gate green.
