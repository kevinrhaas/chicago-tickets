---
id: T-2691
title: Prairie Avenue jogs west at 18th Street: join Sanborn sheet 20 to sheet 28 and clear the roadway seam line
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 4:57:27 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T21:57:27.953Z
decision: null
decision_answer: null
---

Prairie Avenue jogs west at 18th Street: join Sanborn sheet 20 to sheet 28 and clear the roadway seam line.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 184 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-reported defect (Kevin, 2026-10-16 project thread 'Prairie Avenue jog north of Glessner'), worked now in an interactive session

**Acceptance:**

- Checked against the maps: Sanborn 1911 sheets 20 and 28 both draw the Prairie & 18th crossing, all four corners, with Prairie straight through it. So the jog is a georeference seam, not history, and the fix is to the fit, not a liberty.
- Sheet 20's fit is joined to sheet 28's at that crossing (`tools/georef_prairie_1904.py`, `join` block in its GCP file), and its self-test holds the two sheets' crossing within 0.02 m. Its RMS stays under the 4.0 m ceiling.
- Prairie's 16th-18th carriageway meets the 18th-20th one within 0.4 m a side at 18th Street (it was 1.5 m west). Lots, walks, parkway trees, footprints, drafts, refined houses, the IC edge and tracks on sheet 20 are re-derived or moved with the fit, and every tool's `--check` passes.
- The light seam line up the 16th-18th roadway is gone: the street-grid renderer no longer splits a roadway lengthwise where another roadway's edge crosses it.
- Before and after shots of the owner's view (dev 1904, looking NNW from 18th & Prairie), desktop and 390x780, are in the project folder prairie-street-jog/.
- Gate green; the moved draft houses and the e1871_postfire ground and water are rebaked, so validate --stale is clean.
