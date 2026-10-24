---
id: fc:abb-pvs-60-tl-us-w23
type: FaultCode
name: ABB / FIMER PVS-60-TL W023
aliases:
- W023
- w23
- ABB / FIMER W023
- date/time changed
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W023
code_key: w23
display_message: date/time changed
vendor_severity: Warning
page: 153
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r9
    h: 297e19e7a46b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r9
    h: 297e19e7a46b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:clock-time-changed
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r9
    h: 297e19e7a46b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r9
    h: f948f5938c4c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r9
    h: f948f5938c4c
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: 67fd1567335e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r9
    h: 67fd1567335e
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r9
    h: e0a1f09213fe
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  note: User-made change, only logged in event history
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r9
    h: 297e19e7a46b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r9
    h: f948f5938c4c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r9
    h: f948f5938c4c
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r9
    h: 67fd1567335e
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r9
    h: 67fd1567335e
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r9
    h: e0a1f09213fe
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r9
    h: 297e19e7a46b
  review: drafted
---
