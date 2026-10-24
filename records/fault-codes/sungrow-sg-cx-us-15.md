---
id: fc:sungrow-sg-cx-us-15
type: FaultCode
name: Sungrow SG-CX-US 015
aliases:
- '015'
- '15'
- Sungrow 015
- Grid overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '015'
code_key: '15'
display_message: Grid overvoltage
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  review: drafted
- claim_id: c3
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
- claim_id: c4
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
  review: drafted
  review_note: 'support check: partial - Service escalation stated, but explicit fault classification
    is not.'
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
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
- claim_id: c10
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
- claim_id: c11
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r3
    h: 8ede75869601
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=35.r3
    h: 8ede75869601
  review: drafted
---
