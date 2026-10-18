# Session recovery checkpoint — 2026-10-18

Code repository: `kevinrhaas/chicago`, branch `steward/period-transport-2793`.
Latest commit: `6b51f65ca01921cfcdf447566774205671aca43d` (based on `dev`).
First checkpoint: `7c61614c8f197e42da3720f6628d62722f6a560e`.

Start with `chicago/4d/docs/RESEARCH/period-transport-2026-10-18/README.md` in that commit. It records regeneration, inspection, browser checks, source limitations and next work. The transport collection is at `renderers/web/transport/`; it includes articulated wagon and carriage, a genuinely skinned horse with idle/walk, modular breastcollar harness, and a coupled moving hitch fixture. Generators, parameters, GLBs, screenshots, test receipts and compressed hitch observations are committed together.

Validation before commit: clean full `tools/check.sh` passed all 971 steps, exit 0 (374 intentional self-tests). All four GLBs passed independent Khronos validation with zero errors/warnings; regeneration matched bytes. Desktop/mobile specimen and hitch checks passed. Actual skinned sole vertices were sampled over 1,001 walk frames; compensated stance drift is now 0.0201 mm (first checkpoint 6.43 mm). These checks establish development-study behavior, not photographic or historical production acceptance.

No production ticket is closed. T-2792/T-2799 research and T-2793/T-2794/T-2800/T-2801 models/gear are started. T-2795 coupling is partially explored. Preserve queue bands 8D/8E below portable humans. Continue source-plate and measured-construction review, anatomical/material quality, harness routing and robust fit margins (former 45 mm shaft-loop mismatch resolved by reconstructed tugs; breastcollar/upperlimb sampled margin only 0.589 mm), LODs and collision qualification before town traffic, riders or boarding. Carriage/hitch motion now reads exported dimensions and stride, verified by metadata perturbation and actual wheel-center travel. Changes to geometry still require renewed fit checks. Existing static town wagons remain intact.

Research reports here distinguish inspected photographs, actually read OCR, and unread catalog/plate leads. Pullman ownership is unproven. Stubbs edition metadata is `1766 [i.e. 1815?]`; plates remain unseen. OCR component dimensions are not page-verified measurements.

Git transport works. GitHub API access returned proxy CONNECT 403, so no PR is claimed; open a PR into `dev` when API access is available. Additional archive/network rules and tested environment installation/start instructions are saved in the environment draft; saved rules do not establish live access. Do not bypass the proxy. Do not merge or publish to production as part of recovery.

## Follow-up recovery

Read [fit-followup.md](fit-followup.md) for the second checkpoint. Its exact full precommit gate passed 971 steps, none red, exit 0; local log `/tmp/transport-followup-check-complete.log`. Horse silhouettes/gait, physical tugs, actual front-turntable rolling and collar fit are refined. Full triangle checks replaced misleading nearest-face signs in the limb test. Corrected and failed receipts are preserved. No photographic, continuous-collision, animal-suitability, braking/holdback or production scene acceptance is claimed.
