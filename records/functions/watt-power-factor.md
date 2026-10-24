---
id: func:watt-power-factor
type: Function
name: Watt-power factor
aliases:
- cos phi(P)
- PF(P)
- Watt-PF
- Cosphi(P)
- Watt/Cosphi
- PF_of_P
- Power Factor vs. Power
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: -100
    max: 100
    unit: unit:PERCENT
  conditions: Active power points (independent values) of the PF_of_P curve, as a percentage of nominal
    apparent power, in SMA documentation
  cite:
  - src: src:sma-doc-265222
    loc: tbl=41.r4
    h: 9c98dd7908ea
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 0.8
    max: 1
    unit: unit:UNITLESS
  conditions: Power factor points (dependent values) of the PF_of_P curve, settable from ±0.8 to 1.0,
    in SMA documentation
  cite:
  - src: src:sma-doc-265222
    loc: tbl=41.r4
    h: 9c98dd7908ea
  - src: src:sma-doc-265222
    loc: tbl=41.r5
    h: cb1002511df3
  review: drafted
---
Watt-power factor, also called cos phi(P), sets the inverter's power factor as a function of its present active power output, so reactive power feed-in changes as output changes. The power factor is set according to a configured reference value, and the curve is drawn with active power on the horizontal axis and cos phi on the vertical axis. In SMA documentation the curve is set with the parameter PF_of_P: its active power points run from -100% to 100% of nominal apparent power and its power factor points from ±0.8 to 1.0. FIMER warns that these reactive power parameters should not be changed unless the grid operator asks for it.

<!-- review notes
- sentence 2: support check: partial - The passages say cos phi is specified based on the set reference value, but they don't state the axes (active power horizontal, cos phi vertical) in text.
- sentence 4: support check: partial - The passage says not to change these parameters unless the grid operator requests it, but it doesn't name FIMER as the source in the passage text.
-->
