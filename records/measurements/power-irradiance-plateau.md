---
id: meas:power-irradiance-plateau
type: Measurement
name: Power plateau at high irradiance
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power flattens at a constant ceiling as irradiance keeps rising
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance continues above the level where power stops increasing
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 0.05
    unit: unit:PERCENT
  conditions: Annual energy loss from inverter power limitation for one example PV plant, deduced from
    measured data by PR extrapolation (PR 200-900 W/m² vs 900-1200 W/m², weighted by irradiation).
  note: Plateau visible above 897 W/kWp specific AC output in the 5-min scatter of the same system.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 0.03
    unit: unit:PERCENT
  conditions: Simulated inverter limitation loss for the same example system at its actual PV-to-inverter
    ratio of 1.12.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
---
On a scatter of AC power against plane-of-array irradiance, this signature is a flat ceiling: at high irradiance the points stop rising and level off at a fixed power. The usual cause is inverter clipping, also called inverter power limitation, which happens when the inverter is rated below the installed module power. Cold, sunny conditions make this limit most likely, because that is when the array can produce more than the inverter's rating. In one example system using 5-minute averages, the limit showed up above 897 W/kWp of specific AC output. The lost energy cannot be measured directly. One way to estimate it is to compare the performance ratio between 200 and 900 W/m² (89.5%) with the ratio between 900 and 1200 W/m² (88.4%), where clipping occurs. Before reading the plateau, use a reliable plane-of-array irradiance sensor, because sensor or mounting errors move the points sideways.

<!-- review notes
- sentence 1: support check: partial - Figure 37 shows limitation in specific AC output vs irradiance, but the passages do not explicitly describe a flat ceiling leveling off at a fixed power.
- sentence 2: support check: partial - The passages say inverters are underrated relative to module power and may limit output (power limitation, clipping in Fig 27), but 'usual cause' of a plateau is not stated.
- sentence 3: support check: partial - Cold and sunny conditions are said to cause limiting, but the explanation that the array then produces more than the inverter rating and the 'most likely' claim are not stated explicitly.
- sentence 6: support check: partial - The passages list irradiance sensor calibration and mounting not in plane as error causes and recommend POA pyranometers, but do not say these errors move points sideways or tie this to reading the plateau.
-->
