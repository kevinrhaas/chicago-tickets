# 1904 Prairie streetscape: what the pictures show (owner ask, 2026-10-27)

The owner, 2026-10-27, thread "Improve 1904 Prairie streetscape", with four pictures (the
Detroit Publishing Pullman view = `a16-pullman-det-4a08065`, his crop of its hydrant, the
c. 1887 Glessner stable end = `a18-gh-cornell-glessner-rear-c1887`, and Taylor 2135 =
`a18-rba-taylor-2135-glessner-ne`):

1. *"i dont need to have those carriage steps at every house. i dont see that in photos of
   prarie anywhere"* — then *"what you keep you should vary them in appearance so that they do
   not look like clones"* and *"they mostly should go i think because i dont see them in
   photos, unless you do"*.
2. *"I do see evidence of streetlamps at the corners of major streets"*.
3. *"there are ramps down into the street. they appear to be stone"*.
4. *"either a thing to tie up horse or a hydrant in front of the pullman house, please research
   and identify that and place them appropriately in the prairie ave district"*.
5. *"on the houses that are completing or you have done some significant work on them ... make
   sure that you have their walkways to their house correct and the front gate/fence/borders
   and side fence/borders etc are correct photographic match ... others are missing, cant
   enter, or are just plain wrong"* — and to make sure of it for the future.
6. *"there also appears in some places to be some electrical poles? look at the glessner photo
   and validate that and where they would go. they seem like not on main prairie ave"*.
7. *"plants in front of the houses they seem to be missing flora on the property"*.

Every picture named below is in the image store:
`https://raw.githubusercontent.com/kevinrhaas/chicago-images/main/prairie-1904/files/<id>.jpg`
(github.io is proxy-blocked in cloud containers; raw.githubusercontent.com is not). Records:
`chicago/prairie_1904_v1/research/images/stream-*.json` in kevinrhaas/chicago. Read the
pictures themselves, not these notes.

## 1. Carriage blocks: the 2026-10-13 reading was wrong

T-2474 put a 3 x 2 ft carriage block at the curb of every lot 40 ft or wider (91), citing the
Flinn/Picturesque Chicago sidewalk photograph and the 1905 *Views of Chicago* plate. Read again,
both show the **lot-line coping** (Glessner's rounded-top granite curbing; a row of rounded stone
copers along the walk's inside edge) and not blocks at the curb. The Pullman views
(`a16-pullman-det-4a08065`, `st-randmcnally-1910-pullman-corner-18th`,
`a16-ghm-blog-pullman-completed`) show the parkway edge clear.

Where a picture does show stones at the curb or the walk, keep them, each to its picture:

| id | what | where |
|---|---|---|
| `a20-chicagology-2110-rees-street-c1895` | a row of round-topped stone posts at the east curb (right edge) | east side, 2100 block |
| `st-chicagology-prairie-avenue-about-1890-photo` | square stone posts at the curb, right foreground | the website's text puts it on the 1600-1700 east side; block unconfirmed |
| `cgn-1811-coleman-ames-photo` | rock-faced stone blocks either side of the walk at the lot line (a block plus a low coping, not at the curb) | 1811 Prairie |
| `a20-chicagology-2036-street-engraving-1880` | "wooden carriage blocks/benches" (1880 engraving: old) | 2036 Prairie |

So: drop the rule-placed blocks; keep only those with a picture (each at its picture's place,
shape and material: square post, round-topped post, rock-faced block); vary the kept ones
(size, top, dressing, weathering) so no two read as clones. The paved carriage walks across the
parkway are a separate question: the pictures show some (Glessner's, HABS) and not at every lot;
thin them the same way (keep where pictured or where a house's carriage door/drive needs one).
Liberty to amend: L-prairie-carriage-walks-2474.

## 2. Street lamps: gas lamps on cast-iron posts, at corners and along the parkway

Attested at corners: Glessner, 18th & Prairie SW (`a18-rba-taylor-2135-glessner-ne`,
`a18-gh-cornell-glessner-front-c1887`, `a18-gh-1800-block-looking-sw-c1888`); Kimball, 18th &
Prairie SE (`a18-cgy-1801-kimball-early`); Pullman, 18th & Prairie NE (`a16-pullman-det-4a08065`,
`a16-ghm-blog-pullman-completed`: the lamp stands in a curbed grass corner of the parkway);
Tucker, 22nd & Prairie (`a20-chicagology-2140-photo-a`, `-photo-b`, `a20-nypl-dennis-tucker-1010-prairie-stereo`);
the Ward 1887 engraving at 20th (`st-ghm-ward-1887-prairie-north-from-20th`, east parkway corner).
Mid-block: 1811 (`cgn-1811-coleman-ames-photo`, a lamp at the parkway near the house's walk),
1700 (`st-ghm-1700-1706-under-construction-1901`, right edge), 1721 Dexter
(`a16-ghm-blog-1721-dexter-c1888`), 1816 Henderson, 1905 Field, 2120 Gorton, and the right-hand
1905 *Views of Chicago* view (several along one parkway). Electric lamps appear only in pictures
dated after 1904 (`a19-cgy-1912-exterior`, 1919 programme): 1904 is gas.

The post (read off 1811, Taylor 2135 and 2140): a fluted cast-iron column about 2.6-2.9 m to the
lantern's foot on a moulded base, a ladder bar under the lantern, a four-sided tapered glass
lantern with a pyramidal cap and finial; on a small stone footing at the curb corner in Taylor
2135. Place at every intersection corner of the district's streets (the owner's ask, and the
pictures above), plus mid-block lamps at a reconstructed spacing where the pictures show them,
lit at night if the scene has a night (check world.js before building any light).

## 3. The corner crossings and their ramps

`a18-rba-taylor-2135-glessner-ne` (Glessner corner): the walk is carried across the parkway at the
corner to the curb, and two broad slabs slope from the curb's top down to the roadway, one for each
crossing direction, the lamp's footing between them. `a16-pullman-det-4a08065`: flat stone
crossing slabs at the curb at both corners (foreground left and right). The Ward engraving draws
pale stone crossing flags across the intersection. Build at each corner where a crossing meets the
curb: a dressed limestone/granite slab (about 1.5-1.8 m wide) ramping from the curb's top
(7 in reveal, `data/street_section/1904.json`) down to the road surface over about 1.2-1.5 m;
optional flagstone crossing strip across the roadway (the existing per-crossing paving in
`street-grid.js` is where crossings already live).

## 4. The Pullman object is a FIRE HYDRANT

The owner's crop of `a16-pullman-det-4a08065` shows a post hydrant: a barrel about 0.8-0.9 m tall
on a flared foot, a band below a domed bonnet with an operating nut on top, side nozzle caps. The
same hydrant shows in `a16-ghm-blog-pullman-completed` (parkway by the walk on Prairie, north of
the corner); a hydrant of the same type stands on the parkway at 22nd & Prairie
(`a20-chicagology-2140-photo-b`, left foreground) and one is noted at 1936 Prairie
(`a19-cgy-1936-thompson-photo`). Hitching posts are not shown at Pullman. Place: the Pullman one
where the pictures put it (attested), the 2140 one (attested), and the rest at a reconstructed
spacing on the parkway near corners (one per intersection, alternating corners, plus mid-block on
long blocks), in the grass near the curb, never in a walk or crossing.

## 6. Utility poles: on 18th Street and the alleys, not on Prairie

`a18-gh-cornell-glessner-rear-c1887`: a wooden pole with crossarms and insulator pins on 18th
Street's parkway at Glessner's stable (west end of the 18th Street front, near the alley).
`st-ghm-1700-1706-under-construction-1901`: an overhead wire across the 1700 block's front
(service wire, high). `a20-chicagology-2140-photo-a`: trolley wires over 22nd Street (a
streetcar street, `st-uchicago-1902-surface-street-railroads`). No picture shows a pole on
Prairie's parkway. So: wooden poles with crossarms down the alleys and along 18th Street (the
cross streets), wires between them; trolley span wires over 22nd if the street railway map puts a
line there in 1904; none on Prairie's parkway. Poles are inferred (18th: attested at Glessner's
end) and the alley line reconstructed; record a liberty.

## 5. Walks, gates and fences on the worked houses

The K11 kit (`generators/archetypes/k11_frontage.py`, `data/components/prairie_1904/k11_ironwork.json`)
builds each worked house's boundary from its record's `boundary`. The owner reports some are
missing, some cannot be entered, some are wrong. A pass per block, for every K01/K16 house that is
not a draft: find each house's pictures (its stream record, its `data/reference_views/`), and check
(a) a paved walk from the public sidewalk to the door's foot, (b) an opening or gate in the boundary
on that walk that the walker can pass, (c) the front boundary's kind (iron on a coping, stone
coping, low wall, none) and its height, (d) side boundaries and side passages, against the
pictures. Fix in the record and rebake. For the future: a gate step that refuses a worked house
with no walk to its door or no opening in its front boundary.

## 7. Front-yard plantings

Pictures show foundation shrubs and low beds against the fronts (`a16-pullman-det-4a08065`,
`a16-ghm-blog-pullman-completed`, `a16-pullman-det-4a08066` shrubbery along 18th), ivy or
creeper on walls (Pullman, 1912 Moulton-Lowden `a19-cgy-1912-exterior`), urns on stoops, and
mown lawns. Nothing records species or beds per house: lawn + foundation shrubs + a few
beds per lot, varied per lot by seed, is reconstructed; attested specifics where a picture shows them.
