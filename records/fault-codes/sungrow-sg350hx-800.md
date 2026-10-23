---
id: fc:sungrow-sg350hx-800
type: FaultCode
name: Sungrow SG350HX 800
aliases:
- '800'
- Sungrow 800
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '800'
code_key: '800'
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
  rel: has_event_class
  target: ec:fault
  note: Listed in the fault table as a generic system fault
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; if not, restart after isolating switches, then contact service if
    it persists
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - Waiting for self-recovery is step 1, but the clear mechanism
    is not stated as automatic; restart is manual.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  note: Second step, used if the inverter does not recover on its own
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Last step, if the fault persists after a restart
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
---
