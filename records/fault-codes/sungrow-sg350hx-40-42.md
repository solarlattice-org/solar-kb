---
id: fc:sungrow-sg350hx-40-42
type: FaultCode
name: Sungrow SG350HX 040-042
aliases:
- 040-042
- 40-42
- Sungrow 040-042
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: 040-042
code_key: 40-42
code_from: 40
code_to: 42
display_message: System Fault
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: 'Escalation: power-cycle after 15 minutes, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r4
    h: 8a5b02233bf8
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - The wait-for-recovery step implies self-clearing, but the manual
    power cycle and service escalation make auto-reset only partly supported.'
- claim_id: c5
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
---
