---
id: T-3775
title: dev's 1835 first-visit boot payload measures 49.767 MB, over SITE-BUDGET § 4's 49.6 MB: every PR's smoke (desktop, 1-2) is red on it — the photo-face libraries' two review.json (0.166 MB) now load at boot (dev 71566d43b, after T-3767/T-3768)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
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

dev's 1835 first-visit boot payload measures 49.767 MB, over SITE-BUDGET § 4's 49.6 MB: every PR's smoke (desktop, 1-2) is red on it — the photo-face libraries' two review.json (0.166 MB) now load at boot (dev 71566d43b, after T-3767/T-3768).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content-build smoke (desktop, 1-2) is red on measure_boot_payload --check for every PR, #2369 included

**Acceptance:** `node tools/measure_boot_payload.mjs --check` passes on dev (≤ 49.6 MB), either by keeping the photo-face libraries' review data out of the 1835 first visit (fetched when a face first needs it, or a slimmer boot index) or — if the owner-approved faces must stand in the first view — by a measured, written re-budget in SITE-BUDGET § 4 the way T-3651 did it. Never by loosening the measurement.

## Reading (slice 1/5, 2026-11-26 ~23:00Z)

Measured locally with `tools/measure_boot_payload.mjs --entries`, on dev `71566d43b` and on PR #2369 merged with dev `b1bdedd82` — both read **49.767 MB across 1,400 requests**, identical to CI's red `smoke (desktop, 1-2)` on #2369 (job 140177125274). dev's own standing record has desktop part 1 PASS at 15:57Z, so the breach landed on dev after that.

Against T-3732's entries file (`docs/measurements/T-3732-boot-payload-entries.json`, the last reading under budget): **+0.281 MB** (MiB in the file's bytes: +0.248 arrived, +0.033 grew, nothing left). The arrivals:

| arrived at boot | on the wire |
|---|---|
| `/data/humans/web/photo_faces/pilot/review.json` | 0.155 MB |
| `/walk/js/human-trim.js` | 0.024 MB |
| `/walk/js/human-drape.js` | 0.017 MB |
| `/data/humans/web/photo_faces/children/review.json` | 0.011 MB |
| `/walk/js/bug-report.js`, `controls/gamepad.js`, `human-fair.js`, `human-layover.js`, `human-pits.js`, `flight-clearance.js`, `graphics-settings.js`, `photo-face-pages.js` | 0.040 MB together |

The two `review.json` files are fetched unconditionally by `renderers/web/js/human-variation.js` (the `photoMode !== 'off'` branch added for T-3767/T-3768) as soon as the variation kit loads — before any face needs them. Largest single growth: `main.js` +0.008 MB.
