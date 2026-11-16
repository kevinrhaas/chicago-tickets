---
id: T-3562
title: 1815 Prairie's remaining photograph differences: the pavilion's full 4 m width with the door in it, its dentil band and shoulders, the corner bay's set-out past the flank, the rock-faced south flank, the door's pedimented hood, the stoop's newels, arched underside and basement doorway, the mansard's curb height, cresting, finials and south-flank dormer, the north stack's place, and which front stood in 1904 (after the piece before it)
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1893
opened: 2026-11-12
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

1815 Prairie's remaining photograph differences: the pavilion's full 4 m width with the door in it, its dentil band and shoulders, the corner bay's set-out past the flank, the rock-faced south flank, the door's pedimented hood, the stoop's newels, arched underside and basement doorway, the mansard's curb height, cresting, finials and south-flank dormer, the north stack's place, and which front stood in 1904 (after the piece before it).

Piece 2 of 2 of **T-1893 — Refine 1815 Sears-Meeker altered house**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1893 was split (2026-11-12T09:04:45.659Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 11/12/2026, 3:01:58 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/43187061918) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/43187061918) may be working one of the pieces now.

## Image gate stays on T-1893

T-1893 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Released 2026-11-12** (claim of run 11/12/2026, 5:20:10 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43324228229): PR #1972 builds the door's pediment on its carved brackets (a K01 door-hood option, in the front's stone, finial on its apex) and the stoop's swept cheeks with a capped newel at each foot, off the square-on photograph; both match records re-judged (hood, cheeks and newels fixed). Still open in the match records: the pavilion's full 4 m width with the door in it (and so the pediment built 1.72 m against the print's 2.55 m), its dentil band and shoulders, the corner bay's set-out past the flank, the rock-faced south flank, the stoop's arched underside, iron rail and basement doorway, the mansard's curb height, cresting, finials and south-flank dormer, the north stack's place, the narrow light over the door, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-13** (claim of run 11/13/2026, 4:42:53 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43407648656): PR #1986 (resume, CI gate 8/8 green, awaiting the aggregate check) lays the south flank in the front's rock-faced stone (a new K01 option, stone_front.flanks) and moves the flank dormer to 13.9 m behind the south stack, off the oblique print; both match records re-judged. Still open in the match records: the pavilion's full 4 m width with the door in it (so the pediment's width and the shoulders), its dentil band, the corner bay's set-out past the flank, the stoop's arched underside, iron rail and basement doorway, the mansard's curb height (the flank dormer about 1 m low with it), cresting and finials, the north stack's place, the narrow light over the door, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-13** (claim of run 11/13/2026, 1:59:23 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43495486095): PR #2013 (gated locally green; CI gate queued at hand-off) stands 1815 Prairie's north stack on the north wall's cornice over the stair projection, bare of pots, as the square-on print draws it (K15 params gain a per-stack pot override, no other house's inputs moved); both match records re-judged (north stack's place and its bare head fixed). Still open in the match records: the pavilion's full 4 m width with the door in it (so the pediment's width and the shoulders), its dentil band, the corner bay's 0.75 m set-out past the flank, the stoop's arched underside, iron rail and basement doorway, the mansard's curb height (and the flank dormer with it), cresting and finials, the south stack's longer pots (about 1.0-1.1 m: a K15 kit profile, which every K01 house hashes, so a district rebake) and sunk panels, the narrow light over the door, the north fence, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-14** (claim of run 11/13/2026, 10:07:03 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43554183147): PR #2032 (resume, gated locally green; CI gate queued at hand-off) lays 1815 Prairie's narrow light over the door's south jamb at its own size off the square-on photograph (0.43 x 1.09 m, sill 6.19 m; K01's front_bays_by_storey takes a light read off the picture on an upper storey, params-only, no other house's inputs moved); the square-on match record re-judged (narrow light fixed). Still open in the match records: the pavilion's full 4 m width with the door in it (its dentil band, shoulders and the pediment's width), the basement doorway and rail under the stoop, the mansard's cresting, finials and curb, the corner bay's set-out past the flank, the stack's panels and pots, and which front stood in 1904.

**Released 2026-11-14** (claim of run 11/14/2026, 5:47:15 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43590578896): PR #2043 lets K01's mansard deck stand under a hipped crown (each cresting run stopped short of the crown's slates, k01_mansard_deck.crown_gap) and gives a crown a cross finial; 1815 takes 0.45 m of iron cresting on its street and south flank curbs (the print's band, rail y 146-150 to foot y 178), a 0.9 m cross on the pavilion's crown and a 0.45 m finial on the street dormer, whose light is re-read to 1.65 m under a 42-degree gable (it had been judged fixed 0.35 m short). Square-on record: cresting and finials fixed; a new open item, the deck showing over the rail where the print shows sky, one question with the curb's height (0.2 m high on the square-on, 0.8 m low on the oblique). Still open: the pavilion's full 4 m width with the door in it (its dentil band, shoulders and the pediment's width), the basement doorway and rail under the stoop, the curb's height and the deck over it, the corner bay's set-out past the flank, the stack's panels and pots, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-15** (claim of run 11/15/2026, 9:58:37 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43732146697): PR #2082 builds the three sunk panels the oblique print draws down 1815's south stack (0.15 m across, 11.35-13.45 m), cut in the stack's own stone: K15 now sinks a stone stack's panel in its stone, and a cornice stack may name panel_foot_m (all 52 K01 houses rebuilt byte-identical, only their input hashes moved); the oblique match record re-judged (panels fixed). Still open in the match records: the pavilion's full 4 m width with the door in it (its dentil band, shoulders and the pediment's width; needs a door through an ordinary pavilion and an attic narrower than the pavilion under it, which K08 cannot build), the basement doorway, open underside and iron rail under the stoop's north landing, the curb's height and the deck over it, the corner bay's set-out past the flank, the stack's pots (a district rebake), the north fence, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-15** (claim of run 11/15/2026, 1:23:39 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43749054258): PR #2082 (stack's sunk stone panels, one of the ticket's differences) lapped onto dev and handed on with resume (CI gate queued); the image gate still has 13 differences open across both views, so the ticket stays open for them

**Released 2026-11-15** (claim of run 11/15/2026, 5:24:08 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43772091684): PR #2082 (south stack's sunk stone panels) merged to dev 2026-11-15 on a green CI gate; the merged tree re-checked locally (validate --stale 0 errors). The image gate's other differences remain open in the match records, so the ticket stays open for them

**Released 2026-11-15** (claim of run 11/15/2026, 10:21:29 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43802090689): PR #2097 (resume, gated locally green: check.sh 1/4-4/4 and smoke desktop 1, desktop 3, mobile 3; CI gate queued at hand-off) builds 1815's low iron railing across the north side yard off the square-on photograph: K11's coping front may name passage_fence, a kit spear run on its own curb square to the street (1815's on u 15.6, 1.9 m behind the front, 0.79 m to the tips, from the lot line to the stair projection); all 51 other K01 houses rebuilt byte-identical, only input hashes moved; the square-on match record's north fence fixed. Still open in the match records: the pavilion's full 4 m width with the door in it (its dentil band, shoulders and the pediment's width), the basement doorway, open underside and iron rail under the stoop, the curb's height and the deck over it, the corner bay's set-out past the flank, the stack's pots, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-16** (claim of run 11/16/2026, 6:04:34 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43860632654): PR #2108 (resume, gated locally green: check.sh 1/4-4/4, smoke desktop 1, desktop 3, mobile 3; CI gate queued at hand-off) gives K15 a slender 1.1 m pot (long) and stands it on 1815's south stack's three flues off the oblique (the kit's 0.72 m tall pot stood 0.3-0.5 m short); all 51 other K01 houses rebuilt byte-identical, only input hashes moved; the oblique match record's pot height fixed. Newly open there: a possible fourth pot (four 0.21 m flues do not fit the 1.1 m stack) and K15's soot band rendering red brick on this stone stack's head. Still open: the pavilion's full 4 m width with the door in it (its dentil band, shoulders and the pediment's width), the basement doorway, open underside and iron rail under the stoop, the curb's height and the deck over it, the corner bay's set-out past the flank, and which front stood in 1904. Not split: the gate stays on this ticket.

**Released 2026-11-16** (claim of run 11/16/2026, 3:39:23 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43959852180): PR #2125 (resume, gated locally green: check.sh 1/4-4/4, smoke desktop 1, desktop 3, mobile 3; CI gate queued at hand-off) keeps a stone K15 stack in its own stone through the soot band, so 1815's south stack (oblique) and north stack (square-on) no longer show a red brick band under their heads; kit specimen regenerated, all 51 other K01 houses rebuilt byte-identical (input hashes only); both match records re-judged (the band fixed). Still open in the match records: the pavilion's full 4 m width with the door in it (its dentil band, shoulders and the pediment's width), the basement doorway, open underside and iron rail under the stoop, the curb's height and the deck over it, the corner bay's set-out past the flank, a possible fourth pot, and which front stood in 1904. Not split: the gate stays on this ticket.
