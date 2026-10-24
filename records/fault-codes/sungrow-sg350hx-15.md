---
id: fc:sungrow-sg350hx-15
type: FaultCode
name: Sungrow SG350HX 015
aliases:
- '015'
- '15'
- Sungrow 015
- Grid Overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '015'
code_key: '15'
display_message: Grid Overvoltage
page: 87
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Service escalation stated, but explicit fault classification
    is not.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Inverter disconnects and reconnects once grid voltage is normal.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: 'If repeated: measure grid, review settings, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
  review_note: 'support check: partial - Measuring the actual grid voltage is a check step; not stated
    as detection method.'
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: When measured grid voltage exceeds the set value.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:ac-cable
  note: Check cable cross-section adequacy.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
---
