---
id: fc:sungrow-sg-cx-us-2
type: FaultCode
name: Sungrow SG-CX-US 002
aliases:
- '002'
- '2'
- Sungrow 002
- Grid overvoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '002'
code_key: '2'
display_message: Grid overvoltage
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
  review_note: 'support check: partial - The row describes a fault code and the device reconnects, but
    never labels it a ''fault'' class; a protection stop…'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Reconnection after grid normalizes implies the inverter disconnected,
    but production stop is not explicitly stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects when grid normalizes; if repeated, check grid and settings, then contact service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r1
    h: 4e1fbd3f8aad
  review: drafted
- claim_id: c11
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  review: drafted
  review_note: 'support check: partial - AC cable cross-section is a check item, but the passages don''t
    say the fault affects the cable; it is a…'
- claim_id: c12
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=46.r1
    h: 34f30afcef21
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=32.r1
    h: 34f30afcef21
  review: drafted
---
