---
id: symptom:reverse-polarity
type: Symptom
name: Reverse polarity
aliases:
- PVx input reverse connection
- PVxReverse
- MPPT Reverse Connection
- reversed string
claims:
- claim_id: c1
  rel: observed_as
  target: meas:double-voltage-between-string-positives
  note: 'Combiner box test before fuses are inserted: strings share a common negative bus and the meter
    goes between the first string''s positive pole and each other string''s positive pole. A correctly
    wired string reads near zero (within ±15 V). A reversed string reads about twice the system voltage.'
  quote: A reverse polarity condition will be very evident if it exists - the measured voltage will be
    twice the system voltage.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.3
    h: 210834c56bc7
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:negative-polarity-reading
  note: In a plain multimeter polarity check, a reversed string shows a minus sign. This is easy to overlook
    when many circuits are checked.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.3
    h: 210834c56bc7
  review: drafted
  review_note: 'support check: partial - Passage says the ''-'' symbol is easy to overlook in a multimeter
    polarity check, but doesn''t explicitly say a reversed string shows a minus sign (implied only).'
- claim_id: c3
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: With a reversed PV input the inverter goes into a fault or alarm state, reported per input or
    string (e.g. CPS PVxReverse, Sungrow PV/MPPT Reverse Connection), and does not operate normally.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=h133
    h: 80af7eb48e69
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r3
    h: 3a00291b1227
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=44.r2
    h: a863e081c095
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r2
    h: ef214f6e526a
  review: drafted
---
Reverse polarity means a PV string is wired into the inverter or combiner box with plus and minus swapped, and the inverter reports it as a reverse-connection fault or alarm for the affected input or string. A reversed input keeps the inverter in a fault or alarm state, so it will not run normally. A reversed string in a combiner box is easy to miss, and the inverter does not protect it; at high irradiance it can blow the string fuse, and the voltage across that fuse can reach about twice Voc, which risks a fire. To find it, turn the DC switch off, open the fuse holders to isolate the strings, and use a meter to identify the string wired backwards before you correct it. In a combiner box, a reversed string shows up clearly: measured positive to positive against a reference string on a shared negative bus, it reads about twice the system voltage instead of near zero. Sungrow says to change the polarity only once the string current has dropped below 0.5 A. Check the polarity of all DC cables before closing switches or inserting fuses, and if a reversed string is found on a system that was already connected, check its modules and bypass diodes for damage. Even inverters with reverse polarity protection can have those circuits or the inverter itself damaged by a reversed connection left in place for a long time.

<!-- review notes
- sentence 8: support check: partial - Passage is about Solis inverters specifically and says prolonged reverse connection may damage protection circuits/inverter; the generalization to all inverters with protection is broader.
-->
