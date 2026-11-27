---
id: T-3792
title: Scalable period hair with controlled motion and shared GPU budgets
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: null
claimed_by: Codex continuing owner-authorized hair while photo review completes 11/27/2026, 3:20:01 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T21:20:02.535Z
decision: null
decision_answer: null
---

Scalable period hair with controlled motion and shared GPU budgets.

**Acceptance:** Improve the existing dedicated hair-card renderer as one visible, scalable hair pass. Use the current Light/Balanced/Full detail settings and viewing distance: Light keeps stable low-cost silhouettes, Balanced uses bounded near hair cards, and Full provides denser layered detail and controlled secondary motion. Keep roots fixed, constrain motion under hats, and keep tied period hair appropriately restrained. Apply the same quality policy to adults and children without changing their head proportions or named photo mappings. Preserve William and Sarah Grey's original fitted heads and full photographic skins. Bound total near-hair geometry and active motion work, release resources correctly during LOD/detail changes, and add no new per-person texture atlas. Supply actual app front/oblique comparisons at the detail tiers, meaningful geometry/motion/lifecycle tests, the project gate and appropriate published desktop/mobile checks. Record what remains unmeasured on physical GPUs rather than claiming hardware frame rates.

**Owner request, 2026-11-27:** “you need a whole focus on hair specifically ... aaa games ... break hair into its own module with its own physics and rendering ... downscaled ... higher processing with gpus ... Low power computers also”. The owner then explicitly authorized starting the hair work while the current photo-face rollout is merging: “You can start working that while we wait for all the merging”. Work in an isolated branch so the qualified T-3762 face payload remains stable.

**Starting point:** T-3414 already delivered a separate `human-hair.js` card generator and shader, `human-hair-styles.js` period style data, and body-LOD-based density. This pass improves that system's visual presentation and adds explicit quality/motion budgets; it does not present the existing module as newly built. Original portrait mappings are the reference, and all newly chosen hair movement is reconstructed.
