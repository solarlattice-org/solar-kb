---
id: symptom:string-reverse-current
type: Symptom
name: String reverse current
aliases:
- String Current Reflux
- Reve-DC
---
Sungrow lists four things to check: a string with fewer modules than the others, shading on the string, an abnormal open-circuit voltage or wiring fault, and modules facing the wrong way. Solis gives two causes for its matching reverse DC alarm: a string connected with reversed polarity, or string inputs with different numbers of modules. Find reverse polarity first. With a meter, a reversed string shows a negative voltage. In a combiner box, a reversed string reads about twice the system voltage between string positives where good strings read near zero. If polarity is correct, count the modules in each string and compare. Then look for shading or modules mounted at the wrong orientation. Only open the DC switch to fix wiring or configuration once the string current has fallen below 0.5 A, for example at night or when irradiance is low. The SG250HX monitors current on each string, so the affected input can be found by comparing it against the other strings in the monitoring data.

<!-- review notes
- sentence 4: support check: partial - The Solis passage supports checking polarity and then module counts, and the Sungrow row lists shading and orientation, but the order (shading and orientation after counting) and 'compare' across two sources is a synthesis; the Sungrow list is not tied to a polarity-correct condition.
- sentence 5: support check: partial - Passages say to disconnect the DC switch when string current drops below 0.5 A (night or low irradiance is mentioned only in the Solis text), but the 'only' prohibition is not stated for these alarms, and the Sungrow row says nothing about night.
- sentence 6: support check: partial - The SG250HX supports string current monitoring and a string n current parameter exists, but comparing against other strings is described only by the string-failure detection of a different (SMA-style) source, not tied to the SG250HX.
-->
