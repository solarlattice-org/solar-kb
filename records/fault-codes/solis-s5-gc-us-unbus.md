---
id: fc:solis-s5-gc-us-unbus
type: FaultCode
name: Solis S5-GC UN-BUS
aliases:
- UN-BUS
- unbus
- Solis UN-BUS
- DC BUS voltage is too low
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: UN-BUS
code_key: unbus
display_message: DC BUS voltage is too low
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Internal damage or loose internal wire; replacement after measurements.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  review: drafted
---
