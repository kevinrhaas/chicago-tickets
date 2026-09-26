---
id: T-1631
title: From the air and at distance the 1835 world looks flooded: the horizon reads as open water with trees standing in it
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
claimed_by: run 9/26/2026, 1:27:59 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36262483597
claimed_at: 2026-09-26T18:27:59.543Z
decision: null
decision_answer: null
---

From the air and at distance the 1835 world looks flooded: the horizon reads as open water with trees standing in it.

**Owner report, 2026-09-26.** He flew the 1835 scene over the South Division river front and compared it against Wright 1834 (`wright_1834`, `wright_1834_nara_hup`) and Hathaway 1834 (`hathaway_1834`), with screenshots of both sheets over the Clark–State reach. His words: *"i think there is some river geometry that needs to be changed and a lot of it is not an issue but some of it may be an issue so we may want some of these tickets moved up."* Four tickets came from it: T-1628, T-1629, T-1630 and T-1631. They lead band 5A because the South Water Street river front (T-1200) is built on this bank. Its lots, landings and plank walk seat against the waterline, so the waterline is settled first.


## The owner's report

*"note that when we are flying or in the distance it looks like the world is flooded, you see the blue in the horizon"*

In his screenshots, flying north over the South Division at about 600 ft, everything past the North Division's first blocks turns the same blue-grey as the river and lake. The trees in that band stand up out of what reads as water, and a flat blue band fills the horizon.

## The work

1. **Diagnose which of three things it is**, with a measurement and not a guess. (a) The distance haze colour is the water's blue, so fogged ground reads as lake (T-1244 made the haze total beyond a distance). (b) The modelled ground ends at the box walls or skirt, and a water plane or lake surface fills the view beyond it. (c) Both. Screenshot the same view with the fog turned off to separate them.
2. **Fix it so land reads as land to the horizon.** The haze should tint toward a prairie or atmospheric colour that ground and water take differently, and ground should continue (a far skirt or low-cost far ground) so the horizon over the prairie west and north is land. Only the lake to the east should read as water. Do not raise scene cost past the frame ceilings the gate measures. If a ceiling blocks it, say which one.
3. Check both themes and both widths (390×780 is a release gate), and flying as well as walking.

**Acceptance:** from the owner's view (fly, about 600 ft, looking north over the river), the ground past the North Division reads as prairie fading into haze, not as water, and trees never stand in blue. East toward the lake still reads as lake. The frame ceilings hold. Before and after screenshots are in the PR.
