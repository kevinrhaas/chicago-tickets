---
id: T-2058
title: Take liberties.json off the boot path: a first visit downloads 13.122 MB against the 13 MB budget
state: open
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Take liberties.json off the boot path: a first visit downloads 13.122 MB against the 13 MB budget.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 201 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1272's acceptance requires every unmet budget to leave as a named successor, and no open ticket owns this: T-2047 measured it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Found by T-2047 (2026-10-04), the measurement this ticket starts from

`node tools/measure_boot_payload.mjs --check` on dev @ `cb56e2e4`, on the steward runner:
**13.122 MB across 1306 requests — over the 13 MB budget** of docs/SITE-BUDGET.md §4.
The same tool on `49d0a226` (T-1973's merge, where the budget was re-set) reads
**12.575 MB across 1289 requests**, matching T-1973's own reading to the byte, so the
+0.547 MB is real growth and not a change of method. Where it came from (wire bytes):

| what | at 49d0a226 | at cb56e2e4 | Δ |
|---|---|---|---|
| `data/sidecars/1835/` (per-structure sidecars) | 3.339 MB | 3.601 MB | +0.263 |
| `walk/fonts/` (T-2036's skins, `css/skins.css`) | 0.012 | 0.083 | +0.071 |
| `data/enclosures/` (`town_entrance_aprons.json` new) | 0.090 | 0.140 | +0.050 |
| `walk/js/` | 0.737 | 0.785 | +0.048 |
| `data/liberties.json` | 0.559 | 0.594 | +0.035 |
| `data/yard/`, `data/frontage/`, `data/residents/`, `data/gltf/` | | | +0.082 |

None of it is the arrival-and-jaunts section: the catalog, the jaunt files and the
source index are not fetched at boot, and the section's own boot cost (`arrival.js`,
`welcome.js`, `loading-early.js`, `data/loading/statuses.json`) is 11.5 KB.

The cut SITE-BUDGET §4b names first is `liberties.json` (0.594 MB now), awaited at boot
by `main.js` `mountLiberties` although only the Evidence panel and an open provenance
card read it (`popup.setLiberties` already redraws when it arrives late). Three smoke
parts read it synchronously. The nightly bake enforces the check (`chicago-4d-bake.yml`,
T-1156), but every dev bake since 2026-10-03 was cancelled by a newer push, so no gate
has yet said this out loud. Do not raise the budget to fit: §4b says what to ask first.
