---
id: mit:bypass-diode-integration
type: Mitigation
name: Bypass diode integration
---
Bypass diodes are fitted in the module junction box. They stop single cells from being driven into reverse bias beyond the cell's allowed voltage, and they reduce the power lost to partial shading. This protects against module hotspots, which can form when cracked cells, soiling shadows or mismatch force part of a module into reverse bias. If a diode is missing or fails open, no current flows through it. A shaded or damaged cell can then be reverse biased past its design limit and develop hotspots, browning, burn marks or even fire. This fault is hard to find until the module is actually exposed to those conditions. A diode that fails short permanently lowers module voltage and power. It causes uneven cell heating and can deform or burn the junction box. Diodes have to be sized correctly. Undersized diodes, and diodes hit by lightning or other high-voltage events, tend to fail. The Schottky diodes usually used are sensitive to static discharge and mechanical stress. Diodes that run hot because of frequent partial shading fail more often, so avoiding partial shading extends diode lifetime. IEC 62979 assesses whether a diode mounted in a module is at risk of thermal runaway. IEC TS 62916 covers testing diodes for electrostatic discharge. Where hotspots or burn marks are found, check that the bypass diodes still activate, to prevent more severe degradation.

<!-- review notes
- sentence 1: support check: partial - Passage states the purpose (avoid excess reverse bias, reduce partial-shading loss) and mentions the junction box only for failure effects, not that diodes are fitted there.
-->
