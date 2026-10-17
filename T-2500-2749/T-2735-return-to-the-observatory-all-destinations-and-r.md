---
id: T-2735
title: Return to the Observatory: All destinations and Recall ask first, then a light reverse ring carries you back
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-17
closed: 2026-10-17
pr: 987
claimed_by: run 10/17/2026, 1:23:55 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T20:09:13Z
claimed_run: null
claimed_at: 2026-10-17T18:23:55.666Z
decision: null
decision_answer: null
---

Return to the Observatory: All destinations and Recall ask first, then a light reverse ring carries you back.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The owner asked for it in the project thread 'Return to the Observatory' on 2026-10-17; no band-3 ticket covers a confirm or a reverse ring on the way home (T-2655 shipped Recall as a plain link).

**Owner, 2026-10-17, project thread "Return to the Observatory":** *"when you click on all destinations, there should be a verification that you are about to return to the temporal observatory, and have a light reverse time travel circle sequence like you have from before when you are traveling to but check first"*.

## What to build

Every way home from a destination (the arrival card's "← All destinations", the Jump app's Recall key, the
stalled-jump BACK TO THE OBSERVATORY) goes through one recall step instead of a bare link:

1. **Confirm first.** A small in-world prompt in the machine voice: TEMPORAL RECALL, "Return to the
   Temporal Observatory?", what you leave (the destination year), with CANCEL and RETURN. Esc or a tap
   outside cancels. Styled by each machine skin. The stalled-jump button skips the question (there is
   nothing to lose there) but still plays the ring.
2. **Then the reverse ring.** The outbound transfer's rings run backwards (large and faint, converging
   to the centre) with the sequence lamps reading Arrive › Lock › Scan in reverse, about a second, and the
   page goes to the Observatory. The journey moves to `recall` only on RETURN, so CANCEL leaves the scene
   exactly as it was.
3. **The Observatory picks up the tail**, as T-2615 does on the way out: a page opened within 10 s of a
   recall stamp opens with the ring's last contraction settling, so the trip home reads as one shot.

Reduced motion skips both animations and keeps the confirm.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Clicking "← All destinations" or Recall shows the confirm; CANCEL keeps you in the scene with the journey state unchanged; RETURN plays the reverse ring and lands on the Observatory.
- [ ] Works on a 390x844 phone (iPhone Chrome sized) and a 1440x900 laptop, in all four machine skins, and with reduced motion (no animation, confirm kept).
- [ ] The 390x780 mobile smoke (the release gate) passes; every element id the smoke reads is preserved.
- [ ] A changelog.d/T-2735.json entry says what a visitor will see.
