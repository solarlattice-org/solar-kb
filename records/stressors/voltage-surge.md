---
id: stressor:voltage-surge
type: Stressor
name: Voltage surge event
aliases:
- Voltage spikes
- Overvoltages
- surge attempts
---
A voltage surge is a short spike of excess voltage. It can arrive at an inverter over the AC grid lines or over the PV DC lines. Surges on the DC side are mostly caused by lightning. A surge protection device protects the inverter by blocking surge voltages above a safe threshold or by shorting them to ground. Surges can make surge arresters trip. On SMA inverters, a tripped arrester, or one that is not seated correctly, raises a fault overvoltage protector event. To fix this, check that each surge arrester is seated correctly and replace any that have tripped with new ones. Some surge protection devices keep a log of low and medium surge events, recording the affected phase and a timestamp. If surge protection is missing, a lightning-induced overvoltage can travel over network or data cables into the building and to connected devices, where it is a risk of fatal electric shock. To reduce exposure, include every networked device and the battery in the existing surge protection. Also fit a surge protection device where an outdoor data cable enters the building.

<!-- review notes
- sentence 4: support check: partial - Event 7801 'Fault overvoltage protector' is caused by tripped or incorrectly inserted arresters, but the passages never say surges cause the trips, and nothing in them says it is specific to SMA inverters.
- sentence 6: support check: partial - The passages show phase indicators for low and medium surge events and a timestamp for medium events, but they show no timestamp for low events and no explicit log of both event types.
- sentence 4: review: partial - Event 7801 Fault overvoltage protector is stated to come from tripped or incorrectly inserted surge arresters, but the passages never say that surges cause the trips.
-->
