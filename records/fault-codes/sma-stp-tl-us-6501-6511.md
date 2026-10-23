---
id: fc:sma-stp-tl-us-6501-6511
type: FaultCode
name: SMA STP-TL-US 6501-6511
aliases:
- 6501-6511
- SMA 6501-6511
- Self diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 6501-6511
code_key: 6501-6511
code_from: 6501
code_to: 6511
display_message: Self diagnosis > Interference device
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
  review_note: 'support check: partial - Fans are cleaned as a measure, but the passage doesn''t say the
    fan is the affected component.'
- claim_id: c4
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r5
    h: cea4d1332e3a
  review: drafted
---
