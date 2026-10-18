---
id: T-2775
title: 1904 restarts on an iPhone walking down Prairie Avenue: the lakefront railway keeps 215 MB of geometry a phone never lets go of; lay the full rail section only near the eye and release the railway's page copies after upload
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: 2026-10-18
pr: 1018
claimed_by: run 10/18/2026, 9:06:14 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T15:16:18Z
claimed_run: null
claimed_at: 2026-10-18T14:06:14.749Z
decision: null
decision_answer: null
---

1904 restarts on an iPhone walking down Prairie Avenue: the lakefront railway keeps 215 MB of geometry a phone never lets go of; lay the full rail section only near the eye and release the railway's page copies after upload.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner's crash report 2026-10-18 (iPhone, Chrome, 1904 free roam); no open ticket covers the railway layer's memory, measured 215 MB of the phone's 854 MB at spawn

**Owner's report, 2026-10-18 (iPhone, Chrome):** "took a couple times to load and then when I got there I went to free roam and just navigate down the street and it restarted, this was 1904". A restart is the tab killed for memory.

**Measured** (`node tools/measure_memory.mjs --year 1904 --only mobile`, phone profile 390x780 DPR 3, published door, spawn):
- prod e2f67357 (release-v1888): 1040.5 MB resident estimate (gpu textures 311.2 MB; residency is not on prod yet).
- dev 7b146804: 854.1 MB. The `railway` layer (T-2478/T-2479) alone keeps 214.9 MB of page arrays: full-section rails for all 57 zones (78.4 MB, never drawn on a phone, whose near reach is 60 m), far rails 18.1 MB, ballast beds 42.6, cinders 19.0, lake face 8.9, made ground 8.2, verges 5.6, plus instance arrays. The layer was not in upload-release's RELEASE_KEEP, so a phone kept every array beside its GPU copy.
- Walking Prairie Avenue south from 16th (new `--walk prairie-street`, total per station without forced GC): dev holds ~850 MB flat with slow heap growth; the walk does not spike, the baseline is what sits at the iPhone's limit.

**Acceptance:**
1. The full rail section is laid per zone only while the eye is within its near reach and dropped once well past, on every tier; walking 600 m along the tracks keeps at most a few zones built.
2. On a phone the railway lets go of its page arrays after upload (RELEASE_KEEP `railway: []`), with its pick no longer raycasting triangles: a tap on the tracks still answers with the nearest track's card, the stone face and made ground with the edge's card.
3. 1904 phone resident estimate at spawn falls by at least 150 MB against dev on the same machine; zero page errors; the 1904 ceilings in tools/memory_ceilings.json lowered to the new reading by the file's rule.

**Result (PR):** phone 854.1 -> 696.4 MB (arraybuffers 379.3 -> 197.9; railway layer kept 214.9 -> 33.5 MB). Desktop 1328.9 MB (railway 215 -> 141 MB). Walking the tracks: built near zones 1..4. Ceilings: 1904 mobile 950 -> 775 MiB, desktop 1550 -> 1475 MiB.
