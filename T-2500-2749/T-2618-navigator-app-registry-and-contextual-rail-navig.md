---
id: T-2618
title: Navigator app registry and contextual rail: navigator.register with when(ctx) and badge(ctx), icons that slide in and out within 240 ms with a lamp-amber first-appearance dot, at most 10 icons
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-202
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: 940
claimed_by: run 10/17/2026, 12:42:27 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T06:40:37Z
claimed_run: null
claimed_at: 2026-10-17T05:42:27.525Z
decision: null
decision_answer: null
---

Navigator app registry and contextual rail: navigator.register with when(ctx) and badge(ctx), icons that slide in and out within 240 ms with a lamp-amber first-appearance dot, at most 10 icons.

**Navigator Mk II — NAV-202.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2617 (NAV-201) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§06 "The rail: when each app shows", §14 "App registry".
`navigator.register({ id, icon, label, code, when(ctx), badge(ctx), mount(el), unmount() })`.

| App | Shows when |
|---|---|
| Home | always |
| Jaunts | always |
| Inspect | a building is selected, or one is under the reticle within 40 m |
| People | the scene has people records (1835 yes; 1904 the Glessner household) |
| Map, Confidence (icon glows while the view is on), Move, Jump | always |
| Guide, Settings | always, pinned to the bottom of the rail |

At most 10 icons, usually 8. Contextual icons slide in under Jaunts (240 ms slide + glint) with a
lamp-amber dot on first appearance. Switching apps runs a 160 ms "tube warm-up" (scanline sweep and
header flicker); reduced motion uses a crossfade. What's new's dot shows on the Settings icon, never in
the HUD. Apps whose own ticket has not landed register as stubs that mount the existing panel.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-07: look at Glessner House, then away; the Inspect icon appears with the target and leaves 300 ms after the target is lost (unless selected).
- [ ] People shows in 1835 and 1904 (Glessner household) and is absent where a scene has no people records.
- [ ] Never more than 10 icons; switching apps shows the warm-up, or a crossfade under reduced motion.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
