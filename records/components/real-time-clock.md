---
id: comp:real-time-clock
type: Component
name: Real-time clock module
aliases:
- RTC
---
A real-time clock is the device's internal clock. Time sources such as IRIG or SNTP set it, and the device uses it to time durations and to timestamp records. Some devices run the real-time clock from a battery and report that battery's voltage as a measured value. On Fronius Galvo, Primo and Symo inverters, a status code reports a communication error with the real-time clock module, a form of real-time clock failure. A hardware error in the clock module shows a message on the display and stops the inverter feeding current into the grid. If the code persists, call a Fronius-trained service technician. When the clock module goes into emergency mode, the time can become inaccurate or be lost, but the inverter keeps feeding the grid normally. The fix is to reset the time and date on the inverter. On an Eaton surge protection device, the clock stays synchronized while the unit is on an Ethernet network. Off the network it can drift by up to plus or minus 2 minutes per month at 25°C. IEC 61000-4-30 sets a requirement for real-time clock uncertainty, and SEL-735 meters are rated class A against it.

<!-- review notes
- sentence 2: support check: partial - The passage gives a real-time clock battery voltage measurement, but doesn't say devices run the clock from a battery in general (only implied) and says nothing about 'some devices'.
- sentence 3: support check: partial - Code 752 is a real-time clock module communication error, but the passages don't name the Galvo, Primo and Symo models or call it a form of RTC failure.
-->
