---
id: fc:sungrow-sg200hx-84
type: FaultCode
name: Sungrow SG200HX 84
aliases:
- '84'
- Sungrow 84
- Reverse Connection Alarm of the Meter/CT
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '84'
code_key: '84'
display_message: Reverse Connection Alarm of the Meter/CT
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r4
    h: dc4af01c1b70
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:meter-wiring-reversed
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r4
    h: dc4af01c1b70
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r4
    h: dc4af01c1b70
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:meter-wiring-check
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r4
    h: dc4af01c1b70
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: 'Applies when an existing system is enabled: verify rated power setting of existing inverter.'
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r4
    h: dc4af01c1b70
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r4
    h: dc4af01c1b70
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
