---
id: fc:abb-uno-dm-3-3-5-0-plus-us-e32
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS E032
aliases:
- E032
- e32
- ABB / FIMER E032
- Error Read I
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: E032
code_key: e32
display_message: Error Read I
vendor_severity: Error
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r8
    h: 21aa632794b8
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r8
    h: 21aa632794b8
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:phase-imbalance
  note: Three-phase models only
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r9
    h: c8616fd8b6b3
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r10
    h: 892b8b41c15c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: c19bdccf04a4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r8
    h: 21aa632794b8
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r3
    h: 7347f74a9fc2
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r9
    h: c8616fd8b6b3
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r10
    h: 892b8b41c15c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: c19bdccf04a4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r8
    h: 21aa632794b8
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r3
    h: 7347f74a9fc2
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r9
    h: c8616fd8b6b3
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r10
    h: 892b8b41c15c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: c19bdccf04a4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r8
    h: 21aa632794b8
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r3
    h: 7347f74a9fc2
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r9
    h: c8616fd8b6b3
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r10
    h: 892b8b41c15c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: c19bdccf04a4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r8
    h: 21aa632794b8
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r3
    h: 7347f74a9fc2
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r9
    h: c8616fd8b6b3
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r10
    h: 892b8b41c15c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r5
    h: c19bdccf04a4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r5
    h: c19bdccf04a4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r8
    h: 21aa632794b8
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r3
    h: 7347f74a9fc2
  review: drafted
  review_note: 'support check: partial - Power cycle then contact service is stated, but manual-reset
    clearing isn''t.'
---
