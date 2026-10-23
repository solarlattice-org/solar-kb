---
id: fc:sungrow-sg350hx-44-50
type: FaultCode
name: Sungrow SG350HX 44-50
aliases:
- 44-50
- Sungrow 44-50
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: 44-50
code_key: 44-50
code_from: 44
code_to: 50
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
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  review: drafted
  review_note: 'support check: partial - Row is a generic System Fault covering code 19-25; ''internal
    device fault'' is only loosely implied.'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Normally self-recovers; otherwise power-cycle AC/DC after 15 minutes, then contact service.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  review: drafted
  review_note: 'support check: partial - Row says wait for return to normal, but also requires manual
    power cycle; auto-reset is only the first step, not…'
---
