---
id: T-2672
title: AGENTS.md's standing constraint rewritten to the owner's 2026-10-16 rulings: human figures drawn once the portable-humans pipeline renders them, and Native and Metis people depicted on informed, evidence-bounded judgement
state: review
epic: META
requested_by: owner
seen: true
effort: XS
legacy_id: null
parent: null
opened: 2026-10-16
closed: null
pr: 1046
claimed_by: generic-human-policy 10/18/2026, 3:41:27 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T20:41:27.871Z
decision: null
decision_answer: null
---

AGENTS.md's standing constraint rewritten to the owner's 2026-10-16 rulings: human figures drawn once the portable-humans pipeline renders them, and Native and Metis people depicted on informed, evidence-bounded judgement.

## The owner's words (2026-10-16, in the thread that filed the Navigator tickets)

> "I think human figures are ok once we are able to render them and go through those tickets"

> "And I think ok to for native and Métis depictions based on your fair and reasonable judgement, you have been careful and I trust you to make informed and reasonable depictions"

## What to change

`AGENTS.md` § "Standing constraint — 1835 and Indigenous history" (and every place that restates it:
the L1 line in the 2026-09-17 ruling paragraph, "Blocked on the owner … the L1 constraint", the queue
header in chicago-tickets `QUEUE.md`, and any check that refuses a figure outright).

- **L1 is lifted for the portable-humans path.** Human figures are drawn once the portable-humans
  tickets (band 8C: T-1789, T-1790, T-1791, T-1792) can render them; until a figure renders through
  that pipeline, none is drawn. It applies to everyone uniformly, as before.
- **Native and Métis people may be depicted**, on the project's own informed, fair and reasonable
  judgement, as the owner ruled. Keep what makes that judgement informed: the Newberry Indigenous
  Chicago curriculum and the committed research stay the starting point; depictions are
  evidence-bounded; where evidence is thin a depiction is Reconstructed and listed in
  `docs/LIBERTIES.md` like any other choice; no invented dialogue or ceremony presented as attested.
- **Unchanged:** the scene-date rule — the great Potawatomi gathering and the last war dance are
  August 1835, after the 1 July scene date, and are not staged in it (hard rule 3). Black residents,
  families and businesses stay identified on the `community` field.
- **`review_required`** stays on records as the sentence saying why care was taken
  (`tools/measure_review_constraint.py` keeps passing), but **it no longer blocks a scene from being
  marked `released`** — owner, 2026-10-16, asked whether the trust ruling lifts that too: *"Yes lift
  that"*. Remove the blocking sentence from AGENTS.md and the block from any tool or gate that enforces
  it (search for `review_required` with `released`), keeping the flag and its prose.
- Quote both rulings verbatim in AGENTS.md with their date, the way the 2026-09-17 ruling is quoted.

Do this before any figure lands in a scene: T-1789 onward read AGENTS.md.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] AGENTS.md's standing constraint states both 2026-10-16 rulings verbatim and the rules above; no line elsewhere in AGENTS.md still says no human figure is ever drawn.
- [ ] check.sh passes (the review-constraint measure included); no tool or gate refuses `released` because a record carries `review_required`, and a test shows a flagged record no longer blocks it.
- [ ] The chicago-tickets `QUEUE.md` header's standing-rule line matches (pushed with `ticket.mjs sync`).
