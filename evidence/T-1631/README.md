# T-1631 — the flooded horizon, before and after

Frames referenced by kevinrhaas/chicago PR #89. They live here rather than in the code
repo because the code PR must stay one revertible unit of renderer change, and because
this is a ticket record.

Pose, both frames: free-fly, local `e 120, n -420`, altitude 183 m (600 ft), yaw 0
(north), pitch −8°, desktop 1280×800, animation clock held, HUD hidden. That is the
owner's own reported view over the South Division river front.

| file | what it is |
|---|---|
| `before-fly-north-600ft.png` | as shipped. The ground past the town converges on sRGB (136,163,192) — 31 luminance BRIGHTER than the (103,131,165) sky above it — so it reads as a flat sheet of open water with the far timber standing in it. |
| `after-fly-north-600ft.png` | the haze pointed at the scene's own north horizon sky. The same pixel reads (100,126,157), just below the sky. The bright band and the hard step are gone. |
| `after-fly-east-lake.png` | the same pose turned east. The lake still reads as lake and the near prairie still reads green — the acceptance's second half. |

Reproduce the readings with the fog switched off and the same pixel reads (109,125,84),
green: the ground was drawn the whole time and the reach was never the fault.
