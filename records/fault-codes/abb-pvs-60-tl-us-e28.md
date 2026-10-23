---
id: fc:abb-pvs-60-tl-us-e28
type: FaultCode
name: ABB / FIMER PVS-60-TL E028
aliases:
- E028
- e28
- ABB / FIMER E028
- Error Meas F
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E028
code_key: e28
display_message: Error Meas F
vendor_severity: Error
page: 157
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-measurement-error
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r5
    h: b84626e5e6ba
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r9
    h: 2328009f7962
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r5
    h: b84626e5e6ba
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r9
    h: 2328009f7962
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r5
    h: b84626e5e6ba
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r9
    h: 2328009f7962
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r5
    h: b84626e5e6ba
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r9
    h: 2328009f7962
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r5
    h: b84626e5e6ba
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r9
    h: 2328009f7962
  review: drafted
  review_note: 'support check: partial - The power-cycle and contact-service sequence is stated, but the
    manual-reset clearing isn''t.'
---
