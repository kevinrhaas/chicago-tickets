---
id: T-3609
title: dev's 1835 boot payload measures 45.429 MB over its 45.2 MB budget (1237 requests) since T-3556's townspeople (#2088), which reds smoke (desktop, 1-2) in every PR's content build — measure what grew since T-3599's 44.936 reading and re-budget or cut
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-15
closed: null
pr: 2095
claimed_by: run 11/15/2026, 8:44:21 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43792773193
claimed_at: 2026-11-16T02:44:22.124Z
decision: null
decision_answer: null
---

dev's 1835 boot payload measures 45.429 MB over its 45.2 MB budget (1237 requests) since T-3556's townspeople (#2088), which reds smoke (desktop, 1-2) in every PR's content build — measure what grew since T-3599's 44.936 reading and re-budget or cut.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found 2026-11-16 by the steward lapping #2062 (T-1896).** The content build's desktop `1-2`
leg reds on `node tools/measure_boot_payload.mjs --check` with **BOOT PAYLOAD OVER BUDGET:
45.429 MB > 45.200 MB, 1237 requests**, and reads the same to the byte on two unrelated 1904
PRs whose branches had merged dev through ~00:45Z on 2026-11-15/16:

- #2062 (T-1896, 1827 Prairie) — run 43782254713, job 133028989365
- #2080 (T-1935, 1912 Prairie) — run 43781261707, job 133027180647 (merged into dev at 02:38Z regardless)

dev's own content build at 23:26Z (run 43774799715, job 133005926899) read **45.092 MB, 1235
requests — within budget**. Between the two readings the breakdown moves only in the people's
records (`.json` 3.392 → 3.727 MB): `/data/humans/web/` 0.810 → 0.940 MB (3 → 4 files) and
`/data/humans/` enters the 15 heaviest folders at 0.212 MB (3 files). The dev commit between them
that adds exactly those is **T-3556 (#2088, 13cdea48e)**: `assets/humans/web/hm08_variation_persons_1835.json`,
`data/humans/doors_1835.json`, `data/humans/inside_1835.json`. So the breach is dev's own and
every PR's content build carries it, as with T-3599.

To work it: publish dev, `node tools/measure_boot_payload.mjs --against
docs/measurements/T-3599-boot-payload-entries.json`. Then either re-budget consciously under
AGENTS.md's standing ruling (SITE-BUDGET.md § 4n's form), or make the 1835 doors/inside routines
and the 1835 variation persons load on first use rather than at boot. Making them lazy is a cut
to how the townspeople appear, so check § 4n's caution before you choose it.
