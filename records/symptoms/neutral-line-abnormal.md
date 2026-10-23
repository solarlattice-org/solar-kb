---
id: symptom:neutral-line-abnormal
type: Symptom
name: Abnormal neutral line
aliases:
- N-line abnormal alarm
- N wire abnormality
- Fault7030
---
In the Modbus map it is bit 3 of register 0x841B. One map lists it as a trip fault and the other as a switch fault. The usual cause is a neutral line setting in the inverter that does not match how the N wire is actually connected, so check that setting against the real wiring first. The neutral line setting is where you tell the inverter whether a neutral is connected. Other makers report similar alarms when the neutral or ground conductor is not connected. Possible causes include a missing neutral point ground at the grid transformer, a missing main grounding busbar ground, or a wrong country data set. If it is safe to do so with AC on, measure line-to-line, line-to-neutral, line-to-ground and neutral-to-ground voltages to confirm the neutral connection. If the alarm is still there after you correct the setting, contact after-sales service.

<!-- review notes
- sentence 2: support check: partial - The passage says to check that the inverter's N-line setting matches the actual connection, but it doesn't say this is the usual cause, only a first check.
-->
