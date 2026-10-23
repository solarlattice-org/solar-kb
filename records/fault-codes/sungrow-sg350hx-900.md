---
id: fc:sungrow-sg350hx-900
type: FaultCode
name: Sungrow SG350HX 900
aliases:
- '900'
- Sungrow 900
- System Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '900'
code_key: '900'
display_message: System Alarm
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r3
    h: '737750800967'
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=35.r1
    h: 8c1754ff8b85
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r3
    h: '737750800967'
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r3
    h: '737750800967'
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r3
    h: '737750800967'
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r3
    h: '737750800967'
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Used if the alarm persists after the wiring is checked.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
  review: drafted
---
