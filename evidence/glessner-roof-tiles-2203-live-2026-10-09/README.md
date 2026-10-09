# T-2203 live dev verification

PR [#583](https://github.com/kevinrhaas/chicago/pull/583) merged to dev as `8d3faca666fe462725d23fa13a4fedefd0c46117`. The public `/4d/dev/build.json` reports `8d3faca6`; both served Glessner assets match the reviewed local SHA-256 hashes.

The normal live [1904 app](https://chicago.polecat.live/4d/dev/1904/) passed six fixed views in Full/desktop (1280×800) and Light/mobile (390×780), with zero page errors or failed requests, dark glazing preserved, and all views inside their existing budgets. `browser-validation.json` contains all twelve view receipts; the two screenshots here are representative captures. These are static surface checks, not a frame-rate certification.

[Source review, before/after gallery, physical coverage, and browser logs](https://github.com/kevinrhaas/chicago/blob/8d3faca666fe462725d23fa13a4fedefd0c46117/chicago/4d/docs/RESEARCH/glessner-roof-tiles-2203/README.md). Final preflight: 804 checks passed, plus PR-event checks. Published mobile stages 3 and 12–13: 308/0; published desktop stage 13: 126/0. GitHub's gate and moving-frame checks passed on the merged PR head.

T-2204 still owns distance moire/filtering. T-2220 still owns the owner's lifted/folded NE courtyard copper; it is visible in this courtyard capture and is not claimed fixed. All 26 other manual Glessner audit holds remain blocked-owner, with commented queue entries. Main remains at `31768a188aa65c22c8e204e0aa0755fb890bc50f`; this work was staged to dev only.
