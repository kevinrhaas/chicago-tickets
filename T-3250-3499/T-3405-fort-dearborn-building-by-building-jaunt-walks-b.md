---
id: T-3405
title: Fort Dearborn building-by-building jaunt walks by default, and a chosen Fly is honoured on every jaunt leg
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: 1747
claimed_by: interactive thread 11/5/2026, 11:29:09 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-06T05:29:10.963Z
decision: null
decision_answer: null
---

Owner, 2026-11-06: *"on the fort dearborn bulding by building jaunt, you have two options in traveling fly and instantly and i think for almost everything there the default should be walk because you are mostly just walking around the fort?"* and *"i am not sure that the travel mode in jaunts is working correctly because if i say fly to next it might just go instantly and its not far to fly"*.

`first-fort-dearborn-tour` offers only Fly and Instantly (default Fly). Its twelve stops are a few dozen metres apart in and around a 33 m fort, so they should be walked. Separately, a leg's authored `mode: 'instantly'` (T-3355) applies whenever the visitor is on the jaunt's default mode, so a visitor who picks Fly on a Fly-default jaunt still jumps, and the mode picker cannot even record the choice because Fly is already its value.

**Acceptance:**
- The fort tour offers Walk, and Walk is its default; every leg that is a short walk walks (the router reaches each stop, gates included), and only a genuinely long or impassable leg keeps Fly/Instantly as its authored mode.
- On every jaunt, a mode the visitor picks is honoured on every later leg; an authored leg mode applies only until the visitor picks one, and the picker shows the mode the leg actually travels in.
- Reducer tests cover both; gate and smoke green.
