---
id: fc:abb-uno-dm-3-3-5-0-plus-us-w49
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS W049
aliases:
- W049
- w49
- ABB / FIMER W049
- Global-Settings Event
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: W049
code_key: w49
display_message: Global-Settings Event
vendor_severity: Warning
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r5
    h: 9478415f1e20
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r6
    h: 681145b823ab
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r5
    h: 9478415f1e20
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r6
    h: 681145b823ab
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-standard-changed
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r9
    h: 7a654ec2222f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r5
    h: 9478415f1e20
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r5
    h: 9478415f1e20
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r6
    h: 681145b823ab
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r6
    h: 5bd74e352d18
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: User-made change, only logged in event history
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r9
    h: 7a654ec2222f
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r5
    h: 9478415f1e20
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r5
    h: 9478415f1e20
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r6
    h: 681145b823ab
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r6
    h: 5bd74e352d18
  review: drafted
---
