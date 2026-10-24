---
id: mit:low-current-dc-disconnection
type: Mitigation
name: DC isolation below safe current
aliases:
- disconnect DC switch only below 0.5 A
- turn off AC first then DC
- disconnect after sunset
---
This action means opening the inverter DC switch only after the string current has fallen to a safe low level. Breaking a faulted DC circuit while current is flowing can strike a DC arc, damage the inverter or start a fire. It applies when PV strings are connected with reversed polarity, when the inverter is faulty or not working properly, and to the Sungrow fault codes for a PV grounding fault and a system hardware fault. Measure the DC string current with a clamp meter. If it is above 0.5 A, wait for the irradiance to drop until the current is below 0.5 A, then turn off the DC switch and disconnect the strings. Keep the strings disconnected until the cause, such as the reverse polarity or the ground fault, has been fixed. Otherwise PV energy the next day can cause the failure again. On CPS and Yaskawa string inverters, first shut down the inverter, the AC feed breaker and the AC switch. Open the DC switch only when the MPPT current is below the limit in the manual or the irradiance is clearly low. Do not open a string fuse holder that carries more than 0.25 A. If opening the DC switch causes smoke, turn it back on if that is safe. Continue troubleshooting at low irradiance, about 30 minutes before sunset. Large central inverters use the same order: AC shutoff first, then the DC switch, and the PV combiners last. Never disconnect a combiner while the system is operating. The inverter warranty does not cover damage caused by switching in the wrong way. The DC switch only isolates up to its own terminals, so full isolation also needs the PV array disconnect.

<!-- review notes
- sentence 4: support check: partial - Reverse polarity case (leave disconnected until corrected) and the next-day PV energy reason are stated, and ground fault says do not reinsert strings until cleared, but the passages do not combine them as the statement does; the next-day secondary failure rationale is tied to disconnecting after switch-off, not to the ground fault.
- sentence 5: support check: partial - The shutdown sequence and the 0.25 A fuse holder rule are stated, but the MPPT limit is 24 A or 125 A depending on model, and passages do not name Yaskawa (only CPS marked in one).
- sentence 7: support check: partial - The order (AC shutoff, DC switch, then PV combiners) and the never-disconnect-a-combiner rule are stated, but the passages do not say they apply to large central inverters.
-->
