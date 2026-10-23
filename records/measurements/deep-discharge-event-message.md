---
id: meas:deep-discharge-event-message
type: Measurement
name: Deep discharge event message
aliases:
- Deep discharge protection activated
- Event 9394
- Battery error
- Battery fault
---
The signature is an event log entry saying the battery's deep discharge protection has been activated. The battery management system sets this protection, and some inverter event lists log it as event 9394. Some manuals list it as a battery error or battery fault. It appears when the battery reaches its deep discharge protection range or its deep discharge range. On grid-connected systems, including self-consumption systems, it is only an event message, not a warning. In stand-alone mode it counts as a warning. The protection range is a parameter, set as a percentage of the battery capacity. If this message appears, check whether a fuse has tripped at the grid-connection point.

<!-- review notes
- sentence 6: support check: partial - The parameter is given as a percentage of battery capacity, but the passage names it 'minimum width' of the protection area, not simply the range being set as a parameter; detail slightly differs.
- sentence 7: support check: partial - Passages say a fuse may have tripped at the grid-connection point, implying a check, but do not explicitly instruct to check it.
-->
