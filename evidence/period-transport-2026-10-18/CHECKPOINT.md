# Session recovery checkpoint — 2026-10-18

Code repository: `kevinrhaas/chicago`, branch `steward/period-transport-2793`.
Latest transport commit: `1b3c73d22016596d07b133019df24422c2b54790` (merged dev `7d5daca7d82748acce0fda541c638b260bdd3be4`).
Previous modeling checkpoint: `6b51f65ca01921cfcdf447566774205671aca43d`.
First checkpoint: `7c61614c8f197e42da3720f6628d62722f6a560e`.

Start with `chicago/4d/docs/RESEARCH/period-transport-2026-10-18/README.md` in that commit. It records regeneration, inspection, browser checks, source limitations and next work. The transport collection is at `renderers/web/transport/`; it includes articulated wagon and carriage, a genuinely skinned horse with idle/walk, modular breastcollar harness, and a coupled moving hitch fixture. Generators, parameters, GLBs, screenshots, test receipts and compressed hitch observations are committed together.

Validation before commit: clean full `tools/check.sh` passed all 971 steps, exit 0 (374 intentional self-tests). All four GLBs passed independent Khronos validation with zero errors/warnings; regeneration matched bytes. Desktop/mobile specimen and hitch checks passed. Actual skinned sole vertices were sampled over 1,001 walk frames; compensated stance drift is now 0.0201 mm (first checkpoint 6.43 mm). These checks establish development-study behavior, not photographic or historical production acceptance.

No production ticket is closed. T-2792/T-2799 research and T-2793/T-2794/T-2800/T-2801 models/gear are started. T-2795 coupling is partially explored. Preserve queue bands 8D/8E below portable humans. Continue source-plate and measured-construction review, anatomical/material quality, harness routing and robust fit margins (former 45 mm shaft-loop mismatch resolved by reconstructed tugs; breastcollar/upperlimb sampled margin only 0.589 mm), LODs and collision qualification before town traffic, riders or boarding. Carriage/hitch motion now reads exported dimensions and stride, verified by metadata perturbation and actual wheel-center travel. Changes to geometry still require renewed fit checks. Existing static town wagons remain intact.

Research reports here distinguish inspected photographs, actually read OCR, and unread catalog/plate leads. Pullman ownership is unproven. Stubbs edition metadata is `1766 [i.e. 1815?]`; plates remain unseen. OCR component dimensions are not page-verified measurements.

GitHub API access recovered. Draft PR [#1041](https://github.com/kevinrhaas/chicago/pull/1041) targets dev at exact transport head `1b3c73d22016596d07b133019df24422c2b54790`. The owner explicitly authorized merging to dev once all checks are green. Keep it draft until the full desktop/mobile smokes and required checks pass; then ready and merge that exact head. Production promotion is outside this authorization. Do not bypass the proxy.

## Follow-up recovery

Read [fit-followup.md](fit-followup.md) for the second checkpoint. Its exact full precommit gate passed 971 steps, none red, exit 0; local log `/tmp/transport-followup-check-complete.log`. Horse silhouettes/gait, physical tugs, actual front-turntable rolling and collar fit are refined. Full triangle checks replaced misleading nearest-face signs in the limb test. Corrected and failed receipts are preserved. No photographic, continuous-collision, animal-suitability, braking/holdback or production scene acceptance is claimed.

## Active validation and human work (21:40 UTC)

The exact merged-tree local preflight passed 972 steps, none red. Published fixed
desktop stage 1 passed 95/0; other interrupted earlier runs retain their failures and
are not full passes. The existing smoke harness cold device probe now runs before
the first town render; timing limits and application device behavior are unchanged.
Full desktop smoke [39164186323](https://github.com/kevinrhaas/chicago/actions/runs/39164186323),
full mobile [39164260098](https://github.com/kevinrhaas/chicago/actions/runs/39164260098),
are still running on that exact head. Fast gate
[39164182373](https://github.com/kevinrhaas/chicago/actions/runs/39164182373) passed.
Seventeen of nineteen PR checks have completed without failure; no full CI smoke
pass is claimed while the two full browser runs remain in progress.

Local code checkout is now on `steward/generic-teamster-humans`, branched from
transport head1b3c73d. T2672 policy, T1789 body preparation/canonical builder, and
T2823 documented anonymous-fallback mechanics are committed and pushed at
**e6f72ceb489dd625554dcabdbaced064c0b7e214**, draft
[PR1046](https://github.com/kevinrhaas/chicago/pull/1046). Full preflight passed:
973 check.sh steps, zero failed, plus changelog and ticket-ID checks. The postcommit
changelog check also passed. No local Blender was run. Canonical human workflow
[39168738942](https://github.com/kevinrhaas/chicago/actions/runs/39168738942) was
dispatched with build_teamsters=true on that exact SHA and is running. Download
its actual artifacts and inspect them before accepting model quality. The owner subsequently directed
existing attested/inferred/reconstructed people first, anonymous only if no choice.
The first actual references are existing reconstructed 1835 residents
`rc_bardwell_otis`, `rc_dufresne_joseph`, `rc_flynn_martin`. Do not fabricate new
resident biographies, backdate 1839 occupations, or claim photographic likeness.

Read code `docs/RESEARCH/resident-teamsters-2026-10-18/README.md` for the canonical
CI build route, output IDs and remaining acceptance. Blender is forbidden locally;
CI outputs must be downloaded, independently inspected and then checked/committed.
No new scene placements, seated driver, actual riding tack, photographic human,
or production ticket completion has occurred. The original official CC0 Toigo bronze2048² PNG and exact source receipts are
ingested and packed by the builder. No fabricated4K/detailmaps or portrait
likeness is claimed. Its actual Blender/glTF appearance remains pending the CI
output. Upstream source bytes are pinned; LICENSE.md.gz preserves its original
notice bytes exactly and is hash-verified before preparation.
