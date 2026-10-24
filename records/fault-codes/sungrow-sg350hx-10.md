---
id: fc:sungrow-sg350hx-10
type: FaultCode
name: Sungrow SG350HX 010
aliases:
- '010'
- '10'
- Sungrow 010
- Grid Power Outage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '010'
code_key: '10'
display_message: Grid Power Outage
page: 88
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r3
    h: e30f402aecfe
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r3
    h: e30f402aecfe
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
  review_note: 'support check: partial - Named a fault code and requires service if persisting, but explicit
    fault classification not stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r3
    h: e30f402aecfe
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
  review_note: 'support check: partial - Inverter reconnects after grid returns, implying disconnection,
    but production stop is not explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If repeated, check grid supply, AC wiring and breaker, then contact service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r3
    h: e30f402aecfe
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r3
    h: e30f402aecfe
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r3
    h: e37d4c329c9b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r3
    h: e30f402aecfe
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=30.r3
    h: 1a3868fcd97b
  review: drafted
---
