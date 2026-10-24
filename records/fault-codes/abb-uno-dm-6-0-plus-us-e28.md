---
id: fc:abb-uno-dm-6-0-plus-us-e28
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E028
aliases:
- E028
- e28
- ABB / FIMER E028
- Error Meas F
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E028
code_key: e28
display_message: Error Meas F
vendor_severity: Error
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  review: drafted
- claim_id: c4
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
  review: drafted
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
  rel: applies_to
  target: prod:abb-uno-dm-6-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  review: drafted
---
