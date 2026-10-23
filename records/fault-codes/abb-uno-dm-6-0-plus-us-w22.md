---
id: fc:abb-uno-dm-6-0-plus-us-w22
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS W022
aliases:
- W022
- w22
- ABB / FIMER W022
- Reactive power mode changed
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: W022
code_key: w22
display_message: Reactive power mode changed
vendor_severity: Warning
page: 123
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r8
    h: 20d1f512c6e3
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r8
    h: 3cdae2f5a508
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r8
    h: 20d1f512c6e3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r8
    h: 3cdae2f5a508
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:reactive-power-mode-change
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r8
    h: 3735cef94281
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r8
    h: 20d1f512c6e3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r8
    h: 20d1f512c6e3
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 3cdae2f5a508
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r8
    h: 3cdae2f5a508
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r8
    h: 2aee96f36675
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: User-made change, only logged in event history
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r8
    h: 3735cef94281
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r8
    h: 20d1f512c6e3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r8
    h: 20d1f512c6e3
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 3cdae2f5a508
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r8
    h: 3cdae2f5a508
  review: drafted
---
