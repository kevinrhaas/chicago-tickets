---
id: T-2202
title: Glessner: restore Prairie frontage curbs, thresholds and ground contact
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: 2026-10-09
pr: 578
claimed_by: run 10/9/2026, 9:22:56 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-09T16:21:44Z
claimed_run: null
claimed_at: 2026-10-09T14:22:56.906Z
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Audit item:** GA-04 • **Priority:** P1 • **Basis:** Confirmed visible gap

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

Grass runs directly to the main door and through the porte-cochere in the current captures. The characteristic rounded stone edge/access gaps are absent.

Model the house-side grass-strip curb, entry approach, stone thresholds and carriage passage surface. Tie grades to surveyed/HABS datums and period photos; coordinate public sidewalk ownership.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Main door and porte access have continuous credible surfaces, no grass through the passage.
2. Curved curb sections and access gaps agree with period views, with joints and end returns.
3. No floating, buried or z-fighting thresholds at street-eye level.

## Evidence

- Audit #008: [Glessner, John J., Residence (1800 S. Prairie Ave.) — view from NE (J. W. Taylor #2135)](https://artic.contentdm.oclc.org/digital/collection/mqc/id/28805) — `a18-rba-taylor-2135-glessner-ne`; c. 1889 (RBA); likely 1887–88; visually inspected. Rights: public domain.
- Audit #013: [Glessner House Prairie Avenue front, with the O. R. Keith house (1808) at far left](https://glessnerhouse.blogspot.com/2022/12/the-original-odd-quaint-queer-dutch.html) — `a18-gh-glessner-front-with-keith`; undated (probably 1890s–1920s); visually inspected. Rights: unknown — link only.
- Audit #107: [Porte cochere doors (photograph by George Glessner, about 1888)](https://www.glessnerhouse.org/porte-cochere-doors) — `a18-gho-porte-cochere-doors-c1888`; about 1888; visually inspected. Rights: pending — permission requested.
- Audit #115: [Front elevation](https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060904p) — `a18-glessner-habs-photo-02`; c. 1923 (copied for HABS); visually inspected. Rights: unknown — link only.
- Audit #144: [2. First floor plan - John J. Glessner House, 1800 South Prairie Avenue, Chicago, Cook County, IL](https://www.loc.gov/resource/hhh.il0118.sheet/?sp=2) — `a18-glessner-habs-sheet-2`; 1963; visually inspected. Rights: no known restrictions.

**Current audit views:** entry, porte, prairie. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2200](../T-2000-2249/T-2200-glessner-establish-a-dated-camera-matched-exterior-acceptanc.md)

Coordinate T-1728 street/sidewalk scope and T-1745 legal-lot datums. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## T-2199 retrieval finding — 2026-10-09 UTC

IIT 1945 shows continuous low boundary stones and front ground interfaces; Cornell ca.1887 shows construction-period ground disturbance and temporary frames. Neither date alone proves the 1904 pavement/curb arrangement. NRHP photo 4 (1972, PDF pp.32–33) shows later street conditions and must remain a separate phase.

[Retrieval report and photographic brief](https://github.com/kevinrhaas/chicago/blob/dev/chicago/prairie_1904_v1/docs/glessner-reference-recovery.html). This is evidence handoff only; the owner scheduling hold remains in force.

## Owner selection — 2026-10-09 UTC

> Take 2202 next

T-2202 alone is released for implementation and merge to dev. All other held Glessner audit tickets retain their scheduling holds. T-2200 is done in PR #561; T-1728 is done in PR #187; T-1745 is split and its legal-lot datum work will be read without changing public street ownership.

## Implementation and review — 2026-10-09 UTC

Pinned Blender 4.5.3 bake and full/light derivatives are complete. The record now generates rounded house-side stone edging and returns, two access gaps, entry paving/risers, a stone porte threshold and continuous passage paving to the courtyard drive. Source/tier/datum bounds are in `prairie_frontage` and L-glessner-frontage-2202; T-1728's public street/sidewalk geometry is unchanged. Existing roof, glazing and older comparison versions are preserved.

Dedicated published desktop/full and mobile/light reviews pass, including nine ground-contact rays per detail level, 1,108 numerical access samples and dark-glass/scene-budget checks. Light remains at 199,880 triangles under the unchanged 200,000 ceiling. T-2200's 87 landmark residuals remain unchanged to 0.001 px with frozen cameras. Before/after evidence: `docs/RESEARCH/glessner-frontage-2202/` on branch `steward/t-2202-glessner-frontage`.

First repository preflight passed 801/802 steps. Its sole failure is the inherited withdrawn T-2242 order-book pointer, already assigned to another live run as T-2248. Waiting for that repair while affected published smoke stages 12/13 run; no assertion is weakened and no other Glessner hold is released. This is not a claim of complete whole-house photographic acceptance.


## Completion and live-dev verification — 2026-10-09

Completed and merged to **dev** in [PR #578](https://github.com/kevinrhaas/chicago/pull/578), squash commit `c07c00eafd40dedd25e761d6c40c7653422973ff`. The final PR head `9651832fd799bd5a96734029299609f095e699a5` passed GitHub's repository gate, moving-frame performance check and report check before merge. Main was not promoted.

[Review evidence](https://github.com/kevinrhaas/chicago/tree/c07c00ea/chicago/4d/docs/RESEARCH/glessner-frontage-2202) includes matched before/after desktop/mobile views, asset hashes, frozen-camera comparison and validation receipts. Final local preflight passed all 802 checks, including after integrating T-2247. Published smoke stages **12–13 only** passed 216 checks per viewport with zero failures/page errors. Their actual timings and the desktop run's integration overlap are stated in the report; this is not a full fourteen-stage or frame-rate claim.

[Pages deployment 37958996420](https://github.com/kevinrhaas/chicago/actions/runs/37958996420) succeeded. The [live dev 1904 scene](https://chicago.polecat.live/4d/dev/1904/) reports build `c07c00ea`. Fresh live desktop/full (1280×800) and mobile/light (390×780) reviews both passed: four street-eye views each, zero page/network errors, nine ground-contact rays per detail level, dark glass retained and all stands within existing draw/triangle budgets. Maximum ground-height disagreement after compression is 0.311 mm.

The live files match the tested bytes exactly:
- Full: `5f8e6949250271f15a16881c4782cc1276f5e39731f69390fb118410d3524606`.
- Light: `f21117394c5826374cdb60671a2238add890ef6fbd9ba5b86b1a4fa1a00ce97e` (199,880 triangles; unchanged 200,000 ceiling).

This completes GA-04's frontage/access/ground-contact work. Historical material/profile/joint uncertainties remain explicitly reconstructed; T-2200's frozen photographic exceptions are unchanged. All 27 unselected audit tickets (T-2201 and T-2203–T-2228) remain blocked-owner and commented in their manual group.
