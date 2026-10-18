# Session recovery checkpoint — 2026-10-18

Code repository: `kevinrhaas/chicago`, branch `steward/period-transport-2793`.
Commit: `7c61614c8f197e42da3720f6628d62722f6a560e` (based on `dev`).

Start with `chicago/4d/docs/RESEARCH/period-transport-2026-10-18/README.md` in that commit. It records regeneration, inspection, browser checks, source limitations and next work. The transport collection is at `renderers/web/transport/`; it includes articulated wagon and carriage, a genuinely skinned horse with idle/walk, modular breastcollar harness, and a coupled moving hitch fixture. Generators, parameters, GLBs, screenshots, test receipts and compressed hitch observations are committed together.

Validation before commit: clean full `tools/check.sh` passed all 971 steps, exit 0 (374 intentional self-tests). All four GLBs passed independent Khronos validation with zero errors/warnings; regeneration matched bytes. Desktop/mobile specimen and hitch checks passed. Actual skinned sole vertices were sampled over 1,001 walk frames; compensated stance drift was 6.43 mm. These checks establish development-study behavior, not photographic or historical production acceptance.

No production ticket is closed. T-2792/T-2799 research and T-2793/T-2794/T-2800/T-2801 models/gear are started. T-2795 coupling is partially explored. Preserve queue bands 8D/8E below portable humans. Continue source-plate and measured-construction review, anatomical/material quality, harness routing and socket fit (45 mm shaft-loop gap remains), LODs and collision qualification before town traffic, riders or boarding. Carriage/hitch preview equations currently assume default dimensions and stride; generalize them before changing parameters. Existing static town wagons remain intact.

Research reports here distinguish inspected photographs, actually read OCR, and unread catalog/plate leads. Pullman ownership is unproven. Stubbs edition metadata is `1766 [i.e. 1815?]`; plates remain unseen. OCR component dimensions are not page-verified measurements.

Git transport works. GitHub API access returned proxy CONNECT 403, so no PR is claimed; open a PR into `dev` when API access is available. Additional archive/network rules and tested environment installation/start instructions are saved in the environment draft; saved rules do not establish live access. Do not bypass the proxy. Do not merge or publish to production as part of recovery.
