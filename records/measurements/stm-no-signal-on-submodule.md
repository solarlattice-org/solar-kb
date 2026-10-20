---
id: meas:stm-no-signal-on-submodule
type: Measurement
name: No test signal on submodule
---
With the signal transmission method, the receiver picks up no test signal anywhere along the ribbons of one submodule. To check for this, stop the PV system, connect the transmitter to the module string at the combiner box, then move the receiver along the interconnect ribbons on the front or back of each module. The pattern appears when all cell interconnect ribbons of one cell are disconnected, typically two or three ribbons, or when a string interconnect is disconnected. The signal disappears because the test current flows through the bypass diode built into the disconnected submodule instead. Do not confuse this with a single disconnected ribbon, where the signal is lost only at the break point on that ribbon. A deliberately shaded submodule with a working bypass diode also shows no signal, so only judge the result on unshaded submodules. The source rates this failure as safety class B(f) and power class E.

<!-- review notes
- sentence 1: support check: partial - Passages say no signal is detected anywhere on the disconnected submodule when all ribbons of a cell (or a string interconnect) are disconnected, but the statement omits that condition and wrongly implies it for any ribbon pattern.
- sentence 6: support check: partial - Passage says a shaded submodule with an activated bypass diode shows no signal, but it does not say to judge the result only on unshaded submodules; shading is the deliberate test for diode failure.
-->
