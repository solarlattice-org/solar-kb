---
id: mit:fewer-cells-per-bypass-diode
type: Mitigation
name: Shorter bypass diode substrings
---
This is a module design measure for crystalline silicon modules. Bypass diodes are wired into the cell interconnection circuit so that a shaded cell sees only a limited, non-critical reverse voltage, which prevents breakdown of its pn junction. The reverse voltage a shaded cell can see depends on how many cells share one diode. The source example is a substring of 20 series-connected cells per diode, which can reverse-bias a shaded cell to roughly -12 V. Crystalline cells tolerate reverse bias when the bypass diode protection is well designed. This makes the measure relevant to hot cells and hotspot damage caused by partial shading. Bypass diodes also reduce the power lost to partial shading, because they stop single cells from being reverse-biased beyond their allowed voltage. There are limits: a shaded cell can still overheat without junction breakdown, because its temperature depends on how leakage current is spread over the cell and on current density. The protection only works while the diode works. If a diode fails open circuit, the cell can be pushed to a higher reverse voltage than it was designed for, which can lead to hotspots, browning, burn marks or fire. Diodes that run hot all the time, for example under frequent partial shading, fail more often. Avoiding partial shading extends bypass diode lifetime.

<!-- review notes
- sentence 2: support check: partial - The 20 cells per diode example giving about -12 V is stated. The passage does not say outright that reverse voltage depends on cells per diode, though the example implies it.
- sentence 3: support check: partial - The passages say crystalline cells tolerate reverse bias when the bypass diode protection is well designed, and they link bypass diodes to hot-spot prevention. They do not say the measure is relevant to hot cells caused by partial shading.
-->
