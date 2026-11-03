---
id: T-3328
title: 1812 jaunts: each stop sets its hour, sunset at the fort gate, nine in the morning on the beach
state: claimed
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-02
closed: null
pr: null
claimed_by: run 11/2/2026, 10:29:39 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-03T04:29:41.029Z
decision: null
decision_answer: null
---

1812 jaunts: each stop sets its hour (sunset at the fort gate, nine in the morning on the beach).

The owner, 2026-11-03 (project thread "Add 1812 Fort Dearborn story jaunts"): *"There is another session working on time of day settings so ideally you can integrate that into the jaunts, if not now in a ticket immediately following"*. The time-of-day setting itself is the thread "Add time-of-day setting" (its tickets were not filed yet when this one was written); this ticket waits for the first of them that lets code set the scene's hour.

**Proposed contract (agree it with the time-of-day work before building):**
- A jaunt stop may carry `hour`: a local solar time `"HH:MM"`, or one of the setting's named segments (`daybreak`, `morning`, ...), plus `hour_evidence` naming the claim it rests on. The compiler checks the claim is cited at that stop; an hour no source gives is `inferred` with reasoning, never presented as attested.
- On arrival the runtime eases the scene to that hour; on Explore, ending or leaving the jaunt it restores the visitor's own setting. No stop hour, no change.

**The hours the sources give (T-3325..T-3327 jaunts):**
- Killing of Jean Lalime (`killing-of-jean-lalime`): `the-quarrel` about 18:00, 17 June ("around 6 p.m.", Van Voorhis via the Chicago Reader); `the-gate` sunset ("It was sunset, when they used to shut the gates of the fort", Porthier); `the-flight` night ("In the night he packed up some things", Porthier; Irwin's "about four hours"). Other stops daylight.
- Battle of Fort Dearborn (`battle-of-fort-dearborn`): `lees-place` just before sunset, 6 April ("a little before sunset", Heald); `burns` evening; `covered-way` evening of 13 August ("The same evening the ammunition and liquor were carried", Wau-Bun); `the-gate`, `river-mouth`, `the-bank`, `cottonwoods` the morning of 15 August, from 09:00 (Heald's report); the rest daylight.
- Fort tour (`first-fort-dearborn-tour`): daylight throughout; `the-gate` may show sunset, when the gates shut.
- 1812 night lighting (fort lamps, fires) comes from the time-of-day tickets, not this one.

**Acceptance:**
- The three 1812 jaunts set these hours; leaving a jaunt restores the visitor's hour.
- Compiles and passes the refusals; phone and desktop checked at the dark stops (the sunset gate and the night flight are still readable).

**API agreed with the time-of-day thread (2026-11-03, T-3331):** `api.timeOfDay.set(hourOrName, { date, transient, ease })`. `hourOrName` is `"HH:MM"` local solar time or one of daybreak, morning, daytime, afternoon, sunset, dusk, night. Names resolve against the sun on `date` (`"YYYY-MM-DD"`), so a stop can show 17 June 1812 or 6 April 1812 instead of the scene's 14 August. `transient: true` does not store the choice, `api.timeOfDay.restore()` goes back to the visitor's own hour and date, and `api.timeOfDay.current` reports `{ hhmm, name, transient }`. `set` returns a promise that resolves once the frame is relit. A stop's data therefore carries `hour` and an optional `date` too.
