---
id: fc:abb-uno-dm-3-3-5-0-plus-us-e34
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS E034
aliases:
- E034
- e34
- ABB / FIMER E034
- Interlock fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: E034
code_key: e34
display_message: Interlock fail
vendor_severity: Error
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r10
    h: 07c805c45e9c
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r10
    h: 07c805c45e9c
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:internal-device-fault
  note: IGBT circuitry not ready
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r1
    h: 3143f70ad512
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r2
    h: 047f046564db
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: b2bbc651b042
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r10
    h: 07c805c45e9c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r5
    h: c6d520291519
  review: drafted
  review_note: 'support check: partial - IGBT circuitry not ready, error inside the inverter, is stated;
    ''internal device fault'' is a loose label.'
- claim_id: c5
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r1
    h: 3143f70ad512
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r2
    h: 047f046564db
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: b2bbc651b042
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r10
    h: 07c805c45e9c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r5
    h: c6d520291519
  review: drafted
  review_note: 'support check: partial - IGBT circuitry is named, but ''inverter bridge'' isn''t; the
    passages only say the error is inside the inverter.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r1
    h: 3143f70ad512
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r2
    h: 047f046564db
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: b2bbc651b042
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r10
    h: 07c805c45e9c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r5
    h: c6d520291519
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r1
    h: 3143f70ad512
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r2
    h: 047f046564db
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: b2bbc651b042
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r10
    h: 07c805c45e9c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r5
    h: c6d520291519
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r1
    h: 3143f70ad512
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r2
    h: 047f046564db
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r7
    h: b2bbc651b042
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: b2bbc651b042
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r10
    h: 07c805c45e9c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r5
    h: c6d520291519
  review: drafted
  review_note: 'support check: partial - Passages say switch off/on and contact assistance if it persists,
    but never state it clears by a manual reset classification…'
---
