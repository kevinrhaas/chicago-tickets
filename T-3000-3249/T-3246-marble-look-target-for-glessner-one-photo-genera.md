---
id: T-3246
title: Marble look target for Glessner: one photo-generated world beside our render, evidence only
state: open
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-29
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

Owner, 2026-10-29 (project thread "Assess other 3D project for reuse"), on the World Labs Marble / Spark assessment: *"ok sounds good lets try it out and roll things back if its not productive, i want to improve things best we can if this will work, but dont want to break things"*. Assessment: https://claude.ai/artifact/S5EdbiYNSKK2QrNLU4kAaW; spike files in the project folder `marble-spark-assessment/`.

**What:** generate ONE Marble 1.1 world from a public-domain HABS photograph of Glessner House (World API: 1,580
credits ≈ $1.26 of the $5 minimum purchase). View it in Spark from that photo's solved camera
(`data/reference_views/glessner_house/`) beside our render from the same camera, and write which photographic cues we
lack (stone texture, contact shadow, haze, bounce light), each with the ticket that would fix it.

**Rules:** evidence only, never shipped; everything goes to private kevinrhaas/chicago-evidence. Upload only
public-domain pictures (ToS §3.6 lets World Labs train on uploads). Free-plan output is World Labs' and non-commercial,
so use the API or a paid plan.

**Needs from the owner:** a World Labs API key with $5 of credits, added as an environment secret for the session
that runs it (spending money is the owner's). Invisible run: counts against the one-in-four cap; best done in an
interactive session.

**Acceptance:** side-by-side image + a short findings list in chicago-evidence, linked here.
