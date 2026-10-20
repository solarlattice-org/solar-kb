---
id: method:grid-frequency-measurement
type: DetectionMethod
name: Grid frequency measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:grid-frequency-reading-out-of-limit
  note: Used to confirm grid over-frequency, under-frequency and grid abnormal faults. On Solis units,
    a reading that differs from the LCD value may point to a faulty inverter measurement circuit rather
    than the grid.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  review: drafted
---
Grid frequency measurement means measuring the real grid frequency when an inverter reports a grid over-frequency, under-frequency or grid abnormal fault, and comparing it with the inverter's set protection range. On Solis inverters, turn the DC switch off, then check the frequency at the inverter test points and compare it with the LCD reading, because a faulty measurement circuit can give a false reading. At commissioning, measure the frequency of each phase to ground if your meter can do it, and confirm each value is within local grid standards and the inverter specifications. The inverter display also shows the grid frequency value for a quick comparison. Sungrow SG250HX-US and SG36CX-US/SG60CX-US inverters list a nominal grid frequency of 60 Hz and a grid frequency range of 55 to 65 Hz. If the measured frequency is outside the set range, contact the local utility; on Solis units, raise the upper limit only with the utility's permission. Also check that the protection parameters are set correctly in the app or on the LCD. If the fault continues after these causes are ruled out, contact the manufacturer's service team or replace the inverter.

<!-- review notes
- sentence 2: support check: partial - Passage lists DC switch off, check frequency at test points, and check LCD reading for a bad measurement circuit, but does not explicitly say to compare the two values.
- sentence 4: support check: partial - The display shows F_Grid grid frequency value, but 'for quick comparison' purpose is not stated.
-->
