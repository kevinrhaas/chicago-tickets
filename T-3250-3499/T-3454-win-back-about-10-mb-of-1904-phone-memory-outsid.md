---
id: T-3454
title: Win back about 10 MB of 1904 phone memory outside the people layer, so the four placed figures fit under the 400 MiB line
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
closed: 2026-11-07
pr: 1832
claimed_by: run 11/7/2026, 9:39:59 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-07T17:22:04Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/42386363695
claimed_at: 2026-11-07T15:40:00.127Z
decision: null
decision_answer: null
---

Win back about 10 MB of 1904 phone memory outside the people layer, so the four placed figures fit under the 400 MiB line.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- `memory (1904, mobile)` in chicago-4d-frame-time.yml reads under its unchanged 400 MiB ceiling on CI with all four 1904 figures placed (John and Frances Glessner, Martha Williamson, Mary Reynolds), with a margin of at least 2 MB.
- The saving comes from layers other than `humans`; the people layer keeps its LOD2/LOD3 pictures on a phone.
- Phone-only: every desktop memory and still-frame row reads within noise of before.
- The reading is recorded in tools/memory_ceilings.json (1904 mobile) with its docs/measurements file.

## Source (owner, 2026-11-07)

Decision card in the thread "Place all five catalogue figures", question "Make room on phones for 1904's people, which now sit at the memory line?", the owner chose **Win back town memory**: "I open one ticket to bring 1904 phone memory about 10 MB back under the line, phone-only, with desktop unchanged."

## Findings so far (T-3452, PR #1827)

- CI read 1904 mobile at 399.3 MB on 3d4a760 (Martha alone) and 408.4 MB on 70ef821 (four figures). This container reads about 8 MB lower (400.0 MiB at 70ef821).
- The human layer is 8.5 MB (1.0 geometry, 7.2 MB of 16 textures), inside the 12 MB people pool T-3408 set aside. The rest of 1904 grew about 16 MB on a phone since T-3408's 375.1 MB (2026-11-06).
- Per layer at 70ef821 (this container, MB, gpu geometry / textures): structures 115.1 / 201.9, railway 18.5 / 8.5, street-grid 4.1 / 1.8, context 2.8 / 0, front-yards 2.1 / 0; terrain keeps 8.5 MB on the CPU that is never uploaded. The layer estimate of GPU geometry is 146.5 MB against 178.2 MB measured in GPU buffers, so about 32 MB of buffers are not attributed to a layer; T-3408's bufferData probe (memory chicago-phone-people-pool-3408) attributes them.
- Largest ArrayBuffer retainers: BatchedMesh `_matricesTexture` 5.5 MB in 537 batches, tieCache wordColumns 3.1 MB, terrain BatchedMesh position/normal/index 7.5 MB.
