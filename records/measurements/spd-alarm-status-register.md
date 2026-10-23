---
id: meas:spd-alarm-status-register
type: Measurement
name: SPD alarm status register
aliases:
- Alarm status
- meas:spd-alarm-status-active
- SPD active alarm status
---
On Eaton Power Xpert SPD units, the alarm status is a read-only enumerated register that shows whether the device is still protecting. A value of 0 means the alarm is off and a value of 1 means the alarm is on. On the BACnet interface, the same point is a binary object. It reads Protected when inactive and Protection loss when active. The SPD Status menu on the display shows the same point as either Protected or Active Alarm Replace SPD. An active alarm comes with red phase or neutral-ground LEDs and, on units that have one, an audible alarm. It means protection is compromised or lost, which is the surge protector exhausted failure mode. Probable causes are an SPD rated below the system voltage or an extended temporary overvoltage. The remedy is to replace the SPD, using the correct voltage model and correcting any overvoltage sources first. A separate writable register silences the audible alarm, but silencing does not clear the fault. If the fault is still present after a power cycle, the alarm comes back. If all LEDs and the LCD are dark, there is no alarm reading to interpret. Check whether the SPD is connected to a power source.

<!-- review notes
- sentence 3: support check: partial - The menu shows Alarm Status as Protected or Active Alarm Replace SPD, but the passage doesn't explicitly say it's the same point as the register (implied by name).
- sentence 4: support check: partial - Red LEDs, audible alarm, and protection compromised/lost are stated, but mapping to the 'surge protector exhausted' failure mode isn't in the passages.
- sentence 4: review: partial - Red phase or N-G LEDs, the audible alarm and compromised or lost protection are all stated, but the link to a 'surge protector exhausted' failure mode is not in the passages.
-->
