---
id: T-1635
title: Past about 1.2 km the plain is still a featureless band: the haze DENSITY, not its colour, is what is left of the flooded horizon
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
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

Past about 1.2 km the plain is still a featureless band: the haze DENSITY, not its colour, is what is left of the flooded horizon.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Filed by T-1631, 2026-09-26, out of its own measurement.** T-1631 fixed the COLOUR the haze
fades to: the fog was pinned at the bar photograph's solar-side horizon sky (L 159.4) while this
scene's own horizon sky runs L 122 due north to L 148 due south, so distance rose out of the air
as a bright sheet instead of receding into it. The fog now samples the scene's own sky and turns
with the view. Measured at the owner's pose (fly, 183 m, yaw 0, pitch -8), the pixel below the
sky/land step went from (136,163,192) — 31 luminance BRIGHTER than the sky above it — to
(100,126,157), just below it. The bright band at the skyline and the hard step are gone.

**What that did not fix, and this ticket is.** Past about 1.2 km the plain is still a
featureless band with the far timber standing in it. That is not the haze's colour, it is its
STRENGTH: `FogExp2` at density 0.00125 leaves a surface 10 % of its own colour at 1,200 m and
3 % at 1,500 m, so the prairie's green is gone well before the modelled ground ends. The scene's
lighting note calls the haze "total by 1500 m" deliberately. From the ground that band is a
sliver at the horizon; from 600 ft it is a third of the frame, which is why the owner saw it
flying and not walking.

**Why it is a separate unit and not a tuning.** Two committed things lean on the haze being
total:

- `docs/LIBERTIES.md` **L17** leans on it to hide the radial ground skirt nothing is claimed
  about. Thin the air and the skirt comes back into view.
- `terrain.js`'s `hazeReachM()` DERIVES the ground cull from the density — the distance past
  which a surface provably cannot move an 8-bit channel, 1,883 m at 0.00125. Lowering the
  density pushes that reach out and draws more ground: at the owner's pose the reach currently
  holds back 186 of 217 tiles. That is a frame-cost question with a measured ceiling on it, and
  T-1631 was explicitly told not to spend it.

So the work here is: decide what this scene's visibility actually is, say what it rests on
(the lighting note's own reasoning, or a source on July haze over the 1835 prairie — there may
not be one, in which case this is a stated liberty and belongs in LIBERTIES.md as one), and
then pay for it — L17 re-argued or the skirt dealt with honestly, and the reach's new cost
measured against the frame budget rather than assumed. If the budget refuses it, that refusal
is the deliverable and should be written down with its number.

**Do not start by turning the density down and looking at it.** The number is load-bearing in
three places and the first question is what it is allowed to be, not what looks nicer.
