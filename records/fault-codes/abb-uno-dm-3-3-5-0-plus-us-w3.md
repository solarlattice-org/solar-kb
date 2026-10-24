---
id: fc:abb-uno-dm-3-3-5-0-plus-us-w3
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS W003
aliases:
- W003
- w3
- ABB / FIMER W003
- Grid Fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: W003
code_key: w3
display_message: Grid Fail
vendor_severity: Warning
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r1
    h: e7089c9aee77
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r1
    h: e7089c9aee77
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-parameters-out-of-range
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r1
    h: ae9b94816ed3
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r1
    h: e7089c9aee77
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r9
    h: 02c036f32afe
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:grid-instability
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r1
    h: ae9b94816ed3
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r1
    h: e7089c9aee77
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r9
    h: 02c036f32afe
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r1
    h: ae9b94816ed3
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r1
    h: e7089c9aee77
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r9
    h: 02c036f32afe
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When high grid impedance raises voltage; limits changed only with operator authorisation
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r1
    h: ae9b94816ed3
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r1
    h: e7089c9aee77
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r9
    h: 02c036f32afe
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  note: When supply-point voltage is much lower than at the inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r1
    h: ae9b94816ed3
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r1
    h: e7089c9aee77
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r9
    h: 02c036f32afe
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r1
    h: 1ca0f3fcf49a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r1
    h: e7089c9aee77
  review: drafted
---
