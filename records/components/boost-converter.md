---
id: comp:boost-converter
type: Component
name: DC boost converter
aliases:
- Boost converter
---
A DC boost converter is a power electronics stage that steps up DC voltage. One manufacturer lists boost converter as the topology of its module-level PV device. Some Solis string inverters raise a BoostFal alarm when the DC boost converter circuit has a fault. For a BoostFal alarm, the manual says to inspect the installation, restart the inverter, and replace the inverter if the fault stays. During event 7014 the cooling fan runs all the time. The fix is to contact SMA Service. A Solis certification report names the boost diode as one of the inverter parts that has approved alternate materials.

<!-- review notes
- sentence 1: support check: partial - The passage shows the topology is 'Boost converter' for a device, but doesn't state the definition of a boost converter or that it is module-level or from one manufacturer.
- sentence 3: support check: partial - The solution lists inspect installation, restart, replace inverter, but the 'if the fault stays' condition is not stated.
-->
