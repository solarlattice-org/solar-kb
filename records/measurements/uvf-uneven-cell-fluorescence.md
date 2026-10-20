---
id: meas:uvf-uneven-cell-fluorescence
type: Measurement
name: Uneven cell fluorescence
claims:
- claim_id: c1
  attr: time_to_onset
  value:
    nominal: 1.5
    unit: unit:YR
  conditions: Outdoor exposure in Germany needed to build up a UV dose of about 80 kWh/m², enough for
    a usable fluorescence signal
  note: This is when the encapsulant fluorescence becomes strong enough to image, not when a defect appears.
    Fluorescence is weak in newer modules until then.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.5
    h: da5687053a7f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
The image is taken in the dark, usually at night, with UV light below 400 nm shining on the modules. The camera records the visible fluorescence of the encapsulant, and the modules stay connected and unpowered. Brightness in the image follows how many fluorescent molecules (lumophores) are in the encapsulant. So brighter or darker zones across a cell show areas that have aged or been heated differently. The pattern needs time to build up. The module must have had enough sun exposure, and the result depends on how long it has operated, the climate, and the encapsulant and backsheet types. If part of a cell is isolated by a crack, reverse bias on the part that is still connected raises its fluorescence. Under Cell Cracks, the two areas then look different. With a Cell Interconnection Failure, current flows through only one ribbon. That side of the cell heats more and forms more lumophores, so one side of the cell fluoresces more strongly than the other. Fluorescence fades (photobleaches) along cell edges and cracks where oxygen reaches the encapsulant. Grey zones can also show along the interconnector, which makes nearby cracks hard to read. Very new damage may not show yet, because the signal has had no time to bleach. Modules with UVA-transparent EVA also give weaker results, so check against EL imaging.

<!-- review notes
- sentence 2: support check: partial - Intensity proportional to lumophore concentration is stated, but the inference that brighter/darker zones show areas aged or heated differently is only partly supported (heating mentioned for interconnect case only).
- sentence 4: support check: partial - Table says reverse biasing the non-isolated part increases fluorescence for an isolated cell part, but it does not say the two areas look different under Cell Cracks (though implied).
- sentence 6: support check: partial - Photobleaching along cell edges and cracks via oxygen and grey zones along interconnectors hindering nearby crack identification are stated; however, the passage doesn't say the edge bleaching occurs 'where oxygen reaches' beyond oxygen diffusion via backsheet, which is roughly fine, but is mostly supported.
- sentence 7: support check: partial - New cracks visible only in EL due to no bleaching time and UVA-transparent EVA reducing effectiveness are stated (for drone-based UVF); the advice to check against EL is not explicitly stated.
-->
