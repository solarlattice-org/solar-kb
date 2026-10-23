---
id: symptom:pid-voltage-instability
type: Symptom
name: PID voltage instability
aliases:
- PID voltage stability alarm
- Fault7010
---
The manual says to watch the inverter for 5 minutes to see if the alarm clears by itself, and to call after-sales service if it does not. Do not mix it up with Fault7040, the PID over-voltage warning, which uses Bit4 of the same register. The alarm concerns the inverter's PID function, which includes a nighttime PID voltage setting for P-type panels. Before enabling any anti-PID or PID repair function, confirm that the polarity of the module voltage to ground suits the installed modules, because a wrong voltage scheme can make the function ineffective or damage the modules.

<!-- review notes
- sentence 3: support check: partial - The passage only lists a nighttime PID voltage setting for P-type panels; it doesn't link it to this alarm or say the alarm concerns the PID function that includes it.
-->
