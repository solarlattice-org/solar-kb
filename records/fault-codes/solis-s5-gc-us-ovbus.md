---
id: fc:solis-s5-gc-us-ovbus
type: FaultCode
name: Solis S5-GC OV-BUS
aliases:
- OV-BUS
- ovbus
- Solis OV-BUS
- DC BUS voltage is too high
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: OV-BUS
code_key: ovbus
display_message: DC BUS voltage is too high
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Internal damage or loose internal wire; replacement after measurements.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
---
