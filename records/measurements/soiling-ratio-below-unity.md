---
id: meas:soiling-ratio-below-unity
type: Measurement
name: Soiling ratio below unity
aliases:
- SR
- Cleanness Index
- Soiling Factor
- Soiling Loss Factor
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 4.4
    unit: unit:PERCENT
  conditions: Mean daily production loss from dust on a PV module in Malaga, Spain
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions); possible conflict
    with c8 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 20
    unit: unit:PERCENT
  conditions: Malaga, Spain, during long dry periods of dust accumulation
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 3
    max: 4
    unit: unit:PERCENT
  conditions: Belgium, power loss over a 5-week period
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 5.86
    unit: unit:PERCENT
  conditions: Crete, estimated annual soiling loss
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions); possible conflict
    with c8 (same source; check the conditions)
- claim_id: c5
  attr: typical_power_loss
  value:
    nominal: 6.9
    unit: unit:PERCENT
  conditions: Southern Italy, monthly power loss for a plant on sandy soil
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c4 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions); possible conflict
    with c8 (same source; check the conditions)
- claim_id: c6
  attr: typical_power_loss
  value:
    nominal: 1.1
    unit: unit:PERCENT
  conditions: Southern Italy, monthly power loss for a plant on more compact soil
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c4 (same source; check the conditions); possible conflict with c5 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions); possible conflict
    with c8 (same source; check the conditions)
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 45.8
    unit: unit:PERCENT
  conditions: Kuwait, over a three-month period without cleaning
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: typical_power_loss
  value:
    min: 3
    max: 4
    unit: unit:PERCENT
  conditions: Global estimate of annual PV energy production lost to soiling in 2018, stated as at least
    this range
  note: The source words this as 'at least 3-4%'.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h17
    h: 576c10b1646b
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions)
---
The soiling ratio compares the output of a soiled PV device with the output of the same or a matching device kept clean. A value of one means there is no soiling loss. The value falls as dirt builds up and reaches zero when soiling blocks all light. The soiling loss is one minus the soiling ratio. Dividing the performance ratio by the soiling ratio gives a soiling-corrected performance ratio. Electrical soiling stations measure two PV devices side by side: one is cleaned regularly and the other is left to soil naturally. The pair can be cell-cell, module-module or cell-module. Optical sensors instead estimate the loss from light scattered by dust or from transmission loss. Measure near solar noon: within two hours of noon for fixed systems, or at small angles of incidence for trackers. Typically only clear-sky data above 500 W/m2 effective irradiance is used. The ratio of power outputs is the preferred measure, but the ratio of short-circuit currents is often used instead. With uneven soiling, such as dirt collecting along the bottom cell row, the current ratio can understate the real power loss, because a bypassed substring reduces power without changing short-circuit current. A soiling ratio below one is the signature of soiling losses from dust, snow and other deposits that reduce the light reaching the cells. Check the reference first. If the clean device is not cleaned often enough, the soiling ratio is badly underestimated, and a single dirty irradiance sensor can show apparent soiling that does not represent the array.

<!-- review notes
- sentence 6: support check: partial - Passages say soiling from dust and snow reduces output and SR falls below one with soiling, but do not explicitly state that a ratio below one is the signature of such losses from snow and other deposits.
-->
