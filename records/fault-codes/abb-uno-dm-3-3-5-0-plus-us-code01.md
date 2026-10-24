---
id: fc:abb-uno-dm-3-3-5-0-plus-us-code01
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS CODE:01
aliases:
- CODE:01
- code01
- ABB / FIMER CODE:01
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: CODE:01
code_key: code01
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r2
    h: 36d14076027d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r2
    h: 7fc13c1c7983
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r2
    h: 36d14076027d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r2
    h: 36d14076027d
  review: drafted
  review_note: 'review: partial - The row ties the limitation to grid frequency exceeding certain limits,
    but it describes a user-set over-frequency derating rather than stating that…'
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: Limit percentage is variable and set by parameter; printed values are only examples.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r2
    h: 7fc13c1c7983
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r2
    h: 36d14076027d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r2
    h: 36d14076027d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r2
    h: 7fc13c1c7983
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r2
    h: 36d14076027d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r2
    h: 36d14076027d
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r2
    h: 36d14076027d
  review: drafted
---
