---
id: T-3432
title: Jaunts fly to the start, open on a welcome page, show only readable road notes, mark the last stop and fold Outing complete
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-06
closed: null
pr: null
claimed_by: run 11/6/2026, 2:45:27 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-06T20:45:28.644Z
decision: null
decision_answer: null
---

Jaunts fly to the start, open on a welcome page, show only readable road notes, mark the last stop and fold Outing complete.

Owner (Kevin, 2026-11-06, thread "Polish jaunt start and finish screens"): "For jaunts instead of
jumping right into them, can you fly to the start instead as long as it's like maybe 5-10 seconds
max, and for the first page of the jaunt make it a little more of a welcome and background on the
jaunt as you start it on the first page and make those screens nice and with icons and things so it
looks good, when walking on a jaunt something's the text of your story along the way gets cut off or
if it really fast between locations there is no time to read it so don't show it and when you finish
the last stop screen should be more obvious that you are at the last stop and then when you get to the
outing complete that screen takes up the whole view and you can't see the list of jaunts so make that
"finish" screen outing complete much more concise and expandable so we go back to the jaunt list and
can see that".

**Acceptance:**
- Starting a jaunt flies the eye to its first stop instead of jumping there; the flight takes at most
  about 8 s wall-clock whatever the distance or frame rate, and lands on exactly the framing the jump
  gave. Reduced motion, and a visitor whose jaunt mode is Instantly, still jump.
- The first page is a welcome: the jaunt's family icon, title and premise, chips with icons (stops,
  length, light, mode), and its opening (the background) shown open, then stop 1. It shows during
  the flight too.
- Road notes during a leg are shown whole (never clipped to a line or two), and only the lines there is
  time to read before the leg ends; a leg too quick to read shows none (they stay in the stop's
  On the way fold).
- The last stop says so: a Final stop marker on the page and the bar, and the button reads Finish Jaunt.
- Outing complete is one compact card above the jaunt list (the list stays in view on a phone), with
  the ending, keepsake and counters behind one expand toggle.
- Checked on phone (390x780) and desktop (1280x800) in the four appearances.
