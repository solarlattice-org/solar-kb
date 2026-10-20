---
id: symptom:pv-input-abnormal
type: Symptom
name: Abnormal PV input
aliases:
- PVx abnormal
- PV Abnormal Alarm
- String x output current anomaly
claims:
- claim_id: c1
  rel: observed_as
  target: meas:string-current-below-average
  note: On SG-CX-US units, codes 548-563 and 580-587 are reported as a string output current anomaly.
    The manual lists shading, soiling and abnormal module aging as causes to check.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55
    h: 984f64a5a050
  review: drafted
---
The inverter raises a per-input alarm that a specific PV input or string is abnormal. The fault code tells you which input or string is affected. Start by comparing the voltage and current of the flagged input with the other inputs to narrow down the cause. If that input is not meant to have a string connected, you can ignore the alarm. If it should be connected, check that the connection is secure and tighten any loose wiring. Check the DC fuse for that input and replace it if it is blown. If the current is low, look for shading or soiling on the string's modules and clean or remove it. Also check the modules for abnormal aging. If none of these causes is found and the alarm stays active, contact Sungrow service.

<!-- review notes
- sentence 2: support check: partial - The u3/u4 row says to check whether voltage and current are abnormal, but not to compare the flagged input against other inputs.
- sentence 3: support check: partial - Ignore-if-not-needed and check connection are stated, but 'tighten loose wiring' is only loosely implied (reliably connected/loose wiring).
-->
