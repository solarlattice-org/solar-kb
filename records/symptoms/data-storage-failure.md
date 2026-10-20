---
id: symptom:data-storage-failure
type: Symptom
name: Data storage failure
aliases:
- Data storage not possible
---
This symptom shows up as an event message in the inverter log or monitoring, not as a change in power or current readings. A related event, 7113, means the memory card is full or write-protected, so check the card first. The manual lists no specific cause or fix for events 7201 and 7202, so if they keep appearing, the cause has to be found case by case. Inverters use this storage to record running information and error records, so the log history may have gaps while the fault is active.

<!-- review notes
- sentence 1: support check: partial - The passages show 7201/7202 'Data storage not possible' as an event message in the event table, but nothing says it appears only as a log message rather than in power or current readings.
- sentence 2: support check: partial - 7113 is stated as 'memory card is full or write-protected', but the passages give no corrective measure, so 'check the card first' is an inference.
- sentence 4: support check: partial - The passage says data storage records running information and error records, but it says nothing about gaps in the log history while the fault is active.
-->
