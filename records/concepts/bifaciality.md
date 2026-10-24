---
id: concept:bifaciality
type: Concept
name: Bifaciality
aliases:
- bifaciality factor
- bifacial gain
- bifacial
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:albedo
  note: Rear-side (bifacial) gain depends strongly on ground albedo; high-albedo snow environments favour
    bifacial modules.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=7.2
    h: 6dfea013d08d
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=5.1.2
    h: 262c8de0fd52
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=9.2
    h: d98cb7408bf4
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=9.2
    h: 3db9d4b0fcd4
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h66
    h: 423dacadefd4
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h104
    h: 0efd25269393
  review: drafted
- claim_id: c2
  rel: related_to
  target: fm:soiling-losses
  note: Latitude-tilted bifacial modules soiled more slowly than monofacial ones because the rear side
    collects little dust; the effect grows with higher bifaciality and albedo.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h72
    h: 3c6e7e9ee9a6
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h73
    h: 43622632965c
  review: drafted
- claim_id: c3
  rel: related_to
  target: fm:snow-accumulation-losses
  note: The rear side stays clear of snow and can keep producing; bifacial modules shed snow faster than
    monofacial ones.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h104
    h: 0efd25269393
  review: drafted
- claim_id: c4
  rel: related_to
  target: comp:microinverter
  note: When matching a bifacial module to a microinverter, its temperature-adjusted power, voltage and
    current must fall inside the microinverter's input range.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=7.2
    h: 6dfea013d08d
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=5.1.2
    h: 262c8de0fd52
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=9.2
    h: d98cb7408bf4
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=9.2
    h: 3db9d4b0fcd4
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h66
    h: 423dacadefd4
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:nameplate-rating
  note: Bifacial gain is expressed relative to the module's front-side nominal power rating.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=7.2
    h: 6dfea013d08d
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=9.2
    h: d98cb7408bf4
  review: drafted
---
Bifacial modules make power from both their front and rear faces, which raises total energy output; the extra power from the rear is called bifacial gain. Bifaciality describes how strongly the rear side performs compared with the front; one tested module had a nominal bifaciality of 90%, with 229 Wp on the front and 209 Wp on the back at STC. Bifacial gain depends heavily on design factors such as albedo, module elevation, pitch, temperature and shading, and Enphase gives a range of 0% to 30% of the front-side nominal rating. When pairing bifacial modules with microinverters, the module's temperature-adjusted power, voltage and current must fit within the inverter input range. Older Enphase manuals base this check on front-side values only, while IQ9N manuals require the bifacial gain to be included, following the module maker's guidance. Field studies reported a 14% annual energy gain for bifacial modules over monofacial ones on a two-axis tracker in Vermont, and 5-20% more energy from vertical east-west bifacial arrays in Alaska. Snow-covered ground with high albedo favours bifacial modules: the rear face stays free of snow, and these modules shed snow faster than monofacial ones. Because the rear face collects little dust, bifacial modules lose less energy to soiling than monofacial ones, and vertically mounted bifacial modules showed almost no soiling loss. Shading from the mounting structure can cut rear-side output, so many racking suppliers now design racks specifically for bifacial systems.

<!-- review notes
- sentence 2: support check: partial - The 90% bifaciality with 229 Wp front and 209 Wp back at STC is stated, but the passage doesn't define bifaciality as a rear-versus-front comparison (though the numbers imply it).
- sentence 8: support check: partial - u7 says mounting-structure shading might be an issue and racking companies design bifacial racks, but doesn't say it cuts rear-side output specifically.
-->
