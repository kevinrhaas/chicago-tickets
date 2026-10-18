---
id: T-2751
title: Keith's image gate closed: every reference view of keith_house_1808_prairie reads matches with nothing open, and T-1883's full acceptance (close street, corner and aerial views; liberties, licences and compressed assets) checked off
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2726
opened: 2026-10-18
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

Keith's image gate closed: every reference view of keith_house_1808_prairie reads matches with nothing open, and T-1883's full acceptance (close street, corner and aerial views; liberties, licences and compressed assets) checked off.

Piece 4 of 4 of **T-2726 — Keith's image gate closed: the c. 1888 SW camera re-fit, the Glessner-front stack, the bow lights' and joints' grain, the 1965 tint and pedestal panels and owner-1800's reviewer reason ruled, every view of keith_house_1808_prairie reads matches, and T-1883's acceptance checked off**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2726 was split (2026-10-18T08:54:59.736Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/18/2026, 3:52:48 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39112866799) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39112866799) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. Every reference view of `keith_house_1808_prairie` reads `matches` with nothing `open`, from the GLB in the tree.
2. T-1883's full acceptance (close street, corner and aerial views; liberties, licences and compressed assets) checked off.

## Image gate (owner, 2026-10-11, T-2368)

Carried from T-2726/T-2714/T-2586/T-2580/T-1883: this piece closes the house, so `ticket.mjs done` refuses it until every view of the building below is `matches`.

- keith_house_1808_prairie

The parent T-2726's "Findings carried from T-2725's run" section holds the measurements this piece starts from.

## Findings carried from T-2748's run (2026-10-18)

The c. 1888 SW view (and the owner's reproduction of it) now has a camera that holds the crown, the third-storey lights and grade together (4.1 px RMS; read its `solve`). Two differences it shows for the first time are open in both match records and must be built (Keith rebaked) before this gate can close; split them off this piece if they are more than its run:

- **The cowl ventilator's set-back.** The print's cap tops out at x 1243, y 106 against the render's 1232, 119. The rear pinnacle beside it holds to 1.5 px across, so the 11 px is the cowl's: 0.3 m less set-back behind the return's face moves the render's cap 9 px right (0.3 m further back along the return 11 px, but the plate, Taylor 2135 and the 1887 view fix its place along the return). The print reads it about 0.3 m nearer the face than the reconstructed 0.6 m, and about 0.13 m higher net of the camera's residual.
- **The stoop.** The landing's pierced balustrade reads at x 915-960, y 910-960 against the render's 950-990, 885-925, and the arch under the flight is a low round-headed opening at x 910-937, y 1012-1032 (about 27 x 20 px) against the render's 952-985, 973-1035 (about 33 x 62 px): the stoop stands about 35 px further left (east or south of where it is built) and its arch is far lower than built. Read the 1965 porch view and the 1888 plate's stoop alongside before moving it.
