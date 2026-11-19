---
id: T-3657
title: Where and when: a daily five-photo hunt from the licensed 1904 evidence
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: 2199
claimed_by: run 11/18/2026, 1:41:34 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-18T19:41:36.836Z
decision: null
decision_answer: null
group: T-3657,T-3658
---

Where and when: a daily five-photo hunt from the licensed 1904 evidence.

**Acceptance:** Demonstrate a complete five-photo 1904 hunt at phone and desktop widths: a deterministic UTC daily challenge and validated shareable challenge link, one credited licensed historical photograph at a time, a guess from the current world position with distance-based score, an honest date/range reveal, and an explicit optional visit to its validated camera spot. Derive camera/credit/date from existing compiled evidence; no invented exact dates, added accounts, leaderboard service, second world or eager image collection. Keyboard controls, failure states, bounded local progress and corrupt/unavailable-storage handling must work. Full school accessibility certification and other-year hunts are not claimed.

## Owner scope and implementation plan

The owner asked to continue top-priority non-server items after the first classroom delivery and to checkpoint work to GitHub. This implements list item 7. Runtime work is isolated from PR #2197 while its release gates finish; this follow-up merges after that PR. Candidate evidence ids, subject to canonical data/rights checks: a18-rba-taylor-2135-glessner-ne, a18-gh-cornell-glessner-rear-c1887, a18-rba-taylor-1801-kimball-c1895, a18-rba-levy-1812-wheeler, a16-pullman-det-4a08065. Five photographs of four places are acceptable and should be described honestly. No geometry or photographic-matching work is included.

## Current recovery checkpoint — 19 November 2026

Dependent draft PR #2199 remains at6ee1a689077839dd9923edbc80269dd2cbaccfb6 while parent
#2197 finishes. The final combined follow-up is pushed for review/validation at
ddc78606998ea8aee589941c6ab6cae76a80440a on qa/t3657-t3658-current-dev-keyboard, tree
fa70a0164ccbef670529470937b170677c5a99b0, sole parent b1f507400. It incorporates current
DEVc676aa2f and the keyboard ownership repair described in T3658. All current DEV data,
assets, generators and stamped changelog remain exact; parent budget/harness pins remain.

Full published-renderer groups are queued: desktop1–4 run44426888539,6–12 run44426953188,
13–15 run44426968208, mobile1–15 run44426984452. Historical b501 desktop5 passed30/0 and
13 passed157/0. Only stage5 is retained under a precise proof of identical1835 geometry,
detail policy and direct API behavior; its original source attribution remains. New
keyboard behavior and fresh boot/error checks are covered separately. Source6ee parts
2/3/6/7 passed; its remaining wholly queued parts were cancelled. No incomplete source
gate is treated as green. Final source/moving/upload gates remain required.

After parent #2197 squash/fold, apply the normalized b1-to-ddc patch onto actual DEV and
verify the resulting input differences. Do NOT replay the raw old history or invoke the
03ecd-based changelog merge driver: review proved it can unstamp shipped upstream entries.
Preserve DEV's folded changelog and removal of T3656.json; retain only T3657's entry for
this PR. Exact patch/provenance: /tmp/t3657-t3658-current-dev-keyboard/combined.patch and
provenance.json; remote candidate is the durable copy. If DEV advances again, preserve its
new inputs and validate affected coverage before reuse. Evidence through native keyboard
validation is pushed at chicago-evidence dae64772938ce55ec15cb4bb9dbc0f1c9c6d4ae2.
PR body links the candidate and records the remaining gates. No DEV merge yet.

## Previous recovery checkpoint — 18 November 2026

Dependent draft PR #2199 targets DEV at pushed head
4a2ee67dcbc3067fd8e18fb432098822361f2476 on steward/t3657-t3658-hunt-accessibility.
Final native published tests passed both 390x780 and 1280x800 on feature commit
5674d33d: all five real photograph responses, guards for all destinations, actual Glessner
arrival, distance score, share/reload, notebook/photo integration, and one hunt image per
visible view. Photo date/range and rights were checked against actual source records and
images. Zero page/HTTP errors or overflow; expected request cancellations are recorded
separately. Fixed hidden-image retention, lazy stylesheet loading, and the stale Loading
status after an answered photograph. Focused regression fixtures passed.

Subsequent commits port the parent PR's authorized Full allowance and CI cap only.
Preflight passed 89 source checks in part 1/16 plus changelog/ID metadata; the other
partitions and full renderer gates remain required. Source CI 44407002205 and moving/upload
44407002229 were queued at this checkpoint. Evidence through the final native runs is in
chicago-evidence commit 477191a886b285f53eda33703b8d24f52e116517.

Merge #2197 first when green. Then rebase only commits after boundary
03ecd9678e15988abe44c50e27c2bd9fec569530 onto actual DEV, dropping duplicate parent fixes
and retaining the upstream folded changelog. Finish gates and merge #2199 when green.
The user explicitly authorized periodic PRs and green DEV merges. No new server or
production promotion; no complete WCAG or physical-device certification is claimed.
