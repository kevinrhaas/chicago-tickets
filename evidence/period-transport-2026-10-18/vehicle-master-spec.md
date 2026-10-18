# T-2792 — vehicle master specification, first pass

Parent epic: T-2791. Date: 2026-10-18. Status: **design artifact only**; no new
vehicle geometry, glTF export, historical photo match or runtime integration has
been completed by this document. Research context: [carriages.md](carriages.md).

## First masters and the evidence boundary

**W01: reconstructed 1835 farm-box wagon.** Begin with the committed wagon form in
`chicago/chicago/4d/data/yard/town_trade_goods.json` and mechanics in
`renderers/web/js/yard.js`. Make a portable articulated master of the existing
declared reconstruction. This is an implementable first static vehicle and a
compatibility target for current placements. It is not a replica of a particular
surviving wagon. No rights-pending photograph needs to be traced or sampled.

**C01: reconstructed open four-wheel passenger-carriage study for 1904.** Use an
independently designed procedural prototype with a single-horse shaft interface,
two-person seat and front steering assembly. Its first numeric envelope below is
an engineering starting point, explicitly reconstructed, not measured from the
Clarke/Chrimes or other rights-pending photographs. The selected open-carriage
family is motivated by the reviewed local evidence, but no pixels, silhouettes,
decorative designs, textures or extracted measurements from those photographs
are authorized as asset inputs. Source/rights work should then select an eligible
documented subtype and revise the study before a period-accurate or photographic
quality completion claim. Do not name it a Pullman, Chrimes, manufacturer or museum
replica. The Pullman-location enclosed carriage is a later distinct candidate,
pending high-resolution identification; it is not silently converted into C01.

This sequence permits useful geometry and rig development while source precision
improves. Neither missing dimensions nor missing ownership attribution stops an
honestly labeled independent reconstruction. Rights-pending source derivation
remains excluded.

## Parameter and material ledger

All numbers are metres unless stated. Bounds below are prototype design envelopes,
not statistical historical confidence intervals. `attested` is reserved for a
source actually stating a value; none of the carriage dimensions below earns it.

| Master / attribute | First value / rule | Evidence tier and basis | Replacement trigger |
|---|---|---|---|
| W01 box length × width × side height | 3.05 × 1.07 × 0.55 | Reconstructed; existing data declares these numbers invented. | Documented eligible wagon measurement plus an explicit decision to revise legacy proportions. |
| W01 rear/front wheel diameter | 1.37 / 1.07 | Reconstructed legacy renderer values. | Same; retain wheel/contact relation when changed. |
| W01 bed datum | 0.95 | Reconstructed legacy renderer value, not historical ground clearance. | Verified mechanical section and rebuilt running gear. |
| W01 axle fore/aft offsets | ±(3.05/2 − 0.35) = ±1.175 | Derived implementation value; historical tier remains reconstructed. Wheelbase 2.35. | Measured running gear or an explicit prototype revision. |
| W01 tongue length | 2.75 | Reconstructed legacy renderer value. | Period-compatible hitch study; no unsupported claim that every team fits. |
| W01 track | Read exact hub/wheel offsets from existing builder, record separately from body width. | Reconstructed implementation-derived; do not mistake 1.07 box width for track. | Export of a numerically audited prototype. |
| W01 running gear | Bolsters, reach, hounds, kingbolt retained as separate functional assemblies. | Existing code supplies reconstructed sections and derived placements; T-0087 explains the construction. | Verified measured detail, without regressing support/contact. |
| W01 timber/paint/iron | Procedural timber with existing deterministic coat selection; iron hardware as a separately declared material. | Reconstructed; no particular Chicago wagon's wood species, paint color or iron finish established. | Eligible primary color/material evidence. |
| C01 body envelope, excluding shafts/wheels | 2.20 long × 1.20 wide; editable range 1.90–2.60 × 1.05–1.45 | Reconstructed design envelope for prototype seat and running gear; not a photograph measurement. | Dated catalog, measured museum vehicle or another eligible technical source. |
| C01 wheelbase | 1.90; editable range 1.60–2.20 | Reconstructed engineering choice within current body envelope. | Same. |
| C01 wheel-center track | 1.40; editable range 1.25–1.60 | Reconstructed engineering choice, independently parameterized. | Same; solve wheels, body clearance and turn envelope together. |
| C01 rear/front wheel diameter | 1.10 / 0.90; range 1.00–1.30 / 0.80–1.10 | Reconstructed first geometry; no established manufacturer/type inference. | Same. |
| C01 footwell/seat top above ground | 0.55 / 1.00, subject to collision/occupancy study | Reconstructed ergonomic prototype datums, not historical dimensions. | Measured vehicle and portable-human seating test. |
| C01 usable seat width/depth | 1.00 / 0.45 | Reconstructed two-person prototype; occupants are not shipped by this parcel. | Human contract + eligible vehicle section. |
| C01 shaft length and spacing | 2.20 ahead of front gear; 0.75 inner spacing initially, both editable | Reconstructed coupling study only. Horse clearance must determine final values; do not scale the horse to fit. | Horse/harness rig integration and period source. |
| C01 suspension | Independent spring placeholder with front/rear attachment metadata; no named spring design claimed. | Reconstructed study; historical construction unresolved. | Dated measured reference before faithful finished carriage acceptance. |
| C01 wood/metal/upholstery/paint | Separate procedural material slots; neutral dark paint and unpatterned upholstery for inspection. | Reconstructed choices. A monochrome image cannot attest pigment or upholstery hue. No source-image texture. | Rights-cleared period material/color evidence or explicit bounded reconstruction decision. |

Do not copy generated assets into `assets/` without the project's license entry and
per-attribute provenance/liberty records. Distinguish a license for our authored
mesh/materials from the rights on reference photographs.

## Coordinate and glTF interface

Match `docs/HUMAN-ASSET-CONTRACT.md` and the parallel horse contract: glTF right
handed, Y up, forward +Z, travel/anatomical left +X; metres baked into vertices;
node scales `[1,1,1]`. Root is ground level at the midpoint between front and rear
axle stations, with the straight-running wheel-center line symmetric across X.
If axle radii differ, each axle's Y is its own unloaded radius. A heading in the
project's geographic bearing convention maps to actor yaw
`Math.PI - headingDeg * Math.PI / 180`. Verify with the actual loader before shipping.

Proposed stable node names (not claims about existing files):

```text
vehicle_root
  vehicle_body
    vehicle_seat_driver
    vehicle_seat_passenger_01
    vehicle_board_left
    vehicle_board_right
    vehicle_camera_ride
  vehicle_running_gear_rear
    vehicle_wheel_rear_left
    vehicle_wheel_rear_right
  vehicle_steer_front
    vehicle_wheel_front_left
    vehicle_wheel_front_right
    vehicle_drawgear
      vehicle_hitch_single
      vehicle_hitch_team
  vehicle_collision
```

This is a conceptual hierarchy. Preserve real mechanical attachment if evidence
requires a body-mounted shaft, independent pole or different front gear: declare
the difference in metadata rather than forcing an incorrect hierarchy. Hidden
boarding/seat/hitch nodes are empty transforms, not source-authenticated hardware.

- Wheel pivot: wheel center, axle local X; rolling rotation around X. Record
  signed rolling convention per node and verify forward travel visually. Do not
  assume mirrored node transforms preserve the same sign.
- Steering pivot: kingpin local Y; initial wheels straight at angle zero.
  Provisional steering limit ±25°, marked reconstructed, then reduced if the swept
  wheels collide with the body. Do not claim ±25° is a measured historical limit.
- `vehicle_hitch_single` and `vehicle_hitch_team`: +Z toward horses, +Y up; metadata
  identifies selected hitch, unloaded/loaded pose, attachment height, spacing and
  compatible harness family. An unused interface is disabled, not a second visible
  hitch. Wagon tongue/pair and carriage shafts/single are separate configurations.
- Vehicle root translation is actor driven; clips do not move the root. Wheel
  rotation derives from path distance `angle = distance / radius`. Front steering
  follows a mechanically bounded turn solution. Body pitch/suspension and pole/shaft
  movement must not fight the horse root transform.
- Rig namespace stays `vehicle_*`; horse nodes stay in the horse namespace. A
  coupling record maps frames; no animation looks up another asset's guessed bone.
- Suggested sidecar fields: `asset_id`, `revision`, `scene_eligibility`, `units`,
  `forward_axis`, `root_datum`, `wheelbase_m`, `track_m`, `wheel_radii_m`,
  `steer_pivot`, `steer_limits_deg`, `hitch_profiles`, `seats`, `boarding_points`,
  `collision_shapes`, `materials`, `lods`, `source_attributes`, `liberties`.

## Measurable acceptance matrix

Thresholds are proposed engineering criteria for implementation review, not claims
that a check already exists or passed. Evidence-sensitive values remain adjustable
before implementation; completion must report the actual measured results.

| Gate | Measurement / required result |
|---|---|
| Provenance | Every modeled attribute has a tier and source or bounded liberty; zero invented citations; zero rights-pending image-derived texture/tracing inputs. |
| Units/root/axes | Inspector reports metre units, scale1, +Z forward, Y up; ground root and declared axles agree with generated data within 1 mm. |
| Dimension fidelity | Exported envelope, wheelbase, track, wheel radii and sockets agree with chosen parameter values within 1 mm; reconstructed does not mean arbitrary export drift. |
| Mechanical static integrity | Wheels touch flat ground within 2 mm in unloaded inspection pose; zero unsupported floating box; every axle/body connection visible or declared hidden member. |
| Steering | Sweep zero to both declared limits; no wheel/body or shaft/body mesh collision; report actual limit and swept footprint. |
| Rolling | On a straight ten-wheel-circumference test, each wheel turns ten revolutions within 0.1%; no visible skating. This is a later animation gate, not static-master completion. |
| Coupling | Selected horse/harness sizes fit at walk-ready pose without scaling either asset; record collar/trace/shaft/pole clearances and any reconstructed adjustments. Later integration gate. |
| Static migration | Instance IDs/counts/coordinates/kinds/paint seeds remain equal to the committed baseline unless an explicit reviewed migration states every change. |
| Visual review | Same-camera near (approximately 3 m), mid (15 m), distant (60 m) renders; inspect wheel/suspension silhouette, joinery, material response and aliasing. Record focal length and actual distance. |
| Photo fidelity | When an eligible documented reference is selected, compare actual pixels at a solved/declared camera and log unresolved visible differences. Prototype renders cannot close photographic-quality acceptance. |
| Budgets | Record triangles, materials, draw calls, bytes and peak visible instances for each LOD on desktop/mobile; propose budget after measurement rather than weakening period detail silently. |
| Boarding | Empty sockets accessible and collision-tested before humans; visible seating/riding only after human/horse dependency checks and applicable depiction rules. |

## Preserve and migrate the static wagon layer

1. Snapshot current committed record semantics: 80 trade-goods wagons (25 farm_box,
   17 covered, 38 cart), their stable IDs/positions/bearings/paint seeds, plus the
   separate water-cart record. Measure runtime visible counts independently.
2. Export W01 beside the current renderer behind a development selection. Keep
   the old layer as the comparison baseline; avoid double drawing the same wagon.
3. Compare one representative of every kind at identical transforms. Preserve
   ground sampling, existing stand-refusal logic and static unhitched tongue pose.
   A new root datum must have an explicit placement adapter; never offset terrain
   to disguise the conversion.
4. W01 replaces only eligible farm_box instances at first. Covered wagons, two-wheel
   carts and water carts retain their existing builder until separate compatible
   masters exist. A passenger carriage is not substituted for a freight wagon.
5. Keep per-instance/source identity separate from mesh sharing. Reuse compatible
   static geometry/LODs where beneficial; moving wagons get actor state instead of
   rebuilding the whole static yard buffer every frame.
6. Promote selected instances to mobile actors explicitly. Remove their static
   duplicates, preserve IDs/provenance and hold the rest unchanged. Route logic must
   respect scene chronology and collision; a parked 1835 wagon does not become
   1904 traffic merely because a new master is available.

## Source and rights register still open

| Lead | Current knowledge | Unresolved operation |
|---|---|---|
| LoC `LC-DIG-det-4a08065`, item `2016801921` | No known restrictions in committed record; carriage at Pullman-house kerb; 1893–1901 local bounds. | Retrieve high-resolution original and current institutional rights statement; identify body class. Owner/maker unknown. |
| LoC companion `4a08066`, item `2016794585` | Context reviewed, c1900; no useful equivalent vehicle detail found. | Context only unless higher resolution changes finding. |
| Clarke/Chrimes `a19-gh-clarke-wabash-chrimes` | Clear open carriages: right single, left team count unresolved; after 1872, exact date unknown. | Museum provenance, precise dating and rights. No derived asset input while unresolved. |
| McBirney `a16-ghm-blog-1736-mcbirney-c1890` | Visible J. P. SMITH & CO. ICE wagon with paired draft horses. | Original accession, rights, vehicle dimensions/date; business lettering does not identify manufacturer. |
| `a20-glessner-2100-block-east-side-1890s` | Single horse, enclosed carriage in street profile; 1890s local dating. | Source original, rights and carriage subtype. |
| Trowbridge Green Tree | Retrospective1902 depiction of1835, locally `check_required`; ledger describes wagons. | Open actual source image and resolve rights before derivation; do not call it contemporary1835 photography. |
| Manufacturer/museum technical source | Not yet recovered for C01. | Obtain a dated, eligible section/measurement record to refine independent prototype and support final historical claims. |

External LoC retrieval through the inherited proxy returned403 during the source
audit. A saved network configuration draft does not establish applied access. Retry
after the supported runtime policy changes; preserve TLS verification. Meanwhile
W01 and the independently reconstructed C01 engineering study can proceed under
the stated provenance/rights boundaries. This document closes no modeling ticket.
