---
id: symptom:dc-injection-monitoring-error
type: Symptom
name: DC injection monitoring error
aliases:
- DC feed-in monitoring
- sampling offset of DCI
---
This symptom is the inverter's internal check of DC injection on its AC output reporting an error. It does not mean that high DC injection has been measured. Inverters treat DC injection of the AC output as a protection function and a variable they monitor all the time. On Fronius Primo and Symo inverters it shows up as status code 462, an error in the DC feed-in monitoring routine. Keep this separate from the DCinj-FAULT alarm on other inverters. That alarm reports that high DC injection current was actually detected. For Protect0180, first check whether the inverter will start up. If it does, recalibrate it. If the alarm keeps returning and the inverter cannot start, replace the inverter.

<!-- review notes
- sentence 1: support check: partial - Passages show code 462 is an error in the DC feed-in monitoring routine (implying a monitoring-routine fault), but nothing explicitly says it does not mean high DC injection was measured.
- sentence 3: support check: partial - Code 462 with that description is stated, but the passages given don't mention Fronius Primo and Symo models.
- sentence 4: support check: partial - DCinj-FAULT is described as High DC injection current, but the passages don't explicitly contrast it or say it is on other inverters beyond the label; 'actually detected' is a mild inference.
- sentence 1: review: partial - Code 462 is described as an error in the DC feed-in monitoring routine, but nothing in the passages says that high DC injection was not measured.
-->
