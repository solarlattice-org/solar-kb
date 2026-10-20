---
id: comp:communication-processor
type: Component
name: Communication processor
aliases:
- communication component
---
The communication processor is the part inside an inverter that runs the unit's communication functions. On SMA inverters, event 6702 (Communication failure) means the communication processor has an error, but the inverter keeps feeding power into the grid. Service has to find the cause of event 6702, so contact Service if this message comes up often. SMA event 27301 is a status message saying the inverter is updating its communication component.

<!-- review notes
- sentence 4: support check: partial - Event 27301 'Update communication' says the inverter is updating the communication component, but the passage doesn't call it a status message or classify it.
-->
