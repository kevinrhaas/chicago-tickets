---
id: T-2446
title: Glessner granite: a cooler greige colour pass, and a URL option to compare stone colours
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: run 10/13/2026, 1:12:22 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-13T06:12:22.888Z
decision: null
decision_answer: null
---

Glessner granite: a cooler greige colour pass, and a URL option to compare stone colours.

**The owner, 2026-10-13, with a photograph of the Eighteenth Street front (carriage door):**
"the stone work is overall lovely but it is a bit more brown than this photo from real life, it's
more grey but not a black and white grey, kind of greige but leaning grey, could you do a color
pass and maybe if not too hard do a Glessner color option on the url to show different options
the default is best you choose but maybe there are a few other versions you think might be close
let's build in so we can see those and then we will finalize a default and then we can move on".

His photograph reads, on lit and shaded stone alike, sRGB red/green about 1.04 and blue/green
about 0.95. After T-2416 (#741) the app reads about 1.08-1.11 and 0.92-0.94: too warm.

**Acceptance:**
- A `?stone=<name>` URL option retints Glessner's granite slots (granite, granite_1..4) at load,
  on the full and the light models, with a handful of named presets near the photograph, and
  one that shows the colour as baked.
- With no option, the app shows the preset chosen as the default, measured in the app against
  the photograph (red/green and blue/green within 0.02 of it on the north wall).
- A sheet sets each preset beside the owner's photograph.
- Once the owner picks the default, a follow-up bakes it into GRANITE_TINT and the option stays
  or goes as he says.
