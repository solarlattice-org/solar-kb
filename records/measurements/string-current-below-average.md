---
id: meas:string-current-below-average
type: Measurement
name: String current below average
aliases:
- underperforming strings
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: string input current persistently below about 90% of the average for strings on the same inverter
---
With the system running and the inverters tracking maximum power, measure each string's current with a clip-on ammeter around the string cable and compare it with the expected value. When identical strings see stable irradiance, their currents should match, typically within 5 % of the average string current. A string clearly below that band is the signature. If irradiance is unstable, wait to test, put a second meter on a reference string, correct the readings with an irradiance meter, or run an I-V curve test. Some inverters have a string-failure detection function. It compares each input's total current with the running mean and reports an event when the current goes outside a set tolerance. The function is off by default. Monitoring tools treat strings above 90% of the average current as normal. They can also flag a string that stays below a set ratio of the best string on the same device for a set time, by default 0.8 for 2 hours. The comparison works best when all strings on an inverter have the same azimuth, tilt and shading. Otherwise, check for shading, fewer modules in the string, or a module facing the wrong way. Glass breakage, where a module's glass is completely broken, lowers current and power for the whole string. A module hotspot from cell damage can also lower string output. A string fault, such as a blown string fuse, shows up as a sudden drop in system output roughly equal to one string's power.

<!-- review notes
- sentence 2: support check: partial - The 5% of average for identical strings under stable irradiance is stated, but 'a string clearly below that band is the signature' (of a fault) is not stated.
- sentence 5: support check: partial - 90% of average as normal (string loss calc) and the 0.8 ratio/2 hour default alert vs best string of same component are stated, but 'monitoring tools' are two specific products and 'same device' is approximate.
- sentence 7: support check: partial - Glass breakage lowering whole-string current is stated, and u21 says localized heating reduces string output, but the link of hotspot from cell damage lowering output is only loosely stated; 'completely broken' is fine, hotspot from cell damage is in u21 (cracked cells).
-->
