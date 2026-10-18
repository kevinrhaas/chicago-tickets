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

## Findings carried from T-2771 (2026-10-18): the Glessner-front stack is Keith's, not the camera's

The Glessner-front view's last open item (`a18-gh-glessner-front-with-keith`: the stack from the lattice's lower row down to the head band about 15 px deeper in the render) is ruled, and it is a BUILD this gate still needs:

- **Not the camera.** Every camera here is level, and under a level camera a vertical line on the front images evenly, so on one column the stack's length over the lattice's own 0.40 m row pitch is a ratio no eye height, distance or focal length can change. `tools/keith_crown_stack.py` reads it (report: `docs/RESEARCH/photo-match/keith_house_1808_prairie/a18-gh-glessner-front-with-keith-stack.json`). A tilted camera would need about 45 degrees of pitch to make it and would lean the north arris 173 px over the crown; the print holds it at x 138 on every row.
- **The prints.** Glessner-front (x 15-95): sills at y 115 / 145 in print and render alike, head band's top y 263 against the render's 278: 3.93 pitches against the model's 4.35, so **1.57 m** (1.55 m through the camera's 76 px/m) against **1.74 m**. Florian 1948 (x 204-214): 4.11 pitches, **1.64 m** by its pitch and by its camera alike, 4 px at 45 px/m — the same direction, which T-2680's "rows within 3-5 px" had taken as camera residual. The 1888 Keith plate cannot rule (branches; on x 520-540 its ratio spans 3.3-4.8).
- **Where.** Florian puts the excess above the checker band: lattice sill to the band's top 0.41 m in print against the model's 0.62 m (sill 15.25, cornice box and fillets 15.0-15.12, the K10 moulded course 14.63-14.99), while its checker-plus-gap reads 1.24 m against 1.12 m. In the Glessner-front print the moulded course's shadow hides the band's first row, so it cannot place the excess itself.
- **The build:** take about 0.1-0.17 m out of the stack between the lattice's foot and the head band (the K10 moulded course is the generic 0.36 m section read off 1619 Prairie's drawing, so a shallower course for Keith is the first candidate; Florian's absolute reading wants the crown about 0.1 m lower and the head band where it is), rebake, re-solve the Glessner-front and Florian cameras (both are fitted to controls on the crown), re-render Keith's views, and re-run `tools/keith_crown_stack.py`. One run plus a bake (M); wait for the in-flight Keith rebakes (T-2763, T-2765, T-2769) to land first, since all of them rewrite the same GLB.

## Findings carried from T-2764's run (2026-10-18)

- **The 1965 close view's camera now has depth at the loggia, and it is not what keeps `a18-gh-1808-porch-1965` from matching.** `tools/keith_1965_level_fit.py` fits a level camera on the bow re-picked on T-2765's lights and on the loggia's PLAN (both pairs' shaft silhouettes, the south pedestal's), 25 coordinates at 3.5 px RMS, with the loggia's heights left out so it predicts them: the as-built loggia draws its column 74 px against the print's 101 and its pedestal 30 against 38.5. A free factor on the loggia's heights over its deck reads 1.29-1.32; a free pixel aspect reads 1.05 and does not remove it.
- **The same factor shows on the bow, above the principal lights' heads**: the print draws the string course's foot about 56 px over the south light's head where the render draws 45. The principal and basement lights themselves register (jambs within 6 px, heads within 3).
- **Read inside the loggia with no camera but its heading**, its column's height, its pedestal's height and the south pair's width all read about 45 px to the metre; the south pedestal's width reads 33 and the pairs' 2.5 m spacing about 32. So the slide draws the loggia about 1.35 times taller for its plan than it is built, where the 1888 plate's level fits (T-2763) lowered it to 0.88.
- **Open, for this ticket to rule before porch-1965 can read matches:** which picture errs at the loggia and the bow's upper storey — this slide's optics (a lens or enlarger distortion a level pinhole cannot take), the bow's upper storey heights, or the loggia's plan (the plate reads each pedestal's front at about 47 px, which T-2769's 75 px/m makes about 0.63 m against the built 0.9). The queue was over its ceiling, so this is carried here rather than as a new line.
