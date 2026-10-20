---
id: mit:shade-resistant-modules
type: Mitigation
name: Shade-resistant module design
aliases:
- shade-resistant PV modules
- shading tolerant module technologies
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: Hot cell temperature compared with module temperature for an IBC half-cell module with built-in
    Zener-type bypass behaviour. Measured in an indoor hot-spot test at 55°C module temperature following
    IEC 61215-2:2021.
  note: The rise was much lower than for PERC and SHJ half-cell modules tested under the same conditions.
  quote: the hot cell temperature of the IBC module was at most 25°C higher than the module temperature
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
Shade-resistant module design means choosing module layouts that tolerate partial shading better. Examples include half-cell modules, shingled modules, back contact cells and modules with a diode built in for each cell. It is a preventive measure against hot cells and hotspots. These form when shading or cracked cells cause current mismatch and push weak cells into reverse bias. Hotspots from prolonged shading can lead to follow-up failures such as burn marks, bypass diode failure, glass breakage, arcing or fire. Shading-tolerant technologies are one way to reduce the final shading loss. Placing fewer cells on each bypass diode lowers the hot cell temperature, because the shaded cell runs at a less negative reverse voltage. In some back contact (IBC) cells, a built-in Zener diode acts as a bypass diode. In an indoor hot-spot test, these cells ran much cooler than PERC and SHJ modules. Shade-resistant design does not remove all hot cell risk. Bifacial modules and larger wafer formats can still produce higher hot cell temperatures. Shading should be addressed at the system planning stage, because later changes usually come too late.

<!-- review notes
- sentence 1: support check: partial - Passages list half-cell, shingled, built-in-diode modules and back contact cells as shade-resistant/tolerant technologies, but do not define shade-resistant design as choosing layouts (the term is called poorly defined).
- sentence 2: support check: partial - Passages say shading/cracks cause mismatch and reverse bias leading to hot cells/hotspots and list shade-resistant modules as measures, but don't explicitly call shade-resistant design a preventive measure against hotspots; they say it doesn't eliminate effects.
- sentence 5: support check: partial - Passage supports the Zener built-in BPD and lower temperature than PERC and SHJ, but it's the hot cell temperature rise (at most 25°C) of the IBC module, and 'some' IBC cells and 'much cooler' are not exactly stated.
- sentence 6: support check: partial - Passages say BPDs don't eliminate hot cell effects and that bifacial modules and larger wafers give higher hot cell temperatures, but don't explicitly tie this to shade-resistant designs as a whole.
-->
