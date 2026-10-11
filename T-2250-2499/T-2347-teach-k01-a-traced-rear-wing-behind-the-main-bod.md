---
id: T-2347
title: Teach K01 a traced rear wing behind the main body and retire 1634 Prairie's draft wing onto it
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1863
opened: 2026-10-11
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

Teach K01 a traced rear wing behind the main body and retire 1634 Prairie's draft wing onto it.

Piece 2 of 3 of **T-1863 — Refine 1634 and 1636 stone-front pair**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1863 was split (2026-10-11T05:06:06.922Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/11/2026, 12:03:51 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38113330249) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38113330249) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Also waiting on this: 1628 Prairie's three-storey rear wing (T-2355, 2026-10-11)

T-2355 refined 1628 Prairie's main body onto K01 (`house_1628_prairie`) and, as T-2353 did for 1616,
could not keep the sheet's wing standing: s20fp-1628-b1's second rectangle, the draft's `r2`, a
three-storey brick wing 4.5 m out behind the north part of the rear wall (plan u -4.5..0, v 2.0..6.25
in the record's own frame). It is gone from the scene until this ticket's traced rear wing can carry
it. 1628's rear window at v 4.1 m stands where the wing joins and becomes the opening into it.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

No picture of this building was found by address in the Prairie library on 2026-10-11. Before building, search the library (every record, street views and neighbours' plates included) and `data/sources/`. If one turns up, add an `## Image gate` section here naming the structure id as a bullet.
