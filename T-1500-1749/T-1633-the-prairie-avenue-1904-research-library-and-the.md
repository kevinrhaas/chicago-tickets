---
id: T-1633
title: The Prairie Avenue 1904 research library and the pre-fire viewer's 1834 Wright shortcut, as the owner asked
state: claimed
epic: RESEARCH
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: null
claimed_by: run 9/26/2026, 12:24:38 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-26T17:24:38.293Z
decision: null
decision_answer: null
---

The Prairie Avenue 1904 research library and the pre-fire viewer's 1834 Wright shortcut, as the owner asked.

Filed 2026-09-26 for kevinrhaas/chicago PR #82 (`steward/prairie-1904-library`). The session that built it could not write to the tickets repo, so it had no ticket. The owner asked for the work in that session, and in this one said to take the PR over and merge it when green.

**What it delivers (from the PR):** a Prairie Avenue research library centred on 1904, with dated evidence through 1911, at `/4d/dev/prairie-1904/viewer/`. It carries 62 building and history records, 91 tentative mapped frontages, 73 directory occupancy candidates, 110 source records, the five supplied maps, six Glessner HABS measured drawings and the 27-page HABS report. The pre-fire viewer gains an 1834 quick-year, all 15 reference maps in its menu, and a timeline that moves to the selected map's date. No scene geometry changes. It is research the band 7 Prairie tickets (T-1250-T-1252, T-0474-T-0477) read from, not a claim of a parcel-complete reconstruction.

**Acceptance:** both viewers load on dev at 390×780 and 1280×800 with zero page errors and no horizontal overflow. `check.sh` is green. The library documents what evidence is still missing (census schedules, permits, parcel reconciliation).
