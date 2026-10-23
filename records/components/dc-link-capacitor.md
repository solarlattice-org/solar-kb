---
id: comp:dc-link-capacitor
type: Component
name: DC link capacitor
aliases:
- Bus Electrolytic Capacitor
---
The DC link capacitor stores energy on the internal DC bus of an inverter. It can keep a dangerous charge after the inverter is switched off. One SMA service instruction warns that up to 1000 V can remain in the DC link after shutdown. Before working inside the unit, measure the DC link voltage at the marked contact points with a suitable meter. If the reading is above 5 V, wait 120 minutes and check that it has fallen below 5 V. You can also discharge the link actively with the meter probes until it reads below 5 V. Solis certification records list a bus electrolytic capacitor among the approved alternate parts. This shows the bus capacitor is an electrolytic type in those inverters. The FIMER PVS-166 and PVS-175 inverters have a DC link recharge circuit that lets them run at night and restart.

<!-- review notes
- sentence 1: support check: partial - Passage shows residual voltage in the DC link after shutdown but never mentions a capacitor or that it stores energy on the internal bus.
- sentence 5: support check: partial - Records list Bus Electrolytic Capacitor among alternate materials, but the inference about the bus capacitor type is only implied; the second record just says 'Capacitor'.
- sentence 6: support check: partial - Passage lists the DC link recharge circuit with night time operation with restart capability for the PVS-166/175, but does not state that the circuit enables it as a causal relation, though it's strongly implied.
-->
