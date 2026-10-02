---
id: T-1999
title: Rebuild Glessner west elevation and correct north openings from owner references
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: null
pr: null
claimed_by: glessner-elevation-repair 10/2/2026, 3:28:31 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-02T20:28:31.038Z
decision: null
decision_answer: null
---

Rebuild Glessner west elevation and correct north openings from owner references.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 250 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner explicitly requested this repair and immediate work, 2026-10-02.

**Acceptance:**
- Rebuild the west elevation to the owner-supplied straight elevation (image(2).png), checking against the archival northwest photo (image.png): asymmetric high front gable, lower continuous rear gable roof, four evenly spaced rear openings, two large lower front windows and two upper slits, course schedule, gutters/downpipes, squared dormer hood and finial without a center post or added rear chimney.
- Align the stable turret with the high gable peak in a true west view, including the later Untitled.png correction. Preserve coherent three-dimensional roof joins and the solid south gable.
- Reconcile the north window heads with the measured eave, eliminating protruding frames/trim. Assess the north carriage doors, loft door, stone projection and recessed entrance against the docs and archival image; correct demonstrated discrepancies.
- Record owner-directed reconstruction separately from measured historic evidence. Regenerate canonical full/light assets, inspect exact published derivatives at desktop/mobile sizes, and independently compare north/west/northwest/south-courtyard renders against references. Source and applicable browser gates pass; checkpoint branch is pushed during work; PR targets dev.

References: owner attachments of 2026-10-02, HABS IL-1015 and the existing Glessner source dossier. Supersedes conflicting rear-roof height assumptions in T-1833; source photo pixels are not used as textures.

## Recovery checkpoint — 2026-10-02

Owner instruction: commit and push intermediate work so a failed session can be resumed elsewhere.

- Recovery branch: [checkpoint/t-1999-glessner-20261002](https://github.com/kevinrhaas/chicago/tree/checkpoint/t-1999-glessner-20261002)
- Saved commit: [1460fe5](https://github.com/kevinrhaas/chicago/commit/1460fe5f16571af2fa151687ab83ff7e4e59d7d7)
- [Handoff and resume steps](https://github.com/kevinrhaas/chicago/blob/checkpoint/t-1999-glessner-20261002/chicago/4d/docs/RESEARCH/glessner-elevation-rebuild/RECOVERY.md)
- Preserves the north working tree's four source files, five owner reference review copies with original SHA-256 hashes, and QA scripts. Snapshot base: 10bd9c07e7bf1e02dd0344315aaa435a980167d0.
- This is unvalidated work in progress, not a completed model or ready-to-merge PR. Roof/west/tower reconstruction, regenerated assets and validation remain.
- Continue substantive checkpoints during the repair. Before resuming, compare the active branch `steward/t-1999-glessner-elevation-rebuild` and current PRs against this snapshot to avoid overwriting newer work.

Second checkpoint: [525a3cf](https://github.com/kevinrhaas/chicago/commit/525a3cf7cf78172e96dd4adba66156d9a56e3a3e) on the same recovery branch now includes complete patches for the integration, north and roof working trees, including untracked files. Each patch was verified to apply against its recorded base. The handoff explains how to restore each workstream separately and reconcile shared files. Implementation, bake and visual gates are still pending.

Third checkpoint: [010f213](https://github.com/kevinrhaas/chicago/commit/010f2130bd9e807c8d9a75f2a34a8c0d53955c99) on [steward/t-1999-glessner-elevation-rebuild](https://github.com/kevinrhaas/chicago/tree/steward/t-1999-glessner-elevation-rebuild) now preserves the integrated north/west/turret reconstruction, exact full/light asset archive and rendered review evidence. Full and corrected light pass 186 aperture probes each with zero obstruction hits; the roof envelope passes 1,800 samples, including a new reduced ridge-cap regression. Final source preflight and published desktop/mobile browser checks are still running; this checkpoint is not a merge-ready claim. Continue from this active branch ahead of the earlier patch snapshots.
