---
id: stressor:surface-soiling
type: Stressor
name: Surface soiling
aliases:
- Soiling
- dust soiling
- Module Soiling
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 20
    unit: unit:PERCENT
  conditions: Annual energy yield loss from soiling; depends on module location and angle of incidence
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.6
    h: a3dffa29110f
  review: disputed
  conflicts_with:
  - stressor:surface-soiling#c3
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 25
    unit: unit:PERCENT
  conditions: Annual soiling loss in arid regions with seasonal dry periods and dust when modules are
    not cleaned
  note: Reported as extreme losses of up to 25%/a.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h50
    h: 74abf1c1a974
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h73
    h: 377b9c8765b6
  review: drafted
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 0
    max: 4
    unit: unit:PERCENT
  conditions: Typical annual soiling loss in temperate regions with rain throughout the year
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h50
    h: 74abf1c1a974
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h73
    h: 377b9c8765b6
  review: disputed
  conflicts_with:
  - stressor:surface-soiling#c1
- claim_id: c4
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Rooftop array in Switzerland near a railway, pollution strip at lower frame edge of landscape
    modules, built up through spring 1998 without module cleaning
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=5.3
    h: 42d2f2c6274f
  review: drafted
- claim_id: c5
  attr: typical_power_loss
  value:
    max: 20
    unit: unit:PERCENT
  conditions: Summarized performance loss across test sites, depending on site and boundary conditions
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h70
    h: d27e8de83a79
  review: drafted
---
Surface soiling is dust, dirt, pollen, bird droppings, algae, moss or other material that settles on the module front surface and blocks light from reaching the cells. The particles scatter and absorb light, so module current and plant output fall; the loss is mostly reversible by cleaning and is not a true module failure. Uneven soiling causes current mismatch and hotspots that in extreme cases can permanently damage a module, and soiling can speed up ongoing potential induced degradation. It drives granular dust soiling losses and general soiling losses, and frequent cleaning or sandstorms can abrade the glass and reduce transmittance over time. Losses are worst in arid regions during dry periods, at low tilt angles, and near sources such as railways, farming, mining, roads or construction; humidity and dew can cement dust to the glass. Soiling can also build up slowly in rainy temperate climates, for example as a dirt strip along the lower frame edge. Exposure is reduced by site selection, higher tilt, anti-soiling coatings suited to the local dirt, and cleaning schedules based on measured soiling rate and cleaning cost. Clean with methods the module manufacturer recommends, because careless cleaning can damage components or anti-reflective coatings.

<!-- review notes
- sentence 5: support check: partial - The passages support arid dry periods, low tilt, nearby sources, and humidity/dew cementation, but they do not say roads, mining or construction make losses worst; the sources are mentioned only as origins or as causes of spatially uneven loss.
- sentence 7: support check: partial - Site selection, tilt, anti-soiling coatings suited to the soiling type, and cleaning optimized by soiling rate and cost are supported, but the passages do not state that higher tilt reduces soiling in those words; u22 only says soiling increases as tilt decreases.
-->
