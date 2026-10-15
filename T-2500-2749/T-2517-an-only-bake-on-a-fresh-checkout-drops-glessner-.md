---
id: T-2517
title: An --only bake on a fresh checkout drops glessner_house__as_built_1887.glb from assets/manifest.web.json: web_derivatives.sh's merge keeps only entries whose master is on disk, and that gitignored master is materialized by publish.sh only AFTER the merge, so publish then refuses the Glessner derivative (K39) — found running bake.sh --only house_1601_prairie for T-2492
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
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

An --only bake on a fresh checkout drops glessner_house__as_built_1887.glb from assets/manifest.web.json: web_derivatives.sh's merge keeps only entries whose master is on disk, and that gitignored master is materialized by publish.sh only AFTER the merge, so publish then refuses the Glessner derivative (K39) — found running bake.sh --only house_1601_prairie for T-2492.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
