---
id: fc:abb-pvs-60-tl-us-code00
type: FaultCode
name: ABB / FIMER PVS-60-TL CODE:00
aliases:
- CODE:00
- code00
- ABB / FIMER CODE:00
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: CODE:00
code_key: code00
page: 160
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:user-power-limit
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r1
    h: fb1bdd0da281
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r1
    h: fb1bdd0da281
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r1
    h: e437ee039933
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: Limit percentage is variable and user-set; printed values are only examples.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r1
    h: fb1bdd0da281
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r1
    h: fb1bdd0da281
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r1
    h: e437ee039933
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r1
    h: fb1bdd0da281
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r1
    h: fb1bdd0da281
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r1
    h: e437ee039933
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  review: drafted
---
