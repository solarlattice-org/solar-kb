---
id: state:waiting
type: OperatingState
name: Waiting for feed-in conditions
aliases:
- waiting
- wait
- grid check
- waiting for grid
- Waiting for DC start conditions
- Start conditions not met
- Start cond. not met
category: Inverters
---
In this state the inverter is not yet feeding power into the grid because the conditions for feed-in have not been met. The inverter starts feeding in by itself once the conditions are met, so it leaves this state without anyone stepping in. The green LED flashes slowly, two seconds on and two seconds off. The event log may show Waiting for DC start conditions followed by Start conditions not met. Some models log this as event numbers 3901 to 3902. Normally you do not need to do anything except wait for stronger sunlight. If the message comes up often in the morning, raise the voltage limit for starting feed-in with the Minimum voltage input parameter or the A.VStr and B.VStr parameters. If it comes up often at medium irradiation, check that the PV array is sized correctly.

<!-- review notes
- sentence 3: support check: partial - 2 s on/2 s off flashing is stated, but 'slowly' is only a characterization; essentially supported.
- sentence 5: support check: partial - Waiting for higher irradiation is the first measure, but passages also list further measures for frequent occurrence; 'normally nothing else' is not explicitly stated.
-->
