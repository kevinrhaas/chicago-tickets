---
id: T-3662
title: Dev's smoke part 15 is still red at both viewports after T-3650's #2190: GLTFLoader blob textures refused (Failed to fetch) at /1904/ after the Confidence Jump; find why the blobs are revoked and bring both legs green without weakening zero page errors
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
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

Dev's smoke part 15 is still red at both viewports after T-3650's #2190: GLTFLoader blob textures refused (Failed to fetch) at /1904/ after the Confidence Jump; find why the blobs are revoked and bring both legs green without weakening zero page errors.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content build is red on smoke (desktop, 15) and (mobile, 15) on bare dev d21c6b604 (run 44340476884, after #2190) and on every PR build that draws it (#2192 9aac4f55f run 44385234168, #2150, #2196, #2195's T-3562), so each PR is refused on it and laps spend runs proving the same red

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
