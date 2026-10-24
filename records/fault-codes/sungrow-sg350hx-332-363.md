---
id: fc:sungrow-sg350hx-332-363
type: FaultCode
name: Sungrow SG350HX 332-363
aliases:
- 332-363
- Sungrow 332-363
- Boost Capacitor Overvoltage Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: 332-363
code_key: 332-363
code_from: 332
code_to: 363
display_message: Boost Capacitor Overvoltage Alarm
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=35.r3
    h: 840d89a5aed5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:boost-capacitor-overvoltage
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r4
    h: 840d89a5aed5
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r4
    h: 840d89a5aed5
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r4
    h: 840d89a5aed5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Contact service if the alarm persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r4
    h: 840d89a5aed5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=35.r3
    h: 840d89a5aed5
  review: drafted
---
