---
id: comp:residual-current-device
type: Component
name: Residual current device
aliases:
- RCD
---
A residual-current device is a protective switch that disconnects a circuit automatically when a fault produces residual current. In TT earthing systems it is required as the primary fault protection. Residual-current devices must not be used in TN-C systems. If an external residual-current device is required with SMA inverters, the manufacturer says to install one that trips at a residual current of 100 mA or higher. The RCD sees the inverter's normal leakage current as residual current. The rated residual current set in the inverter must therefore be no higher than the RCD's rating. If the RCD trips often, the inverter value can be set lower so that the inverter disconnects before the RCD trips by mistake. SMA states that a type A device with a rated residual current of 500 mA meets the automatic disconnection requirement for fault protection. For fire protection, local rules can call for a residual-current device, for example in barns or wooden cabins under DIN VDE 0100-482. There, the rated residual current may be at most 300 mA. Many inverters also have a built-in residual current monitoring unit according to IEC 62109-2. It tells a ground fault current apart from normal capacitive leakage current and disconnects the inverter from the grid when a ground fault is detected.

<!-- review notes
- sentence 1: support check: partial - The passage says an RCD is required as primary fault protection in TT systems and that it guarantees automatic disconnection, but it doesn't define an RCD as a protective switch that disconnects when residual current occurs.
- sentence 5: support check: partial - The passage says a type A RCD with 500 mA fulfills the requirement, but only when no other circuit breaker can be used, and the statement leaves out that condition.
- sentence 7: support check: partial - The passages support the IEC 62109-2 monitoring unit and its ground-fault disconnection, but they don't say that many inverters have one, and the standard appears only in a single product's data line.
- sentence 7: review: partial - The ABB row supports IEC 62109-2 residual current monitoring and the Schneider passage supports telling ground faults apart from leakage current and disconnecting, but the passages describe only two specific products, so the 'many inverters' scope is not stated.
-->
