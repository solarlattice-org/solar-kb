---
id: fc:sungrow-sg200hx-70-74
type: FaultCode
name: Sungrow SG200HX 70-74
aliases:
- 70-74
- Sungrow 70-74
- System Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: 70-74
code_key: 70-74
code_from: 70
code_to: 74
display_message: System Alarm
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
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
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
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
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Used if the alarm persists after the wiring is checked.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r2
    h: 82098a62864e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
