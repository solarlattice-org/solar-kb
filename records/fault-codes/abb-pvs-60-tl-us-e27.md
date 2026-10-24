---
id: fc:abb-pvs-60-tl-us-e27
type: FaultCode
name: ABB / FIMER PVS-60-TL E027
aliases:
- E027
- e27
- ABB / FIMER E027
- Error Meas V
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E027
code_key: e27
display_message: Error Meas V
vendor_severity: Error
page: 157
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-voltage-mismatch
  note: Redundant internal grid voltage measurements disagree
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r4
    h: 3d15f0478309
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r9
    h: 0911c8537c35
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r3
    h: 4c42ac0d9b3b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r3
    h: 4c42ac0d9b3b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r8
    h: 7af3ba9699c4
  review: drafted
  review_note: 'support check: partial - Redundant internal grid voltage measurement error is stated,
    but ''disagree/mismatch'' is only implied.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r4
    h: 3d15f0478309
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r9
    h: 0911c8537c35
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r3
    h: 4c42ac0d9b3b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r3
    h: 4c42ac0d9b3b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r8
    h: 7af3ba9699c4
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r4
    h: 3d15f0478309
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r9
    h: 0911c8537c35
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r3
    h: 4c42ac0d9b3b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r3
    h: 4c42ac0d9b3b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r8
    h: 7af3ba9699c4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r4
    h: 3d15f0478309
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r9
    h: 0911c8537c35
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r3
    h: 4c42ac0d9b3b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r3
    h: 4c42ac0d9b3b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r8
    h: 7af3ba9699c4
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r4
    h: 3d15f0478309
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r9
    h: 0911c8537c35
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r3
    h: 4c42ac0d9b3b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r3
    h: 4c42ac0d9b3b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r8
    h: 7af3ba9699c4
  review: drafted
  review_note: 'support check: partial - Power cycle then contact service is stated, but clearing by manual
    reset isn''t stated.'
- claim_id: c8
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r5
    h: 3feb67a5ed3b
  review: drafted
---
