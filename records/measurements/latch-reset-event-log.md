---
id: meas:latch-reset-event-log
type: Measurement
name: Latch reset event log entry
aliases:
- Latch-Manual reset
- W027
- Reset Latch
---
On ABB and FIMER string inverters, a manual reset of latched alarm conditions is written to the event history as warning W027, Latch-Manual reset, and no LED lights up. The customer or installer triggers the reset with the Reset Latch parameter, which clears the latched alarms that are present. Depending on the model, the reset is done through the internal webserver, the display, or the advanced configuration software. The manuals say this entry is not an error and points to no failure mode. It only records in the inverter's event log that someone reset the latches. On the display-equipped UNO-DM model, W027 is not shown on the display, so look for it in the event history. The SEL-735 also latches a power quality alarm bit, which can be cleared manually with an assigned pushbutton. The LED next to that button shows the alarm bit's status.

<!-- review notes
- sentence 5: support check: partial - The row says W027 is not visualised on the display, but it doesn't name UNO-DM or say to look in the event history (it only says the information is saved there).
- sentence 6: support check: partial - The passage says the pushbutton resets the latched PQ alarm and the LED shows the PQALRM bit status, but it doesn't state that the reset is manual in those words beyond pressing the button; the core is there, though it's a close match.
-->
