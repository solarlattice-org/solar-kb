---
id: fc:abb-uno-dm-3-3-5-0-plus-us-e58
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS E058
aliases:
- E058
- e58
- ABB / FIMER E058
- Pin vs Pout check error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: E058
code_key: e58
display_message: Pin vs Pout check error
vendor_severity: Error
page: 132
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:ac-dc-power-deviation
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r4
    h: 9804bb4d579d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r3
    h: 5a6deda9bc8c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r10
    h: 6a979b76c3aa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r3
    h: 7b9ff7c47725
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r4
    h: 9804bb4d579d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r3
    h: 5a6deda9bc8c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r10
    h: 6a979b76c3aa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r3
    h: 7b9ff7c47725
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r4
    h: 9804bb4d579d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r3
    h: 5a6deda9bc8c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r10
    h: 6a979b76c3aa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r3
    h: 7b9ff7c47725
  review: drafted
  review_note: 'support check: partial - Restart is implied as a first step, but the passages don''t say
    it mitigates the fault.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If it persists after a power cycle
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r4
    h: 9804bb4d579d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r3
    h: 5a6deda9bc8c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r10
    h: 6a979b76c3aa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r3
    h: 7b9ff7c47725
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; then service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r4
    h: 9804bb4d579d
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r3
    h: 5a6deda9bc8c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r10
    h: 6a979b76c3aa
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r3
    h: 7b9ff7c47725
  review: drafted
  review_note: 'support check: partial - The power-cycle-then-service sequence is stated, but the passages
    don''t say the fault clears by manual reset.'
- claim_id: c9
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r4
    h: 8ff284658bd9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r10
    h: 0cee5ac4ed22
  review: drafted
---
