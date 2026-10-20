---
id: mit:tilt-optimization
type: Mitigation
name: Module tilt optimization
aliases:
- Tilt angle selection
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 34
    unit: unit:PERCENT
  conditions: Annual snow-related energy loss at zero tilt for unobstructed systems
  quote: annual energy losses decreased dramatically, from 34% to 5%, as tilt angle increased from zero
    to 45 degrees for unobstructed systems
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h106
    h: efd9dc81521c
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Annual snow-related energy loss at 45 degree tilt for unobstructed systems
  note: Same study as the 34% figure at zero tilt; shows the effect of steeper tilt on snow losses.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h106
    h: efd9dc81521c
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
---
Module tilt optimization means picking or changing the module tilt angle so that a site loses less energy to soiling and snow while its yield goes up. For soiling losses, guidance says to set tilt together with cleaning schedules and anti-soiling measures, based on the measured soiling rate and cleaning economics. Soiling loss depends strongly on tilt and is lowest at a vertical 90 degree mount, partly because gravity helps keep dust from settling. For snow accumulation losses in cold regions, steeper tilt is one of the main recommended measures. One study found annual snow losses fell from 34% at zero tilt to 5% at 45 degrees for unobstructed systems. Tilt is usually chosen from angle-of-incidence and inter-row shading calculations. For grid-connected fixed structures it should give the most energy over a whole year. On a fixed roof area with set row spacing, a simulated change of tilt and module orientation raised specific yield by about 4% for one system and about 3.5% for another, at almost no extra cost. Limits: how tilt affects snow shedding is still not well understood, vertical arrays bring shading and structural problems at scale, and roof systems may need a minimum slope to keep their fire class rating. Make tilt or design changes only where the economics justify them, and track winter snow residuals separately from general soiling.

<!-- review notes
- sentence 1: support check: partial - Passages list module tilt as a soiling/snow mitigation, but don't define it or say yield rises as a result.
- sentence 4: support check: partial - Steeper tilt angles and the 34%→5% figures are stated, but 'one of the main recommended measures' for cold regions is only a promising consideration among several.
-->
