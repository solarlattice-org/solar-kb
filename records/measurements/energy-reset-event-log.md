---
id: meas:energy-reset-event-log
type: Measurement
name: Energy reset event log entry
aliases:
- Energy Reset
- Last Energy Reset
- Reset Energy Data
---
An energy reset event is a log entry showing that the device energy registers were reset. On some meters these entries fall under the ER (Energy Reset) category of the event log command, which sits next to separate categories for demand, peak demand, load profile and settings resets. The meter can show the date and time of the last energy reset next to the current energy values, so a technician can check when the counters were cleared. The same menu that shows the last reset time also lets the user reset the energy values, so a logged reset may come from a deliberate operator action. Some inverters also have an interface for resetting their stored energy data. On some inverters a TOTAL reset sets the logged maximum and minimum voltage and the maximum feed-in power back to zero, and this cannot be undone.

<!-- review notes
- sentence 4: support check: partial - The menu function includes resetting energy values, but the passages don't say a logged reset may come from a deliberate operator action (an inference).
- sentence 4: review: partial - The menu function does both display the last reset date/time and reset energy values, but the conclusion that a logged reset may come from a deliberate operator action is not stated.
-->
