---
id: T-2781
title: 1637's south flank finished from the Grosvenor photograph: the bay's columns and carved dress, the pale band along the wall's foot read as water table or coping and built, and the panelled stack at about u 6.0 weighed against the engraving's wing stack and the one the evidence holds built; rebaked, and the Grosvenor record brought to matches
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2756
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

1637's south flank finished from the Grosvenor photograph: the bay's columns and carved dress, the pale band along the wall's foot read as water table or coping and built, and the panelled stack at about u 6.0 weighed against the engraving's wing stack and the one the evidence holds built; rebaked, and the Grosvenor record brought to matches.

Piece 2 of 3 of **T-2756 — 1637 Prairie's two match records brought to matches: what the Grosvenor photograph shows the remodel kept built, and the engraving's last open items (the main cornice's band over the swell bay, the stacks' hooded crowns) built or argued (after the piece before it)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2756 was split (2026-10-18T15:46:29.474Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/18/2026, 10:44:50 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39140721449) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39140721449) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Findings carried from T-2780's run (2026-10-18, PR #1028)

T-2780 built the south bay's body (`bays[south_flank]` on K01's `side.north`, which is this east-side house's south flank) and the round-headed light over it (`window_over`). What it left open, each now an `open` item in `grosvenor_asbuilt_photo.match.json` and owned here:

- **The cheeks' lights are not cut.** The photograph shows a round-arched light in the west cheek between its columns (x 362-398 px, y 515-680) over a small light in its base (y 690-730). K08 holds every window's recess to at least 0.33 m inside its bay (`check_bay_kit.py`, `parts.recess.min_m`), and a 1.0 m cheek 0.75 m out has no room: at 0.33 m the recess's inner corner passes behind the host wall. Opening them needs a shallower light the kit can still close (a blind or a shallow room), which is a K08 rule change to argue, not a record edit.
- **The columns** at the bay's corners and between its lights (x 350-362 and 395-405 px, y 505-690), and **the carved dress**: the frieze's ovals (y 470-500), the capitals' band (y 505-515), the consoles' scrolls and the corona's mouldings. K08 has no column part.
- **The front's light stands about 15-20 px left of the photograph's** (x 406-436 against 420-458). It is centred on the sheet's 2.22 m front, which spans x 395-452 through this camera; the photograph's light runs to the frame's edge, so the front may be wider, or the bay further east, than the sheet says. Weigh that alongside the columns.
- **The window over the bay's open shutters** (x 352-375 and 425-445 px): K06 carries no shutter.
- The base light is built round-headed (0.55 x 0.65 m from 2.04 m); the photograph's is round. K06 has no oculus (L-k01-1637-south-bay-2780).
