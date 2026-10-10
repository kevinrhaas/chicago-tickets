# T-2206 — merged and live verification, 2026-10-10 UTC

[PR #604](https://github.com/kevinrhaas/chicago/pull/604) merged to dev as `04d9e55dc5c026f7bd74e06337970bfa94180a8e`. [Open the audit](https://chicago.polecat.live/4d/dev/walk/glessner-baseline.html#proportion-audit).

The reviewed PR and merged dev commit have the identical tree `658f2781cfbcd501f8ac46aa24c7fc8a4edaebc8`. Local preflight and GitHub's PR gate pass all **806 steps**, including 330 self-tests. PR movement/GPU checks also pass. Exact results and run links are in `pr-checks.json`, `github-gate.txt` and the preflight receipts.

`live-build.json` confirms the deployed dev revision `04d9e55d`. The successful Pages deployment runs from the unchanged production branch and assembles the dev preview; its workflow head therefore differs from the preview revision. This is the normal two-tier publishing pipeline, not a production promotion.

## Live browser proof

`live-browser.log` records **PASS at 1280×800 and 390×780** against the deployed origin. Both exercise all nine comparisons, unchanged cameras, historical/current measurement switching, deliberately stale-asset refusal, 15 dimension rows, source pixel dimensions and rights, Python/Three projection agreement, Full/Light hashes, markers and the actual 1904 house-card link. No horizontal page overflow or browser errors.

- [Desktop reference comparison](1280-north-inclined.png)
- [Mobile reference comparison](390-taylor-ne.png)
- [Dimension table](1280-audit.png)

No restricted reference pixels are included. The three model assets are unchanged by this audit. Six camera tests and 3,000 existing roof-envelope rays pass. The applicable local published stage-12 smoke passed 200 checks with no failures or page errors; it predates the inherited 1835 integrations and is not claimed as the entire fourteen-stage smoke. The live comparison checks above cover the deployed revision.

## Scope and remaining findings

T-2206 is a verify-first audit, not photographic acceptance. Current roof, dormer and courtyard-bay geometry is retained. The main-roof and stair-turret height disagreements remain explicit, with source confidence and the missing controls needed to resolve them. The corrected dining-bay reviewer description is 9.90 ft projection. The northeast copper fold remains in manually held T-2220, and T-2228 retains final photographic sign-off. No other Glessner manual ticket is activated.

[Full research dossier, dimension controls, source identities and before/after evidence](https://github.com/kevinrhaas/chicago/blob/dev/chicago/4d/docs/RESEARCH/glessner-proportions-2206/README.md).
