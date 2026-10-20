---
id: mit:fan-replacement
type: Mitigation
name: Fan replacement
aliases:
- Replace cooling fans
- Replacing Cooling Fans
---
Fan replacement means swapping out a broken inverter cooling fan. It addresses fan failure, which shows up as the ExtFanErr alarm on CPS SCA inverters or a Fan Fail warning on other inverters. The fan matters because a fan that does not work leaves the inverter poorly cooled. Fan failure is one of the listed causes of inverter overheating and temperature derating. Before replacing anything, wait 5 minutes to see if the alarm clears by itself. Next, check the blades for foreign objects. Then switch the external AC disconnect off and back on to reboot the system. On CPS units, if ExtFanErr appears while output is above 50% of rated output and the fan is still spinning, replace the inverter instead, because the problem is in the sensing circuit. If the fan is not spinning, remove the 6 bolts holding the two external fans. Open the white snap-on connector and measure the voltage across the red and black wire pins. Below 6 VDC, replace the inverter. Above 6 V, replace the fan. Before working on the fan, the Solis procedure switches the grid off from the LCD, disconnects AC, turns the DC switch off and waits at least 15 minutes. Then the fan assembly is pulled out, cleaned or replaced, reconnected and the inverter restarted. Fan replacement does not fix every fan alarm. On CPS units, an internal fan error (IntFanErr) calls for replacing the whole inverter, and you should contact post-sales service if the fault remains.

<!-- review notes
- sentence 7: support check: partial - IntFanErr says replace the inverter, but the 'contact post-sales service if fault remains' is only for ExtFanErr alarm, not IntFanErr.
-->
