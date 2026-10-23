---
id: fc:sungrow-sg200hx-60-69
type: FaultCode
name: Sungrow SG200HX 60-69
aliases:
- 60-69
- Sungrow 60-69
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: 60-69
code_key: 60-69
code_from: 60
code_to: 69
display_message: System Fault
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r1
    h: b64052214890
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Generic system fault shared by many codes; the row names no specific failed part.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - Codes 52-58 are a generic System Fault; internal device fault
    is only loosely implied.'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: sec=8.1
    h: eca2a8959712
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: First step is to wait for normal operation; if it persists, power-cycle AC/DC after 15 minutes,
    then contact service.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - First step is waiting for normal, but later steps need manual
    power cycle; auto-reset is not clearly stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  note: Applies if the fault does not clear by itself.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final step if the fault continues after restarting.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
---
