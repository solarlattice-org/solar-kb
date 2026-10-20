---
id: meas:high-string-reverse-voltage
type: Measurement
name: High string reverse voltage
---
This signature shows up during a night bypass diode test. A reverse current of about 3% to 5% of the rated Isc is pushed through each string, and the reverse-bias voltage across the string is recorded. If one string shows a much higher reverse voltage than the others, at least one bypass diode in it is open or not connected. The usual cause is failure mode A: a cold solder joint after the diode in the junction box. Daytime infrared thermography cannot detect it, and it often goes unnoticed until the module is shaded. To find the affected module, inspect the flagged string at night with an infrared camera while the reverse current is applied, and look for a substring that is a few kelvin warmer. Night EL imaging under the same reverse bias can also show the unconnected bypass diode. Treat this finding as a safety issue. A shaded module with a disconnected bypass diode can heat up within seconds and may char or catch fire. Without destructive analysis of the junction box, a failed bypass diode cannot be told apart from an open connection after the diode. Because cold solder joints usually affect a whole production batch, if one failure is found, all modules should be tested.

<!-- review notes
- sentence 2: support check: partial - Passages say a string with extraordinarily high reverse voltage should be searched for mode A failure or open BPD, but 'at least one diode open or not connected' is stated slightly more definitively (mode A is also a cause).
- sentence 3: support check: partial - Cold solder joint after the diode, undetectable by IRT and unnoticed without shade are stated, but 'usual cause' of the high reverse voltage is not stated (open BPD is also a cause and indistinguishable).
- sentence 5: support check: partial - Heating within seconds and charring/burning for a shaded module with failure mode A is stated and it is called a safety failure, but the passages tie it to mode A (indistinguishable from failing BPD) rather than explicitly a disconnected bypass diode; 'treat as safety issue' is implied.
- sentence 6: support check: partial - Passage says failing BPD cannot be differentiated from failure mode A without destructive analysis, which matches, though 'open connection after the diode' is a paraphrase of mode A.
-->
