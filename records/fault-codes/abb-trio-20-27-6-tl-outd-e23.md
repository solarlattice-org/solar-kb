---
id: fc:abb-trio-20-27-6-tl-outd-e23
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL E023
aliases:
- E023
- e23
- ABB / FIMER E023
- DC in error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: E023
code_key: e23
display_message: DC in error
vendor_severity: Error
page: 112
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r3
    h: 81aec677eb76
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r3
    h: 81aec677eb76
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r7
    h: e3c2d26bf93a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r1
    h: 2c4ad9e8b01b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 12609ae2343d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r6
    h: 14d50e25c3f6
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r3
    h: 81aec677eb76
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes on its own; systematic recurrence indicates internal fault needing service.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r7
    h: e3c2d26bf93a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r1
    h: 2c4ad9e8b01b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 12609ae2343d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the error keeps recurring.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r7
    h: e3c2d26bf93a
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r1
    h: 2c4ad9e8b01b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r5
    h: 12609ae2343d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r3
    h: 81aec677eb76
  review: drafted
---
