---
id: mit:polarity-correction
type: Mitigation
name: String polarity correction
aliases:
- Correct the string polarity
- adjust the polarity
---
String polarity correction means reconnecting a string whose positive and negative leads were swapped. It clears reverse-connection faults and alarms, such as the Sungrow string or MPPT reverse connection codes, the Huawei reversed string warning and the Solis Reve-DC alarm. Before changing anything, measure the DC voltage between the string's positive and negative cables with a multimeter. A negative reading means the string is connected in reverse. If a reversed string is already connected and the DC switch is on, do not open the switch or pull the connectors right away. Wait until irradiance is low and the string current has fallen below 0.5 A. Once the current is that low, turn off the DC switches, remove the connectors, swap the polarity and reconnect the string to the inverter. If the polarity turns out to be correct but a Sungrow fault or alarm continues, contact the manufacturer's service team. On Solis inverters, if every string has the correct polarity, check that all strings have the same number of modules, because a mismatch can also trigger the alarm. Check polarity before any other tests and before closing switches. If a reversed string is found on a system that was already connected, inspect its modules and bypass diodes for damage. Huawei warns that equipment damage caused by not following this procedure is not covered by the warranty.

<!-- review notes
- sentence 1: support check: partial - Sungrow, Huawei and Solis reverse-connection cases are in the passages, but the Huawei "warning" classification and the claim that correction clears the codes are not stated (they only give a symptom and suggestion).
- sentence 8: support check: partial - The passage says equipment damage from reversed polarity with the DC switch on, and from unplugging or switching off immediately, is beyond the warranty scope; it does not say this about the whole procedure.
- sentence 1: review: partial - The Sungrow string/MPPT reverse codes, the Huawei reversed-string symptom and the Solis Reve-DC alarm are all cited with polarity correction as the fix, but no passage calls the Huawei item a 'warning'.
-->
