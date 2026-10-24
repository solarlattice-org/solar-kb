---
id: fc:abb-pvs-60-tl-us-e13
type: FaultCode
name: ABB / FIMER PVS-60-TL E013
aliases:
- E013
- e13
- ABB / FIMER E013
- Wrong Mode
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E013
code_key: e13
display_message: Wrong Mode
vendor_severity: Error
page: 155
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
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
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r10
    h: 5beda8ba0a01
  review: drafted
---
