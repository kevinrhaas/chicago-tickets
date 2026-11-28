---
id: T-3730
title: 2130 Prairie's cameras on both 2140 photographs, the photo-match worked down and the image-gate sign-off (after the piece before it)
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1927
opened: 2026-11-22
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

2130 Prairie's cameras on both 2140 photographs, the photo-match worked down and the image-gate sign-off (after the piece before it).

Piece 2 of 2 of **T-1927 — Refine 2130 Murdoch rounded-bay house**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1927 was split (2026-11-23T01:44:52.098Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 11/22/2026, 7:43:26 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/45094892509) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/45094892509) may be working one of the pieces now.

## Image gate stays on T-1927

T-1927 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Released 2026-11-26** (claim of run 11/26/2026, 1:31:03 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45883486125): PR #2366 (branch steward/t3730-2130-photo-match) ships both cameras (the Chicagology print from Prairie & 22nd, 7.4 px RMS; the Van Osdel print, 3.4 px RMS), the tower's cone lowered to 1.6 rise/run and the south flank laid in the front's rock-faced stone. Both match records stay 'differs' on two differences that need new K01 parts this run could not add: neither picture shows the street gable the build carries, and both show a stone gable on the south flank under a ridge running along the avenue to the tower's cone (a side-gabled front block); and the columned porch across the front's south end (no K01 recessed porch). The Chicagology view also has the stack on that ridge open. The sign-off cannot close until those land.

**Released 2026-11-26** (claim of run 11/26/2026, 3:33:37 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45897326014): PR #2374 (steward/t3730-2130-side-gable, on resume until its content build runs) roofs 2130's front as the side-gabled block both photographs show (ridge 4.0 m behind the front at 13.9 m, 52 degrees, the south gable in stone) and moves the stack onto that ridge. Both match records stay 'differs' on three differences that need new K01 parts: the columned porch across the front's south end, the attic light in the south gable (a K05 parapet carries no light), and the front's north part beside the tower carried up as wall to the cone's eave (about 11.2 m) under its own eave. The sign-off cannot close until those land.

**Released 2026-11-27** (claim of run 11/26/2026, 11:11:07 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45943298204): lapped PR #2374 (the side-gabled front, a piece) onto dev 482b8c5 and gated it; it waits only on CI to merge. The image gate still has the porch, south-gable light and north-front wall open, so the ticket stays open for the next piece

**Released 2026-11-27** (claim of run 11/27/2026, 1:25:44 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45951723251): PR #2374 (the side-gabled front, a piece) is complete and level with dev 482b8c5; it waits only on CI runners (69 runs queued). The image gate still has the porch, the south-gable light and the north-front wall open, so the ticket stays open for the next piece

**Released 2026-11-27** (claim of run 11/27/2026, 12:30:43 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/46047840129): PR #2401 (steward/t3730-2130-attic-light, on resume while CI's gate is queued) adds K01's light in a gable parapet (gable_roof.ends.<side>.lights) and builds the Chicagology print's attic light in 2130's south gable, within about 5 px of the print; that difference is fixed. Both match records stay 'differs' on two that need new K01 parts: the columned porch across the front's south end (a recessed corner porch under a K01 front: the loggia needs a round-arched mouth, corner_porch projects) and the front's north part beside the tower carried up as wall to the cone's eave (about 11.2 m) under its own eave. The sign-off cannot close until those land.

**Released 2026-11-28** (claim of run 11/28/2026, 1:16:51 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/46118900269): PR #2425 (steward/t3730-2130-north-front, on resume while CI's gate is queued) carries 2130's front north of v 3.8 up as stone wall to the cone's eave at 11.2 m under its own eave, roofed to the ridge and hipped south at 52 degrees (K01 gable_roof.raised_front), within about 10 px of both 2140 prints; that difference is fixed. Both match records stay 'differs' on one open difference: the columned porch across the front's south end (a recessed corner porch under a K01 front). The sign-off cannot close until it lands

**Released 2026-11-28** (claim of run 11/28/2026, 4:17:21 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/46129628236): PR #2425 (steward/t3730-2130-north-front, the raised north front) is complete and gated: local check.sh 1-4/4 green on dev c18420c merged in, smoke desktop 1 and mobile 3 green, all 8 CI gate parts green; it waits only on the aggregate gate job's runner and is on resume for the janitor. The image gate still has the columned porch across the front's south end open, so the ticket stays open for the next piece
