---
id: fc:abb-uno-dm-6-0-plus-us-w4
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS W004
aliases:
- W004
- w4
- ABB / FIMER W004
- Grid OV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: W004
code_key: w4
display_message: Grid OV
vendor_severity: Warning
page: 122
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r2
    h: 3965adb4feab
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r2
    h: df1c2485a0df
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 59560937bbad
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r2
    h: 3965adb4feab
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r2
    h: df1c2485a0df
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 59560937bbad
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:utility-consultation
  note: When high grid impedance is found; service if values return within limits
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r2
    h: 3965adb4feab
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r2
    h: df1c2485a0df
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 59560937bbad
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:ac-connection-check
  note: When supply-point voltage is much lower than at the inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r2
    h: 3965adb4feab
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r2
    h: df1c2485a0df
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 59560937bbad
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:abb-uno-dm-6-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r2
    h: 59560937bbad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r2
    h: 76e393399eeb
  review: drafted
---
