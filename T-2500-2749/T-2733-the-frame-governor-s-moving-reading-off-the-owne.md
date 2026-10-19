---
id: T-2733
title: The frame governor's moving reading off the owner's phone: the Read frame pacing result copied back and filed, sd and p95 fallen (or not) for walk, turn and flight under Adaptive against Fixed
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2722
opened: 2026-10-17
closed: 2026-10-18
pr: 1056
claimed_by: run 10/18/2026, 7:56:53 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-19T02:17:25Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39181954116
claimed_at: 2026-10-19T00:56:53.810Z
decision: null
decision_answer: null
---

The frame governor's moving reading off the owner's phone: the Read frame pacing result copied back and filed, sd and p95 fallen (or not) for walk, turn and flight under Adaptive against Fixed.

Piece 2 of 2 of **T-2722 — Frame governor's moving reading on a GPU: frame-time sd and p95 fall for walk, turn and flight at light on the phone profile, read on hardware whose frame costs tens of milliseconds (a GPU runner or the owner's phone)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2722 was split (2026-10-17T18:21:54.818Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/17/2026, 1:19:48 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39057123887) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39057123887) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass) — see "The reading" below; the acceptance there replaces this line.

## The reading — the owner's phone, 2026-10-19

Taken by the owner with T-2732's Read frame pacing on the dev preview and pasted back into the thread
that filed it. He was asked to open `/4d/dev/1835/`, so this is the 1835 scene; the readout does not
print the scene or the renderer's pixel ratio (`ratio 3` is the phone's devicePixelRatio — the render
ratio is capped by Sharpness at 1, 1.5 or 2). Verbatim:

```
Read frame pacing (T-2733) — 2026-10-19T00:37:59.075Z
375x636 (screen 375x812) at ratio 3, detail light, 5 s a mode
Mozilla/5.0 (iPhone; CPU iPhone OS 27_0_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/155.0.8059.37 Mobile/15E148 Safari/604.1
build 0.1.0

move    mode      draws  mean    sd   med   p95   max  >33 >50
walk    fixed       163  30.8   6.0  29.0  43.0  59.0   34   3
walk    adaptive    161  31.3   5.0  30.0  41.0  46.0   47   0
  FELL: sd 6.0 → 5.0 ms, p95 43.0 → 41.0 ms
turn    fixed       186  27.1   4.7  27.0  37.0  44.0   16   0
turn    adaptive    157  32.0   6.5  32.0  41.0  73.0   56   3
  DID NOT FALL: sd 4.7 → 6.5 ms, p95 37.0 → 41.0 ms
flight  fixed       162  31.0   3.9  31.0  38.0  45.0   42   0
flight  adaptive    161  31.2   5.0  30.0  41.0  49.0   48   0
  DID NOT FALL: sd 3.9 → 5.0 ms, p95 38.0 → 41.0 ms
```

**What it says.**

- **T-2592's acceptance is not met on this phone.** Adaptive lowered both sd and p95 for **walk** only
  (sd 6.0 → 5.0 ms, p95 43 → 41 ms, frames over 50 ms 3 → 0, max 59 → 46 ms). For **turn** both rose
  (sd 4.7 → 6.5, p95 37 → 41, max 44 → 73 ms, three frames over 50 ms where Fixed had none); for
  **flight** both rose a little (sd 3.9 → 5.0, p95 38 → 41).
- **The phone does not hold 60 at Light even on Fixed**: means of 27–31 ms (about 32–37 fps), medians
  27–31 ms. Adaptive's job there is to pace to 30 fps; its medians sit at 30–32 ms, so it is pacing, but
  the turn reading shows the pace or scale switching making turns less even, not more.
- **Adaptive is the default** (`#s-governor`, first option), so visitors get the setting that made
  turning worse here. One 5-second sample per mode (~160 draws) is a thin reading; a longer one would
  settle whether turn and flight are noise or real.
- Production readers of "walking is laggy" are seeing ~30 fps with p95 near 40 ms on this device.

**Acceptance (rewritten 2026-10-19 now that the reading exists — no hardware needed):**

- [ ] The reading above committed verbatim with its date and device to `docs/measurements/t-2733-owner-phone-1835.txt` (and its rows as JSON beside it), and the verdict — walk fell, turn and flight did not — written into RENDERING.md's frame-governor section, so T-2592 closes as *read, not met* rather than silently.
- [ ] `js/pacing-read.js`'s readout prints the scene year and the renderer's actual pixel ratio (and the Sharpness stop) beside the device ratio, and offers a longer run (e.g. 15 s a mode), so the 1904 reading (T-2719) and any repeat are attributable and less noisy.
- [ ] **Per-scene poses** (owner's 1904 attempt crashed, 2026-10-19 — T-2828): `poseFor` only knows 1835 anchor ids, so in 1904 every move fell back to the `glessner_house` anchor and the walk went due west across Prairie Avenue into the Glessner front. Each scene gets its own walk (in 1904: along the Prairie Avenue sidewalk, north–south, parallel to the street), turn and flight poses, and no pose ever enters a structure footprint (a test walks each scene's poses against the footprints).
- [ ] One follow-up filed with this reading attached: why Adaptive makes **turning** less steady on the owner's phone (max 73 ms, sd up 38 %), and whether Adaptive should stay the default until it does not — a decision card for the owner if the answer is to change the default.
