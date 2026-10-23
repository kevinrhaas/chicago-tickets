---
id: T-3054
title: Phone sun shadow speckles pale sunlit walls (1835 north bank shed pixelated)
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-22
closed: 2026-10-22
pr: 1225
claimed_by: run 10/22/2026, 9:38:35 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-23T03:29:48Z
claimed_run: null
claimed_at: 2026-10-23T02:38:36.067Z
decision: null
decision_answer: null
---

Phone sun shadow speckles pale sunlit walls (1835 north bank shed pixelated).

The owner, 2026-10-23 (iPhone, Chrome iOS, 375x636, build 9e7768f): a stable/shed on the 1835
north bank by the river "was very pixelated when I moved around it"; the cards he opened were
`north_bank_shed_dearborn_w` and `recon_1835_north_d4_012`.

**Finding.** Rendered at 375x636 on the phone profile (light detail, light textures), the shed's
sunlit south wall carries blotchy, blocky dark patches that the desktop render of the same stand
does not; with the sun's shadow off they vanish, so they are the sun's shadow falling on the wall
that casts it (shadow acne). The `light` tier draws the sun's shadow at 23.4 cm a texel (1024
over +/-120 m) where `full`/`balanced` draw 11.7 cm, but `normalBias` stayed 0.045 m, the figure
tuned for the 11.7 cm texel. At the scene's 12:30 sun a south wall is lit at about 70 degrees off
its normal, so a texel's depth slope there outruns the bias, and on a pale untextured board wall
the self-shadow shows as blocks that shift as the walker moves.

**Acceptance:** the phone render of the shed's front wall (stands near/mid in front of it) shows
no self-shadow blotches; the normal bias holds the same fraction of a texel on every tier, so
`full`/`balanced` keep exactly 0.045 m; a gate pins the ratio.
