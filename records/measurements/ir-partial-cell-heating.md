---
id: meas:ir-partial-cell-heating
type: Measurement
name: Partly heated cell in IR
aliases:
- Pointed heating
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    min: 10
    max: 20
    unit: unit:DEG_C
  conditions: Temperature gradients on heated cells seen in field IR inspection; judged unproblematic
    at the current stage but may grow during plant operation
  note: Source recommends close observation in regular thermographic inspections.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h58
    h: df4b70555c37
  review: drafted
- claim_id: c2
  attr: temperature_rise
  value:
    min: 20
    unit: unit:K
  conditions: Example field IR image of a hot spot (figure caption)
  note: Caption refers to a hot spot in general, not specifically to partial cell heating.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=18
    h: 1af510c888f2
  review: drafted
---
In the IR image only part of a cell runs warmer, a pointed or localized heating, rather than the whole cell warming evenly. Localized hot spots are mainly linked to multicrystalline cells and local junction breakdown, while monocrystalline hot cells tend to heat across the whole cell area. Common causes are partial shading, for example a bird dropping or a lightning protection rod, a cracked part of a cell, or an imaging artifact. When a crack is the cause, the power reduction depends on the shape and size of the cracked part, and a close visual inspection of the cell may reveal the crack. Persistent hotspots are also associated with solder bond defects, soiling shadows, bypass diode behaviour or mismatch that drives part of the module into reverse bias. Image modules under load in steady state on a clear day with low wind, at a minimum of 700 W/m2 per one source or above 600 W/m2 per another, and compare short circuit, open circuit and maximum power point conditions where possible. Heated cells with temperature gradients of 10 to 20 °C are considered unproblematic for now but should be watched in regular thermographic inspections.

<!-- review notes
- sentence 1: support check: partial - The u6 row gives 'Pointed heating' as the pattern, but the passages don't explicitly state that only part of a cell is warmer rather than the whole cell, and u14 describes hot cells as homogeneous.
-->
