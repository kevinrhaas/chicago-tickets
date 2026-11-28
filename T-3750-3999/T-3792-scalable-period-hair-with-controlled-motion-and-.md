---
id: T-3792
title: Scalable period hair with controlled motion and shared GPU budgets
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2371
claimed_by: Codex continuing owner-authorized hair while photo review completes 11/27/2026, 5:34:14 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T23:34:15.843Z
decision: null
decision_answer: null
---

Scalable period hair with controlled motion and shared GPU budgets.

**Acceptance:** Improve the existing dedicated hair-card renderer as one visible, scalable hair pass. Use the current Light/Balanced/Full detail settings and viewing distance: Light keeps stable low-cost silhouettes, Balanced uses bounded near hair cards, and Full provides denser layered detail and controlled secondary motion. Keep roots fixed, constrain motion under hats, and keep tied period hair appropriately restrained. Apply the same quality policy to adults and children without changing their head proportions or named photo mappings. Preserve William and Sarah Grey's original fitted heads and full photographic skins. Bound total near-hair geometry and active motion work, release resources correctly during LOD/detail changes, and add no new per-person texture atlas. Supply actual app front/oblique comparisons at the detail tiers, meaningful geometry/motion/lifecycle tests, the project gate and appropriate published desktop/mobile checks. Record what remains unmeasured on physical GPUs rather than claiming hardware frame rates.

**Owner request, 2026-11-27:** “you need a whole focus on hair specifically ... aaa games ... break hair into its own module with its own physics and rendering ... downscaled ... higher processing with gpus ... Low power computers also”. The owner then explicitly authorized starting the hair work while the current photo-face rollout is merging: “You can start working that while we wait for all the merging”. Work in an isolated branch so the qualified T-3762 face payload remains stable.

**Starting point:** T-3414 already delivered a separate `human-hair.js` card generator and shader, `human-hair-styles.js` period style data, and body-LOD-based density. This pass improves that system's visual presentation and adds explicit quality/motion budgets; it does not present the existing module as newly built. Original portrait mappings are the reference, and all newly chosen hair movement is reconstructed.


**Qualified feature checkpoint, 2026-11-28:** The separate hair dynamics module and shared quality controller are included with the photo corrections in source PR #2371, checkpoint 1ec26773c6f4c0b14685fde34690f5e1dd5da421. Balanced admits 12 heads / 72,000 rendered optional near triangles at 20 m with 2 mm tip motion; Full admits 16 / 220,000 at 24 m with 8 mm motion. Light adds no optional near layers or motion. Parked allocations are reported separately from rendered triangles; existing cap/full-Grey/Light-tail geometry retains its existing body-LOD costs. Roots stay pinned, updos and hats constrain motion, and LOD/driver/detail transitions retain and release resources correctly. No new hair atlas or render pass is added.

Full/Balanced/Light actual-app views and child front/side scalp checks are in the current gallery: https://github.com/kevinrhaas/chicago-evidence/blob/bb7fda4/evidence/person-photo-deployment-T-3762/GALLERY.md . Child cap clearance remains above 2.5 mm in the native samples. The complete 1,440-check local feature gate passed before that checkpoint; all raw photo sources and the other original fits remain intact. The new dev integration is being qualified with the PR kept draft after automatic approval review refused readiness with pending checks. Final hosted release checks and dev delivery remain pending, and physical-GPU FPS is explicitly unmeasured.


**Current-dev qualification checkpoint, 2026-11-28T02:24:25.158287+00:00:** Source 14207e824c51c870ad0242b76c3d1044da88fe11 (tree 7dc0e7b1426446a7ade76b0b51088635e7e47041) was normally committed and pushed only after all 1,440 unique native project checks passed. All 18 accepted local partitions retain mandatory readers/base and the 600-second cap. The postcommit published local app verifies all three photographic libraries, every detail page and all four years with zero page errors. Public gallery and 75 hashed evidence artifacts: https://github.com/kevinrhaas/chicago-evidence/blob/e576bc3/evidence/person-photo-deployment-T-3762/GALLERY.md . This checkpoint is fully tested but has not reached dev.

Dev advanced five commits during that gate. The newer integration, tree 4ee19b65a18959ba2aa0517e780e2301abeda35e, preserves all 99 photographic inputs, 536 twice-reproduced outputs, 12 human modules, all 7,610 face assignments and both exact incoming workbook byte sequences. The existing upstream gate-tool repair from PR #2418 (42b8c27ad9277b8097459be5c2f388f138bf5e02) is included; the authored liberty log retains the entire current dev log as prefix and appends the exact original photo/hair records. Canonical regeneration completed all 209 writers, dependency pass and ordered tail.

PR #2371 remains draft at 14207e8. Using the already-established isolated test-merge method, synthetic fixture 8d81efa3d6a66b0137f7e9f5dac37118e9b56f84 on validation/t3762-latest-4ee19b65a189 runs the entire unchanged 1,442-check native gate (all prior 1,440 plus two upstream checks), before any actual source commit on that tree: https://github.com/kevinrhaas/chicago/actions/runs/46097382065 . It is queued, not passed. The source branch and draft status are unchanged by the test ref. Final actual-source desktop/mobile scopes and auxiliary checks, normal expected-head dev merge and live-byte verification remain required. No production action is authorized. Physical-GPU crowd timing remains unmeasured.
