---
id: mit:clock-reset
type: Mitigation
name: Inverter clock reset
aliases:
- Set the system clock
---
An inverter clock reset means entering the correct time and date on the inverter again. It is the listed fix for the Fronius time lost status code 751, which shows a warning message on the display. It is also the remedy for status codes 753 and 758, where the real-time clock module runs in emergency mode. In that state the time may be wrong or lost, but feeding power into the grid continues as normal. On CPS inverters, you set the system clock from the Inverter Clock menu item. If the time lost code returns after the reset, contact a Fronius-trained service technician. A hardware error in the real-time clock module (code 757) is different. It stops grid feed-in, and the listed remedy is to contact a service technician if the code persists. On FIMER inverters with a Clock Fail alarm, switch the inverter fully off on both AC and DC, wait, restart it and check the date and time. If they have gone back to 01/01/2000, replace the clock battery with the inverter fully off and keep the polarity correct.

<!-- review notes
- sentence 4: support check: partial - The passages say Inverter Clock sets the system clock but don't mention CPS inverters or a menu item.
- sentence 7: support check: partial - The steps match, but the passages don't name FIMER, and the battery replacement is for when the date has reset to 01/01/2000, which fits; the FIMER brand is the only gap.
- sentence 4: review: partial - The rows show an 'Inverter Clock' item that sets the system clock, but the CPS brand appears only in the source IDs, and the quoted text never says it is a menu item.
-->
