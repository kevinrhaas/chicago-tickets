# T-2204 — live dev verification

[PR #594](https://github.com/kevinrhaas/chicago/pull/594) merged into **dev** at
2026-10-09 21:56:49 UTC, commit `1b7f7470f9e6c80eae511aa13c5565d95b7dd640`.
[Live 1904 preview](https://chicago.polecat.live/4d/dev/1904/).
Main was not promoted; its SHA remained `31768a188aa65c22c8e204e0aa0755fb890bc50f`.

The actual deployed 1904 app passes normal boot and northeast roof inspection in
Full desktop (1280×800) and Light mobile (390×780): zero page errors, failed
requests or budget overruns; exterior glass remains dark. Screenshots were
visually reviewed. The served Full/Light GLBs and both affected renderer modules
match the reviewed implementation byte for byte: see `served-shas.json`.
`build.json` records the deployment and `browser-validation.json` records the
browser observations. These are software-browser checks, not phone hardware FPS.

The final combined tree passes **806 checks**, with the committed-range changelog
and ticket-ID checks also passing. The implementation review already includes
70 moving/pullback captures, six detail switches and the 36-pass stage-8 shared
renderer regression. [Implementation dossier](https://github.com/kevinrhaas/chicago/blob/1b7f7470f9e6c80eae511aa13c5565d95b7dd640/chicago/4d/docs/RESEARCH/glessner-roof-filtering-2204/README.md).

The first CI movement run on the preceding integration had one 1835 foliage
frame at 63.2 ms against a 60 ms ceiling. Its rerun passed without changing code
or thresholds; the failure transcript is retained here. Final-head CI is recorded
separately when it completes.

All other manually held Glessner work remains held. In particular, the folded
copper connector remains T-2220; this tile-sampling pass does not repair it.
