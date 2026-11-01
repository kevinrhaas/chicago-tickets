---
id: T-3296
title: Content build's bake job dies at its 30-minute cap on every full bake since 2026-10-17 (nightly last green 10-16; dev 99 of 100 cancelled): 262 drifted masters re-derive each time (14 min, Glessner's KTX2 alone ~9) so no bake ever lands to clear the drift, and generator PRs (#1575, #1577) cannot merge
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-01
closed: null
pr: 1582
claimed_by: run 11/1/2026, 12:26:40 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41335811733
claimed_at: 2026-11-01T18:26:41.165Z
decision: null
decision_answer: null
---

Content build's bake job dies at its 30-minute cap on every full bake since 2026-10-17 (nightly last green 10-16; dev 99 of 100 cancelled): 262 drifted masters re-derive each time (14 min, Glessner's KTX2 alone ~9) so no bake ever lands to clear the drift, and generator PRs (#1575, #1577) cannot merge.

## Evidence (2026-11-01, measured)

- Bake job `timeout-minutes: 30`; it ends at 30m16s on every nightly since 2026-10-18 (10-17 failed) and on 99 of the last 100 dev pushes. Last green nightly 2026-10-16 (run 38862791995): Bake step 18.5 min, `4 master(s) moved`.
- 2026-11-01 nightly (run 41280867571): generate + bake 3 min; `262 master(s) moved, unrecorded or underived` → web derivatives 14m13s (Glessner's two KTX2 passes ≈ 9 min of it); sidecars + publish 1 min; embedded gate still running after 9.3 min when the cap hit. 10-16's embedded gate took 13.8 min.
- Cause of the 262: the runner image. 10-16 ran on ubuntu-24.04 (image 20261012.334.1); 11-01 on ubuntu-26.04 (20261025.179.1) after `ubuntu-latest` moved (the same move T-3169 met). `recon_1835_bank_freight_f3_001` rebuilt with pinned Blender 4.5.3 on a 26.04 runner from dev's generators AND from the 10-16 nightly's generators (b1980f5) gives one identical file (sha a028ab79…), twice, run to run — and differs from the committed master (b330bff8…) only in TEXCOORD_0 (max |Δ| 0.93; JSON identical). Not a generator change: an image change.
- Self-perpetuating: no bake lands, so the 26.04 bytes are never committed, so every bake re-derives all 262 and dies again. PR branches touching generators carry the `cancelled` verdict forward and `pr-automerge` refuses them (#1575, #1577 on 2026-11-01).

**Acceptance:** (stated before working)
1. The content build's bake job names an exact image, the one steward runs bake `--only` on (ubuntu-26.04 while polecat-platform's steward runs on `ubuntu-latest`), so CI and PR bakes write the same bytes.
2. Its cap is raised from 30 to a figure derived from the measured steps above (~38 min worst case with the whole drift), not guessed.
3. `tools/check_runner_images.py` refuses a job that runs Blender (sources `generators/blender.pin` or invokes `tools/bake.sh`) on a moving label, with self-tests that fire on dev's workflow as it stood.
4. Follow-up reading, not this PR's gate: the first content build after merge completes inside the cap, and once its bake lands the next whole-town bake derives a handful of masters, not 262. If it does not converge (e.g. CPU-dependent UVs across 26.04 runners), that is a new ticket with the two runs' moved lists.
