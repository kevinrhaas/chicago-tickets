---
id: T-3746
title: Review sixteen photographic faces before population rollout
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-25
closed: null
pr: 2355
claimed_by: run 11/25/2026, 9:29:14 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-26T03:29:16.057Z
decision: null
decision_answer: null
---

Owner request: prepare sixteen photographic starter faces on the existing generic people,
show source/before/after renders before making them the population default, bound the
cost on lower-power PCs, and provide a repeatable single-photo head-fit and face-map path
for future historical portraits. The owner also called out poor hair and glaring eyes.

**Acceptance:** Sixteen credited fictional sources, a runnable review with actual head
geometry and front/three-quarter/profile views, an opt-in existing-resident preview,
shared Full/Light texture budgets, and one historical-photo import command that produces
the same review format without silently overwriting a person's likeness. Expose a
hardware-labelled crowd measurement and keep historical likeness and hardware approval
explicitly separate from completing the pilot implementation.

**Implemented:** Review page and single-photo importer; stable generic-adult opt-in;
historical/visitor face protection; source-fitted head shape and photographic face atlas.
Retain iris detail instead of flattening it to a bright colour; source-guided sclera,
pupil position and radius, measured resting lid aperture and reduced corneal glare.
The town preview retains its existing hair; the separate review shows a small source-hair
scalp proposal. Light town face atlas: 1.33 MiB including mipmaps for all sixteen.

**Measured:** Actual desktop and phone previews, all sixteen simultaneously, and actual
existing residents rendered without browser errors. The available renderer is SwiftShader
software; its exported crowd timing does not satisfy a real-GPU performance acceptance.
Source matching, especially single-photo depth and hair, still needs visual review before
default rollout. Real low-power-PC whole-town performance remains outstanding.

**Final coverage:** All 1,234 drawn people checked through their actual scene assignments:
1,048 generic adults receive photo faces on 1,076 bodies; 160 child and 27 personal-face
assignments remain protected, and multiple bodies retain one face. Four real resident
models verify retained iris maps, source-guided lid rest and softened sclera. The final
extracted viewer ZIP passes Full and phone/Light checks without missing files or browser
errors. Published renderer stage 1 passes 96 checks on each viewport. The desktop run alone
took 11m36s, exceeding the ten-minute foreground budget; the first concurrent attempt hit
a scene-settling timeout. This is stage 1 of 15, not complete renderer qualification.

Evidence and portable viewer:
https://github.com/kevinrhaas/chicago-evidence/tree/ea5f6f31f0f8452b8767e6b8172914bde0ca74f6/evidence/photo-face-pilot-T-3746

The final review preserves fitted head/forehead axes and gives before/after distinct
geometry cache keys. Actual browser parameters and the main body mesh are checked:
1,828 of 13,341 position components change. The final extracted Full face-16 package
also verifies distinct geometry (9,139 changed components), and phone/Light passes.
All final screenshots and software timing were regenerated after the geometry fix.
Two clean write-mode runs reproduce all 24 outputs; a deliberately damaged atlas was
refused and restored byte-exact. Writer registration is measured and explicitly pending
behind its unplaced input writers. Preflight 2/8 and gate 6/8 pass, as does local 1/4;
complete CI and published renderer stages 2–15 remain outstanding on draft PR #2355.

**Owner expansion (T-3761):** The same PR now carries 256 adult samples and a bounded nearby detail page. The original sixteen sources are preserved. Final 256-face evidence and runnable viewer: https://github.com/kevinrhaas/chicago-evidence/tree/86c4851431974d5c9ed6dac8db10bbd6de830563/evidence/photo-face-library-256-T-3761 . Existing hairstyles are the default; the scalp trial and real-GPU whole-town timing still need review. See T-3761 for the current verification and handoff.
