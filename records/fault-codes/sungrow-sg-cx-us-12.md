---
id: fc:sungrow-sg-cx-us-12
type: FaultCode
name: Sungrow SG-CX-US 012
aliases:
- '012'
- '12'
- Sungrow 012
- Excessive leakage current
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '012'
code_key: '12'
display_message: Excessive leakage current
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r4
    h: 9fc64d0d5203
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r4
    h: 9fc64d0d5203
  review: drafted
  review_note: 'support check: partial - Fault name and service escalation given, but explicit fault classification
    is not stated; also auto-reconnects.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r4
    h: 9fc64d0d5203
  review: drafted
  review_note: 'support check: partial - Reconnection after environment improves implies disconnection,
    but production stop not explicitly stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects when damp or low-light conditions improve; otherwise check cable insulation, then service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r4
    h: 9fc64d0d5203
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r4
    h: 9fc64d0d5203
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r5
    h: 843ebdc64972
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r4
    h: 9fc64d0d5203
  review: drafted
---
