---
id: symptom:clamp-capacitor-imbalance
type: Symptom
name: Clamp capacitor voltage imbalance
aliases:
- Clamp capacitance imbalance event
---
Monitoring systems that read the Modbus alarm table show the same condition as alarm 032, hex 0x0020. The Modbus note says to wait for the inverter to recover by itself, and points to the service note in the manual. The event table in the owner's guide gives no solution for code 032. The same table lists related clamp capacitance events: over-voltage (030), under-voltage (031) and pre-charge ground fault (033). Check the event log for these codes, because together they show which of these clamp problems is happening. If the event does not clear by itself, follow the manual's note instead of trying a fix in the field.

<!-- review notes
- sentence 4: support check: partial - Codes 030, 031 and 033 are listed with the stated descriptions, but nothing says to check the event log or that together they show which clamp problem is occurring.
- sentence 5: support check: partial - The note says to wait for automatic recovery and see the NOTE, but the passages don't say what to do if the event doesn't clear or advise against field fixes.
-->
