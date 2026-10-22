# Current handover — 2026-10-22, 20:53 UTC

The user wants visible progress in the DEV app, starting with PR #1175, followed by better parked wagons, carriages and horses. Multiple agents, periodic commits/pushes and ordinary green DEV merges are authorized. Production promotion, admin merges and workflow edits are outside this task.

## First: finish PR #1175

PR #1175 is ready, open and unmerged. Its current pushed head is `03ef5178977184928cf454011737ea2b17607b5d`; the primary checkout `/workspace/chicago` is clean at that head.

Exactly one existing integration workflow was dispatched: **run `39849920673`, `chicago-4d-pr-lap.yml`, input `only=1175`**, started at 20:33:42 UTC. The latest observation at 20:51:12 still showed the rebuild running and the source head unchanged. Agent `ci_parked_recovery` owns the bounded, once-per-minute GET watcher, session `47798`, under `/workspace/shared/PR1175-SCOPED-LAP-39849920673-GET-owner1`.

**The root lap lease was deliberately released so that workflow can push. Native GitHub auto-merge is OFF. Observe the workflow's actual successful final push, then reacquire the lap lease before published qualification and merging.** Taking the lease before its push makes the workflow refuse to push. Do not dispatch a duplicate integration workflow or treat an unchanged head as a new push.

The preceding local merge of DEV `4459c0e2` was saved and safely aborted. Its exact staged tree `2adde358e61e1cc5618f14396d4a606fe5762fca` failed only the generated liberties check: 1,046 of 1,047 checks passed; the file had 687 entries but declared a count of 686. The supported local `--resolve` tail started at step 149 and therefore missed the cleanly merged liberties owner at step 142. This does not prove a compiler bug. The existing CI lap runs full `--run`, which covers that owner. All actual failure logs and recovery data are saved; no failed tree was committed and no own human changes were lost.

After the lap actually pushes:

1. Verify the resulting source, all unchanged human assets/data/runtime and the retained incoming history.
2. Reacquire the lap lease. Verify current normal CI and its actual checkout, then capture the exact GitHub test-merge commit, tree and parents.
3. Create an immutable verification ref at that existing test merge and dispatch the existing 18 published smoke legs once. Both viewports must cover parts 1–15. The reviewed, **unexecuted** helper is `/workspace/shared/PR1175-DISPATCH-TESTMERGE-SMOKES.py`; it records POST intent, guards the source/base/ref and never retries a POST.
4. Collect actual terminal results. Recheck the live head/base and any changed rendering inputs immediately before an ordinary, head-pinned DEV merge. Do not restart for commit metadata alone, or falsely reuse old town-rendering proofs across changed terrain/UI/tree inputs.

Historical `779`/`b092` human proofs retain their original labels and supplemental timing failures. All human files and Bardwell's local sole-area terrain were independently verified unchanged; this avoids repeating the entire custom canonical/person grid for unrelated DEV changes. Current broad town changes still require published desktop/mobile coverage. DEV `d1cea812` includes the actually merged T-3032 rendering-budget fix, PR #1205, and the Glessner changes from PR #1209.

## Parallel work and the local CPU/browser lane

Only one local fullgate or browser lane runs at a time. Remote CI runs independently.

- **Horse:** `horse_completion` owns `/workspace/chicago-waistcoat`, clean and pushed at `fde6bc317f6c82b57a1eaaf77a46d6d8274ecfd8`. Full preflight passed 1,047 checks / 381 self-tests; publication passed. One **original mobile** run, session `51298`, is now active with unchanged cameras, 15-second/1.5-owned-second criterion, contacts, budgets and whole-run cap. It owns the sole browser lane. No automatic retry. On its actual closure, release the CPU lane for the carriage fullgate.
- **Carriage:** `carriage_v17_visual` owns `/tmp/chicago-covered-sag`. Its source is ready at staged tree `3acbf2788b8196e11c1f82e96f14d9280e5c918f`, based on DEV `d1cea812`, with 34 staged files and no unstaged changes. Exact current Glessner recovery, the 59-step supported tail from step 142, native/schema checks, isolation and audit all passed. Two automatic rebuild laps converged. A Brougham-only support solve fixes the real 4.866 mm pole-shoe penetration while preserving the stand, model and limits; nine rejection controls and six legacy comparisons pass. Full preflight, rendered tree/canopy clearance, scene budgets, commit/push and PR remain pending. Hold its fullgate until the horse browser closes. The complete recovery capsule is `T2794-V17-DEVd1cea-SUPPORTED-REBUILD-20261022.zip`, SHA256 beginning `2ed15a84`.
- **Horse walk:** `animated_horse_source` preserved the failed V4 candidate. Rest geometry and gait mechanics pass, but posed skin deformation fails. Independent agent `horse_skin_review` found opposite 100% body/shoulder handles across one 25.77 mm mesh edge, explaining the 4.681× stretch; maximum-four-weight pruning is not the cause. It is preparing one separate candidate with soft proximal priors and physical blend constraints. No CPU runs during the mobile browser, no assertion relaxation, no mesh/joint/stride changes and no app installation or accepted gait.
- **Covered wagons:** draft PR #1208 is pushed at `065646706`. Full preflight passed 1,046 checks / 381 self-tests; publication and normal CI passed. Actual desktop/mobile stage 8 each passed 21 checks with zero failures. Stage 8 is targeted evidence, not the whole published gate; current DEV integration and remaining qualification are pending.
- **Route and driver:** the current rigid-team corridor is source-only; worn-track alternatives remain failed and all live/qualified flags are false. Driver V2 has CPU bench clearance for all four LODs, but canonical export, float32 verification, full support/reins and live use remain pending. Do not change PR #1175's person assets on its merge critical path.

## Horse clock finding: preserve its scope

The actual desktop diagnostic closed FAIL after 228.72 seconds, with browser/server/PIDs cleaned up. The original 15-wall-second/1.5-owned-second criterion failed. Three real eligible host updates supplied only `3 × .25 = .75` seconds; the source produced exactly:

`(.75 − .5750385086459663) × .9802204318391672 = .17150082861027566`

The accounting error was zero. The page was visible/focused and all visibility, confidence, distance and media gates allowed playback. This proves clock wiring for the observed span; later surface-motion, hoof, pause and lifecycle checks were skipped and remain unproved in-world.

Independent review found the 15/1.5 target in the private caller, not the product clock contract. Keep both timing failures as failures. A separate continuation diagnostic is prepared but **held and unexecuted**; it preserves the original timing failure and final FAIL/exit 1 while collecting later unchanged product checks. Its first source revision `098ba976` has a pre-execution progress-writer newline issue: **do not release it**. The horse agent is preparing a separately named correction. No source, timeout, camera or threshold change is authorized by this note.

## Durable checkpoints and claims

The latest source/evidence checkpoint is:

`evidence/parked-vehicles-2026-10-22/checkpoint-carriage-source-ready-and-horse-clock-diagnosis/`

Its `MANIFEST.json` authenticates the complete carriage source, actual horse-clock diagnosis, actual failed walk candidate, original mobile release packet and compact failed-person-gate proof. The previous checkpoint is ticket commit `8f8cb799`; older chronological handovers remain in Git history and the saved checkpoint artifacts. Verify the latest `ticket.mjs sync` commit before claiming it is pushed.

Root is the sole writer of canonical `/workspace/chicago/chicago/4d/tickets`. Seven independent claims—T-1789, T-2794, T-2800, T-2980, T-2803, T-2795 and T-2796—were renewed at 19:35:35–53 UTC. Renew before **22:35 UTC** if still active, or release inactive parcels with recoverable work. Four bounded tickets T-2792/T-2799/T-2979/T-2981 remain DONE through merged PR #1174. Broad photographic, occupied and riding parents stay open. Use `resume` with a reason/waiting ticket on unfinished handoff, never agent-applied `hold`; release the lap lease when actually handing off.

## Environment notes

Four local CPU cores; about 4 GB free in `/workspace` and 5 GB in `/tmp`. Copy global `/tmp/preflight-*` logs immediately when a fullgate closes. Use the existing shared Python 3.11 readers and one math thread. Node commands that spawn Git need escalated tool permission here to avoid `spawnSync git EPERM`. Name `kevinrhaas/chicago` explicitly in GitHub calls. Edit PR bodies through REST with structured JSON; `gh pr edit` encounters a deprecated Projects-classic GraphQL query. Do not install Blender or create more full worktrees/ticket clones. Preserve all actual failures and source bindings.
