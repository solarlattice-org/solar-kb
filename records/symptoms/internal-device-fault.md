---
id: symptom:internal-device-fault
type: Symptom
name: Internal device fault
aliases:
- Internal alarm
- Internal fault of the inverter
- Device fault
- Internal failure
- Internal protection of the inverter
---
An internal device fault is an inverter alarm or fault code that points to a problem inside the inverter itself, not in the array or the grid. Other inverters show it as a generic device fault, or as a Warning or Failure message with a three-digit number on the display. For EepromErr, wait a few minutes to see if the alarm clears by itself, and call post-sales service if it does not. For CPLD, Mini MCU and leakage-sensor faults, start by switching both AC and DC off, waiting a minute for the energy to discharge, and switching back on. If that restart does not clear the fault, the part to replace depends on the code: the control board for a CPLD fault, the filter board for a leakage-sensor fault, or the whole inverter. For a DCI sampling offset, recalibrate if the inverter can still start up, and replace the inverter if the alarm keeps coming back and it cannot start. For SMA and Solectria units, the manuals say the cause of an internal failure has to be found by manufacturer service.

<!-- review notes
- sentence 1: support check: partial - Passages define internal fault/protection as an internal problem of the inverter, but nothing contrasts it with array or grid problems.
- sentence 3: support check: partial - Evidence says observe for 5 minutes for auto-clear then contact post-sales; 'a few minutes' is a loose paraphrase of the stated 5 minutes.
- sentence 7: support check: partial - Passages say the Service determines the cause and Solectria says contact its Support Team, but nothing in them attributes the 'Device fault' text to SMA.
-->
