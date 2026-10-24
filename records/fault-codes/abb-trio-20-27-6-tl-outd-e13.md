---
id: fc:abb-trio-20-27-6-tl-outd-e13
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL E013
aliases:
- E013
- e13
- ABB / FIMER E013
- Wrong Mode
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: E013
code_key: e13
display_message: Wrong Mode
vendor_severity: Error
page: 111
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r1
    h: f171a8fd5d45
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r1
    h: f171a8fd5d45
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Parallel input mode with channel voltages differing by more than 20 Vdc.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 42a071b1f615
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 42a071b1f615
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r8
    h: 3561cf9a0cd8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r8
    h: 3561cf9a0cd8
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 42a071b1f615
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 42a071b1f615
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r8
    h: 3561cf9a0cd8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r8
    h: 3561cf9a0cd8
  review: drafted
  review_note: 'support check: partial - The passages mention the PV string checks as part of the solution,
    but the alarm is about input configuration; PV…'
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 42a071b1f615
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 42a071b1f615
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r8
    h: 3561cf9a0cd8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r8
    h: 3561cf9a0cd8
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Check input mode and jumpers first, then string composition; contact service if both conform.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r6
    h: 42a071b1f615
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 42a071b1f615
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r8
    h: 3561cf9a0cd8
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r8
    h: 3561cf9a0cd8
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r1
    h: f171a8fd5d45
  review: drafted
---
