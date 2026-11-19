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

## Current recovery checkpoint — 19 November 2026, 01:38 UTC

Dependent draft PR #2199 remains in review at
`6ee1a689077839dd9923edbc80269dd2cbaccfb6`, pending parent #2197. Normalized QA
`ddc78606998ea8aee589941c6ab6cae76a80440a` is pushed on
`qa/t3657-t3658-current-dev-keyboard`, tree `fa70a0164ccbef670529470937b170677c5a99b0`,
sole parent b1. It preserves current DEV c676 data/assets/generators/stamped
changelog and parent policy/harness pins, with the T-3658 keyboard repair.

Exact ddc published desktop **1–4 passed 320/0 in 38m29s**, run44426888539:
307 staged checks plus 13 always-on checks once for the whole group, with
complete final suite, zero-page-error and vendor assertions. Desktop 6–12
(44426953188), desktop 13–15 (44426968208) and mobile 1–15 (44426984452) are
active at this checkpoint; no partial group counts as passed. Historical b501
desktop 5 is retained only under the documented unchanged-1835 geometry,
detail-policy and direct-API proof; it is not fresh ddc or keyboard validation.

The isolated local ddc source gate completed **part 1/8 PASS175**, including
63 self-tests. Its original shell-exit receipt was lost at compaction; the
complete final CHECK PASS is present, so no exit code is invented. Receipt:
`/tmp/t3657-ddc-source-part1of8.log`, SHA256
`ffab42c3b5fb9de8e89e11dc768f89362d031c6386e9be93ebbad872d6a28b39`;
provenance: `/tmp/t3657-ddc-source-provenance.json`. All eight parts, preflight
and final integrated-head source/moving checks remain required. The active
validation worktree and its separate tickets clone must remain undisturbed.

Parent renderer coverage is complete under its scoped retained/fresh matrix,
and moving/upload passed; parent source attempt 2 has only part 4 green.
Parts 2/6/8 have runners, 1/3/5/7 are queued, and aggregate remains pending.
[Evidence46910da](https://github.com/kevinrhaas/chicago-evidence/tree/46910daedcd6f68a9b07f50d58328c21c16207a4/evidence/t3657-t3658-hunt-accessibility-2026-11-18) preserves
completed ddc/native/keyboard receipts and the primary matrix separately.

After #2197's actual squash/fold, apply the normalized b1-to-ddc contribution
onto actual DEV, preserving its folded changelog and removal of T-3656.json;
retain only this PR's T-3657 entry. Do not replay raw old history or the unsafe
03ecd-based changelog merge driver. Compare the resulting runtime/data and
any new DEV inputs before reusing coverage, then complete affected renderer
and final source/moving gates. The [normalized patch and provenance](https://github.com/kevinrhaas/chicago-evidence/tree/46910daedcd6f68a9b07f50d58328c21c16207a4/evidence/t3657-t3658-hunt-accessibility-2026-11-18/current-dev-keyboard)
are durable. Neither PR has merged; keep both tickets in review.

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
