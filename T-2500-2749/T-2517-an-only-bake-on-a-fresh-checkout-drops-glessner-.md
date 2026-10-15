---
id: T-2517
title: An --only bake on a fresh checkout drops glessner_house__as_built_1887.glb from assets/manifest.web.json: web_derivatives.sh's merge keeps only entries whose master is on disk, and that gitignored master is materialized by publish.sh only AFTER the merge, so publish then refuses the Glessner derivative (K39) — found running bake.sh --only house_1601_prairie for T-2492
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: null
claimed_by: run 10/15/2026, 11:01:34 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38764258679
claimed_at: 2026-10-15T16:01:34.479Z
decision: null
decision_answer: null
---

An --only bake on a fresh checkout drops glessner_house__as_built_1887.glb from assets/manifest.web.json: web_derivatives.sh's merge keeps only entries whose master is on disk, and that gitignored master is materialized by publish.sh only AFTER the merge, so publish then refuses the Glessner derivative (K39) — found running bake.sh --only house_1601_prairie for T-2492.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
