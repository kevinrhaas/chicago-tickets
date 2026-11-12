---
id: T-3551
title: 1812 seasonal nature, dirt and snow hoofbeats, and visible work sounds
state: review
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-11
closed: null
pr: 1934
claimed_by: run 11/11/2026, 2:19:06 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-11T20:19:08.295Z
decision: null
decision_answer: null
---

1812 seasonal nature, dirt and snow hoofbeats, and visible work sounds.

**Owner request:** Fill 1812 nature first; add hoofbeats appropriate to mostly dirt or snow and visible work sounds. Activities and sounds vary by season. Improve 1904 afterward.

**Acceptance:**
- 1812 has recorded nature selected by its live habitat, viewing season and time of day; summer insects do not play in winter. Existing 1835 nature rules remain intact, and 1904 is not silently activated.
- Hoof sounds follow actual moving, visible 1812 horses and measured gait events. Dirt uses recorded dirt-road steps; snow uses an explicitly declared damped recorded proxy matched to the renderer's snow state. No autonomous beat loop or silent substitution of synthetic effects.
- At least one visible, appropriate 1812 work action has a corresponding recorded sound at its actual tool/contact location. Actor/date/hour/season eligibility, Stop/hidden/mute behavior and action timing agree. Default 1812 must have a demonstrable work activity, not only an off-date candidate.
- Bounded voices, retained/transient decoded memory and lazy network behavior are measured; recordings already hosted may be reused. Rights and reconstruction provenance remain explicit; no unperformed listening review is claimed.
- Focused real-browser playback and visual checks at phone/desktop sizes, required local gates and published scene checks pass. Commit/push recoverable code, create a PR and merge only DEV when green; verify deployed behavior.

**Scope:** 1812 first. Voices/narration and broad 1904 expansion remain subsequent work. The owner's earlier authorization allows reconstructed proxies and concurrent DEV merges.

## Owner hold and recovery handover — 2026-11-11

Owner requested stop and HOLD on 2026-11-11 to preserve context; do not resume or merge PR #1934 until explicit owner release.

PR https://github.com/kevinrhaas/chicago/pull/1934 remains open DRAFT with `hold`; repository automation must skip it. Work is not complete and has not merged to DEV. Do not reopen/reclaim/rebuild this work automatically.

Code committed and pushed through `c5de44a61e8cd0c254e4d213f5ecd1046cbe4000` on `steward/1812-seasonal-audio`; application worktree clean. Local gate parts 1–3 pass; part 4 and two desktop close visual views remain. Current-head hosted gate, moving frames, portable humans and mobile stage 13 pass; desktop stage 13 was running at hold. Both phone close views accepted. No local work processes remain.

[Full handover, exact resume sequence and evidence](https://github.com/kevinrhaas/chicago-evidence/blob/a4c875a851848ec3e2d035c687c9bc439ff05ec6/evidence/1812-audio-2026-11-11/HANDOVER-HELD.md). The same evidence commit includes a recovery archive (helpers, logs, receipts, chronology, 1904 read-only notes) and the approved phone images. No new R2 upload needed. Resume only after owner explicitly releases hold; finish required checks and visual review before DEV merge, then verify deployed DEV. Never promote MAIN as part of this ticket.

## Owner resumed — 2026-11-12

The owner explicitly released the hold and requested completion, periodic recovery commits, and green DEV merge. Earlier hold instructions are historical and superseded. PR1934 is draft while final local/visual validation runs. Hosted desktop13 passed; all 18 source-qualified renderer runs now pass. DEV advanced with PR1933 and PR1935; integrating those before final validation. No new feature scope.
