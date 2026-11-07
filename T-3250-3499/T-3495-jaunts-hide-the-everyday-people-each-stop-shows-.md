---
id: T-3495
title: Jaunts hide the everyday people; each stop shows only the people it calls for
state: open
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
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

Kevin, 2026-11-07: "I wonder if by default with the jaunts when going on them the people should be hidden so that they don't interfere what do you think ? We can add people to jaunts but I am concerned about all these soldiers around the fort hanging out 24 7" — and, on the plan to hide the everyday crowd during a jaunt and show only the people each stop calls for: "Sure".

- While a jaunt is under way (from the flight to its first stop until it ends, pauses to the Jaunts menu or completes), the everyday standing and walking figures are not drawn, advanced or picked: 1812's 50-odd garrison soldiers around the fort, 1835's and 1904's figures alike.
- A stop calls for people by name: its own `people` list (new, optional, schema + compile_jaunts.py check that each id is a person of the scene), and the people its person card links name. Those stand where they stand; everyone else is held out.
- Drivers on their seats and the carriages and horses are not touched (Settings > Show > Carriages and horses is their switch).
- Everyone comes back when the jaunt ends, completes, or goes to the menu; Settings > Show > People hidden stays hidden throughout and after.
- The soldiers' day/night schedule is a separate thread's work.

**Acceptance:** on the 1812 battle jaunt no garrison soldier is drawn at any stop, and the fort's figures are back on End; an 1835 stop that links Philip Peck still shows Peck at his store and no one else; Settings > Show > People hidden is never undone by a jaunt; gate green; desktop and phone checked.
