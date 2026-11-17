---
id: T-3627
title: Load on first use the walk modules the 1835 first visit imports but never runs (sign-in, XR controls, narration, human-fight/human-blood, the boat helm, the story teller) — a measured boot-payload cut against T-3624's reading
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: null
pr: 2130
claimed_by: run 11/16/2026, 6:32:53 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43987836953
claimed_at: 2026-11-17T00:32:54.657Z
decision: null
decision_answer: null
---

Load on first use the walk modules the 1835 first visit imports but never runs (sign-in, XR controls, narration, human-fight/human-blood, the boat helm, the story teller) — a measured boot-payload cut against T-3624's reading.

**Acceptance:** (stated at claim, 2026-11-17)
- None of the named modules is fetched by the 1835 first visit (`measure_boot_payload.mjs --against docs/measurements/T-3624-boot-payload-entries.json` lists each as LEFT): the boat helm (boat-pilot.js), the XR session (controls/xr.js), the narration player (narration.js), the 18+ telling's human-fight.js and human-blood.js, and the story teller (tale-teller.js and what only it reads).
- Each still works on first use: Take her loads the helm and takes the boat (the smoke's helm check), Tell me a story and Ask a question are offered where Greet is and load the teller when chosen, Enter VR is shown only where a headset is offered and still starts from the click, an outing's stage still arms, wounds and burns.
- The unit tests that read these modules stay green (check_xr_mode, test_narration, test_tales, test_vessels, test_human_fight, test_human_lod_park, test_jaunt_stage, test_jaunt_start_finish), and narration.js still imports nothing.
- The cut is measured against dev's own head, published the same way, and written up in docs/SITE-BUDGET.md with its per-URL reading committed.
- Sign-in is NOT in the cut: the gate is on at chicago.polecat.live, so a real first visitor runs sign-in.js; only localhost and automation skip it. Deferring it would cut the meter, not the visitor's cost.
