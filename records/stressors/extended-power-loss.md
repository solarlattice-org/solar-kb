---
id: stressor:extended-power-loss
type: Stressor
name: Extended power outage
aliases:
- extended power loss
- extended grid outage
- multi-day grid outage
- extended outage
---
An extended power outage is a long loss of supply to equipment, for example a grid outage that lasts many hours or several days. Clocks inside devices run on a small backup store, such as a supercapacitor. A long outage can drain that store, so the clock loses sync and event time stamps become inaccurate. This is how the outage leads to real-time clock failure. One surge protective device's timekeeping is built to last several days without power. After a longer outage, its time may be affected, and the manual strongly recommends updating the date and time. After power returns, set the clock and use the SNTP feature so time stamps stay accurate. In battery-backed PV systems, a long grid outage can drain the battery to its minimum state of charge. The battery then goes to sleep and the system shuts off, often overnight. The sleeping battery checks for solar power at regular intervals. When it finds solar power, it wakes the system and starts charging again. Otherwise the system restarts when grid power returns. Shedding large non-essential loads as soon as the outage starts makes the battery last longer during the outage. Examples are dryers, pool pumps, hot tubs and electric vehicles.

<!-- review notes
- sentence 1: support check: partial - Passages use 'extended or multi-day grid outage' but never define it as a long loss lasting many hours or several days.
- sentence 2: support check: partial - Supercap drained during extended power loss causing unsynced clock and inaccurate time stamps is stated, but the general explanation of clocks running on backup store and 'real-time clock failure' is somewhat extrapolated.
-->
