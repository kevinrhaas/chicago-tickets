---
id: T-2045
title: Boot variants for the arrival and jaunts path: warm, throttled slow, essential and optional failure, reduced motion, background and resume, stale timing history, a failed catalog fetch
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1272
opened: 2026-10-03
closed: 2026-10-03
pr: 376
claimed_by: run 10/3/2026, 6:42:40 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T04:09:53Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37162470526
claimed_at: 2026-10-03T23:42:40.198Z
decision: null
decision_answer: null
---

Boot variants for the arrival and jaunts path: warm, throttled slow, essential and optional failure, reduced motion, background and resume, stale timing history, a failed catalog fetch.

Piece 2 of 4 of **T-1272 — Verify arrival, jaunts and source browsing on the published mobile app**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## 2026-10-03 — acceptance, stated before the work (slice 5/5)

One harness, `tools/measure_arrival_jaunt_variants.mjs`, boots the PUBLISHED mirror
(`site/4d`, gzipped, cacheable) eight ways at 390×780 touch AND 1280×800, and each
variant must show: the arrival counts down and reads 1835 only once `api.ready`; the
welcome is reached (or, for the essential failure, is NOT, and Retry is offered); a
jaunt then starts at stop 1 (the catalog variant: entry on your own still works, and
Try again recovers); zero page errors.

- **warm** — second visit, same browser: < 5 % of the cold bytes from the network;
  the first visit's timing history paces the arrival.
- **slow** — CPU 4× + Fast 3G: ≥ 4 distinct years shown; arrives; jaunt starts.
- **essential** — terrain.js throws: failure named, Retry, no welcome, year ≥ 1836;
  Retry reloads and arrives.
- **optional** — people.json 503: arrives at 1835, error recorded on `people`.
- **reduced** — prefers-reduced-motion: ≤ 5 years, no digit animations.
- **background** — tab hidden mid-boot (no frames, `document.hidden`): no flips
  while hidden, continues on return; hidden at a stop and mid-ride: same stop, ride lands.
- **stale** — another build's history ignored; an absurd history from this build
  clamped to 0.25–4× defaults; corrupt history and a corrupt or older-version saved
  outing discarded with their notices.
- **catalog** — statuses.json 503 still arrives with a loading card; catalog.json 503
  → "Jaunts could not load" + Try again; Explore Myself enters; Try again recovers.

Evidence: `docs/measurements/arrival_jaunts_boot_variants_2026-10.md` with stills.
Any integration defect found is fixed here or filed as a named successor beside T-2047.
