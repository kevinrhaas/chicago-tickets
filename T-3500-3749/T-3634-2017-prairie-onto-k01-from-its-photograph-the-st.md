---
id: T-3634
title: 2017 Prairie onto K01 from its photograph: the stone front, the mansard with gabled dormers and cresting, the gabled projecting bay, the columned porch with its balcony and balusters, the basement grilles
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1917
opened: 2026-11-17
closed: null
pr: null
claimed_by: run 11/22/2026, 5:28:08 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/45082635865
claimed_at: 2026-11-22T23:28:09.010Z
decision: null
decision_answer: null
---

2017 Prairie onto K01 from its photograph: the stone front, the mansard with gabled dormers and cresting, the gabled projecting bay, the columned porch with its balcony and balusters, the basement grilles.

Piece 2 of 3 of **T-1917 — Refine 2017, 2021 High and 2027 Cobb-associated group**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1917 was split (2026-11-17T12:10:53.401Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 11/17/2026, 6:10:00 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/44079072792) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/44079072792) may be working one of the pieces now.

## Image gate stays on T-1917

T-1917 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Released 2026-11-18** (claim of run 11/18/2026, 3:55:31 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44397638657): taken 52 min into a run after its lap of #2196 was overtaken by a lockless sibling (slice 1/8 shipped the same fix); scoped before building: the 2017 photo is not yet ingested (source record, rights baseline, camera solve) and the draft record must be rewritten as a full K01 spec (2021's T-3633 was 41 files), which with emit, bake, photo-match and the ~50 min gate does not fit the 95 min left — released untouched for a fresh run

**Released 2026-11-18** (claim of run 11/18/2026, 4:44:51 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44409897979): Built and on PR #2202 (resume: CI gate queued, nothing red): 2017 Prairie on K01 off its photograph, camera solved, match record differs. done is refused because T-3634 became T-1917's last open piece (T-3635 went to review) and so inherits the parent's image-gate sign-off for 2017 and 2021; 2017's open items need kit work (K08 gable lights and bargeboards, K10 crenellated cresting, carved dormer lunettes, ring-pierced porch parapet, a north stack on the flank's face, grilles on two lights in one K08 storey, a low area railing) and 2021's record is differs. Whoever takes this next: merge or confirm #2202, then do the sign-off

**Released 2026-11-19** (claim of run 11/19/2026, 12:43:14 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44458298526): slice 7/8 only lapped PR #2202 (merged dev, re-baked, re-derived, gated green locally; handed on with resume while CI queued); the image gate still has 8 differences open on house_2017_prairie, so done --pr is refused

**Released 2026-11-19** (claim of run 11/19/2026, 4:05:03 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44501074758): PR #2212 fixes two of 2017's open photograph differences (the crenellated crest along the mansard's curb, and grilles on the projection's two basement lights; the 'iron drawn twice' was the 0.1 m ring's legs lying on the 3rd and 5th bars). The sign-off still cannot close: 6 differences stay open on 2017 (dormer lunettes, gable bargeboards and dentil band, the gable's two attic lights — K08 cuts no light in a gable's face — the porch's ring-pierced parapet and ball finials, the north stack's place, the low area railing) and 7 on 2021's view, each needing kit work. Released untouched by any further claim; the next run takes the next kit gap

**Released 2026-11-20** (claim of run 11/20/2026, 2:12:31 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44699461008): PR #2251 cuts 2017's two gable attic lights (K08 coped gable now takes roof.gable.lights); gated green locally (check.sh 4/4, smoke desktop 1+3, mobile 1), handed on with resume while CI's smoke legs were still queued — the janitor or the next run merges it. done stays refused by the image gate: 5 differences open on 2017 (dormer lunettes, gable bargeboards and dentil band, porch ring-pierced parapet and finials, north stack's place, low area railing), and 2021's view needs photo_match re-run (its flora inputs moved) besides its own open items. Next run: confirm #2251 merged, then take the next kit gap

**Released 2026-11-20** (claim of run 11/20/2026, 11:23:05 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44780408119): lap of #2251 handed on with resume (gate queued on saturated runners); PR is a partial piece — 2017 still differs from its photograph, so the ticket returns to the queue as the PR body states

**Released 2026-11-21** (claim of run 11/21/2026, 7:33:12 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44908730438): PR #2280 dresses 2017's two dormers as the photograph's classical pediments (pilasters, frieze, level cornice, 45-degree rake) with a carved lunette in each tympanum (K10's dressed pediment now takes dress.lunette; stone-faced dormers lay their dress in the front's stone); gated green locally (check.sh whole by round-robin parts; 66 other K01 meshes byte-identical), merging on CI. done stays refused by T-1917's image gate: 4 differences open on 2017 (gable bargeboards and dentil band, porch ring-pierced parapet and finials, north stack's place, low area railing) and 2021's view still has its own open items. Next run: confirm #2280 merged, then take the next kit gap

**Released 2026-11-21** (claim of run 11/21/2026, 11:41:46 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44930744685): PR #2283 builds 2017's porch parapet as the photograph's coped band pierced with five rings under ball finials on plinths (K01 hood railing takes pierced/finials) and stands the north stack on the cornice astride the flank at the photograph's edge, top 12.5 m (K01 mansard deck lets a cornice stack break the curb, cresting stopping short); 107 K01-family meshes rebuilt byte-identical; check.sh parts green after re-deriving, smoke desktop 1 pass; merging on CI. done stays refused by T-1917's image gate: 2 differences open on 2017 (gable bargeboards, dentilled band and ventilator; low iron railing at the front's foot) and 2021's view has its own. Next run: confirm #2283 merged, then take the next kit gap

**Released 2026-11-22** (claim of run 11/21/2026, 10:30:44 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44984079196): PR #2292 builds 2017's gable as the photograph's: a dentilled foot cornice (shelf, 21 dentils, fillet), bargeboards under both rakes, a latticed ventilator in its peak, rakes at the print's 1.4 pitch to its 12.2 m apex (K08 coped gable takes foot_cornice/bargeboards/ventilator; 68 other K08 meshes byte-identical); handed on with resume while CI's gate was queued, nothing red. done stays refused by T-1917's image gate: 1 difference open on 2017 (the low iron area railing before the basement, which needs a K11 layout with iron both sides of the stoop on a line close before the house) and 2021's view has its own. Next run: confirm #2292 merged, then take the railing

**Released 2026-11-22** (claim of run 11/22/2026, 1:29:30 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44997480270): slice 2/5 lapped PR #2292 onto dev twice (2120 and 2013 Prairie landed mid-run): re-hashed/re-derived, local check.sh 8/8 green, handed on with resume while CI's gate ran (0 red). done stays refused by T-1917's image gate: 1 difference open on 2017 (the low iron area railing) and 2021's view has its own. Next run: confirm #2292 merged, then take the railing

**Released 2026-11-22** (claim of run 11/22/2026, 10:38:41 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45043184859): slice 4/5 lapped PR #2292 onto dev after T-3726 (#2295) landed: manifest conflict cleared by merge_asset_registry (71 GLBs byte-identical), doors_1904 re-derived, local check.sh 8/8 green, mobile smoke 1 full pass; handed on with resume while CI's gate was queued (0 red). done stays refused by T-1917's image gate: 1 difference open on 2017 (the low iron area railing) and 2021's view has its own. Next run: confirm #2292 merged, then take the railing

**Released 2026-11-22** (claim of run 11/22/2026, 1:44:57 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45061778096): slice 1/5 lapped PR #2292 onto dev after T-3718 (#2294) landed: manifest conflict cleared by merge_asset_registry (71 GLBs byte-identical), doors_1904 re-derived, local check.sh 8/8 green, mobile smoke 1 PASS 95/0 (desktop 1 cut at the 590 s cap, 0 red); handed on with resume after two 540 s merge laps while CI's gate was queued (0 red). done stays refused by T-1917's image gate: 1 difference open on 2017 (the low iron area railing) and 2021's view has its own. Next run: confirm #2292 merged, then take the railing
