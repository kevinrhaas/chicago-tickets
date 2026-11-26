---
id: T-3760
title: 1871 tree cleanup: Water Tower and citywide leftover planting
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-25
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

Owner request during Better Trees implementation: "there were a few bogus trees leftover in 1871 i think also around water tower ... maybe a lot more to fix there". Continue alongside T-3747/T-3748 and merge the completed correction to dev through the normal gate/PR process.

Initial read: 1871's street layer already grows 6,741 trees, but `city-context.js` independently draws 3,538 generic portable deciduous crowns from its kit. Inspect these and the Water Tower/pumping works grounds for old tree representations, duplicate planting or placement errors. Reconstructed planting is not an identified historical tree; retain that distinction and check the existing period views before deleting or moving plants.

**Acceptance:**
1. Audit the 1871 context and named grounds planting paths, starting at the Water Tower. Identify each leftover representation and any duplicate or invalid placements in a written receipt, with source/data locators.
2. Replace obsolete tree representations through the shared adaptive grown-tree path where appropriate, or remove proven duplicates/invalid placements. Preserve supported planting, historical grades, geography and inspectable provenance. No broad clearing based on a guess.
3. Verify Water Tower/pumping works and representative city districts in published phone and desktop views, with before/after images, all seasons and all three detail levels. Check both street and context planting, collisions/duplicates, Confidence view, budgets and disposal/retiering.
4. Follow local partitioned check.sh, preflight, required CI and mapped published smoke before PR merge to dev. Record the visible change in What's New/STATUS, artistic choices in LIBERTIES, and bulky evidence in chicago-evidence.
