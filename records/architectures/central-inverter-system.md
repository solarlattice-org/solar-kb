---
id: arch:central-inverter-system
type: Architecture
name: Central inverter system
aliases:
- central inverter architecture
- central inverters
- Utility-Scale Modular Central inverters
- Modular Central Inverter
- centralized inverter system architecture
- central inverter configuration
category: System topology
---
In a central inverter system the PV modules are wired together in series and parallel, and one large inverter feeds the energy into the utility grid. Many modules are connected in series to make high-voltage strings, those strings are paralleled into the inverter, and this layout is still the first choice for many medium and large plants. Central inverters are usually three-phase and often contain a grid-frequency transformer. The transformer gives galvanic isolation from the grid but adds weight, size, and load and no-load losses. The topology needs much more DC wiring and more DC disconnects. Work on live combiner boxes and array circuits needs NFPA 70E-trained electricians with arc-rated PPE, because a DC arc lasts longer than an AC arc. The inverter is a single point of failure: when it is down, the whole block's production is lost, and a long repair lead time can cause large yield losses. There is no MPPT for each string and mismatch losses are higher, so arrays with mixed tilts or orientations, shading, or different module types are a poor fit. On the plus side, monitoring is simpler, grid features such as reactive power, curtailment and ride-through are easier to add, and parts such as control cards, IGBT matrices and capacitors can be repaired one at a time. One example is the Solectria XGI 1500-1MW 1500 VDC modular central inverter, which is used with matching remote PV combiners.

<!-- review notes
- sentence 4: review: partial - The passage supports much more DC wiring, NFPA 70E training and arc-rated PPE for live combiner and array work, and DC arcs being more persistent, but it says DC disconnects are more expensive, not that more of them are needed,…
-->
