---
id: fc:sungrow-sg-cx-us-8
type: FaultCode
name: Sungrow SG-CX-US 008
aliases:
- '008'
- '8'
- Sungrow 008
- Grid overfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '008'
code_key: '8'
display_message: Grid overfrequency
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
  review_note: 'support check: partial - No explicit fault classification; only implied.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
  review_note: 'support check: partial - Passages say the inverter reconnects after grid normal (implying
    it disconnected), but never state production stops or a trip explicitly.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
  review_note: 'support check: partial - Passages say to measure the actual grid frequency as a check,
    but not that the inverter detects the fault by…'
- claim_id: c8
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=34.r1
    h: fb249c3b40c0
  review: drafted
---
