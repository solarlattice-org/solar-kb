---
id: fc:solis-s6-gc-us-phasefault
type: FaultCode
name: Solis S6-GC PHASE FAULT
aliases:
- PHASE FAULT
- phasefault
- Solis PHASE FAULT
- Abnormal phase of the grid
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: PHASE FAULT
code_key: phasefault
display_message: Abnormal phase of the grid
page: 75
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-phase-angle-abnormal
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
  review_note: 'support check: partial - Fault class is not explicit in the row.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Check grid wiring and phase angles, then restart; replace inverter if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
  review_note: 'support check: partial - Steps are stated, but manual reset clearing is not explicit.'
- claim_id: c8
  rel: applies_to
  target: prod:solis-s6-gc-us
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r8
    h: f73d799fd7e4
  review: drafted
---
