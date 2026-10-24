---
id: fc:abb-uno-dm-6-0-plus-us-e50
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E050
aliases:
- E050
- e50
- ABB / FIMER E050
- AFDD Activated
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E050
code_key: e50
display_message: AFDD Activated
vendor_severity: Error
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
  review_note: 'support check: partial - Passages state a possible PV arc detected, not a confirmed arc
    fault.'
- claim_id: c5
  rel: indicates
  target: fm:arc-fault
  note: Possible arc on the PV DC side
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:pv-array
  note: Arc located on the DC side
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the problem recurs after restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  note: Arc protection activated; unit must restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Arc protection activated and unit restarts, implying stop, but
    trip is not explicitly stated.'
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: First occurrence cleared by operator restart; persistent case needs service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r7
    h: e02c4b196d17
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r8
    h: 3cb1bcaa2b59
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r12
    h: 4aa26767d844
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r4
    h: edbd0ff9c5c0
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
  review_note: 'support check: partial - First occurrence: operator presses ESC and restarts; persistent:
    contact assistance; manual-reset is implied rather than stated.'
- claim_id: c11
  rel: applies_to
  target: prod:abb-uno-dm-6-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r12
    h: 4aa26767d844
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r4
    h: edbd0ff9c5c0
  review: drafted
---
