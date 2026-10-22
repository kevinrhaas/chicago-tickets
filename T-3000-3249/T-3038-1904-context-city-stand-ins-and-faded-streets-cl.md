---
id: T-3038
title: 1904 context city: stand-ins and faded streets clear of streets, walks, the IC right of way and each other; lots east of Calumet to the tracks
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-22
closed: 2026-10-22
pr: 1215
claimed_by: run 10/22/2026, 3:22:06 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-22T21:50:33Z
claimed_run: null
claimed_at: 2026-10-22T20:22:07.517Z
decision: null
decision_answer: null
---

1904 context city: stand-ins and faded streets clear of streets, walks, the IC right of way and each other; lots east of Calumet to the tracks.

**Owner, 2026-10-22 (thread "Context buildings in the street"):** "you put a building in the middle of the street, fix this and any others that you did that", then "some white things sitting in the tracks and also some streets that dont quite connect and the area would be filled in with buildings or whatever was there ... it seems odd to have streets ending like that do sharp edges for stuff like that and make it more logical and correct, based on history of what was there". Screenshots: a projected stand-in on 18th Street's curve into Calumet Avenue; a faded street lying in the IC tracks north of 20th; the field east of Calumet south of 20th with faded cross streets stopping in the grass.

**Found on dev (contract run on dev's data/context/1904.json):** 55 stand-ins whose rectangle overlaps a roadway, walk, alley, faded street or the IC right of way (the generator tested a stand-in's centre and corners against parcels and blocks only, never against carriageways or the railway); 35 projected railway sheds stacked inside each other; 26 trees in roadways or on the tracks; 2 faded streets on the right of way; east of Calumet below the curve the lots stopped 46 m behind Calumet's east line, though Sanborn 1911 sheet 28 draws Calumet's east lots at 20th running back to the railway's line. Sweep of the placed 1904 structures: First Presbyterian Church (T-3009 draft, 2029 Indiana) stood mirrored across 21st Street (the site builder's v axis runs south for a west front, and the row's v figures were not mirrored).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- No stand-in rectangle overlaps a street-grid carriageway, walk, parkway, curb or alley, a faded street (plus a walk's width), the IC right of way (plus a 3 m fence strip), or another projected stand-in; no tree stands in a roadway, alley, faded street, on the right of way or inside a stand-in; no faded street lies on the right of way. `build_context_1904.py --check` fails on any of these, and `--self-test` proves each refusal fires, including the owner's exact case.
- Faded streets end square, to 0.1 m, at what stops them; cross streets east of Calumet run to the right of way's west verge.
- East of Calumet south of the curve, lots run back to the right of way; where the railway bears away, the projection's avenues carry the city up to it.
- First Presbyterian stands north of 21st Street on its corner lot; `draft_prairie_1904.py --check` holds it.
- Before/after shots of the owner's views, desktop 1280x800 and phone 390x780; liberty amended; gate green.
