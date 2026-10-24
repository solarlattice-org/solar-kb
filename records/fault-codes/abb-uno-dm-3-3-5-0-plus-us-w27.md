---
id: fc:abb-uno-dm-3-3-5-0-plus-us-w27
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS W027
aliases:
- W027
- w27
- ABB / FIMER W027
- Latch-Manual reset
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: W027
code_key: w27
display_message: Latch-Manual reset
vendor_severity: Warning
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r1
    h: 2c53c270cb8b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: 05b933b68f8a
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r1
    h: 2c53c270cb8b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: 05b933b68f8a
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:latch-alarm-reset
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r3
    h: eda9102f1499
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r1
    h: 2c53c270cb8b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r2
    h: 05b933b68f8a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - W027 is a latch alarm manual reset event, not an error; ''reports
    latched alarm reset'' fits, though it is a…'
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: Operator action that is only logged in the event history; not an error.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r3
    h: eda9102f1499
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r1
    h: 2c53c270cb8b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r2
    h: 05b933b68f8a
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r1
    h: 2c53c270cb8b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: 05b933b68f8a
  review: drafted
---
