---
id: T-1594
title: A step label in check.sh carries backticks inside double quotes, so every gate run prints a bash syntax error to stderr and the label loses the word it quoted
state: done
epic: META
requested_by: loop
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: 58
claimed_by: run 9/25/2026, 8:28:35 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-26T02:26:36Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36208278578
claimed_at: 2026-09-26T01:28:35.159Z
decision: null
decision_answer: null
---

A step label in check.sh carries backticks inside double quotes, so every gate run prints a
bash syntax error to stderr and the label loses the word it quoted.

## The measurement, 2026-09-25

Every `./tools/check.sh` run on this runner prints, to stderr, before any step:

```
./tools/check.sh: command substitution: line 2270: syntax error near unexpected token `done'
./tools/check.sh: command substitution: line 2270: `done'
```

The cause is T-1548's step label, which quotes a verb name in backticks inside a
double-quoted string, so bash reads the backticks as a command substitution and tries to
run `done` as a command:

```
selftest "…and the tripwire scanner behind `done` still fires, and still ignores prose" \
  node tools/ticket.mjs tripwire-self-test
```

Two consequences, both small and both real:

* the label the gate prints and records has a hole in it where the word `done` should be —
  the step reads "…and the tripwire scanner behind  still fires", so the transcript names a
  step by a label that is not the one in the file;
* the gate writes bash's complaint to stderr on every single run, and the gate's own
  contract is that "every transcript line is tagged, stderr included" — this one is not,
  because it is emitted while the file is being parsed, before any step exists to tag it.

It has been there since T-1548 and is harmless to the verdict: the substitution fails, bash
substitutes the empty string, and the step still runs. It is noise in the one output a run
is told to read.

**Acceptance:** the label quotes the verb in a way bash does not expand — single quotes
around the whole label, or `\`done\`` escaped — the printed label contains the word
`done`, and a `./tools/check.sh` run on a clean tree writes nothing to stderr that is not
tagged. Grep the rest of check.sh for the same shape while there: any other step or
selftest label with an unescaped backtick pair has the same two faults.
