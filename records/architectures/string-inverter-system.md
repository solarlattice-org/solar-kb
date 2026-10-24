---
id: arch:string-inverter-system
type: Architecture
name: String inverter system
aliases:
- string inverter architecture
- string inverters
- string technology
- string inverter concept
category: System topology
---
In a string inverter system the PV array is divided into strings of modules wired in series, and several inverters each serve their own strings instead of one central inverter. Because each string gets its own MPP tracking, independent of the other strings, the design handles mixed orientations, different module types and partial shading better than a central inverter, which suffers more mismatch loss. The string approach was developed to cut installation cost, mainly the DC wiring and the AC distribution work, and string inverters can cover a very wide power range at low production cost. When the AC connection is lost, string inverters shut down as IEEE 1547 requires, so the AC wiring to the switchgear goes dead and only the connected module strings stay energized. A failed unit is usually swapped out whole rather than repaired. An electrician can do this without an inverter specialist, keeping spares on site is practical, and one failure takes out fewer arrays. The drawbacks are that a large fleet always has some units down, that monitoring many inverters is more complex, and that advanced grid-support features add more to the per-watt cost than they do on central inverters. String inverters may be transformerless, which gives higher efficiency and lower weight. These units need extra protection, such as DC-sensitive earth-leakage breakers and Protection Class II across the installation, and they cause more electromagnetic interference. Each string array's current must stay within the inverter's limits. Some grid-tied string inverters cannot hold up the grid voltage by themselves, so they cannot run islanded.

<!-- review notes
- sentence 6: support check: partial - Passages support the monitoring complexity, higher per-watt cost of advanced features, and some units down at any time, but say it is unlikely all are down and only 'a corresponding probability' that some are, not 'always'.
- sentence 8: support check: partial - Array current must fall within inverter limits is stated, but the passage says inverters in general cannot support the grid voltage, not just 'some' grid-tied string inverters.
-->
