# T-2198 implementation receipts

[Delivery PR #549](https://github.com/kevinrhaas/chicago/pull/549), targeting **dev**.
The source-review findings are committed with the library at
`chicago/prairie_1904_v1/docs/glessner-source-review.md`.

- `source-integrity.json`: all 168 original IDs, rights, local-copy metadata and source URLs preserved; previous changed fields match baseline exactly; four Florian filenames checked against the corrected subjects.
- `browser.log`: nine representative image-detail records, each at 1280×800 and 390×780. Correct captions, history, exclusions, family navigation, unavailable-image status and link-only rights; no page errors or horizontal overflow.
- `grid.log`: all 171 Glessner records displayed at both widths; no horizontal overflow; disputed-attribution search returns exactly one record.
- `desktop-quarantine.png`, `mobile-quarantine.png`: the source-use restriction in the published library. Screenshots are unmodified.
- `smoke-mobile.log`: published app stage 12, 101 checks passed. This is the part selected by `smoke_budget.mjs --for-diff` for the changelog; it is not a claim to have rerun all 14 renderer stages.
- `smoke-desktop.log`: idle rerun of published stage 12; 101 checks passed, zero page errors.
- `smoke-desktop-startup-timeout.log`: first desktop stage-12 attempt, retained as failed. It ran during concurrent checks and timed out before the scene became ready; zero page errors. The later idle rerun is recorded separately.

Local repository gate: 792 steps passed. `tools/preflight.sh` passed all three gates.
Library: `python3 tools/validate.py` passed, including the six tests in
`tools/test_evidence_review.py`. Desktop and mobile stage 12 each passed 101 checks. CI results are on the delivery PR.

No geometry or source-image bytes were added or changed. Three new records link to
museum-hosted Florian photographs with copyright/link-only rights. The 17 inaccessible
records remain catalog-only; the other 30 programme tickets remain on manual hold.
