---
id: fc:sungrow-sg350hx-208
type: FaultCode
name: Sungrow SG350HX 208
aliases:
- '208'
- Sungrow 208
- PV Reserve Connection Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '208'
code_key: '208'
display_message: PV Reserve Connection Fault
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
  review_note: 'support check: partial - Passage says to check string polarity, but doesn''t describe
    detection by a polarity measurement method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct polarity only once string current is low; contact service if the fault persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29
    h: dc2fe17831d7
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
---
