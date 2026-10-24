---
id: fc:abb-pvs-166-175-tl-us-w7
type: FaultCode
name: ABB / FIMER PVS-166-175-TL W007
aliases:
- W007
- w7
- ABB / FIMER W007
- Grid UF
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: W007
code_key: w7
display_message: Grid UF
vendor_severity: Warning
page: 137
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r5
    h: 5b1fc71784aa
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r5
    h: 5b1fc71784aa
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r5
    h: 5b1fc71784aa
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r5
    h: f72b1cc89f2b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r5
    h: 2ac9e907557c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r5
    h: 2ac9e907557c
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r5
    h: 8883ba67bd06
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r5
    h: 5b1fc71784aa
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r5
    h: f72b1cc89f2b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r5
    h: 2ac9e907557c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r5
    h: 2ac9e907557c
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r5
    h: 8883ba67bd06
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if frequency is back within limits yet alarm continues
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r5
    h: 5b1fc71784aa
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r5
    h: f72b1cc89f2b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r5
    h: 2ac9e907557c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r5
    h: 2ac9e907557c
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r5
    h: 8883ba67bd06
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:abb-pvs-166-175-tl-us
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r5
    h: 5b1fc71784aa
  review: drafted
---
