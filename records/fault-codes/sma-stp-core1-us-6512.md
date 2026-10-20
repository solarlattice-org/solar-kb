---
id: fc:sma-stp-core1-us-6512
type: FaultCode
name: SMA CORE1-US 6512
aliases:
- '6512'
- SMA 6512
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '6512'
code_key: '6512'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-undertemperature
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  note: Feed-in is withheld until minimum temperature is reached
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  review: drafted
  review_note: 'support check: partial - Feed-in withheld is stated, but fault vs warning classification
    is only implied.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes feed-in once inverter temperature reaches the stated minimum
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  review: drafted
---
