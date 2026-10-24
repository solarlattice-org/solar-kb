---
id: fc:abb-uno-dm-3-3-5-0-plus-us-w6
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS W006
aliases:
- W006
- w6
- ABB / FIMER W006
- Grid OF
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: W006
code_key: w6
display_message: Grid OF
vendor_severity: Warning
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: 1b9be1fc2507
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: 3e4a0c96f15a
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: 1b9be1fc2507
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: 3e4a0c96f15a
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r4
    h: 092ec9aa40de
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r4
    h: d232479296d0
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: 1b9be1fc2507
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r4
    h: 1b9be1fc2507
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r4
    h: 3e4a0c96f15a
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r4
    h: 092ec9aa40de
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r4
    h: d232479296d0
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: 1b9be1fc2507
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r4
    h: 1b9be1fc2507
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r4
    h: 3e4a0c96f15a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if frequency is back within limits yet alarm continues
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r4
    h: 092ec9aa40de
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r4
    h: d232479296d0
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: 1b9be1fc2507
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r4
    h: 1b9be1fc2507
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r4
    h: 3e4a0c96f15a
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: 1b9be1fc2507
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: 3e4a0c96f15a
  review: drafted
---
