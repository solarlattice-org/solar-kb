---
id: fc:abb-pvs-166-175-tl-us-w21
type: FaultCode
name: ABB / FIMER PVS-166-175-TL W021
aliases:
- W021
- w21
- ABB / FIMER W021
- P-reduction Star t
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: W021
code_key: w21
display_message: P-reduction Star t
vendor_severity: Warning
page: 138
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r6
    h: 6ad62536a56b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r6
    h: 6ad62536a56b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  note: Start of one of several power limitations, e.g. user, grid, or temperature
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r6
    h: 6ad62536a56b
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r7
    h: 8cebcc25b981
  review: drafted
  review_note: 'support check: partial - Power reduction activation and causes like user settings, grid,
    temperature are stated, but nothing says the symptom is derating beyond…'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: No reduced-output value stated
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r6
    h: 6ad62536a56b
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r7
    h: 8cebcc25b981
  review: drafted
---
