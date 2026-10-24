---
id: fc:abb-trio-20-27-6-tl-outd-e4
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL E004
aliases:
- E004
- e4
- ABB / FIMER E004
- Bulk OV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: E004
code_key: e4
display_message: Bulk OV
vendor_severity: Error
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r2
    h: 9eeda4723b68
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r10
    h: 2a1ab1ede0c3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r10
    h: e5fc2b55d5c9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r11
    h: 3df47917de46
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r11
    h: 88c2dbfe10d9
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-link-capacitor
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r2
    h: 9eeda4723b68
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r10
    h: 2a1ab1ede0c3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r10
    h: e5fc2b55d5c9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r11
    h: 3df47917de46
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r11
    h: 88c2dbfe10d9
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r2
    h: 9eeda4723b68
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r10
    h: 2a1ab1ede0c3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r10
    h: e5fc2b55d5c9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r11
    h: 3df47917de46
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r11
    h: 88c2dbfe10d9
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
  review_note: 'support check: partial - The alarm is triggered by bulk capacitor voltage and the solution
    says to check input voltage, but no detection method…'
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When input voltage is near the input overvoltage threshold.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r2
    h: 9eeda4723b68
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r10
    h: 2a1ab1ede0c3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r10
    h: e5fc2b55d5c9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r11
    h: 3df47917de46
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r11
    h: 88c2dbfe10d9
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Protection intervention followed by automatic restart.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r2
    h: 9eeda4723b68
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r10
    h: 2a1ab1ede0c3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r10
    h: e5fc2b55d5c9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r11
    h: 3df47917de46
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r11
    h: 88c2dbfe10d9
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
  review_note: 'support check: partial - A protection intervention followed by automatic restart is stated,
    but a production stop is only implied.'
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Transient case from high grid voltage; internal causes require service.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r2
    h: 9eeda4723b68
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r10
    h: 2a1ab1ede0c3
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r10
    h: e5fc2b55d5c9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r11
    h: 3df47917de46
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r11
    h: 88c2dbfe10d9
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r4
    h: e32f501b3271
  review: drafted
---
