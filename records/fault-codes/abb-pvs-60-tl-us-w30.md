---
id: fc:abb-pvs-60-tl-us-w30
type: FaultCode
name: ABB / FIMER PVS-60-TL W030
aliases:
- W030
- w30
- ABB / FIMER W030
- Energy Meter ER- ROR
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W030
code_key: w30
display_message: Energy Meter ER- ROR
vendor_severity: Warning
page: 154
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r4
    h: 367f2ea372d3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r4
    h: 367f2ea372d3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r4
    h: 367f2ea372d3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r4
    h: 367f2ea372d3
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r4
    h: 367f2ea372d3
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Check the RS485 line first; if it persists after a power cycle, contact service.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r4
    h: 367f2ea372d3
  review: drafted
---
