---
id: fc:sungrow-sg200hx-8
type: FaultCode
name: Sungrow SG200HX 008
aliases:
- '008'
- '8'
- Sungrow 008
- Grid Overfrequency
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '008'
code_key: '8'
display_message: Grid Overfrequency
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
- claim_id: c4
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
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - Passages say the inverter reconnects after grid normal (implying
    it disconnected), but never state production stops or a trip explicitly.'
- claim_id: c5
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
- claim_id: c6
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
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passages say to measure the actual grid frequency as a check,
    but not that the inverter detects the fault by…'
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=30.r1
    h: 57332801a426
  review: drafted
---
