---
id: T-3760
title: 1871 tree cleanup: Water Tower and citywide leftover planting
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-11-25
closed: null
pr: 2414
claimed_by: Better Trees season pass 11/27/2026, 5:26:28 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T23:26:28.891Z
decision: null
decision_answer: null
group: T-3747,T-3748,T-3760
---

Owner request during Better Trees implementation: "there were a few bogus trees leftover in 1871 i think also around water tower ... maybe a lot more to fix there". Continue alongside T-3747/T-3748 and merge the completed correction to dev through the normal gate/PR process.

Initial read: 1871's street layer already grows 6,741 trees, but `city-context.js` independently draws 3,538 generic portable deciduous crowns from its kit. Inspect these and the Water Tower/pumping works grounds for old tree representations, duplicate planting or placement errors. Reconstructed planting is not an identified historical tree; retain that distinction and check the existing period views before deleting or moving plants.

**Acceptance:**
1. Audit the 1871 context and named grounds planting paths, starting at the Water Tower. Identify each leftover representation and any duplicate or invalid placements in a written receipt, with source/data locators.
2. Replace obsolete tree representations through the shared adaptive grown-tree path where appropriate, or remove proven duplicates/invalid placements. Preserve supported planting, historical grades, geography and inspectable provenance. No broad clearing based on a guess.
3. Verify Water Tower/pumping works and representative city districts in published phone and desktop views, with before/after images, all seasons and all three detail levels. Check both street and context planting, collisions/duplicates, Confidence view, budgets and disposal/retiering.
4. Follow local partitioned check.sh, preflight, required CI and mapped published smoke before PR merge to dev. Record the visible change in What's New/STATUS, artistic choices in LIBERTIES, and bulky evidence in chicago-evidence.

**Scope/size after initial audit:** reduced from M to S. The leftover crowns share one runtime path; the named Water Tower/pumping grounds contain kerbs and railings, with no baked foliage to rebuild. The bounded correction is the shared grown-tree handoff, preserved reconstructed records/picking and control integration, without a planting-data rewrite. It fits with T-3748 because that pass enables 1871 seasons. Initial audit and exact input hashes: https://github.com/kevinrhaas/chicago-evidence/blob/20648926d4217e326a479028b1a669eccd6fbd46/evidence/vegetation-realism-2026-11-25/T-3760-initial-audit.json .

**Earlier prototype audit, superseded for integration:** a citywide raw-data scan checked 10,279 trunk centres against 39,777 context building plans, strictly more than 0.25 m inside a wall. No context-tree trunk centre was inside one; two street trees, `tree.01161` and `tree.01162`, stood 2.53 and 2.52 m inside `context1871_core_0133_008_s_r08` (a frame shop). No named-structure footprint lies near enough to displace that shop in the current scene. The published 1871 phone check on 8 October (Balanced) confirms `containsBuilding` is true at both withdrawn trunk centres, neither tree remains in the drawn records, all 3,538 context stems are handed to the grown layer, and no portable context-tree mesh remains. The street recipe now withholds those two after stable ID assignment and retains their records and reasons under `withdrawn`. Every other street-tree record is unchanged (6,739 remain); all 3,538 context planting records are unchanged. This adds a bounded two-placement correction, without a citywide planting rewrite or a bake. The generic grown handoff, cards, confidence hide and winter zero-leaf-area contract pass focused native tests. Published images, budgets and full gates remain pending.

**Earlier named-footprint follow-through (superseded inputs):** the same starting population of 10,279 trunk centres was checked against 19 compiled named solid footprint parts, using the renderer compass rotation and excluding open grounds. No trunk centre was more than 0.25 m inside a named wall plan. The pumping-works tree `tree1871_8387` is on the grounds west of the building, retains its recorded height/crown, and now has a generic reconstructed inspection card in the grown renderer. This is a trunk-centre audit, not a claim that all crowns clear every wall. The native handoff fixture also proves that Full → Light removes the leaf-relief sampler and Full reuses the same atlas, while season/detail replacements remain atomic. Evidence: https://github.com/kevinrhaas/chicago-evidence/blob/c986553/evidence/vegetation-realism-2026-11-25/T-3760-named-footprint-audit.json .


**Current integration audit:** upstream `172bbb62b9ff07352a683a291bf34ea6d392b57d` regenerated the city. It now has 6,693 street and 3,543 context trees (10,236 total), with 38,598 context building plans. A new immutable-input scan finds zero trunk centres strictly more than 0.25 m inside a context building plan; the 19 compiled named solid footprint parts also have zero hits. This does not establish crown clearance. The old two coordinates remain as `tree.01139`/`tree.01140` but are no longer inside buildings. Old IDs `tree.01161`/`tree.01162` now name valid, unrelated trees. Discard the prototype's old placement-deletion edits and preserve all current planting. The old pumping-works tree `tree1871_8387` is absent upstream and must not be reintroduced; the nearest current context record to Water Tower is `tree1871_9715`, about 164 m away. Use a current generic context-tree close probe plus the wider Tower view for final image acceptance.

The bounded renderer correction remains S: hand the 3,543 current context records to the shared grown tree renderer, retain their generic reconstructed cards and dimensions, and preserve the upstream Great Fire burnt-tree API through season/detail rebuilds. Whole integrated native/CI, current published captures and budgets remain pending. Current audit receipts and the superseded-input warning: https://github.com/kevinrhaas/chicago-evidence/tree/597d620/evidence/vegetation-realism-2026-11-25 .
