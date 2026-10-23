---
id: symptom:high-ambient-temperature
type: Symptom
name: High ambient temperature
aliases:
- Excessively High Ambient Temperature
- Outside temperature is too high
- ambient temperature too high
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-temperature-high
  note: Inverter manuals list high ambient temperature as one cause of cabinet or internal overtemperature
    alarms, for example Huawei alarm 321 and the Chint TempOver protection.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r2
    h: bdc729b2548c
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r4
    h: 8cc1cda60aae
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=19
    h: 1017406d3f0d
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r1
    h: b1305c5fc121
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r6
    h: 8ec9d90047d2
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:temperature-derated-output
  note: Inverter output power is reduced once ambient temperature rises above the full-power limit. For
    the CPS SCA25KTL-DO/US-208 this limit is 45°C.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=10.3.1
    h: 5e0ffb64a1b8
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=51.r1
    h: 3dc3d0553f86
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r2
    h: a719f704eb73
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r1
    h: 6f58f18f43fc
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r4
    h: 5b52ed835ea5
  review: drafted
- claim_id: c3
  attr: output_limit
  value:
    nominal: 21.1
    unit: unit:KiloW
  conditions: Huawei SUN2000-25KTL-US at 850 V DC MPPT input and 60°C ambient (rated 25 kW up to 45°C)
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r2
    h: a719f704eb73
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c4
  attr: output_limit
  value:
    nominal: 21.5
    unit: unit:KiloW
  conditions: Huawei SUN2000-25KTL-US at 560 V DC MPPT input and 60°C ambient (rated 25 kW up to 45°C)
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r1
    h: 6f58f18f43fc
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c5
  attr: output_limit
  value:
    nominal: 25.4
    unit: unit:KiloW
  conditions: Huawei SUN2000-30KTL-US at 850 V DC MPPT input and 53°C ambient (rated 30 kW up to 45°C)
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r4
    h: 5b52ed835ea5
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: output_limit
  value:
    nominal: 21.6
    unit: unit:KiloW
  conditions: Huawei SUN2000-30KTL-US at 850 V DC MPPT input and 60°C ambient (rated 30 kW up to 45°C)
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=53.r4
    h: 5b52ed835ea5
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
---
High ambient temperature around an inverter shows up as overtemperature alarms. Examples are Huawei cabinet overtemperature alarm 321, SMA Sunny Central error 6508, Sungrow fault 37 and the Chint TempOver protection. The same alarms can also come from poor ventilation, a blocked air inlet or dusty filter, direct sunlight on the unit, or a fan that is stopped or faulty. This means inverter overheating caused by fan failure has to be ruled out. First compare the measured ambient temperature with the inverter's specified operating range. The Huawei SUN2000 units are rated for -25°C to +60°C. If the ambient temperature and ventilation are both within requirements, check the fan and the air inlet. If the alarm persists after that, contact the manufacturer. Before a trip, high ambient temperature often shows up as derated AC output. One CPS model starts to derate above 45°C, and the Huawei 30 kW model is limited to 21.6 kW at 60°C. These faults usually clear by themselves once the temperature returns to normal. Some manuals suggest watching for about 30 minutes before taking further action. High ambient temperature also lowers the current-carrying capacity of cables, so check cable sizing on hot sites.

<!-- review notes
- sentence 2: support check: partial - The passages give poor ventilation, blocked inlet or dusty filter, sunlight and fan faults as causes. The 'has to be ruled out' conclusion is an inference, and not every cause appears for every alarm.
- sentence 4: support check: partial - The Huawei and Chint passages support checking the fan and air inlet and then contacting support. The fixed order, and contacting the manufacturer after checking the fan, comes from a mix of vendors.
- sentence 5: support check: partial - The 45°C CPS derating and the Huawei 21.6 kW at 60°C are stated. 'Before a trip, derating often shows up' is not stated in the passages.
- sentence 6: support check: partial - Sungrow says the inverter generally resumes when temperature normalizes, and Chint says to observe for 30 minutes. 'Usually clear by themselves' across all of these faults is a generalization.
- sentence 7: support check: partial - The passage says higher ambient temperature around a cable reduces ampacity. The advice to check cable sizing on hot sites is not stated.
-->
