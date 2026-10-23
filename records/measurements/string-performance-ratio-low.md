---
id: meas:string-performance-ratio-low
type: Measurement
name: Low string performance ratio
aliases:
- String Performance Alert
- Abnormal String Power
- PV string abnormal alarm
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: normalized string current stays below a set fraction of the highest string for hours
---
This signature shows up when a string's normalized DC current stays below a set fraction of the best string on the same inverter or combiner. A common default fraction is 0.8 of the best string. Strings of different sizes are normalized first, for example by the number of modules or the DC capacity per string, so that they can be compared fairly. The low ratio has to last for a set time during daylight hours. Periods just after sunrise and just before sunset are ignored, and the best string has to carry more than a minimum current. Inverters raise similar alarms. Sungrow flags one string that is abnormally low against another string on the same MPPT. Huawei flags abnormal string power when a string has been shaded for a long time or has degraded abnormally. Typical causes are shading, strings facing different directions, a string with fewer modules than the others, or a string that has been removed from an inverter that remembers its strings. Low current with normal voltage can come from faulty modules, open or damaged array connections, low irradiance, a faulty measuring device, or a weak string in a parallel group that limits the current of the strings combined with it. To confirm, move the suspect string to another MPPT. If the low current moves with the string, the fault is in the string, so run an IV curve trace on it rather than replacing the inverter.

<!-- review notes
- sentence 5: support check: partial - Shading, different orientation, fewer modules (in the 1548-1579 String Current Reflux row) and a removed string with string memory are all stated. The 1548-1579 row and the other alarm texts do not tie fewer modules to the same alarm, so the statement merges causes from different alarms.
-->
