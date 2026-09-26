---
id: T-1629
title: Two notches enter the main stem near the foot of State Street and Wright and Hathaway draw one: the State Street slough enters at Wright's re-entrant just east of State, and the second notch goes
state: claimed
epic: GROUND
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: null
claimed_by: run 9/26/2026, 12:58:32 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36260744936
claimed_at: 2026-09-26T17:58:32.672Z
decision: null
decision_answer: null
---

Two notches enter the main stem near the foot of State Street and Wright and Hathaway draw one: the State Street slough enters at Wright's re-entrant just east of State, and the second notch goes.

**Owner report, 2026-09-26.** He flew the 1835 scene over the South Division river front and compared it against Wright 1834 (`wright_1834`, `wright_1834_nara_hup`) and Hathaway 1834 (`hathaway_1834`), with screenshots of both sheets over the Clark–State reach. His words: *"i think there is some river geometry that needs to be changed and a lot of it is not an issue but some of it may be an issue so we may want some of these tickets moved up."* Four tickets came from it: T-1628, T-1629, T-1630 and T-1631. They lead band 5A because the South Water Street river front (T-1200) is built on this bank. Its lots, landings and plank walk seat against the waterline, so the waterline is settled first.


## The owner's ruling

*"you have closer to the fort, further east 2 sloughs that goes in a bit there is only one just east of state, the other slough does not appear to be depicted in either the wright or the hathaway map, correct the slough east of state so it matches the wright map"*

## What stands now

Two notches reach the river within 40 m of each other at the foot of State Street:

- **The built mouth** of `state_slough_mouth`, crossing the waterline square at about **E +809.5, N +25**, which is WEST of State (State's ground control is E +825..+838). T-0118 moved it there so the reach would run straight under the committed **Slough Log Bridge** deck (E +805..+813). `tools/measure_slough_crossing.py` holds the deck over water on every commit.
- **Wright's traced re-entrant** at **E +848.6** (T-0795 re-read it on the NA/HUP sheet, 1.4 m from the trace), just EAST of State. The spec kept it "exactly as traced in the waterline" and "no longer claimed as this drain's outfall".

On the owner's reading of both sheets, the drawn slough is the one just east of State. The built mouth west of State is the invention.

## The work

1. **One mouth, at Wright's re-entrant just east of State.** Re-route `state_slough_mouth`'s last reach so the slough enters the river at the traced notch, square to the bank as T-0118 required. Fill the built mouth at E +809.5 back to the bank line, so only one notch reads from the river.
2. **The crossing moves with the water.** The Slough Log Bridge and its `slough_west`/`slough_east` approach cuts were placed over the old reach. Re-seat the bridge where Water Street crosses the new reach, update its position record, and keep `measure_slough_crossing.py` green against the new geometry. T-0118 declined this move because of the State ridge toe. The owner has now ruled that it moves (below), so derive the approach cut depths it needs, state them, and build them.
3. **The inland course stays** unless the move forces it. The route (public-square pond, Tremont House site, foot of State) is documented by chicagology, not by Wright, and the owner's ruling is about the mouth. Only its last reach bends to the new mouth.
4. Amend `docs/RESEARCH/main_branch_sloughs_1833.md` and the liberties, re-derive, and bake (`needs_bake`).

**Acceptance:** from the river and from the air, exactly one slough mouth is visible between Clark and the fort, at Wright's re-entrant just east of State. The log bridge spans water on Water Street (`measure_slough_crossing.py` passes). `check.sh` and the named smoke legs are green at both widths.

## Owner confirmation, 2026-09-26 (second message, with a screenshot of the foot of State)

*"keep the inland state slough, move the bridge, i thgink there should only be one slough though? and from the wright map it appears to start east of state. you have two slough entry points there"*

His screenshot, looking down on the foot of State Street, shows the problem plainly. The built drain reaches the river WEST of the State Street road, under the plank walk's east end, and the bank has a second notch EAST of the road where the green ground meets the sand. That makes two entry points, and there should be one.

So, settled and not to be re-asked:
- **One slough, one mouth, east of State**, at Wright's re-entrant (E +848.6). The built mouth west of State is filled back to the bank.
- **The inland course stays** as documented: public-square pond, Tremont House site, toward the foot of State. Only its last reach re-routes. Because the course runs west of State and the mouth is east of it, the drain now **crosses State Street** near the river. That crossing needs its own plank or log deck and approach grading, with a committed position record, the same way Water Street's does. Name which street each deck carries.
- **The Slough Log Bridge moves** to wherever Water Street crosses the new reach. The ridge-toe cost is accepted by the owner, so there is no `ask` escape on this point: build the approaches and state their depths.
