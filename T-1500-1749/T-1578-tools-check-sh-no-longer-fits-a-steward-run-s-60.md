---
id: T-1578
title: tools/check.sh no longer fits a steward run's 600 s foreground command: 322 and 326 of its 357 steps in two runs at the ceiling, and AGENTS.md still calls it 'seconds'
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-25
closed: null
pr: 51
claimed_by: run 9/25/2026, 3:41:04 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36186957649
claimed_at: 2026-09-25T20:41:04.395Z
decision: null
decision_answer: null
---

tools/check.sh no longer fits a steward run's 600 s foreground command: 322 and 326 of its 357 steps in two runs at the ceiling, and AGENTS.md still calls it 'seconds'.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## MEASURED 2026-09-25, steward slice 3 on T-1572

`./tools/check.sh` was run twice in the foreground, in a GitHub Actions steward sandbox,
each redirected to a file. Both were cut off by the 600 s ceiling a steward run's single
foreground command has:

| run | wall | `== ` step headings reached | of |
|---|---|---|---|
| 1 | `timeout 560` | 322 | 357 |
| 2 | `timeout 585`, `CHECK_TIMINGS` on, mirror already published | 326 | 357 |

Neither transcript carried an untagged `FAIL`; neither reached `check_summary`. So a run
in this sandbox cannot obtain the gate's verdict at all — not a red one, not a green one —
and a PR whose diff check.sh is the only cover for (prose, docs, anything the smoke does
not read) has no local gate available to it.

**Where the time goes**, from `CHECK_TIMINGS` on run 2 — 364 timed steps totalling
**561.2 s**, worst first:

    61.5 s  selftest  placement_policy_1835.py --self-test
    26.3 s  selftest  measure_face_rule.py --self-test
    21.7 s  step      generate_yard_goods.py --check
    20.9 s  step      generate_dooryard_plantings.py --check
    19.6 s  step      test_validate.py
    17.6 s  step      placement_policy_1835.py --check --quiet

The top two are both self-tests, and `placement_policy_1835.py` appears twice for 79.1 s
between them — 14 % of the whole gate in one tool.

**This contradicts the gate's own contract, twice.** `tools/check.sh`'s header says
"Seconds, no Blender, runs in every agent sandbox", and its reason for not building
geometry is stated as "A gate that takes four minutes gets skipped". It is now about
620 s — more than two and a half times the duration its own design note treats as the
point at which a gate stops being run. AGENTS.md § 9 repeats "It takes seconds".

**Why it matters beyond the wording.** `check_harness.sh`'s own note on `CHECK_TIMINGS`
(T-1289) says it: "The gate's duration is the window in which `dev` can move under an open
pull request, so it is the number that decides how much a merge round costs." At 620 s
that window is ten minutes wide, on a lane running three slices.

**Not proposing a remedy here** — whether the answer is a `--since`/`--only` selector, a
cheaper `placement_policy_1835.py --self-test`, splitting the self-tests onto their own
command, or simply amending the contract to match the gate, is the ticket's to decide.
What is established is that the sentence "it takes seconds" is no longer true and that a
steward run cannot run this gate to completion.
