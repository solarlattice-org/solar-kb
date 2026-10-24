---
id: fc:sungrow-sg200hx-3
type: FaultCode
name: Sungrow SG200HX 003
aliases:
- '003'
- '3'
- Sungrow 003
- Grid Overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '003'
code_key: '3'
display_message: Grid Overvoltage
page: 88
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Transient overvoltage event.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
  review_note: 'support check: partial - Fault code row with reconnection, but no explicit fault classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Reconnection implies disconnection, but production stop is not
    explicit.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Repeated occurrence escalates to manufacturer service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r2
    h: 8a8b6ec00b3f
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg200hx
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
---
