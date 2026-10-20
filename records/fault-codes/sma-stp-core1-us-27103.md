---
id: fc:sma-stp-core1-us-27103
type: FaultCode
name: SMA CORE1-US 27103
aliases:
- '27103'
- SMA 27103
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '27103'
code_key: '27103'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r8
    h: c5550759f780
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r8
    h: c5550759f780
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r8
    h: c5550759f780
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r8
    h: c5550759f780
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r8
    h: c5550759f780
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r8
    h: c5550759f780
  review: drafted
  review_note: 'support check: partial - Row is a status message, but no production effect is stated.'
---
