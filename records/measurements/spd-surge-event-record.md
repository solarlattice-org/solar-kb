---
id: meas:spd-surge-event-record
type: Measurement
name: SPD surge event record
aliases:
- medium surge event log
- high surge event log
- low surge event log
- Surge Event Screen
---
The surge protection device keeps separate event logs for low, medium and high surge events, and these can be read over its register map. For each severity level, a phase indicator register shows which phase took the surge, with separate entries for phase A, phase B and phase C. An index register points to the most recent logged event, and each low surge event is stored with a timestamp. On units with a display, a detected surge brings up a surge event screen and sounds an audio alarm. Both stay active until an operator acknowledges them with the center button. Any further surges that happen before acknowledgment are still recorded and queued, and the main screen then shows the details of the surge. If a phase or neutral-to-ground green LED goes off while the matching red LED is lit and the audible alarm sounds, a significant surge event is the probable cause. After a significant surge event shown this way, the guidance is to replace the SPD, because its protection may be compromised or lost.

<!-- review notes
- sentence 7: support check: partial - Replace SPD is stated for significant surge events, but protection compromised or lost is stated only for the neu/gnd row, not generally.
-->
