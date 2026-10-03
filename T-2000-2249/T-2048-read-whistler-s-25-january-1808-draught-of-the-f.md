---
id: T-2048
title: Read Whistler's 25 January 1808 draught of the first Fort Dearborn into a measured component register: the sheet committed with its source record, every index number it draws located in fort feet, the scale and its cross-checks, and what the sheet does not show
state: done
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-0469
opened: 2026-10-03
closed: 2026-10-03
pr: 366
claimed_by: run 10/3/2026, 3:16:28 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-03T22:56:45Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37150559146
claimed_at: 2026-10-03T20:16:28.598Z
decision: null
decision_answer: null
---

Read Whistler's 25 January 1808 draught of the first Fort Dearborn into a measured component register: the sheet committed with its source record, every index number it draws located in fort feet, the scale and its cross-checks, and what the sheet does not show.

Piece 1 of 3 of **T-0469 — Reconstruct the first Fort Dearborn complex as it stood in August 1812**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. The sheet Quaife prints facing p. 164 (Whistler's draught of 25 January 1808, from the War Department original) has a source record, and its working copy is pinned by URL and sha256. The raster is not committed (data/traces/README.md: large rasters are not).
2. `data/traces/whistler_1808_fort_dearborn.json` carries every one of the index's 34 numbers as one of three things: **located** on the sheet (pixel box, and fort feet where the sheet is to scale), **not located** (with why), or **omitted by the drafter** (33 and 34, which the index itself says are "Omited in their places").
3. The scale is measured, not assumed: the "75 feete" flagstaff is drawn laid down from its own foot, so its length gives px/ft. The register states the cross-checks that hold and the ones that fail.
4. `tools/read_whistler_1808.py --check` holds the register's arithmetic and completeness offline in `check.sh`. `--remeasure` fetches the sheet, verifies its sha256 and re-measures the staff.
5. No fabric is authored. T-2049 builds from this register, and T-2050 seats it.

Nothing a visitor sees changes. This is exemption 2 of the visible-progress rule (the measurement half of a split), and the PR says so.
