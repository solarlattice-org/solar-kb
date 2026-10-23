---
id: mit:impedance-matching
type: Mitigation
name: Grid impedance matching
aliases:
- Impedance matching adjustment
---
Grid impedance matching means checking and correcting the impedance between the inverter and the grid, so the inverter sees a grid it can operate against stably. Use it when an inverter reports that grid impedance is above its limit, as with Schneider CL125 event 015, or when it flags an unstable grid, as with Solis GRID-INTF. On the CL125, check that the AC cable type and size and the transformer impedance follow the CL125 Solution Guide or local electrical rules, then let the inverter recover by itself. For Solis GRID-INTF, measure AC voltage and test the AC line for harmonic distortion with the DC switch off and then on. Try turning off one of several inverters, then make an impedance matching adjustment or fit a matching box. At design stage, Schneider recommends keeping AC cable impedance up to 3% of nominal voltage and transformer impedance up to 6%. It also recommends oversizing the transformer by 5-10% and calculating the grid impedance at the point of common coupling first. Cable sizing should account for the reactive part of cable impedance, not just the resistance. Weak, high-impedance grids should be avoided because they can cause resonance problems when many inverters run in parallel. Impedance matching cannot fix internal inverter damage or a wire that came loose in shipping. Those causes need to be checked separately.

<!-- review notes
- sentence 1: support check: partial - Passages discuss grid impedance limits and recommendations but never define 'grid impedance matching' as checking and correcting impedance so the inverter sees a stable grid; only GRID-INTF mentions an 'impedance matching adjustment or box'.
- sentence 4: support check: partial - The steps are listed, but 'harmonic distortion' for THD is a paraphrase and the passage does not specify measuring AC voltage in either switch state or the exact ordering, so the sequence is somewhat inferred.
- sentence 7: support check: partial - Internal damage and a loose wire are listed as separate causes or checks, but the passage does not say that impedance matching cannot fix them.
-->
