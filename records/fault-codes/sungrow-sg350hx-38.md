---
id: fc:sungrow-sg350hx-38
type: FaultCode
name: Sungrow SG350HX 038
aliases:
- '038'
- '38'
- Sungrow 038
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '038'
code_key: '38'
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
    loc: tbl=51.r2
    h: 9e64adaac1e9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r2
    h: 9e64adaac1e9
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
    loc: tbl=51.r2
    h: 9e64adaac1e9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r2
    h: 9e64adaac1e9
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
    loc: tbl=51.r2
    h: 9e64adaac1e9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r2
    h: 9e64adaac1e9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - The row says to wait for the inverter to return to normal (self-recovery),
    but it also requires manual power cycling;…'
---
