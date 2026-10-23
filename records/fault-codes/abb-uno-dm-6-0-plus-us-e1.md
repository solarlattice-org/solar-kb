---
id: fc:abb-uno-dm-6-0-plus-us-e1
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E001
aliases:
- E001
- e1
- ABB / FIMER E001
- Input OC
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E001
code_key: e1
display_message: Input OC
vendor_severity: Error
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r7
    h: 06edbae723de
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r8
    h: 22477180987e
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r7
    h: 06edbae723de
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r8
    h: 22477180987e
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r6
    h: e790b7311a7d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r11
    h: 97e257a8a81d
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r7
    h: 06edbae723de
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r7
    h: 06edbae723de
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r8
    h: 22477180987e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r8
    h: 22477180987e
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r1
    h: 3e78137a63a8
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r6
    h: e790b7311a7d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r11
    h: 97e257a8a81d
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r7
    h: 06edbae723de
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r7
    h: 06edbae723de
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r8
    h: 22477180987e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r8
    h: 22477180987e
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r1
    h: 3e78137a63a8
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Check array composition and input parallel configuration first; contact service if both are correct.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r6
    h: e790b7311a7d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r11
    h: 97e257a8a81d
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r7
    h: 06edbae723de
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r7
    h: 06edbae723de
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r8
    h: 22477180987e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r8
    h: 22477180987e
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r1
    h: 3e78137a63a8
  review: drafted
---
