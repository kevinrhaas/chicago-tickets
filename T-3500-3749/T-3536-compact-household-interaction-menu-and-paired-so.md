---
id: T-3536
title: Compact household interaction menu and paired social breaks
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-10
closed: 2026-11-10
pr: 1922
claimed_by: run 11/10/2026, 9:01:59 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-10T21:45:20Z
claimed_run: null
claimed_at: 2026-11-10T15:02:01.288Z
decision: null
decision_answer: null
---

The owner wants long activity buttons collected under Interact, with short labels
and icons. A requested discussion should pair people already outside or bring a
companion through a door, then let them resume their duties. Normal outdoor
activities remain available beyond their usual time slots; Go inside and existing
jaunts remain available.

**Acceptance (recorded from the owner's follow-up):**

- Multiple actions collapse under Interact, with short labels, icons, keyboard
  access and a list that fits a phone viewport.
- Requested and scheduled 1904 discussions reserve an available companion,
  preferring someone outside and otherwise bringing one out through a door.
- Both people meet before speaking, take turns and return to their daily duties
  afterward. Go inside, greetings and jaunt takeover release the pair.
- Household chores keep residents occupied; the coachman retains his logical watch.
- Door calls and requests for normal outdoor activities remain available.
- The published phone and desktop interactions and required repository checks pass
  before the PR merges into dev.

**Implementation / verification:** PR #1922. The published 23:00 phone and desktop
probe passes for compact controls, real meetings, returns indoors and Go inside.
An unrelated driver joining the roster exposed a cancellation; the fix preserves
resident state, with a regression that fails before it and passes afterward.
All four final local gate partitions, preflight, and standard PR checks pass.
The full final-runtime smoke passes all 15 stages on both viewports: 1,655
assertions across 16 successful jobs. Its first desktop 14–15 attempt passed
164 checks but failed the zero-page-error check on an external reference thumbnail;
the unchanged full-stage rerun passed all 165 checks. Both readings remain in the
verification record. Final PR checks also pass on receipt commit `b848f1e6e0bf`.
The source-bound receipts are in
`docs/RESEARCH/household-interactions-3536/README.md`.

**Merged into dev:** [PR #1922](https://github.com/kevinrhaas/chicago/pull/1922),
merge commit `a137020b15e03310ef2321660fd6125ff7e87de0`.
