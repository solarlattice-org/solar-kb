---
id: comp:memory-unit
type: Component
name: Memory unit
---
The memory unit is the internal data store of an inverter. Fronius Primo and Symo inverters report status codes when they cannot communicate with it. Status code 451 means a memory error was detected. The inverter tries to reconnect on its own and resumes feeding the grid if it can. If code 451 keeps coming back, call a Fronius-trained service technician. Status codes 516 and 519 mean the inverter cannot communicate with the memory unit. Each one raises a warning message for the memory unit. Status code 772 means the memory unit is unavailable. A different status code, 461, points to an error in the DSP data memory. Some metering devices run a checksum self-test on their nonvolatile memory. If the test fails, the meter is disabled and a latched alarm is set. Flash memory is a type of nonvolatile memory used to store large blocks of data.

<!-- review notes
- sentence 1: support check: partial - Codes 516/519 report inability to communicate with the memory unit, but the passages don't define the memory unit as the inverter's internal data store (nor name Primo/Symo).
- sentence 1: review: partial - The rows support status codes for when communication with the memory unit is not possible, but no passage defines the memory unit as the inverter's internal data store.
-->
