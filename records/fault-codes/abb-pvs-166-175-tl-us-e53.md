---
id: fc:abb-pvs-166-175-tl-us-e53
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E053
aliases:
- E053
- e53
- ABB / FIMER E053
- AFDD Fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E053
code_key: e53
display_message: AFDD Fault
vendor_severity: Error
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r10
    h: 029eb57fa1fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r13
    h: 7d7e6c35e11f
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r13
    h: 7d7e6c35e11f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r5
    h: 43a11c14d441
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 43a11c14d441
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r10
    h: 029eb57fa1fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r13
    h: 7d7e6c35e11f
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r13
    h: 7d7e6c35e11f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r5
    h: 43a11c14d441
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 43a11c14d441
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r10
    h: 029eb57fa1fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r13
    h: 7d7e6c35e11f
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r13
    h: 7d7e6c35e11f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r5
    h: 43a11c14d441
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 43a11c14d441
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r10
    h: 029eb57fa1fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r13
    h: 7d7e6c35e11f
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r13
    h: 7d7e6c35e11f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r5
    h: 43a11c14d441
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 43a11c14d441
  review: drafted
  review_note: 'support check: partial - Switching off and on is implied as a first step, but the passages
    don''t say it resolves the fault; they…'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r10
    h: 029eb57fa1fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r13
    h: 7d7e6c35e11f
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r13
    h: 7d7e6c35e11f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r5
    h: 43a11c14d441
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 43a11c14d441
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r10
    h: 029eb57fa1fa
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r13
    h: 7d7e6c35e11f
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r13
    h: 7d7e6c35e11f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r5
    h: 43a11c14d441
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 43a11c14d441
  review: drafted
  review_note: 'support check: partial - Power cycle then contact assistance is stated, but the passages
    don''t state that the code clears by manual reset.'
- claim_id: c9
  rel: applies_to
  target: prod:abb-pvs-166-175-tl-us
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r9
    h: caaf5e18b7d4
  review: drafted
---
