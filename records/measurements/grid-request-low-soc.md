---
id: meas:grid-request-low-soc
type: Measurement
name: Low SOC grid request
aliases:
- GdSocOn
- E501
- Grid request due to SOC
---
This signature is an event message from a battery inverter. It reports that the inverter has requested the utility grid because the battery state of charge is too low. Depending on the manual and device, it is logged as event 1609 or as display code E501, which carries the name GdSocOn. It has a counterpart message, E502, which shows that the grid was released again once the battery state of charge was high enough. The grid request based on state of charge only works if the parameter GdSocEna is enabled, and it is disabled by default. The state of charge levels at which the grid is switched on and off are set by parameters, and separate limits can be set for two time windows. The inverter calculates the state of charge it compares against these limits from ampere-hour counting, including full-charge detection, and recalibrates it against battery voltage. Taken alone, this message is an operating record of low battery charge and does not by itself mean a hardware fault.

<!-- review notes
- sentence 7: support check: partial - Passages list it as a grid request event without fault classification, but don't explicitly say it is not a hardware fault.
- sentence 7: review: partial - The tables list E501 as an operating grid-request event next to other routine events, but they never say it does not indicate a hardware fault.
-->
